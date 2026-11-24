"""Hệ thống thiết kế giao diện (Design System) tập trung cho GA-EHO-TSP GUI.

Cung cấp bảng màu, typography, khoảng cách và hàm apply_theme định dạng toàn bộ ttk widgets.
"""

from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk


@dataclass(frozen=True)
class ColorPalette:
    # Màu nhận diện chính (Primary - Blue 600)
    primary: str = "#2563EB"
    primary_hover: str = "#1D4ED8"
    primary_pressed: str = "#1E40AF"
    primary_disabled: str = "#93C5FD"
    primary_light: str = "#EFF6FF"

    # Màu điểm nhấn (Accent - Orange/Amber 600)
    accent: str = "#EA580C"
    accent_hover: str = "#C2410C"
    accent_light: str = "#FFF7ED"

    # Nền và bề mặt (Slate system)
    background: str = "#F8FAFC"       # Slate-50: nền chính của app
    surface: str = "#FFFFFF"          # Trắng: nền card, dialog
    surface_variant: str = "#F1F5F9"  # Slate-100: nền phụ, tab chưa chọn
    surface_hover: str = "#E2E8F0"    # Slate-200: hover nhẹ
    card_bg: str = "#FFFFFF"

    # Viền phân cách
    border: str = "#E2E8F0"           # Slate-200
    border_strong: str = "#CBD5E1"    # Slate-300
    border_focus: str = "#3B82F6"     # Blue-500

    # Màu chữ
    text: str = "#0F172A"             # Slate-900: chữ đậm rõ
    text_muted: str = "#64748B"       # Slate-500: chữ phụ, chú thích
    text_subtle: str = "#94A3B8"      # Slate-400
    text_on_primary: str = "#FFFFFF"
    text_on_danger: str = "#FFFFFF"

    # Trạng thái
    success: str = "#10B981"          # Emerald-500
    success_bg: str = "#ECFDF5"       # Emerald-50
    success_text: str = "#065F46"     # Emerald-800
    warning: str = "#F59E0B"          # Amber-500
    warning_bg: str = "#FFFBEB"       # Amber-50
    warning_text: str = "#92400E"     # Amber-800
    danger: str = "#EF4444"           # Red-500
    danger_hover: str = "#DC2626"
    danger_pressed: str = "#B91C1C"
    danger_disabled: str = "#FCA5A5"
    danger_bg: str = "#FEF2F2"
    danger_text: str = "#991B1B"
    info: str = "#0284C7"             # Sky-600
    info_bg: str = "#F0F9FF"

    # Nút phụ (Secondary)
    secondary_bg: str = "#F1F5F9"
    secondary_hover: str = "#E2E8F0"
    secondary_pressed: str = "#CBD5E1"
    secondary_text: str = "#334155"

    # Màu cho biểu đồ Matplotlib
    chart_bg: str = "#FFFFFF"
    chart_history_best_so_far: str = "#2563EB"   # Blue
    chart_history_best_current: str = "#EA580C"  # Amber/Orange
    chart_history_mean: str = "#64748B"          # Slate
    chart_history_diversity: str = "#10B981"     # Emerald
    chart_route_node: str = "#3B82F6"            # Node bình thường
    chart_route_node_text: str = "#FFFFFF"
    chart_route_start: str = "#EA580C"           # Điểm bắt đầu
    chart_route_edge: str = "#1E40AF"            # Cạnh tour
    chart_route_arrow: str = "#2563EB"           # Mũi tên
    chart_grid: str = "#E2E8F0"


COLORS = ColorPalette()

# Typography (Segoe UI chuẩn Windows, fallback sans-serif; Consolas cho code)
FONT_FAMILY = "Segoe UI"
FONT_MONO = "Consolas"

FONT_TITLE = (FONT_FAMILY, 13, "bold")
FONT_SUBTITLE = (FONT_FAMILY, 9)
FONT_HEADING = (FONT_FAMILY, 10, "bold")
FONT_SUBHEADING = (FONT_FAMILY, 9, "bold")
FONT_BODY = (FONT_FAMILY, 9)
FONT_BODY_BOLD = (FONT_FAMILY, 9, "bold")
FONT_SMALL = (FONT_FAMILY, 8)
FONT_SMALL_BOLD = (FONT_FAMILY, 8, "bold")
FONT_CODE = (FONT_MONO, 9)
FONT_STAT_VAL = (FONT_FAMILY, 11, "bold")
FONT_STAT_LBL = (FONT_FAMILY, 8)
FONT_BADGE = (FONT_FAMILY, 8, "bold")

