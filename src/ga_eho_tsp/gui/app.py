"""Giao diện đồ họa (GUI) chính cho ứng dụng GA-EHO-TSP.

Bố cục hai panel hiện đại, hệ thống thẻ Card phân cấp thị giác rõ ràng,
bảng số liệu trực quan, biểu đồ thời gian thực và điều phối worker thread an toàn.
"""

from dataclasses import asdict
import json
from pathlib import Path
import re
import sys
from time import perf_counter
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from ..data.matrix_loader import load_matrix
from ..domain.models import EHOConfig, GAConfig, IterationStat, RunResult, TSPProblem
from .controller import ALGORITHMS, RunController, bundled_datasets
from .controls import ConfigForm, EHOConfigForm, preset_config
from .export import export_history, export_json
from .plots import SCHEMATIC, draw_history, draw_route
from .theme import (
    COLORS,
    FONT_BADGE,
    FONT_BODY,
    FONT_BODY_BOLD,
    FONT_CODE,
    FONT_HEADING,
    FONT_SMALL,
    FONT_SMALL_BOLD,
    FONT_STAT_LBL,
    FONT_STAT_VAL,
    FONT_SUBTITLE,
    FONT_TITLE,
    SPACING_MD,
    SPACING_SM,
    SPACING_XS,
    apply_theme,
)


