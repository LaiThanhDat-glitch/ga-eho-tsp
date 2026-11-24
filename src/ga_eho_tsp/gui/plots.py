"""Trực quan hóa đồ thị tuyến đường và hội tụ bằng Matplotlib cho GUI GA-EHO-TSP.

Không gọi solver hay thay đổi cấu trúc dữ liệu miền; toàn bộ màu sắc và kiểu dáng lấy từ theme.py.
"""

from collections.abc import Sequence
from math import cos, sin, tau

from matplotlib.figure import Figure

from ..domain.models import IterationStat, RunResult, TSPProblem
from .theme import COLORS, FONT_FAMILY

SCHEMATIC = "Sơ đồ minh họa, không phải vị trí địa lý"


def draw_route(figure: Figure, problem: TSPProblem, result: RunResult | None = None) -> None:
    """Vẽ hành trình TSP trên figure Matplotlib."""
    figure.clear()
    figure.patch.set_facecolor(COLORS.chart_bg)

    ax = figure.add_subplot(111)
    ax.set_facecolor(COLORS.chart_bg)

    points = problem.coordinates
    if points is None:
        points = tuple(
            (cos(tau * i / problem.dimension), sin(tau * i / problem.dimension))
            for i in range(problem.dimension)
        )

    # 1. Vẽ các cạnh của tour (nếu đã chạy)
    if result is not None:
        tour = (*result.best_route, result.best_route[0])
        xs = [points[i][0] for i in tour]
        ys = [points[i][1] for i in tour]

        # Đường tour chính
        ax.plot(
            xs,
            ys,
            color=COLORS.chart_route_edge,
            linewidth=2.0,
            alpha=0.85,
            zorder=2,
            solid_capstyle="round",
            solid_joinstyle="round",
        )

        # Mũi tên chỉ hướng đi giữa các thành phố
        for i in range(len(tour) - 1):
            u, v = tour[i], tour[i + 1]
            p1 = points[u]
            p2 = points[v]
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            # Đặt mũi tên tại vị trí khoảng 55% đoạn đường
            start_x = p1[0] + 0.40 * dx
            start_y = p1[1] + 0.40 * dy
            end_x = p1[0] + 0.58 * dx
            end_y = p1[1] + 0.58 * dy
            ax.annotate(
                "",
                xy=(end_x, end_y),
                xytext=(start_x, start_y),
                arrowprops=dict(
                    arrowstyle="-|>",
                    color=COLORS.chart_route_arrow,
                    lw=1.5,
                    mutation_scale=10,
                ),
                zorder=3,
            )

        title = f"{problem.name}  •  {result.algorithm.upper()}  •  Chi phí: {result.best_distance:g}"
    else:
        # Chưa chạy: vẽ vòng tròn kết nối mờ gợi ý
        title = f"{problem.name}  •  {problem.dimension} thành phố  •  Chưa chạy"
        ax.text(
            0,
            0,
            "Chưa có hành trình\n(Chọn cấu hình và nhấn 'Chạy')",
            ha="center",
            va="center",
            fontsize=9,
            color=COLORS.text_muted,
            style="italic",
            fontfamily=FONT_FAMILY,
            zorder=1,
        )

    # 2. Vẽ các nút thành phố (Nodes)
    node_size = 180 if problem.dimension <= 30 else (120 if problem.dimension <= 50 else 70)
    font_size = 8 if problem.dimension <= 30 else 7

    # Các node thông thường
    norm_x = [points[i][0] for i in range(1, problem.dimension)]
    norm_y = [points[i][1] for i in range(1, problem.dimension)]
    if norm_x:
        ax.scatter(
            norm_x,
            norm_y,
            s=node_size,
            color=COLORS.chart_route_node,
            edgecolors=COLORS.surface,
            linewidths=1.5,
            zorder=4,
            alpha=0.95 if result is not None else 0.6,
        )

    # Đánh số thứ tự thành phố (1-based: 1..n)
    for i, (x, y) in enumerate(points):
        label = str(i + 1)
        if i == 0:
            continue
        ax.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            color=COLORS.chart_route_node_text,
            fontsize=font_size,
            fontweight="bold",
            fontfamily=FONT_FAMILY,
            zorder=5,
        )

    # 3. Nút bắt đầu / kết thúc (Thành phố 1 - index 0) nổi bật
    start_point = points[0]
    ax.scatter(
        start_point[0],
        start_point[1],
        s=node_size * 1.5,
        color=COLORS.chart_route_start,
        edgecolors=COLORS.surface,
        linewidths=2.0,
        label="Khởi hành / Đích (TP 1)",
        zorder=6,
    )
    # Vòng tròn bao ngoài điểm bắt đầu
    ax.scatter(
        start_point[0],
        start_point[1],
        s=node_size * 2.3,
        facecolors="none",
        edgecolors=COLORS.chart_route_start,
        linewidths=1.5,
        linestyle="--",
        zorder=5,
    )
    ax.text(
        start_point[0],
        start_point[1],
        "1",
        ha="center",
        va="center",
        color="#FFFFFF",
        fontsize=font_size + 1,
        fontweight="bold",
        fontfamily=FONT_FAMILY,
        zorder=7,
    )

    ax.set_title(
        title,
        fontsize=10,
        fontweight="bold",
        pad=16,
        color=COLORS.text,
        fontfamily=FONT_FAMILY,
    )
    ax.legend(
        loc="lower left",
        fontsize=8,
        frameon=True,
        facecolor=COLORS.surface,
        edgecolor=COLORS.border,
    )
    ax.set_aspect("equal", adjustable="datalim")
    ax.margins(0.18)
    ax.set_axis_off()

    note_text = SCHEMATIC if problem.coordinates is None else "Tọa độ do dataset cung cấp"
    figure.text(
        0.5,
        0.02,
        note_text,
        ha="center",
        fontsize=8,
        color=COLORS.text_muted,
        fontfamily=FONT_FAMILY,
    )
    figure.subplots_adjust(left=0.06, right=0.94, top=0.90, bottom=0.08)