# Spacing
SPACING_XS = 4
SPACING_SM = 8
SPACING_MD = 12
SPACING_LG = 16


def apply_theme(root: tk.Misc) -> ttk.Style:
    """Áp dụng theme clam với hệ thống màu và typography hiện đại."""
    style = ttk.Style(root)
    style.theme_use("clam")

    if isinstance(root, tk.Tk):
        root.configure(bg=COLORS.background)

    # 1. Base frames & Card
    style.configure("TFrame", background=COLORS.background)
    style.configure("Card.TFrame", background=COLORS.surface, relief="solid", borderwidth=1, bordercolor=COLORS.border)
    style.configure("Surface.TFrame", background=COLORS.surface)
    style.configure("Header.TFrame", background=COLORS.surface)

    # 2. Labels
    style.configure("TLabel", background=COLORS.background, foreground=COLORS.text, font=FONT_BODY)
    style.configure("Title.TLabel", background=COLORS.surface, foreground=COLORS.text, font=FONT_TITLE)
    style.configure("Subtitle.TLabel", background=COLORS.surface, foreground=COLORS.text_muted, font=FONT_SUBTITLE)
    style.configure("Heading.TLabel", background=COLORS.surface, foreground=COLORS.text, font=FONT_HEADING)
    style.configure("Subheading.TLabel", background=COLORS.surface, foreground=COLORS.text, font=FONT_SUBHEADING)
    style.configure("Muted.TLabel", background=COLORS.surface, foreground=COLORS.text_muted, font=FONT_SMALL)
    style.configure("Status.TLabel", font=FONT_BODY_BOLD)

    # Label trong Card/Surface
    style.configure("Card.TLabel", background=COLORS.surface, foreground=COLORS.text, font=FONT_BODY)
    style.configure("CardMuted.TLabel", background=COLORS.surface, foreground=COLORS.text_muted, font=FONT_SMALL)
    style.configure("CardHeading.TLabel", background=COLORS.surface, foreground=COLORS.text, font=FONT_HEADING)

    # Badge styles
    style.configure("Badge.TLabel", font=FONT_BADGE, padding=(6, 2), relief="flat")

    # 3. Buttons
    # Base TButton
    style.configure(
        "TButton",
        font=FONT_BODY_BOLD,
        padding=(10, 5),
        background=COLORS.secondary_bg,
        foreground=COLORS.secondary_text,
        bordercolor=COLORS.border,
        darkcolor=COLORS.secondary_bg,
        lightcolor=COLORS.secondary_bg,
        relief="flat",
        borderwidth=1,
    )
    style.map(
        "TButton",
        background=[("pressed", COLORS.secondary_pressed), ("active", COLORS.secondary_hover), ("disabled", COLORS.surface_variant)],
        foreground=[("disabled", COLORS.text_subtle)],
        bordercolor=[("active", COLORS.border_strong), ("disabled", COLORS.border)],
    )

    # Primary.TButton (Nút Chạy - Xanh dương)
    style.configure(
        "Primary.TButton",
        font=FONT_BODY_BOLD,
        padding=(14, 6),
        background=COLORS.primary,
        foreground=COLORS.text_on_primary,
        bordercolor=COLORS.primary,
        darkcolor=COLORS.primary,
        lightcolor=COLORS.primary,
        relief="flat",
        borderwidth=0,
    )
    style.map(
        "Primary.TButton",
        background=[
            ("pressed", COLORS.primary_pressed),
            ("active", COLORS.primary_hover),
            ("disabled", COLORS.primary_disabled),
        ],
        foreground=[("disabled", "#DBEAFE")],
    )

    # Danger.TButton (Nút Dừng - Đỏ)
    style.configure(
        "Danger.TButton",
        font=FONT_BODY_BOLD,
        padding=(12, 6),
        background=COLORS.danger,
        foreground=COLORS.text_on_danger,
        bordercolor=COLORS.danger,
        darkcolor=COLORS.danger,
        lightcolor=COLORS.danger,
        relief="flat",
        borderwidth=0,
    )
    style.map(
        "Danger.TButton",
        background=[
            ("pressed", COLORS.danger_pressed),
            ("active", COLORS.danger_hover),
            ("disabled", COLORS.danger_disabled),
        ],
        foreground=[("disabled", "#FEE2E2")],
    )

    # Secondary.TButton (Export, Duyệt file, Reset)
    style.configure(
        "Secondary.TButton",
        font=FONT_BODY,
        padding=(9, 4),
        background=COLORS.surface,
        foreground=COLORS.text,
        bordercolor=COLORS.border_strong,
        darkcolor=COLORS.surface,
        lightcolor=COLORS.surface,
        relief="solid",
        borderwidth=1,
    )
    style.map(
        "Secondary.TButton",
        background=[
            ("pressed", COLORS.secondary_pressed),
            ("active", COLORS.surface_variant),
            ("disabled", COLORS.surface),
        ],
        foreground=[("disabled", COLORS.text_subtle)],
        bordercolor=[("active", COLORS.primary), ("disabled", COLORS.border)],
    )

    # Action.TButton (Giữ tương thích ngược với code cũ)
    style.configure("Action.TButton", font=FONT_BODY_BOLD, padding=(12, 6))

    # 4. Entry & Combobox
    style.configure(
        "TEntry",
        fieldbackground=COLORS.surface,
        foreground=COLORS.text,
        bordercolor=COLORS.border,
        lightcolor=COLORS.border,
        darkcolor=COLORS.border,
        padding=(6, 4),
    )
    style.map(
        "TEntry",
        bordercolor=[("focus", COLORS.border_focus), ("invalid", COLORS.danger)],
    )

    style.configure(
        "TCombobox",
        fieldbackground=COLORS.surface,
        background=COLORS.surface_variant,
        foreground=COLORS.text,
        bordercolor=COLORS.border,
        arrowcolor=COLORS.text_muted,
        padding=(6, 4),
    )
    style.map(
        "TCombobox",
        fieldbackground=[("readonly", COLORS.surface), ("disabled", COLORS.surface_variant)],
        bordercolor=[("focus", COLORS.border_focus), ("active", COLORS.border_strong)],
        arrowcolor=[("disabled", COLORS.text_subtle), ("active", COLORS.primary)],
    )

    # 5. Checkbutton
    style.configure(
        "TCheckbutton",
        background=COLORS.surface,
        foreground=COLORS.text,
        font=FONT_BODY,
        indicatormargins=(0, 0, 4, 0),
    )

    # 6. Notebook & Tab
    style.configure(
        "TNotebook",
        background=COLORS.background,
        borderwidth=0,
        tabmargins=(2, 2, 2, 0),
    )
    style.configure(
        "TNotebook.Tab",
        font=FONT_BODY_BOLD,
        padding=(16, 6),
        background=COLORS.surface_variant,
        foreground=COLORS.text_muted,
        bordercolor=COLORS.border,
        lightcolor=COLORS.surface_variant,
        darkcolor=COLORS.surface_variant,
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", COLORS.surface), ("active", COLORS.surface_hover)],
        foreground=[("selected", COLORS.primary), ("active", COLORS.text)],
        bordercolor=[("selected", COLORS.border)],
    )

    # 7. Labelframe
    style.configure(
        "TLabelframe",
        background=COLORS.surface,
        bordercolor=COLORS.border,
        relief="solid",
        borderwidth=1,
    )
    style.configure(
        "TLabelframe.Label",
        background=COLORS.surface,
        foreground=COLORS.text,
        font=FONT_HEADING,
    )

    # 8. Progressbar
    style.configure(
        "Horizontal.TProgressbar",
        troughcolor=COLORS.surface_variant,
        background=COLORS.primary,
        bordercolor=COLORS.border,
        lightcolor=COLORS.primary,
        darkcolor=COLORS.primary,
        borderwidth=0,
        thickness=10,
    )

    # 9. Scrollbar
    style.configure(
        "Vertical.TScrollbar",
        background=COLORS.surface_variant,
        troughcolor=COLORS.background,
        bordercolor=COLORS.border,
        arrowcolor=COLORS.text_muted,
        relief="flat",
        borderwidth=0,
    )
    style.map(
        "Vertical.TScrollbar",
        background=[("pressed", COLORS.border_strong), ("active", COLORS.surface_hover)],
    )

    # 10. Separator
    style.configure("TSeparator", background=COLORS.border)

    return style