class Application:
    """Ứng dụng GUI chính cho GA & EHO TSP."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.controller = RunController()
        self.problem: TSPProblem | None = None
        self.run_problem: TSPProblem | None = None
        self.result: RunResult | None = None
        self.closing = False
        self.live_history: list[IterationStat] = []
        self.started = 0.0
        self.run_config: GAConfig | EHOConfig | None = None
        self.last_live_plot = 0.0
        self.algorithm_keys = list(ALGORITHMS)
        self.dataset_paths = {p.name: p for p in bundled_datasets()}

        # 1. Cấu hình cửa sổ & Theme
        root.title("Genetic Algorithm & EHO")
        root.geometry("1260x740")
        root.minsize(1180, 640)
        root.protocol("WM_DELETE_WINDOW", self.request_close)

        # Áp dụng Design System tập trung
        apply_theme(root)

        # 2. Khung chứa chính (Main container)
        main_container = ttk.Frame(root, style="TFrame")
        main_container.pack(fill="both", expand=True)

        # 3. Header thanh lịch
        self._build_header(main_container)

        # 4. PanedWindow (Trái = Input/Config, Phải = Execution/Results)
        panes = ttk.Panedwindow(main_container, orient="horizontal")
        panes.pack(fill="both", expand=True, padx=SPACING_MD, pady=(0, SPACING_MD))

        # Panel trái và phải
        left = ttk.Frame(panes, width=430)
        right = ttk.Frame(panes)
        panes.add(left, weight=0)
        panes.add(right, weight=1)

        # Đặt kích thước tối thiểu cho panel trái để không bị co quá nhỏ
        try:
            panes.paneconfig(left, minsize=410)
        except Exception:
            pass

        self._build_inputs(left)
        self._build_results(right)

        # 5. Khởi động vòng lặp kiểm tra worker thread
        self.poll_id = root.after(100, self._poll)

        # 6. Chọn dataset mặc định ban đầu
        if self.dataset_paths:
            name = (
                "15Cities-1194.txt"
                if "15Cities-1194.txt" in self.dataset_paths
                else next(iter(self.dataset_paths))
            )
            self.dataset_var.set(name)
            self.select_dataset()
        else:
            self.dataset_info.set("Không tìm thấy data/ cạnh package. Hãy duyệt file ma trận .txt.")

        self._update_actions()

    # =========================================================================
    # XÂY DỰNG GIAO DIỆN: HEADER
    # =========================================================================
    def _build_header(self, parent: ttk.Frame) -> None:
        """Header trên cùng với tiêu đề, phụ đề và badges trạng thái."""
        header_frame = tk.Frame(parent, bg=COLORS.surface, padx=SPACING_MD, pady=10)
        header_frame.pack(fill="x", pady=(0, SPACING_SM))

        # Khối bên trái: Tiêu đề + Phụ đề
        left_box = tk.Frame(header_frame, bg=COLORS.surface)
        left_box.pack(side="left", fill="y")

        title_lbl = tk.Label(
            left_box,
            text="GA & Elephant Herding Optimization · Traveling Salesman Problem",
            font=FONT_TITLE,
            fg=COLORS.text,
            bg=COLORS.surface,
        )
        title_lbl.pack(anchor="w")

        subtitle_lbl = tk.Label(
            left_box,
            text="Ứng dụng thuật toán Genetic Algorithm và Elephant Herding Optimization cho bài toán người du lịch (Traveling Salesman Problem - TSP)",
            font=FONT_SUBTITLE,
            fg=COLORS.text_muted,
            bg=COLORS.surface,
        )
        subtitle_lbl.pack(anchor="w", pady=(2, 0))

        # Khối bên phải: Badges hiển thị nhanh
        right_box = tk.Frame(header_frame, bg=COLORS.surface)
        right_box.pack(side="right", fill="y")

        self.badge_algo_var = tk.StringVar(value="GA")
        self.badge_dataset_var = tk.StringVar(value="15Cities")

        # Badge Thuật toán
        self.badge_algo = tk.Label(
            right_box,
            textvariable=self.badge_algo_var,
            font=FONT_BADGE,
            bg=COLORS.primary_light,
            fg=COLORS.primary,
            padx=10,
            pady=4,
            relief="flat",
        )
        self.badge_algo.pack(side="left", padx=4)

        # Badge Dataset
        self.badge_dataset = tk.Label(
            right_box,
            textvariable=self.badge_dataset_var,
            font=FONT_BADGE,
            bg=COLORS.accent_light,
            fg=COLORS.accent,
            padx=10,
            pady=4,
            relief="flat",
        )
        self.badge_dataset.pack(side="left", padx=4)

        # Đường kẻ phân cách mảnh
        sep = tk.Frame(parent, height=1, bg=COLORS.border)
        sep.pack(fill="x", pady=(0, SPACING_SM))

    # =========================================================================
    # XÂY DỰNG GIAO DIỆN: PANEL TRÁI (INPUTS)
    # =========================================================================
    def _build_inputs(self, parent: ttk.Frame) -> None:
        """Panel bên trái chứa các Card: Dataset, Thuật toán & Preset, Form tham số, Ghi chú."""
        # 1. Card: Dataset TSP
        dataset_card = tk.Frame(
            parent,
            bg=COLORS.surface,
            highlightbackground=COLORS.border,
            highlightthickness=1,
            padx=10,
            pady=8,
        )
        dataset_card.pack(fill="x", pady=(0, SPACING_SM))

        card_title = tk.Label(
            dataset_card,
            text="1. Dữ liệu bài toán (Dataset)",
            font=FONT_HEADING,
            fg=COLORS.text,
            bg=COLORS.surface,
        )
        card_title.pack(anchor="w", pady=(0, 6))

        # Hàng chọn dataset + nút duyệt
        ds_row = tk.Frame(dataset_card, bg=COLORS.surface)
        ds_row.pack(fill="x", pady=(0, 4))

        self.dataset_var = tk.StringVar()
        self.dataset_box = ttk.Combobox(
            ds_row,
            textvariable=self.dataset_var,
            values=list(self.dataset_paths),
            state="readonly",
        )
        self.dataset_box.pack(side="left", fill="x", expand=True)
        self.dataset_box.bind("<<ComboboxSelected>>", lambda event: self.select_dataset())

        self.browse_button = ttk.Button(
            ds_row,
            text="Duyệt .txt…",
            style="Secondary.TButton",
            command=self.browse_dataset,
        )
        self.browse_button.pack(side="left", padx=(6, 0))

        # Thông tin dataset (n, đối xứng, finite...)
        self.dataset_info = tk.StringVar()
        self.dataset_info_lbl = tk.Label(
            dataset_card,
            textvariable=self.dataset_info,
            font=FONT_SMALL,
            fg=COLORS.text_muted,
            bg=COLORS.surface,
            justify="left",
            wraplength=380,
            anchor="w",
        )
        self.dataset_info_lbl.pack(fill="x", pady=(2, 0))

        dataset_card.bind(
            "<Configure>",
            lambda event: self.dataset_info_lbl.configure(
                wraplength=max(200, event.width - 24)
            ),
        )

        # 2. Card: Thuật toán & Preset
        algo_card = tk.Frame(
            parent,
            bg=COLORS.surface,
            highlightbackground=COLORS.border,
            highlightthickness=1,
            padx=10,
            pady=8,
        )
        algo_card.pack(fill="x", pady=(0, SPACING_SM))

        algo_title = tk.Label(
            algo_card,
            text="2. Thuật toán & Cấu hình sẵn (Preset)",
            font=FONT_HEADING,
            fg=COLORS.text,
            bg=COLORS.surface,
        )
        algo_title.pack(anchor="w", pady=(0, 6))

        self.algorithm_var = tk.StringVar(value=ALGORITHMS["ga"].label)
        self.algorithm_box = ttk.Combobox(
            algo_card,
            textvariable=self.algorithm_var,
            values=[a.label for a in ALGORITHMS.values()],
            state="readonly",
        )
        self.algorithm_box.pack(fill="x", pady=(0, 6))
        self.algorithm_box.bind("<<ComboboxSelected>>", lambda event: self._algorithm_changed())

        preset_row = tk.Frame(algo_card, bg=COLORS.surface)
        preset_row.pack(fill="x")

        self.preset_var = tk.StringVar(value="Mặc định")
        self.preset_box = ttk.Combobox(
            preset_row,
            textvariable=self.preset_var,
            state="readonly",
            values=("Demo nhanh", "Mặc định", "Giới hạn evaluations"),
        )
        self.preset_box.pack(side="left", fill="x", expand=True)
        self.preset_box.bind("<<ComboboxSelected>>", lambda event: self.apply_preset())

        self.reset_button = ttk.Button(
            preset_row,
            text="Reset default",
            style="Secondary.TButton",
            command=self.reset_defaults,
        )
        self.reset_button.pack(side="left", padx=(6, 0))

        # 3. Card: Form Tham số (GA / EHO)
        self.param_card = tk.Frame(
            parent,
            bg=COLORS.surface,
            highlightbackground=COLORS.border,
            highlightthickness=1,
            padx=10,
            pady=8,
        )
        self.param_card.pack(fill="both", expand=True, pady=(0, SPACING_SM))

        param_title = tk.Label(
            self.param_card,
            text="3. Tham số cấu hình",
            font=FONT_HEADING,
            fg=COLORS.text,
            bg=COLORS.surface,
        )
        param_title.pack(anchor="w", pady=(0, 4))

        self.form = ConfigForm(self.param_card)
        self.form.pack(fill="both", expand=True)

        self.eho_form = EHOConfigForm(self.param_card)
        self.eho_form.pack(fill="both", expand=True)
        self.eho_form.pack_forget()

        # 4. Ghi chú biến thể đang kích hoạt (Variant banner)
        variant_card = tk.Frame(
            parent,
            bg=COLORS.surface_variant,
            highlightbackground=COLORS.border,
            highlightthickness=1,
            padx=10,
            pady=6,
        )
        variant_card.pack(fill="x")

        self.variant = tk.StringVar(value="GA thuần · adaptive/2-opt OFF mặc định")
        self.variant_lbl = tk.Label(
            variant_card,
            textvariable=self.variant,
            font=FONT_SMALL_BOLD,
            fg=COLORS.accent,
            bg=COLORS.surface_variant,
            justify="left",
            wraplength=380,
            anchor="w",
        )
        self.variant_lbl.pack(fill="x")

        variant_card.bind(
            "<Configure>",
            lambda event: self.variant_lbl.configure(
                wraplength=max(200, event.width - 24)
            ),
        )

        self.form.variables["local_search_enabled"].trace_add(
            "write", lambda *args: self._variant_changed()
        )
        self.form.variables["adaptive_mutation"].trace_add(
            "write", lambda *args: self._variant_changed()
        )

    # =========================================================================
    # XÂY DỰNG GIAO DIỆN: PANEL PHẢI (RESULTS & VISUALIZATIONS)
    # =========================================================================
    def _build_results(self, parent: ttk.Frame) -> None:
        """Panel bên phải chứa Card Trạng thái/Điều khiển và Card Trực quan hóa."""
        # 1. Card: Điều khiển & Trạng thái chạy
        control_card = tk.Frame(
            parent,
            bg=COLORS.surface,
            highlightbackground=COLORS.border,
            highlightthickness=1,
            padx=12,
            pady=10,
        )
        control_card.pack(fill="x", pady=(0, SPACING_SM))

        # Hàng 1: Nút hành động [Chạy | Dừng] bên trái, nhóm [Export] bên phải
        action_bar = tk.Frame(control_card, bg=COLORS.surface)
        action_bar.pack(fill="x", pady=(0, 8))

        # Nhóm Run & Stop
        self.run_button = ttk.Button(
            action_bar,
            text="▶ Chạy GA",
            style="Primary.TButton",
            command=self.start_run,
        )
        self.run_button.pack(side="left")

        self.stop_button = ttk.Button(
            action_bar,
            text="■ Dừng",
            style="Danger.TButton",
            command=self.stop_run,
        )
        self.stop_button.pack(side="left", padx=(8, 0))

        # Nhóm Export gom bên phải
        export_box = tk.Frame(action_bar, bg=COLORS.surface)
        export_box.pack(side="right")

        self.export_buttons = []
        export_specs = (
            ("⬇ JSON", "json"),
            ("⬇ CSV", "csv"),
            ("🖼 Tuyến", "route"),
            ("📈 Hội tụ", "history"),
        )
        for label, kind in export_specs:
            btn = ttk.Button(
                export_box,
                text=label,
                style="Secondary.TButton",
                command=lambda k=kind: self.save(k),
            )
            btn.pack(side="left", padx=2)
            self.export_buttons.append(btn)

        # Hàng 2: Trạng thái & Thanh tiến trình
        status_bar = tk.Frame(control_card, bg=COLORS.surface)
        status_bar.pack(fill="x", pady=(0, 4))

        self.status = tk.StringVar(value="Sẵn sàng")
        self.status_icon_lbl = tk.Label(
            status_bar,
            text="●",
            font=("Segoe UI", 11, "bold"),
            fg=COLORS.success,
            bg=COLORS.surface,
        )
        self.status_icon_lbl.pack(side="left", padx=(0, 4))

        self.status_text_lbl = tk.Label(
            status_bar,
            textvariable=self.status,
            font=FONT_BODY_BOLD,
            fg=COLORS.text,
            bg=COLORS.surface,
        )
        self.status_text_lbl.pack(side="left")

        # Nhãn phần trăm tiến độ
        self.progress_percent = tk.StringVar(value="0%")
        self.percent_lbl = tk.Label(
            status_bar,
            textvariable=self.progress_percent,
            font=FONT_SMALL_BOLD,
            fg=COLORS.primary,
            bg=COLORS.surface,
        )
        self.percent_lbl.pack(side="right")

        self.progress = ttk.Progressbar(
            control_card,
            mode="determinate",
            maximum=100,
            value=0,
            style="Horizontal.TProgressbar",
        )
        self.progress.pack(fill="x", pady=(0, 10))

        # Hàng 3: Bảng số liệu (Metric Tiles) dạng thẻ số liệu hiện đại
        self.metrics = tk.StringVar(value="Chưa có kết quả. Chọn dataset và cấu hình rồi Chạy GA.")

        metric_grid = tk.Frame(control_card, bg=COLORS.surface)
        metric_grid.pack(fill="x")
        for c in range(5):
            metric_grid.columnconfigure(c, weight=1)

        self.tile_cost = tk.StringVar(value="--")
        self.tile_iters = tk.StringVar(value="--")
        self.tile_evals = tk.StringVar(value="--")
        self.tile_time = tk.StringVar(value="--")
        self.tile_seed = tk.StringVar(value="--")

        tiles_spec = [
            ("CHI PHÍ TỐT NHẤT", self.tile_cost, COLORS.primary),
            ("VÒNG LẶP ĐÃ CHẠY", self.tile_iters, COLORS.text),
            ("EVALUATIONS", self.tile_evals, COLORS.text),
            ("RUNTIME SOLVER", self.tile_time, COLORS.text),
            ("SEED", self.tile_seed, COLORS.text_muted),
        ]

        for col, (title, var, val_color) in enumerate(tiles_spec):
            tile_box = tk.Frame(
                metric_grid,
                bg=COLORS.surface_variant,
                highlightbackground=COLORS.border,
                highlightthickness=1,
                padx=8,
                pady=6,
            )
            tile_box.grid(row=0, column=col, sticky="ew", padx=3)

            lbl_t = tk.Label(
                tile_box,
                text=title,
                font=FONT_STAT_LBL,
                fg=COLORS.text_muted,
                bg=COLORS.surface_variant,
            )
            lbl_t.pack(anchor="center")

            lbl_v = tk.Label(
                tile_box,
                textvariable=var,
                font=FONT_STAT_VAL,
                fg=val_color,
                bg=COLORS.surface_variant,
            )
            lbl_v.pack(anchor="center", pady=(2, 0))

        # 2. Card: Kết quả trực quan (Notebook 3 tab)
        visual_card = tk.Frame(
            parent,
            bg=COLORS.surface,
            highlightbackground=COLORS.border,
            highlightthickness=1,
            padx=10,
            pady=8,
        )
        visual_card.pack(fill="both", expand=True)

        self.tabs = ttk.Notebook(visual_card)
        self.tabs.pack(fill="both", expand=True)

        route_tab = ttk.Frame(self.tabs, style="Surface.TFrame")
        history_tab = ttk.Frame(self.tabs, style="Surface.TFrame")
        detail_tab = ttk.Frame(self.tabs, style="Surface.TFrame")

        self.tabs.add(route_tab, text=" Tuyến đường ")
        self.tabs.add(history_tab, text=" Biểu đồ hội tụ ")
        self.tabs.add(detail_tab, text=" Chi tiết JSON ")

        # Tab Tuyến đường
        self.layout_note = tk.StringVar(value=SCHEMATIC)
        self.layout_note_lbl = tk.Label(
            route_tab,
            textvariable=self.layout_note,
            font=FONT_SMALL,
            fg=COLORS.accent,
            bg=COLORS.surface,
        )
        self.layout_note_lbl.pack(anchor="center", pady=(4, 2))

        self.route_figure = Figure(figsize=(6, 4), dpi=92)
        self.history_figure = Figure(figsize=(6, 4), dpi=92)
        self.route_canvas = FigureCanvasTkAgg(self.route_figure, master=route_tab)
        self.history_canvas = FigureCanvasTkAgg(self.history_figure, master=history_tab)

        for canvas in (self.route_canvas, self.history_canvas):
            canvas.get_tk_widget().pack(fill="both", expand=True)

        draw_history(self.history_figure, [])

        # Khung hiển thị Tour text (dễ đọc, dễ copy)
        tour_box = tk.Frame(
            route_tab,
            bg=COLORS.surface_variant,
            highlightbackground=COLORS.border,
            highlightthickness=1,
            padx=8,
            pady=4,
        )
        tour_box.pack(fill="x", pady=(4, 0))

        self.tour_text = tk.StringVar(value="Tour 1-based khép vòng sẽ xuất hiện sau khi chạy.")
        self.tour_lbl = tk.Label(
            tour_box,
            textvariable=self.tour_text,
            font=FONT_CODE,
            fg=COLORS.text,
            bg=COLORS.surface_variant,
            justify="left",
            wraplength=720,
            anchor="w",
        )
        self.tour_lbl.pack(fill="x")

        tour_box.bind(
            "<Configure>",
            lambda event: self.tour_lbl.configure(wraplength=max(300, event.width - 20)),
        )

        # Tab Chi tiết (ScrolledText)
        detail_container = tk.Frame(detail_tab, bg=COLORS.surface)
        detail_container.pack(fill="both", expand=True, padx=4, pady=4)

        self.details = scrolledtext.ScrolledText(
            detail_container,
            wrap="none",
            font=FONT_CODE,
            width=65,
            height=15,
            bg=COLORS.surface,
            fg=COLORS.text,
            insertbackground=COLORS.primary,
            relief="flat",
            highlightthickness=1,
            highlightbackground=COLORS.border,
        )
        self.details.pack(fill="both", expand=True)
        self.details["state"] = "disabled"

    # =========================================================================
    # LOGIC VẬN HÀNH & ĐIỀU PHỐI (GIỮ NGUYÊN HOÀN TOÀN)
    # =========================================================================
    def _variant_changed(self) -> None:
        local = self.form.variables["local_search_enabled"].get()
        adaptive = self.form.variables["adaptive_mutation"].get()
        text = (
            ("GA + 2-opt (biến thể thực nghiệm)" if local else "GA thuần, không local search")
            + (" · adaptive ON" if adaptive else " · adaptive OFF")
        )
        self.variant.set(text)

    def _algorithm(self) -> str:
        return self.algorithm_keys[self.algorithm_box.current()]

    def _algorithm_changed(self) -> None:
        algo = self._algorithm()
        is_eho = algo == "eho"
        self.root.title(
            "Elephant Herding Optimization (EHO)" if is_eho else "Genetic Algorithm"
        )
        self.badge_algo_var.set("EHO" if is_eho else "GA")

        if is_eho:
            self.form.pack_forget()
            self.eho_form.pack(fill="both", expand=True)
            self.variant.set("EHO baseline · clan-best attraction + separation")
        else:
            self.eho_form.pack_forget()
            self.form.pack(fill="both", expand=True)
            self._variant_changed()

        self._update_actions()

    def _update_actions(self) -> None:
        busy = self.controller.active or self.closing
        available = ALGORITHMS[self._algorithm()].solver is not None
        for widget in (self.dataset_box, self.algorithm_box, self.preset_box):
            widget["state"] = "disabled" if busy else "readonly"
        for widget in (self.browse_button, self.reset_button):
            widget["state"] = "disabled" if busy else "normal"

        active_form = self.eho_form if self._algorithm() == "eho" else self.form
        active_form.set_enabled(not busy and available)
        self.preset_box["state"] = "disabled" if busy or self._algorithm() == "eho" else "readonly"

        run_text = "▶ Chạy EHO" if self._algorithm() == "eho" else "▶ Chạy GA"
        self.run_button.configure(text=run_text)
        self.run_button["state"] = (
            "normal" if not busy and available and self.problem is not None else "disabled"
        )
        self.stop_button["state"] = (
            "normal" if self.controller.active and not self.closing else "disabled"
        )
        for widget in self.export_buttons:
            widget["state"] = "normal" if self.result is not None and not busy else "disabled"

        if not available and not busy:
            self._set_status_badge("Solver chưa khả dụng.", COLORS.danger, "✖")
        elif not busy and self.status.get().startswith("Solver"):
            self._set_status_badge("Sẵn sàng", COLORS.success, "●")

    def _set_status_badge(self, text: str, color: str, icon: str) -> None:
        """Cập nhật trạng thái kèm màu sắc và biểu tượng."""
        self.status.set(text)
        self.status_icon_lbl.configure(text=icon, fg=color)

    def _error(self, title: str, error: Exception | str) -> None:
        self._set_status_badge(f"Lỗi: {error}", COLORS.danger, "✖")
        messagebox.showerror(title, str(error), parent=self.root)

    def select_dataset(self, path: str | Path | None = None) -> None:
        if self.controller.active or self.closing:
            return
        path = path or self.dataset_paths.get(self.dataset_var.get())
        self.problem = None
        try:
            if path is None:
                raise ValueError("Chưa chọn file ma trận .txt.")
            self.problem = load_matrix(path)
        except (ValueError, OSError) as error:
            self.dataset_info.set(str(error))
            self._error("Dữ liệu không hợp lệ", error)
        else:
            p = self.problem
            self.dataset_info.set(
                f"{p.name} · n={p.dimension} · vuông/đối xứng/finite/chéo 0: hợp lệ\nNguồn: {p.source}"
            )
            self.badge_dataset_var.set(f"{p.name} (n={p.dimension})")
            self._set_status_badge("Sẵn sàng", COLORS.success, "●")

            # Kết quả cũ không được gắn lên dataset mới
            self.result = None
            self.run_problem = None
            self.layout_note.set(SCHEMATIC if p.coordinates is None else "Tọa độ do dataset cung cấp")
            self.tour_text.set("Chưa có tour cho dataset vừa chọn.")
            self.metrics.set("Chưa chạy dataset này.")

            # Reset các metric tiles
            self.tile_cost.set("--")
            self.tile_iters.set("--")
            self.tile_evals.set("--")
            self.tile_time.set("--")
            self.tile_seed.set("--")
            self.progress.configure(value=0)
            self.progress_percent.set("0%")

            draw_route(self.route_figure, p)
            draw_history(self.history_figure, [])
            self._set_details({"dataset": p.name, "source": p.source, "metadata": dict(p.metadata)})
            self.route_canvas.draw_idle()
            self.history_canvas.draw_idle()

        self._update_actions()

    def browse_dataset(self) -> None:
        path = filedialog.askopenfilename(
            parent=self.root,
            title="Chọn ma trận khoảng cách whitespace",
            filetypes=[("Ma trận khoảng cách", "*.txt")],
        )
        if path:
            name = str(Path(path).resolve())
            self.dataset_paths[name] = Path(path)
            self.dataset_box.configure(values=list(self.dataset_paths))
            self.dataset_var.set(name)
            self.select_dataset(path)

    def apply_preset(self) -> None:
        if not self.controller.active:
            self.form.set_config(preset_config(self.preset_var.get()))

    def reset_defaults(self) -> None:
        self.preset_var.set("Mặc định")
        if self._algorithm() == "eho":
            self.eho_form.set_config(EHOConfig())
        else:
            self.apply_preset()

    def start_run(self) -> None:
        if self.controller.active or self.closing:
            return
        try:
            algorithm = self._algorithm()
            if self.problem is None:
                raise ValueError("Hãy chọn dataset hợp lệ trước khi chạy.")
            config = self.eho_form.config() if algorithm == "eho" else self.form.config()
            self.run_problem = self.problem
            self.controller.start(algorithm, self.run_problem, config)
        except (ValueError, RuntimeError) as error:
            self._error("Không thể chạy", error)
            return

        self.result = None
        self.run_config = config
        self.live_history = []
        self.started = perf_counter()

        run_label = "EHO baseline" if algorithm == "eho" else self.variant.get()
        self._set_status_badge(f"Đang chạy · {run_label}", COLORS.warning, "⏳")

        self.progress.configure(value=0)
        self.progress_percent.set("0%")
        self.metrics.set(f"seed={config.seed}; đang khởi tạo quần thể…")
        self.tile_seed.set(str(config.seed))
        self.tile_cost.set("Đang tìm…")
        self.tile_iters.set("0")
        self.tile_evals.set("0")
        self.tile_time.set("0.0s")

        self.tour_text.set("Đang tối ưu hành trình…")
        self._set_details(
            {
                "dataset": self.run_problem.name,
                "source": self.run_problem.source,
                "config_thuc_chay": asdict(config),
            }
        )

        draw_route(self.route_figure, self.run_problem)
        draw_history(self.history_figure, [])
        self.route_canvas.draw_idle()
        self.history_canvas.draw_idle()
        self._update_actions()

    def stop_run(self) -> None:
        if self.controller.active:
            self.controller.cancel()
            self._set_status_badge("Đang dừng · chờ solver trả kết quả tốt nhất…", COLORS.text_muted, "⏹")
            self.stop_button["state"] = "disabled"

    def _poll(self) -> None:
        for kind, payload in self.controller.drain():
            if kind == "progress":
                self.live_history.append(payload)
                seed = self.run_config.seed if self.run_config else payload.iteration
                self.metrics.set(
                    f"seed={seed} · vòng={payload.iteration} · evaluations={payload.evaluations} · "
                    f"best={payload.best_so_far:g} · runtime={payload.elapsed_seconds:.2f}s"
                )

                # Cập nhật các ô số liệu (Metric Tiles)
                self.tile_cost.set(f"{payload.best_so_far:g}")
                self.tile_iters.set(f"{payload.iteration}")
                self.tile_evals.set(f"{payload.evaluations:,}")
                self.tile_time.set(f"{payload.elapsed_seconds:.2f}s")
                self.tile_seed.set(str(seed))

                cap = self.run_config.max_evaluations if self.run_config else None
                cap = cap or (self.run_config.max_iterations if self.run_config else 1)
                current = (
                    payload.evaluations
                    if self.run_config and self.run_config.max_evaluations
                    else payload.iteration
                )
                prog_val = min(current, cap)
                self.progress.configure(maximum=max(1, cap), value=prog_val)
                pct = int(100 * prog_val / max(1, cap))
                self.progress_percent.set(f"{pct}%")

                if (
                    self.tabs.index(self.tabs.select()) == 1
                    and perf_counter() - self.last_live_plot >= 0.3
                ):
                    draw_history(self.history_figure, self.live_history[-1000:])
                    self.history_canvas.draw_idle()
                    self.last_live_plot = perf_counter()

            elif kind == "result":
                self.show_result(payload)
            elif kind == "error":
                self._set_status_badge(f"Lỗi solver: {payload[0]}", COLORS.danger, "✖")
                self._set_details({"error": payload[0], "traceback": payload[1]})
                if not self.closing:
                    messagebox.showerror("Lỗi solver", payload[0], parent=self.root)
                self._update_actions()

        if self.closing and not self.controller.active:
            self._destroy()
            return

        if self.controller.active:
            self.root.title(f"GA–EHO–TSP · Đang chạy {perf_counter() - self.started:.1f}s")

        self.poll_id = self.root.after(100, self._poll)

    def show_result(self, result: RunResult) -> None:
        self.result = result
        p = self.run_problem
        assert p is not None
        self.layout_note.set(SCHEMATIC if p.coordinates is None else "Tọa độ do dataset cung cấp")

        status_str = "Đã hủy" if result.stopping_reason == "CANCELLED" else "Hoàn thành"
        status_color = COLORS.text_muted if result.stopping_reason == "CANCELLED" else COLORS.success
        status_icon = "⏹" if result.stopping_reason == "CANCELLED" else "✔"
        self._set_status_badge(
            f"{status_str} · {result.stopping_reason} · {result.algorithm.upper()}",
            status_color,
            status_icon,
        )

        self.root.title(
             "Elephant Herding Optimization (EHO)" if result.algorithm == "eho" else "Genetic Algorithm"
        )

        self.metrics.set(
            f"{p.name} · n={p.dimension} · distance={result.best_distance:g}\n"
            f"seed={result.seed} · iterations={result.iterations_completed} · "
            f"evaluations={result.evaluations} · runtime solver={result.elapsed_seconds:.6f}s"
        )

        # Cập nhật số liệu các Metric Tiles
        self.tile_cost.set(f"{result.best_distance:g}")
        self.tile_iters.set(f"{result.iterations_completed}")
        self.tile_evals.set(f"{result.evaluations:,}")
        self.tile_time.set(f"{result.elapsed_seconds:.4f}s")
        self.tile_seed.set(str(result.seed))

        cap = (
            (self.run_config.max_evaluations if self.run_config else None)
            or (self.run_config.max_iterations if self.run_config else result.iterations_completed)
        )
        current = (
            result.evaluations
            if self.run_config and self.run_config.max_evaluations
            else result.iterations_completed
        )
        prog_val = min(current, cap)
        self.progress.configure(maximum=max(1, cap), value=prog_val)
        pct = int(100 * prog_val / max(1, cap)) if cap else 100
        self.progress_percent.set(f"{pct}% · Hoàn tất")

        # Hiển thị tuyến đường dạng chuỗi 1-based
        self.tour_text.set("Tour 1-based khép vòng: " + " → ".join(str(i + 1) for i in (*result.best_route, 0)))

        draw_route(self.route_figure, p, result)
        draw_history(self.history_figure, result.history)
        self.route_canvas.draw_idle()
        self.history_canvas.draw_idle()

        detail = asdict(result)
        detail["dataset_source"] = p.source
        detail["dimension"] = p.dimension
        detail["note"] = (
            "History hiển thị tối đa 200 snapshot cuối; JSON/CSV xuất đầy đủ. "
            "Chi phí theo ma trận, không mặc định km."
        )
        detail["history"] = detail["history"][-200:]
        if p.known_optimum is not None and p.known_optimum > 0:
            detail["relative_gap_percent"] = (
                100 * (result.best_distance - p.known_optimum) / p.known_optimum
            )
        self._set_details(detail)
        self._update_actions()

    def _set_details(self, values: dict) -> None:
        """Hiển thị chi tiết JSON trong tab Chi tiết."""
        self.details["state"] = "normal"
        self.details.delete("1.0", "end")
        text = json.dumps(values, ensure_ascii=False, indent=2)
        self.details.insert("1.0", text)
        self.details["state"] = "disabled"

    def save(self, kind: str) -> None:
        if self.result is None or self.controller.active:
            return
        extension = ".json" if kind == "json" else ".csv" if kind == "csv" else ".png"
        path = filedialog.asksaveasfilename(
            parent=self.root,
            title=f"Lưu kết quả {self.result.algorithm.upper()}",
            defaultextension=extension,
            initialfile=f"{self.result.problem_name}-{self.result.seed}-{kind}{extension}",
            filetypes=[(extension, "*" + extension)],
            confirmoverwrite=True,
        )
        if not path:
            return
        try:
            if kind == "json":
                export_json(self.result, path)
            elif kind == "csv":
                export_history(self.result, path)
            else:
                figure = self.route_figure if kind == "route" else self.history_figure
                figure.savefig(path, dpi=160, bbox_inches="tight")
        except (ValueError, OSError) as error:
            self._error("Không lưu được kết quả", error)
        else:
            self._set_status_badge(
                f"Đã lưu thành công: {Path(path).name}", COLORS.success, "✔"
            )

    def request_close(self) -> None:
        if self.closing:
            return
        if self.controller.active:
            if not messagebox.askyesno(
                "Đóng cửa sổ",
                "Solver đang chạy. Bạn có muốn dừng và đóng sau khi solver kết thúc?",
                parent=self.root,
            ):
                return
            self.closing = True
            self.controller.cancel()
            self._set_status_badge("Đang dừng worker trước khi đóng…", COLORS.warning, "⏳")
            self._update_actions()
        else:
            self._destroy()

    def _destroy(self) -> None:
        self.root.after_cancel(self.poll_id)
        for canvas in (self.route_canvas, self.history_canvas):
            # Hủy draw_idle pending trước khi hủy Tcl interpreter
            idle = canvas._idle_draw_id
            if idle:
                canvas.get_tk_widget().after_cancel(idle)
                canvas._idle_draw_id = None
        self.root.destroy()


def main() -> int:
    try:
        root = tk.Tk()
    except tk.TclError as error:
        print(f"Không mở được GUI Tkinter/display: {error}", file=sys.stderr)
        return 1
    Application(root)
    root.mainloop()
    return 0