def draw_history(figure: Figure, history: Sequence[IterationStat]) -> None:
    """Vẽ biểu đồ hội tụ chi phí và độ đa dạng quần thể."""
    figure.clear()
    figure.patch.set_facecolor(COLORS.chart_bg)

    ax, diversity = figure.subplots(
        2, 1, sharex=True, gridspec_kw={"height_ratios": [3, 1]}
    )
    ax.set_facecolor(COLORS.chart_bg)
    diversity.set_facecolor(COLORS.chart_bg)

    # Định dạng spines & grid
    for panel in (ax, diversity):
        panel.spines["top"].set_visible(False)
        panel.spines["right"].set_visible(False)
        panel.spines["left"].set_color(COLORS.border_strong)
        panel.spines["bottom"].set_color(COLORS.border_strong)
        panel.tick_params(colors=COLORS.text_muted, labelsize=8)
        panel.grid(True, linestyle="--", alpha=0.5, color=COLORS.chart_grid)

    if history:
        x = [s.evaluations for s in history]

        # 3 đường chi phí với phân cấp thị giác rõ ràng
        ax.step(
            x,
            [s.best_so_far for s in history],
            where="post",
            label="Best toàn lịch sử",
            color=COLORS.chart_history_best_so_far,
            linewidth=2.0,
            zorder=4,
        )
        ax.step(
            x,
            [s.best_current for s in history],
            where="post",
            label="Best thế hệ hiện tại",
            color=COLORS.chart_history_best_current,
            linewidth=1.3,
            alpha=0.85,
            zorder=3,
        )
        ax.step(
            x,
            [s.mean_fitness for s in history],
            where="post",
            label="Trung bình thế hệ",
            color=COLORS.chart_history_mean,
            linewidth=1.1,
            linestyle="--",
            alpha=0.75,
            zorder=2,
        )

        # Đánh dấu điểm best cuối cùng bằng marker + annotation
        last_stat = history[-1]
        ax.scatter(
            last_stat.evaluations,
            last_stat.best_so_far,
            color=COLORS.chart_history_best_so_far,
            s=40,
            zorder=5,
        )
        ax.annotate(
            f" {last_stat.best_so_far:g}",
            (last_stat.evaluations, last_stat.best_so_far),
            xytext=(6, 0),
            textcoords="offset points",
            fontsize=8,
            fontweight="bold",
            color=COLORS.chart_history_best_so_far,
            fontfamily=FONT_FAMILY,
            va="center",
        )

        # Đường Diversity
        available = [s for s in history if s.population_diversity is not None]
        if available:
            diversity.step(
                [s.evaluations for s in available],
                [s.population_diversity for s in available],
                where="post",
                color=COLORS.chart_history_diversity,
                linewidth=1.4,
                label="Diversity",
            )
            diversity.legend(
                loc="upper right",
                fontsize=7,
                frameon=True,
                facecolor=COLORS.surface,
                edgecolor=COLORS.border,
            )

        ax.legend(
            loc="upper right",
            fontsize=8,
            frameon=True,
            facecolor=COLORS.surface,
            edgecolor=COLORS.border,
        )
    else:
        ax.text(
            0.5,
            0.5,
            "Chưa có dữ liệu lịch sử hội tụ",
            ha="center",
            va="center",
            transform=ax.transAxes,
            fontsize=9,
            color=COLORS.text_muted,
            style="italic",
            fontfamily=FONT_FAMILY,
        )

    ax.set_title(
        "Hội tụ từ snapshot thực của solver",
        fontsize=9,
        fontweight="bold",
        pad=8,
        color=COLORS.text,
        fontfamily=FONT_FAMILY,
    )
    ax.set_ylabel("Chi phí hành trình", fontsize=8, color=COLORS.text, fontfamily=FONT_FAMILY)
    diversity.set_xlabel(
        "Số lần đánh giá hàm mục tiêu (Evaluations)",
        fontsize=8,
        color=COLORS.text,
        fontfamily=FONT_FAMILY,
    )
    diversity.set_ylabel("Diversity", fontsize=8, color=COLORS.text, fontfamily=FONT_FAMILY)
    diversity.set_ylim(-0.05, 1.05)

    figure.subplots_adjust(left=0.14, right=0.96, top=0.91, bottom=0.13, hspace=0.22)
