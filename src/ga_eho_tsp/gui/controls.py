"""Form cấu hình GAConfig và EHOConfig cho GUI GA-EHO-TSP.

Đảm bảo hợp đồng dữ liệu schema domain, hiển thị nhãn thân thiện theo nhóm,
tích hợp help cố định và xử lý cuộn mượt mà không bị cắt widget.
"""

from dataclasses import asdict, replace
import tkinter as tk
from tkinter import ttk

from ..domain.models import EHOConfig, GAConfig
from .theme import COLORS, FONT_BODY, FONT_CODE, FONT_HEADING, FONT_SMALL, FONT_SUBHEADING

CHOICES = {
    "selection_method": ("tournament", "rank", "roulette_wheel"),
    "crossover_method": ("ox", "pmx"),
    "mutation_method": ("inversion", "swap", "insertion", "scramble"),
    "initialization_method": ("random", "nearest_neighbor", "mixed"),
}

OPTIONAL_INTS = {"max_evaluations", "stagnation_patience"}

ADVANCED = {
    "stagnation_patience", "adaptive_mutation", "adaptive_min_rate", "adaptive_max_rate",
    "adaptive_patience", "local_search_enabled", "local_search_max_moves",
    "local_search_max_probes", "time_limit_seconds", "record_history_every",
}

HELP = {
    "population_size": "Số tour trong quần thể, >= 4; ngân sách phải đủ cho quần thể ban đầu.",
    "generations": "Số thế hệ; thực tế chạy tối đa min(generations, max_iterations).",
    "max_iterations": "Giới hạn vòng lặp thứ hai; muốn vượt 250 cần tăng cả hai giới hạn.",
    "seed": "Seed số nguyên >= 0. Cùng cấu hình & seed sẽ cho kết quả tái lập tuyệt đối.",
    "max_evaluations": "Tổng số lần đánh giá hàm mục tiêu (gồm cả 2-opt probes). Trống = không giới hạn.",
    "elite_count": "Số cá thể tốt nhất giữ lại nguyên vẹn sang thế hệ sau, 0 <= elite < population_size.",
    "tournament_size": "Số ứng viên mỗi lần tournament (k), từ 2 đến population_size.",
    "mutation_rate": "Xác suất đột biến áp dụng trên toàn bộ tour con, trong khoảng [0, 1].",
    "crossover_rate": "Xác suất lai ghép cặp cha mẹ, trong khoảng [0, 1].",
    "initialization_method": "random: baseline ngẫu nhiên; nearest_neighbor/mixed: heuristic tham lam khởi đầu.",
    "nn_seed_fraction": "Tỷ lệ tour NN trong mixed, trong [0, 1]; không ép các tour phải duy nhất.",
    "local_search_enabled": "Kích hoạt GA + 2-opt (biến thể thực nghiệm tối ưu cục bộ).",
    "local_search_max_moves": "Khi tắt phải bằng 0; khi bật cần >= 1 bước cải thiện / con.",
    "local_search_max_probes": "Giới hạn số phép thử full objective cho mỗi con, >= 1.",
    "stagnation_patience": "Dừng sớm sau k thế hệ liên tiếp không cải thiện global best. Trống = tắt.",
    "time_limit_seconds": "Giới hạn thời gian chạy thực tế (giây). Trống = không giới hạn.",
    "record_history_every": "Lưu snapshot lịch sử mỗi k thế hệ; snapshot đầu và cuối luôn được lưu.",
    "adaptive_mutation": "Tự thích nghi xác suất đột biến theo độ trì trệ và tính đa dạng.",
    "adaptive_min_rate": "Cận dưới xác suất đột biến thích nghi [0, 1], <= max_rate.",
    "adaptive_max_rate": "Cận trên xác suất đột biến thích nghi [0, 1].",
    "adaptive_patience": "Số vòng lặp trì trệ để tăng áp lực đột biến thích nghi, >= 1.",
    "selection_method": "tournament (mặc định), rank hoặc roulette_wheel cho bài toán tối thiểu hóa chi phí.",
    "crossover_method": "OX (Order Crossover) hoặc PMX (Partially Mapped Crossover), luôn khóa thành phố 0.",
    "mutation_method": "inversion (đảo đoạn), swap (đổi chỗ), insertion (chèn) hoặc scramble (xáo trộn).",
}

