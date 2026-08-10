#!/usr/bin/env python3
"""
Constellation plotting worksheets for kids.
- Real star positions (J2000 RA/Dec) projected onto a centered x,y plane
  (gnomonic projection, sky orientation: north up, east to the left).
- Scaled to fit an 8.5x11 landscape page, snapped to half-unit coordinates.
- Answer key: stars plotted, connected, labeled with (x, y).
- Worksheet: empty grid + coordinate table placed in dead space.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch
import string

# ---------------- page/grid geometry ----------------
PAGE_W, PAGE_H = 11.0, 8.5
GX, GY = 10, 7            # grid half-extents in units  (x: -10..10, y: -7..7)
UNIT = 0.5                # inches per unit -> grid area 10in x 7in
AX_W, AX_H = 2 * GX * UNIT, 2 * GY * UNIT
AX_X0 = (PAGE_W - AX_W) / 2.0
AX_Y0 = 0.45
FIT_X, FIT_Y = 9.5, 6.5   # keep stars within this box

NAVY = "#1a2e5a"
LINE = "#3a5da8"
GRID_MINOR = "#d7dee9"
GRID_MAJOR = "#b7c3d6"
AXIS_COL = "#33415c"

# ---------------- constellation data ----------------
# stars: (name, RA_hours, Dec_deg)  in letter order A, B, C ...
# paths: list of letter-strings; consecutive letters get connected.
CONSTELLATIONS = [
    dict(
        key="big_dipper", title="The Big Dipper",
        subtitle="part of Ursa Major, the Great Bear",
        stars=[("Alkaid", 13.792, 49.313), ("Mizar", 13.399, 54.925),
               ("Alioth", 12.900, 55.960), ("Megrez", 12.257, 57.033),
               ("Phecda", 11.897, 53.695), ("Merak", 11.030, 56.382),
               ("Dubhe", 11.062, 61.751)],
        paths=["ABCDEFGD"],
    ),
    dict(
        key="little_dipper", title="The Little Dipper",
        subtitle="Ursa Minor, the Little Bear — home of the North Star!",
        stars=[("Polaris", 2.530, 89.264), ("Yildun", 17.537, 86.586),
               ("Epsilon UMi", 16.766, 82.037), ("Zeta UMi", 15.734, 77.795),
               ("Eta UMi", 16.291, 75.755), ("Pherkad", 15.345, 71.834),
               ("Kochab", 14.845, 74.156)],
        paths=["ABCDEFGD"],
    ),
    dict(
        key="orion", title="Orion", subtitle="The Hunter",
        stars=[("Betelgeuse", 5.919, 7.407), ("Meissa", 5.585, 9.934),
               ("Bellatrix", 5.419, 6.350), ("Mintaka", 5.533, -0.299),
               ("Alnilam", 5.604, -1.202), ("Alnitak", 5.679, -1.943),
               ("Rigel", 5.242, -8.202), ("Saiph", 5.796, -9.670)],
        paths=["ABC", "CDEFA", "DGHF"],
    ),
    dict(
        key="scorpius", title="Scorpius", subtitle="The Scorpion",
        stars=[("Acrab", 16.090, -19.805), ("Dschubba", 16.005, -22.622),
               ("Pi Sco", 15.981, -26.114), ("Sigma Sco", 16.353, -25.593),
               ("Antares", 16.490, -26.432), ("Tau Sco", 16.598, -28.216),
               ("Epsilon Sco", 16.836, -34.293), ("Mu Sco", 16.864, -38.048),
               ("Zeta Sco", 16.910, -42.361), ("Eta Sco", 17.203, -43.239),
               ("Sargas", 17.622, -42.998), ("Iota Sco", 17.793, -40.127),
               ("Kappa Sco", 17.708, -39.030), ("Shaula", 17.560, -37.104),
               ("Lesath", 17.513, -37.296)],
        paths=["AB", "CB", "BDEFGHIJKLMNO"],
    ),
    dict(
        key="sagittarius", title="Sagittarius",
        subtitle='The Archer — find the "Teapot"!',
        stars=[("Alnasl", 18.096, -30.424), ("Kaus Australis", 18.403, -34.385),
               ("Ascella", 19.043, -29.880), ("Phi Sgr", 18.762, -26.991),
               ("Kaus Borealis", 18.466, -25.421), ("Kaus Media", 18.350, -29.828),
               ("Nunki", 18.921, -26.297), ("Tau Sgr", 19.115, -27.670)],
        paths=["ABCDEFA", "DGHC"],
    ),
    dict(
        key="draco", title="Draco", subtitle="The Dragon",
        stars=[("Giausar", 11.523, 69.331), ("Kappa Dra", 12.558, 69.788),
               ("Thuban", 14.073, 64.376), ("Edasich", 15.415, 58.966),
               ("Theta Dra", 16.031, 58.565), ("Eta Dra", 16.399, 61.514),
               ("Zeta Dra", 17.146, 65.715), ("Chi Dra", 18.351, 72.734),
               ("Tyl", 19.803, 70.268), ("Delta Dra", 19.209, 67.661),
               ("Grumium", 17.892, 56.873), ("Eltanin", 17.943, 51.489),
               ("Rastaban", 17.507, 52.301), ("Nu Dra", 17.537, 55.184)],
        paths=["ABCDEFGHIJK", "KLMNK"],
    ),
    dict(
        key="cassiopeia", title="Cassiopeia",
        subtitle='The Queen — the famous "W"',
        stars=[("Caph", 0.153, 59.150), ("Schedar", 0.675, 56.537),
               ("Gamma Cas", 0.945, 60.717), ("Ruchbah", 1.430, 60.235),
               ("Segin", 1.907, 63.670)],
        paths=["ABCDE"],
    ),
    dict(
        key="crux", title="Crux", subtitle="The Southern Cross",
        stars=[("Gacrux", 12.519, -57.113), ("Acrux", 12.443, -63.099),
               ("Mimosa", 12.795, -59.689), ("Imai", 12.252, -58.749),
               ("Ginan", 12.356, -60.401)],
        paths=["AB", "CD"],
        note="Star E (Ginan) is a bonus star — plot it, but no line!",
    ),
    dict(
        key="summer_triangle", title="The Summer Triangle",
        subtitle="three bright stars from three constellations",
        stars=[("Vega (in Lyra)", 18.616, 38.784),
               ("Deneb (in Cygnus)", 20.690, 45.280),
               ("Altair (in Aquila)", 19.846, 8.868)],
        paths=["ABCA"],
    ),
    dict(
        key="lyra", title="Lyra", subtitle="The Harp",
        stars=[("Vega", 18.616, 38.784), ("Epsilon Lyr", 18.739, 39.613),
               ("Zeta Lyr", 18.746, 37.605), ("Delta Lyr", 18.908, 36.899),
               ("Sulafat", 18.982, 32.690), ("Sheliak", 18.835, 33.363)],
        paths=["BAC", "CFEDC"],
    ),
    dict(
        key="cygnus", title="Cygnus",
        subtitle="The Swan — the Northern Cross",
        stars=[("Deneb", 20.690, 45.280), ("Sadr", 20.370, 40.257),
               ("Albireo", 19.512, 27.960), ("Delta Cyg", 19.750, 45.131),
               ("Gienah", 20.770, 33.970), ("Iota Cyg", 19.495, 51.729),
               ("Zeta Cyg", 21.215, 30.227)],
        paths=["ABC", "FDBEG"],
    ),
    dict(
        key="aquila", title="Aquila", subtitle="The Eagle",
        stars=[("Altair", 19.846, 8.868), ("Tarazed", 19.771, 10.613),
               ("Alshain", 19.921, 6.407), ("Okab", 19.090, 13.863),
               ("Delta Aql", 19.425, 3.115), ("Lambda Aql", 19.104, -4.882),
               ("Eta Aql", 19.874, 1.006), ("Theta Aql", 20.188, -0.821)],
        paths=["CAB", "BDEF", "EGH"],
    ),
]

# ---------------- projection & snapping ----------------
def project(stars):
    """Gnomonic projection centered on the constellation, north up, east left."""
    ra = np.array([s[1] for s in stars]) * 15.0 * np.pi / 180.0
    dec = np.array([s[2] for s in stars]) * np.pi / 180.0
    # centroid of unit vectors
    vx = np.cos(dec) * np.cos(ra); vy = np.cos(dec) * np.sin(ra); vz = np.sin(dec)
    cx, cy, cz = vx.mean(), vy.mean(), vz.mean()
    ra0 = np.arctan2(cy, cx); dec0 = np.arctan2(cz, np.hypot(cx, cy))
    d = ra - ra0
    cosc = np.sin(dec0) * np.sin(dec) + np.cos(dec0) * np.cos(dec) * np.cos(d)
    x = np.cos(dec) * np.sin(d) / cosc
    y = (np.cos(dec0) * np.sin(dec) - np.sin(dec0) * np.cos(dec) * np.cos(d)) / cosc
    return -x, y  # flip x: RA increases to the left (sky view)

def fit_and_snap(x, y, factor=1.0):
    x = x - (x.max() + x.min()) / 2.0
    y = y - (y.max() + y.min()) / 2.0
    sx = FIT_X / max(abs(x).max(), 1e-9)
    sy = FIT_Y / max(abs(y).max(), 1e-9)
    s = min(sx, sy) * factor
    xs = np.round(x * s * 2) / 2.0
    ys = np.round(y * s * 2) / 2.0
    # resolve any collisions after snapping
    pts = list(zip(xs, ys))
    for i in range(len(pts)):
        while pts[:i].count(pts[i]) > 0:
            pts[i] = (pts[i][0] + 0.5, pts[i][1])
    xs = np.array([p[0] for p in pts]); ys = np.array([p[1] for p in pts])
    return xs, ys

def fmt(v):
    return str(int(v)) if float(v).is_integer() else f"{v:g}"

# ---------------- drawing helpers ----------------
def make_axes(fig):
    ax = fig.add_axes([AX_X0 / PAGE_W, AX_Y0 / PAGE_H, AX_W / PAGE_W, AX_H / PAGE_H])
    ax.set_xlim(-GX, GX); ax.set_ylim(-GY, GY)
    ax.set_aspect("equal"); ax.axis("off")
    # minor grid (half units)
    for v in np.arange(-GX, GX + 0.001, 0.5):
        lw, c = (0.4, GRID_MINOR) if v % 1 else (0.7, GRID_MAJOR)
        ax.plot([v, v], [-GY, GY], lw=lw, color=c, zorder=0)
    for v in np.arange(-GY, GY + 0.001, 0.5):
        lw, c = (0.4, GRID_MINOR) if v % 1 else (0.7, GRID_MAJOR)
        ax.plot([-GX, GX], [v, v], lw=lw, color=c, zorder=0)
    # main axes
    ax.annotate("", xy=(GX + 0.35, 0), xytext=(-GX - 0.35, 0),
                arrowprops=dict(arrowstyle="-|>,head_width=0.25", color=AXIS_COL, lw=1.4), zorder=2)
    ax.annotate("", xy=(0, GY + 0.3), xytext=(0, -GY - 0.3),
                arrowprops=dict(arrowstyle="-|>,head_width=0.25", color=AXIS_COL, lw=1.4), zorder=2)
    ax.text(GX + 0.42, 0.25, "x", fontsize=11, style="italic", color=AXIS_COL, ha="left", va="center")
    ax.text(0.28, GY + 0.1, "y", fontsize=11, style="italic", color=AXIS_COL, ha="left", va="center")
    # tick labels on the axes
    for v in range(-GX, GX + 1):
        if v == 0: continue
        ax.text(v, -0.28, str(v), fontsize=6.5, ha="center", va="top", color=AXIS_COL, zorder=3)
        ax.plot([v, v], [-0.09, 0.09], lw=0.9, color=AXIS_COL, zorder=3)
    for v in range(-GY, GY + 1):
        if v == 0: continue
        ax.text(-0.22, v, str(v), fontsize=6.5, ha="right", va="center", color=AXIS_COL, zorder=3)
        ax.plot([-0.09, 0.09], [v, v], lw=0.9, color=AXIS_COL, zorder=3)
    ax.text(-0.22, -0.28, "0", fontsize=6.5, ha="right", va="top", color=AXIS_COL, zorder=3)
    return ax

def title_block(fig, c, answer_key):
    t = c["title"]
    fig.text(0.5, 0.955, t, fontsize=21, fontweight="bold", color=NAVY,
             ha="center", va="top", family="DejaVu Sans")
    fig.text(0.5, 0.916, c["subtitle"], fontsize=11.5, color="#4a5a7a",
             ha="center", va="top", style="italic")
    if answer_key:
        fig.text(0.985, 0.975, "ANSWER KEY", fontsize=13, fontweight="bold",
                 color="#b03030", ha="right", va="top")
    else:
        fig.text(0.015, 0.975, "Name: ____________________", fontsize=10,
                 color=AXIS_COL, ha="left", va="top")

def connect_text(paths):
    parts = [" → ".join(p) for p in paths]
    return parts

def path_segments(paths):
    segs = []
    for p in paths:
        for a, b in zip(p[:-1], p[1:]):
            segs.append((string.ascii_uppercase.index(a), string.ascii_uppercase.index(b)))
    return segs

# ------- table block placement -------
def table_geom(c):
    """Return dict with table layout numbers."""
    n = len(c["stars"])
    names = [s[0] for s in c["stars"]]
    name_w = max(2.1, 0.105 * max(len(nm) for nm in names) + 0.65)
    row_h = 0.48 if n <= 10 else 0.44
    col_w = 0.75 + name_w + 1.95
    rows_per = int(np.ceil(n / 2))
    conn = connect_text(c["paths"])
    extra_h = 0.4 * len(conn) + 0.5 + (0.38 if c.get("note") else 0)
    w_blk = col_w + 0.45
    single_h = 0.62 + (n + 1) * row_h + 0.15 + extra_h
    h1 = 0.62 + (rows_per + 1) * row_h + 0.15
    h2 = 0.62 + (n - rows_per + 1) * row_h + 0.15 + extra_h
    return dict(n=n, names=names, name_w=name_w, row_h=row_h,
                col_w=col_w, rows_per=rows_per, conn=conn,
                w_blk=w_blk, single_h=single_h, h1=h1, h2=h2)

def sample_lines(c, xs, ys, step=0.2):
    """Points along every connecting line (obstacles for table placement)."""
    pts = []
    for a, b in path_segments(c["paths"]):
        x1, y1, x2, y2 = xs[a], ys[a], xs[b], ys[b]
        n = max(2, int(np.hypot(x2 - x1, y2 - y1) / step))
        for t in np.linspace(0, 1, n):
            pts.append((x1 + t * (x2 - x1), y1 + t * (y2 - y1)))
    return pts

def find_block_pos(w, h, xs, ys, pad=1.15, avoid_rects=(), line_pts=(), line_pad=0.3):
    """Find top-left corner for a w x h block avoiding stars (with padding)."""
    cands = []
    xs_range = np.arange(-GX + 0.25, GX - w - 0.24, 0.25)
    ys_range = np.arange(-GY + h + 0.24, GY - 0.24, 0.25)
    lp = np.array(line_pts) if len(line_pts) else None
    for bx in xs_range:
        for by in ys_range:
            # block rect: (bx, by-h) to (bx+w, by)
            ok = True
            for sx, sy in zip(xs, ys):
                if bx - pad < sx < bx + w + pad and by - h - pad < sy < by + pad:
                    ok = False; break
            if ok and lp is not None:
                inside = ((lp[:, 0] > bx - line_pad) & (lp[:, 0] < bx + w + line_pad) &
                          (lp[:, 1] > by - h - line_pad) & (lp[:, 1] < by + line_pad))
                if inside.any(): ok = False
            if ok:
                for r in avoid_rects:
                    if rect_overlap((bx - 0.4, by - h - 0.4, bx + w + 0.4, by + 0.4), r):
                        ok = False; break
            if not ok: continue
            # prefer corners: distance from nearest corner of grid
            corner_d = min(
                np.hypot(bx + GX, by - GY), np.hypot(GX - (bx + w), by - GY),
                np.hypot(bx + GX, -GY - (by - h)), np.hypot(GX - (bx + w), -GY - (by - h)))
            # penalty for covering the axes (keeps origin/tick labels visible)
            axis_pen = 0.0
            if bx < 0.6 and bx + w > -0.6: axis_pen += 2.0
            if by > -0.8 and by - h < 0.8: axis_pen += 2.0
            cands.append((corner_d + axis_pen, bx, by))
    if not cands:
        return None
    cands.sort()
    return cands[0][1], cands[0][2]

def draw_block(ax, c, xs, ys, geom, pos, idx_range, title, with_connect, with_header=True):
    """Draw one table block (single column) with rows idx_range."""
    letters = string.ascii_uppercase
    names, name_w, row_h = geom["names"], geom["name_w"], geom["row_h"]
    w = geom["col_w"] + 0.45
    n_rows = len(idx_range)
    h = (0.62 if title else 0.2) + (n_rows + (1 if with_header else 0)) * row_h + 0.15
    total_h = h + (0.4 * len(geom["conn"]) + 0.5 +
                   (0.38 if c.get("note") else 0) if with_connect else 0)
    bx, by = pos
    r = FancyBboxPatch((bx, by - total_h), w, total_h,
                       boxstyle="round,pad=0.12,rounding_size=0.18",
                       fc="white", ec=NAVY, lw=1.2, zorder=4, alpha=0.97)
    ax.add_patch(r)
    ty = by - 0.15
    if title:
        ax.text(bx + w / 2, by - 0.42, title, fontsize=10.5, fontweight="bold",
                color=NAVY, ha="center", va="center", zorder=6)
        ty = by - 0.7
    cx0 = bx + 0.22
    yy = ty - row_h / 2
    if with_header:
        ax.text(cx0 + 0.35, yy, "Pt", fontsize=7.5, fontweight="bold", color=NAVY,
                ha="center", va="center", zorder=6)
        ax.text(cx0 + 0.8, yy, "Star", fontsize=7.5, fontweight="bold", color=NAVY,
                ha="left", va="center", zorder=6)
        ax.text(cx0 + 0.75 + name_w + 1.0, yy, "(x, y)", fontsize=7.5, fontweight="bold",
                color=NAVY, ha="center", va="center", zorder=6)
        ax.plot([cx0, cx0 + geom["col_w"] - 0.3], [yy - row_h / 2 + 0.03] * 2,
                lw=0.8, color=GRID_MAJOR, zorder=6)
        yy -= row_h
    for i in idx_range:
        ax.text(cx0 + 0.35, yy, letters[i], fontsize=8, fontweight="bold",
                color="#b03030", ha="center", va="center", zorder=6)
        ax.text(cx0 + 0.8, yy, names[i], fontsize=7.5, color="#222",
                ha="left", va="center", zorder=6)
        ax.text(cx0 + 0.75 + name_w + 1.0, yy,
                f"({fmt(xs[i])}, {fmt(ys[i])})", fontsize=8, color="#222",
                ha="center", va="center", zorder=6)
        yy -= row_h
    if with_connect:
        cy0 = yy - 0.05
        ax.text(bx + 0.25, cy0, "Connect the dots:", fontsize=8.5, fontweight="bold",
                color=NAVY, ha="left", va="center", zorder=6)
        yy = cy0 - 0.4
        for line in geom["conn"]:
            ax.text(bx + 0.4, yy, line, fontsize=8, color="#222",
                    ha="left", va="center", zorder=6)
            yy -= 0.4
        if c.get("note"):
            ax.text(bx + 0.25, yy, c["note"], fontsize=7.5, style="italic",
                    color="#4a5a7a", ha="left", va="center", zorder=6)
    return (bx - 0.15, by - total_h - 0.15, bx + w + 0.15, by + 0.15)

def draw_table(ax, c, xs, ys, geom, place):
    rects = []
    if place["mode"] == "single":
        n = geom["n"]
        # single-column block with all rows
        rects.append(draw_block(ax, c, xs, ys, geom, place["pos1"], range(n),
                                "Star Points to Plot", with_connect=True))
    else:
        half = geom["rows_per"]
        n = geom["n"]
        L = string.ascii_uppercase
        rects.append(draw_block(ax, c, xs, ys, geom, place["pos1"], range(half),
                                f"Star Points ({L[0]}–{L[half-1]})", with_connect=False))
        rects.append(draw_block(ax, c, xs, ys, geom, place["pos2"], range(half, n),
                                f"Star Points ({L[half]}–{L[n-1]})", with_connect=True))
    return rects

def label_offsets():
    return [(0.3, 0.3), (-0.3, 0.3), (0.3, -0.42), (-0.3, -0.42),
            (0.6, 0), (-0.6, 0), (0, 0.5), (0, -0.58),
            (0.75, 0.55), (-0.75, 0.55), (0.75, -0.65), (-0.75, -0.65)]

def rect_overlap(r1, r2):
    return not (r1[2] < r2[0] or r2[2] < r1[0] or r1[3] < r2[1] or r2[3] < r1[1])

def label_rect(lx, ly, ha, va, w=2.1, h=0.55):
    x0 = lx if ha == "left" else (lx - w if ha == "right" else lx - w / 2)
    y0 = ly if va == "bottom" else (ly - h if va == "top" else ly - h / 2)
    return (x0, y0, x0 + w, y0 + h)

def draw_stars(ax, c, xs, ys, block_rects, labeled=True):
    letters = string.ascii_uppercase
    for a, b in path_segments(c["paths"]):
        ax.plot([xs[a], xs[b]], [ys[a], ys[b]], lw=2.0, color=LINE, zorder=7,
                solid_capstyle="round")
    ax.scatter(xs, ys, s=95, marker="*", color="#e8a90c", edgecolor="#8a6400",
               linewidth=0.7, zorder=8)
    if not labeled:
        return
    placed = []   # rects of placed labels
    for i in range(len(xs)):
        best, bestscore = None, -1e9
        for dx, dy in label_offsets():
            lx, ly = xs[i] + dx, ys[i] + dy
            ha = "left" if dx > 0 else ("right" if dx < 0 else "center")
            va = "bottom" if dy > 0 else ("top" if dy < 0 else "center")
            rect = label_rect(lx, ly, ha, va)
            score = 0.0
            if rect[0] < -GX + 0.1 or rect[2] > GX - 0.1 or rect[1] < -GY + 0.1 or rect[3] > GY - 0.1:
                score -= 30
            for br in block_rects:
                if rect_overlap(rect, br): score -= 60
            for pr in placed:
                if rect_overlap(rect, pr): score -= 40
            for j in range(len(xs)):
                if j == i: continue
                sx, sy = xs[j], ys[j]
                if rect[0] - 0.25 < sx < rect[2] + 0.25 and rect[1] - 0.25 < sy < rect[3] + 0.25:
                    score -= 25
            score -= 0.35 * np.hypot(dx, dy)  # prefer close offsets, all else equal
            if score > bestscore:
                bestscore, best = score, (lx, ly, ha, va, rect)
        lx, ly, ha, va, rect = best
        placed.append(rect)
        ax.annotate(f"{letters[i]} ({fmt(xs[i])}, {fmt(ys[i])})",
                    xy=(xs[i], ys[i]), xytext=(lx, ly), ha=ha, va=va,
                    fontsize=8, fontweight="bold", color=NAVY, zorder=9,
                    bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.75))

def make_page(c, xs, ys, geom, place, answer_key):
    fig = plt.figure(figsize=(PAGE_W, PAGE_H))
    ax = make_axes(fig)
    title_block(fig, c, answer_key)
    rects = draw_table(ax, c, xs, ys, geom, place)
    if answer_key:
        draw_stars(ax, c, xs, ys, rects, labeled=True)
    return fig

# ---------------- build ----------------
FACTORS = (1.0, 0.94, 0.88, 0.82, 0.76, 0.7)

def layout(c):
    """Project, then shrink until the table fits in true dead space."""
    x, y = project(c["stars"])
    geom = table_geom(c)
    n = geom["n"]
    modes = ["single", "split"] if n <= 9 else ["split", "single"]
    for mode in modes:
        for factor in FACTORS:
            xs, ys = fit_and_snap(x, y, factor)
            lpts = sample_lines(c, xs, ys)
            if mode == "single":
                pos = find_block_pos(geom["w_blk"], geom["single_h"], xs, ys, pad=1.05,
                                     line_pts=lpts)
                if pos is not None:
                    return xs, ys, geom, dict(mode="single", pos1=pos), factor
            else:
                pos1 = find_block_pos(geom["w_blk"], geom["h1"], xs, ys, pad=1.05,
                                      line_pts=lpts)
                if pos1 is None: continue
                r1 = (pos1[0] - 0.15, pos1[1] - geom["h1"] - 0.15,
                      pos1[0] + geom["w_blk"] + 0.15, pos1[1] + 0.15)
                pos2 = find_block_pos(geom["w_blk"], geom["h2"], xs, ys, pad=1.05,
                                      avoid_rects=[r1], line_pts=lpts)
                if pos2 is not None:
                    return xs, ys, geom, dict(mode="split", pos1=pos1, pos2=pos2), factor
    xs, ys = fit_and_snap(x, y, 1.0)
    pos = find_block_pos(geom["w_blk"], geom["single_h"], xs, ys, pad=0.5,
                         line_pts=sample_lines(c, xs, ys)) or (-GX + 0.3, GY - 0.3)
    return xs, ys, geom, dict(mode="single", pos1=pos), 1.0

def main():
    layouts = {}
    for c in CONSTELLATIONS:
        xs, ys, geom, place, factor = layout(c)
        layouts[c["key"]] = (xs, ys, geom, place)
        print(f"{c['key']}: factor={factor} mode={place['mode']} "
              f"pos1=({place['pos1'][0]:.2f}, {place['pos1'][1]:.2f})"
              + (f" pos2=({place['pos2'][0]:.2f}, {place['pos2'][1]:.2f})"
                 if place["mode"] == "split" else ""))
    for fname, key_flag in [("Constellation_Worksheets.pdf", False),
                            ("Constellation_Answer_Keys.pdf", True)]:
        with PdfPages("/home/claude/out/" + fname) as pdf:
            for c in CONSTELLATIONS:
                xs, ys, geom, place = layouts[c["key"]]
                fig = make_page(c, xs, ys, geom, place, answer_key=key_flag)
                pdf.savefig(fig); plt.close(fig)
    print("done")

if __name__ == "__main__":
    main()