FIELD_LABELS = {
    # GA Cơ bản
    "seed": "Seed ngẫu nhiên",
    "population_size": "Kích thước quần thể (P)",
    "generations": "Số thế hệ (generations)",
    "max_iterations": "Vòng lặp tối đa",
    "selection_method": "Chọn lọc (selection)",
    "tournament_size": "Kích thước giải đấu (k)",
    "crossover_method": "Lai ghép (crossover)",
    "crossover_rate": "Xác suất lai ghép",
    "mutation_method": "Đột biến (mutation)",
    "mutation_rate": "Xác suất đột biến",
    "elite_count": "Số cá thể tinh hoa (elites)",
    "initialization_method": "Phương pháp khởi tạo",
    "nn_seed_fraction": "Tỷ lệ Nearest-Neighbor",
    # GA Nâng cao
    "max_evaluations": "Giới hạn evaluations",
    "time_limit_seconds": "Giới hạn thời gian (giây)",
    "stagnation_patience": "Dừng khi trì trệ (vòng)",
    "record_history_every": "Tần suất lưu lịch sử",
    "adaptive_mutation": "Đột biến thích nghi",
    "adaptive_min_rate": "Xác suất đột biến min",
    "adaptive_max_rate": "Xác suất đột biến max",
    "adaptive_patience": "Chu kỳ thích nghi (vòng)",
    "local_search_enabled": "Bật tìm kiếm 2-opt",
    "local_search_max_moves": "Số bước 2-opt tối đa",
    "local_search_max_probes": "Số probe 2-opt tối đa",
}

GA_BASIC_SECTIONS = [
    ("Quần thể & Vòng lặp", ["seed", "population_size", "generations", "max_iterations"]),
    ("Toán tử Chọn lọc", ["selection_method", "tournament_size"]),
    ("Toán tử Lai ghép", ["crossover_method", "crossover_rate"]),
    ("Toán tử Đột biến", ["mutation_method", "mutation_rate"]),
    ("Khởi tạo & Tinh hoa", ["elite_count", "initialization_method", "nn_seed_fraction"]),
]

GA_ADVANCED_SECTIONS = [
    ("Ngân sách & Điều kiện dừng", ["max_evaluations", "time_limit_seconds", "stagnation_patience", "record_history_every"]),
    ("Đột biến thích nghi (Adaptive)", ["adaptive_mutation", "adaptive_min_rate", "adaptive_max_rate", "adaptive_patience"]),
    ("Tìm kiếm cục bộ (2-opt)", ["local_search_enabled", "local_search_max_moves", "local_search_max_probes"]),
]


def preset_config(name: str) -> GAConfig:
    """Preset cấu hình GA từ schema chuẩn."""
    default = GAConfig()
    if name == "Demo nhanh":
        return replace(default, population_size=40, generations=60, max_iterations=60)
    if name == "Giới hạn evaluations":
        return replace(default, generations=2000, max_iterations=2000, max_evaluations=6000,
                       record_history_every=5)
    return default


def parse_config(values: dict[str, str | bool]) -> GAConfig:
    """Chuyển đổi chuỗi từ form sang GAConfig hợp lệ."""
    defaults = asdict(GAConfig())
    parsed = {}
    for name, default in defaults.items():
        value = values[name]
        try:
            if type(default) is bool:
                if type(value) is not bool:
                    raise ValueError("cần giá trị bật/tắt")
                parsed[name] = value
            elif name in CHOICES:
                parsed[name] = str(value).strip().lower()
            elif name in OPTIONAL_INTS or name == "time_limit_seconds":
                text = str(value).strip()
                parsed[name] = None if not text else (float(text) if name == "time_limit_seconds" else int(text))
            else:
                parsed[name] = type(default)(str(value).strip())
        except (TypeError, ValueError) as error:
            expected = "số thực" if isinstance(default, float) or name == "time_limit_seconds" else "số nguyên"
            raise ValueError(f"{name}: cần {expected} hợp lệ. {HELP.get(name, '')}") from error
    return GAConfig(**parsed)


class ConfigForm(ttk.Frame):
    """Form tham số GA với phân nhóm trực quan, cuộn mượt và help cố định."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.variables: dict[str, tk.Variable] = {}
        self.widgets: list[ttk.Widget | tk.Widget] = []
        self.help_text = tk.StringVar(value="Chọn một tham số bất kỳ để xem giải thích chi tiết.")

        # Container chứa Notebook (phần trên) và Help Card (cố định bên dưới)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        tabs = ttk.Notebook(self)
        tabs.grid(row=0, column=0, sticky="nsew")

        sections_map = {
            False: GA_BASIC_SECTIONS,
            True: GA_ADVANCED_SECTIONS,
        }

        for advanced, title in ((False, "Cơ bản"), (True, "Nâng cao")):
            page = ttk.Frame(tabs)
            tabs.add(page, text=title)

            page.columnconfigure(0, weight=1)
            page.rowconfigure(0, weight=1)

            canvas = tk.Canvas(page, highlightthickness=0, bg=COLORS.surface)
            scroll = ttk.Scrollbar(page, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=scroll.set)

            canvas.grid(row=0, column=0, sticky="nsew")
            scroll.grid(row=0, column=1, sticky="ns")

            body = ttk.Frame(canvas, padding=(10, 8, 10, 20), style="Surface.TFrame")
            window = canvas.create_window((0, 0), window=body, anchor="nw")

            body.bind("<Configure>", lambda event, c=canvas: c.configure(scrollregion=c.bbox("all")))
            canvas.bind("<Configure>", lambda event, c=canvas, w=window: c.itemconfigure(w, width=event.width))

            body.columnconfigure(1, weight=1)

            current_row = 0
            for section_title, fields in sections_map[advanced]:
                # Section Header
                sec_header = ttk.Label(
                    body,
                    text=f"• {section_title}",
                    style="CardHeading.TLabel",
                    font=FONT_SUBHEADING,
                    foreground=COLORS.primary,
                )
                sec_header.grid(row=current_row, column=0, columnspan=2, sticky="w", pady=(8, 4))
                current_row += 1

                for name in fields:
                    default = getattr(GAConfig(), name)
                    label_text = FIELD_LABELS.get(name, name)
                    lbl = ttk.Label(body, text=label_text, style="Card.TLabel", font=FONT_BODY)
                    lbl.grid(row=current_row, column=0, sticky="w", pady=3, padx=(4, 8))

                    var = tk.BooleanVar(value=default) if type(default) is bool else tk.StringVar(
                        value="" if default is None else str(default)
                    )
                    self.variables[name] = var

                    if name in CHOICES:
                        widget = ttk.Combobox(
                            body,
                            textvariable=var,
                            values=CHOICES[name],
                            state="readonly",
                            width=18,
                        )
                    elif type(default) is bool:
                        widget = ttk.Checkbutton(body, text="Kích hoạt", variable=var)
                    else:
                        widget = ttk.Entry(body, textvariable=var, width=18)

                    widget.grid(row=current_row, column=1, sticky="ew", pady=3)
                    widget.bind("<FocusIn>", lambda event, n=name: self.help_text.set(HELP.get(n, n)))

                    # Cuộn chuột mượt mà khi hover vào ô
                    def _on_mousewheel(event, c=canvas):
                        c.yview_scroll(-int(event.delta / 120), "units")

                    widget.bind("<MouseWheel>", _on_mousewheel)
                    lbl.bind("<MouseWheel>", _on_mousewheel)
                    body.bind("<MouseWheel>", _on_mousewheel)

                    self.widgets.append(widget)
                    current_row += 1

                # Đường kẻ ngăn cách nhẹ giữa các section
                sep = ttk.Separator(body, orient="horizontal")
                sep.grid(row=current_row, column=0, columnspan=2, sticky="ew", pady=(4, 6))
                current_row += 1

        # Khung Help CỐ ĐỊNH ở dưới form, không bị cuộn mất
        help_card = tk.Frame(
            self,
            bg=COLORS.surface_variant,
            highlightbackground=COLORS.border,
            highlightthickness=1,
            padx=8,
            pady=6,
        )
        help_card.grid(row=1, column=0, sticky="ew", pady=(8, 0))

        help_title = tk.Label(
            help_card,
            text="ℹ Trợ giúp tham số:",
            font=FONT_SMALL,
            fg=COLORS.text,
            bg=COLORS.surface_variant,
            anchor="w",
        )
        help_title.pack(anchor="w")

        self.help_label = tk.Label(
            help_card,
            textvariable=self.help_text,
            font=FONT_SMALL,
            fg=COLORS.text_muted,
            bg=COLORS.surface_variant,
            justify="left",
            wraplength=360,
            anchor="w",
        )
        self.help_label.pack(fill="x", anchor="w", pady=(2, 0))

        # Cập nhật wraplength tự động khi form resize
        help_card.bind(
            "<Configure>",
            lambda event: self.help_label.configure(wraplength=max(200, event.width - 24)),
        )

    def config(self) -> GAConfig:
        return parse_config({name: var.get() for name, var in self.variables.items()})

    def set_config(self, config: GAConfig) -> None:
        for name, value in asdict(config).items():
            self.variables[name].set("" if value is None else value)

    def set_enabled(self, enabled: bool) -> None:
        for widget in self.widgets:
            if isinstance(widget, ttk.Combobox):
                widget["state"] = "readonly" if enabled else "disabled"
            else:
                widget["state"] = "normal" if enabled else "disabled"


class EHOConfigForm(ttk.Frame):
    """Form cấu hình tham số Elephant Herding Optimization (EHO)."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master, padding=(10, 10, 10, 10), style="Surface.TFrame")
        defaults = asdict(EHOConfig())
        self.variables: dict[str, tk.StringVar] = {}
        self.widgets: list[ttk.Widget | tk.Widget] = []

        ttk.Label(
            self,
            text="Tham số Elephant Herding Optimization (EHO)",
            style="CardHeading.TLabel",
            font=FONT_HEADING,
            foreground=COLORS.primary,
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        fields = (
            ("clan_count", "Số lượng Clan (đàn con)"),
            ("elephants_per_clan", "Số voi trong mỗi clan"),
            ("alpha", "Hệ số Clan (Alpha α)"),
            ("beta", "Hệ số Matriarch (Beta β)"),
            ("separation_count_per_clan", "Số voi tách clan (separation)"),
            ("max_iterations", "Vòng lặp tối đa"),
            ("max_evaluations", "Giới hạn evaluations"),
            ("seed", "Seed ngẫu nhiên"),
        )

        for row, (name, label) in enumerate(fields, start=1):
            lbl = ttk.Label(self, text=label, style="Card.TLabel", font=FONT_BODY)
            lbl.grid(row=row, column=0, sticky="w", padx=(0, 8), pady=4)

            value = defaults.get(name)
            if name == "max_iterations":
                value = defaults["iterations"]
            var = tk.StringVar(value="" if value is None else str(value))
            self.variables[name] = var

            entry = ttk.Entry(self, textvariable=var, width=16)
            entry.grid(row=row, column=1, sticky="ew", pady=3)
            self.widgets.append(entry)

        self.columnconfigure(1, weight=1)

        # Chú thích cố định bên dưới
        note_card = tk.Frame(
            self,
            bg=COLORS.surface_variant,
            highlightbackground=COLORS.border,
            highlightthickness=1,
            padx=8,
            pady=6,
        )
        note_card.grid(row=len(fields) + 1, column=0, columnspan=2, sticky="ew", pady=(12, 0))

        note_lbl = tk.Label(
            note_card,
            text="ℹ Gợi ý: Để trống 'Giới hạn evaluations' = không giới hạn.\nEHO áp dụng mô hình phân cụm clan và toán tử tách voi đực rời rạc.",
            font=FONT_SMALL,
            fg=COLORS.text_muted,
            bg=COLORS.surface_variant,
            justify="left",
            wraplength=340,
            anchor="w",
        )
        note_lbl.pack(fill="x", anchor="w")

        note_card.bind(
            "<Configure>",
            lambda event: note_lbl.configure(wraplength=max(200, event.width - 20)),
        )

    def config(self) -> EHOConfig:
        try:
            values = {
                name: (None if not text.strip() and name == "max_evaluations" else text.strip())
                for name, text in ((key, var.get()) for key, var in self.variables.items())
            }
            integer_fields = {
                "clan_count", "elephants_per_clan", "separation_count_per_clan",
                "max_iterations", "seed", "max_evaluations"
            }
            parsed = {
                key: (None if value is None else int(value)) if key in integer_fields else float(value)
                for key, value in values.items()
            }
        except (TypeError, ValueError) as error:
            raise ValueError("Tham số EHO phải là số hợp lệ.") from error
        parsed["iterations"] = parsed.pop("max_iterations")
        return EHOConfig(**parsed)

    def set_config(self, config: EHOConfig) -> None:
        for name, value in self.variables.items():
            field = "iterations" if name == "max_iterations" else name
            value.set("" if getattr(config, field) is None else str(getattr(config, field)))

    def set_enabled(self, enabled: bool) -> None:
        for widget in self.widgets:
            widget["state"] = "normal" if enabled else "disabled"
