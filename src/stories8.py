# -*- coding: utf-8 -*-
"""Story data: Euclid and the Elements. Every checkpoint is a problem or proof step from the Elements."""
import math

# ---------------------------------------------------------------------------
# Diagram helper (same conventions as stories7: math y-axis up, figures drawn
# from real coordinates so every picture is true to the numbers in the text).
# ---------------------------------------------------------------------------
A_COL, B_COL, C_COL = "#3a5da8", "#e8a90c", "#b03030"
A_FILL, B_FILL, C_FILL = "rgba(58,93,168,.22)", "rgba(232,169,12,.30)", "rgba(176,48,48,.18)"
INK, TRI = "#22304f", "#e6d9b8"
LIGHT, GOLDQ = "#eef1fb", "#ffd97a"


class _Fig(object):
    def __init__(self, w, h, scale, ox, oy, label, dark=False):
        self.w, self.h, self.s, self.ox, self.oy = w, h, scale, ox, oy
        self.label, self.dark, self.parts = label, dark, []

    def xy(self, x, y):
        return (self.ox + x * self.s, self.oy - y * self.s)

    def poly(self, pts, fill="none", stroke=INK, sw=2, extra=""):
        p = " ".join("%.1f,%.1f" % self.xy(x, y) for x, y in pts)
        self.parts.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s" '
                          'stroke-linejoin="round"%s/>' % (p, fill, stroke, sw, extra))
        return self

    def line(self, x1, y1, x2, y2, stroke=INK, sw=2, dash=None):
        a, b = self.xy(x1, y1), self.xy(x2, y2)
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        self.parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                          'stroke-width="%s" stroke-linecap="round"%s/>' % (a[0], a[1], b[0], b[1], stroke, sw, d))
        return self

    def circle(self, x, y, r, stroke=INK, sw=2, fill="none", dash=None):
        c = self.xy(x, y)
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        self.parts.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="%s"%s/>'
                          % (c[0], c[1], r * self.s, fill, stroke, sw, d))
        return self

    def arc(self, cx, cy, r, a1, a2, stroke=INK, sw=2, fill="none"):
        """Arc of radius r round (cx, cy) from angle a1 to a2 (degrees, counter-clockwise).
        With a fill colour it becomes a wedge."""
        p1 = self.xy(cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
        p2 = self.xy(cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2)))
        large = 1 if ((a2 - a1) % 360) > 180 else 0
        rp = r * self.s
        if fill != "none":
            c = self.xy(cx, cy)
            d = "M%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 %d 0 %.1f,%.1f Z" % (c[0], c[1], p1[0], p1[1], rp, rp, large, p2[0], p2[1])
        else:
            d = "M%.1f,%.1f A%.1f,%.1f 0 %d 0 %.1f,%.1f" % (p1[0], p1[1], rp, rp, large, p2[0], p2[1])
        self.parts.append('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (d, fill, stroke, sw))
        return self

    def corner(self, x, y, dx1, dy1, dx2, dy2, size=0.4, stroke=INK):
        pts = [(x + dx1 * size, y + dy1 * size),
               (x + (dx1 + dx2) * size, y + (dy1 + dy2) * size),
               (x + dx2 * size, y + dy2 * size)]
        p = " ".join("%.1f,%.1f" % self.xy(a, b) for a, b in pts)
        self.parts.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.5"/>' % (p, stroke))
        return self

    def tick(self, x1, y1, x2, y2, n=1, stroke=INK, size=0.18):
        """Little equal-length marks across the middle of a side."""
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        for k in range(n):
            off = (k - (n - 1) / 2.0) * 0.16
            cx, cy = mx + ux * off, my + uy * off
            self.line(cx - uy * size, cy + ux * size, cx + uy * size, cy - ux * size, stroke, 2)
        return self

    def dot(self, x, y, r=4, fill=INK):
        c = self.xy(x, y)
        self.parts.append('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>' % (c[0], c[1], r, fill))
        return self

    def text(self, x, y, s, size=14, fill=None, bold=False, anchor="middle", italic=False, halo=True):
        c = self.xy(x, y)
        fill = fill or (LIGHT if self.dark else INK)
        h = ""
        if halo:
            h = ' stroke="%s" stroke-width="4" paint-order="stroke" stroke-linejoin="round"' % (
                "#141c42" if self.dark else "#fffdf4")
        self.parts.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s%s%s>%s</text>' % (
            c[0], c[1] + size * 0.35, size, fill, anchor,
            ' font-weight="bold"' if bold else "", ' font-style="italic"' if italic else "", h, s))
        return self

    def raw(self, s):
        self.parts.append(s)
        return self

    def svg(self):
        if self.dark:
            style = "display:block;margin:14px auto 6px;max-width:100%;height:auto;"
        else:
            style = "background:#fffdf4;border:1px solid #d9c9a3;border-radius:10px;max-width:100%;height:auto;"
        cls = "" if self.dark else ' class="illus"'
        return ('<svg%s width="%d" height="%d" viewBox="0 0 %d %d" role="img" aria-label="%s" style="%s">'
                '<g font-family="Georgia,serif">%s</g></svg>' % (
                    cls, self.w, self.h, self.w, self.h, self.label, style, "".join(self.parts)))


def _pol(r, deg):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


# ---- figures in the story text (light) ----
def _circle_defs():
    f = _Fig(345, 230, 1, 140, 115, "A circle with its centre, one radius and one diameter labelled")
    f.circle(0, 0, 90, INK, 2.5, "#fff8e6")
    f.line(-90, 0, 90, 0, A_COL, 3)
    rx, ry = _pol(90, 62)
    f.line(0, 0, rx, ry, C_COL, 3)
    f.dot(0, 0, 4.5)
    f.text(0, -16, "centre", 13, INK, italic=True)
    f.text(-45, 14, "diameter", 14, A_COL, True)
    f.text(32, 50, "radius", 14, C_COL, True, anchor="end")
    f.text(100, 62, "circle", 14, INK, True, anchor="start", halo=False)
    f.text(100, 44, "(the curved line)", 11, "#4a5878", anchor="start", italic=True, halo=False)
    return f.svg()


def _i32():
    f = _Fig(380, 230, 42, 70, 190, "Euclid's figure for Book One, Proposition 32: a triangle with a line through its "
             "top corner parallel to its base, and the angles matched by colour")
    A, B, C = (0, 0), (6, 0), (2, 3.5)
    angA = math.degrees(math.atan2(3.5, 2))
    angB = math.degrees(math.atan2(3.5, 4))
    f.poly([A, B, C], TRI, INK, 2.5)
    f.line(-1.2, 3.5, 6.6, 3.5, "#4a5878", 2, "6 4")
    f.arc(0, 0, 0.7, 0, angA, A_COL, 2.5, A_FILL)
    f.arc(6, 0, 0.8, 180 - angB, 180, "#8a6400", 2.5, B_FILL)
    f.arc(2, 3.5, 0.6, 180 + angA, 360 - angB, C_COL, 2.5, C_FILL)
    f.arc(2, 3.5, 0.75, 180, 180 + angA, A_COL, 2.5, A_FILL)
    f.arc(2, 3.5, 0.75, 360 - angB, 360, "#8a6400", 2.5, B_FILL)
    f.text(0.95, 0.42, "a", 15, A_COL, True)
    f.text(4.95, 0.33, "b", 15, "#8a6400", True)
    f.text(2.05, 2.55, "c", 15, C_COL, True)
    f.text(1.0, 3.17, "a", 15, A_COL, True)
    f.text(3.05, 3.2, "b", 15, "#8a6400", True)
    f.text(6.7, 3.85, "parallel to the base", 11, "#4a5878", anchor="end", italic=True, halo=False)
    return f.svg()


def _donkey():
    f = _Fig(380, 190, 50, 50, 150, "A donkey at one corner of a triangle and hay at another: the straight side is "
             "shorter than the way round by the third corner")
    A, B, C = (0, 0), (5.6, 0), (2.4, 2.4)
    f.line(A[0], A[1], C[0], C[1], "#8a6400", 2.5, "7 5")
    f.line(C[0], C[1], B[0], B[1], "#8a6400", 2.5, "7 5")
    f.line(A[0], A[1], B[0], B[1], "#1e7d43", 3.5)
    for p in (A, B, C):
        f.dot(p[0], p[1], 5)
    f.text(0, -0.42, "donkey", 14, INK, True)
    f.text(5.6, -0.42, "hay", 14, INK, True)
    f.text(2.8, 0.3, "straight: shorter", 13, "#1e7d43", True)
    f.text(2.4, 2.75, "the long way round", 13, "#8a6400", True)
    return f.svg()


def _ii4():
    f = _Fig(300, 270, 40, 60, 235, "A square whose side is cut into two parts a and b, divided into a square on a, "
             "a square on b and two rectangles a by b")
    a, b = 3, 2
    f.poly([(0, b), (a, b), (a, a + b), (0, a + b)], A_FILL, A_COL, 2)
    f.poly([(a, 0), (a + b, 0), (a + b, b), (a, b)], B_FILL, "#8a6400", 2)
    f.poly([(a, b), (a + b, b), (a + b, a + b), (a, a + b)], C_FILL, C_COL, 2)
    f.poly([(0, 0), (a, 0), (a, b), (0, b)], C_FILL, C_COL, 2)
    f.poly([(0, 0), (a + b, 0), (a + b, a + b), (0, a + b)], "none", INK, 3)
    f.text(a / 2.0, b + a / 2.0, "a&#178;", 20, A_COL, True)
    f.text(a + b / 2.0, b / 2.0, "b&#178;", 18, "#8a6400", True)
    f.text(a + b / 2.0, b + a / 2.0, "ab", 17, C_COL, True)
    f.text(a / 2.0, b / 2.0, "ab", 17, C_COL, True)
    f.text(a / 2.0, a + b + 0.3, "a", 15, INK, True, halo=False)
    f.text(a + b / 2.0, a + b + 0.3, "b", 15, INK, True, halo=False)
    f.text(-0.3, b + a / 2.0, "a", 15, INK, True, halo=False)
    f.text(-0.3, b / 2.0, "b", 15, INK, True, halo=False)
    return f.svg()


def _hexagon():
    f = _Fig(300, 270, 36, 150, 135, "A regular hexagon inside a circle, with spokes from the centre to every corner "
             "making six triangles")
    R = 3.2
    pts = [_pol(R, 60 * k) for k in range(6)]
    f.circle(0, 0, R, "#4a5878", 1.5, "#fff8e6")
    f.poly(pts, "rgba(232,169,12,.18)", INK, 2.5)
    for p in pts:
        f.line(0, 0, p[0], p[1], "#4a5878", 1.5, "4 4")
        f.dot(p[0], p[1], 3.5)
    f.poly([(0, 0), pts[0], pts[1]], A_FILL, A_COL, 2)
    f.arc(0, 0, 0.6, 0, 60, C_COL, 2)
    f.text(0.85, 0.48, "60&#176;", 12, C_COL, True)
    f.text(1.35, 0.58 + 0.9, "r", 15, A_COL, True)
    f.text(0.95, -0.25, "r", 15, A_COL, True)
    f.dot(0, 0, 4)
    return f.svg()


# ---- figures for the dark checkpoint panels ----
def _cp_cross():
    f = _Fig(320, 210, 46, 160, 110, "Two straight lines crossing. One angle is marked 130 degrees, the angle beside it "
             "is marked x, and the angle opposite it is marked y", dark=True)
    f.line(-3.2, 0, 3.2, 0, LIGHT, 2.5)
    p, q = _pol(2.3, 50), _pol(2.3, 230)
    f.line(q[0], q[1], p[0], p[1], LIGHT, 2.5)
    f.arc(0, 0, 0.62, 50, 180, B_COL, 2.5)
    f.arc(0, 0, 0.8, 0, 50, "#8fb0ff", 2.5)
    f.arc(0, 0, 0.62, 230, 360, GOLDQ, 2.5)
    f.text(-0.62, 0.88, "130&#176;", 14, B_COL, True)
    f.text(1.2, 0.48, "x", 17, "#8fb0ff", True)
    f.text(0.62, -0.92, "y", 17, GOLDQ, True)
    return f.svg()


def _cp_isosceles():
    h = 4.0
    b = h * math.tan(math.radians(20))
    f = _Fig(260, 230, 46, 130, 200, "An isosceles triangle with two equal sides, an angle of 40 degrees at the top, "
             "and question marks at the two bottom corners", dark=True)
    A, B, C = (-b, 0), (b, 0), (0, h)
    f.poly([A, B, C], "rgba(232,169,12,.16)", LIGHT, 2.5)
    f.tick(A[0], A[1], C[0], C[1], 2, LIGHT)
    f.tick(B[0], B[1], C[0], C[1], 2, LIGHT)
    f.arc(0, h, 0.75, 250, 290, B_COL, 2)
    f.text(0, h - 1.2, "40&#176;", 14, B_COL, True)
    f.text(-b + 0.5, 0.32, "?", 18, GOLDQ, True)
    f.text(b - 0.5, 0.32, "?", 18, GOLDQ, True)
    return f.svg()


def _cp_exterior():
    A, B = (0, 0), (5, 0)
    ac = 5 * math.sin(math.radians(60)) / math.sin(math.radians(70))
    C = _pol(ac, 50)
    E = (C[0] + 1.9 * math.cos(math.radians(50)), C[1] + 1.9 * math.sin(math.radians(50)))
    f = _Fig(340, 280, 44, 50, 250, "A triangle with angles of 50 and 60 degrees at the bottom. One side is extended "
             "past the top corner, and the outside angle there is marked with a question mark", dark=True)
    f.poly([A, B, C], "rgba(232,169,12,.16)", LIGHT, 2.5)
    f.line(C[0], C[1], E[0], E[1], LIGHT, 2.5, "6 4")
    f.arc(0, 0, 0.7, 0, 50, "#8fb0ff", 2.5)
    f.arc(5, 0, 0.7, 120, 180, "#8fb0ff", 2.5)
    f.arc(C[0], C[1], 0.55, -60, 50, GOLDQ, 2.5)
    f.text(1.2, 0.42, "50&#176;", 14, "#8fb0ff", True)
    f.text(3.9, 0.42, "60&#176;", 14, "#8fb0ff", True)
    f.text(C[0] + 0.95, C[1] + 0.05, "?", 19, GOLDQ, True)
    return f.svg()


def _cp_right():
    f = _Fig(330, 190, 16, 60, 160, "A right triangle with legs 8 and 15 and its long side marked with a question mark",
             dark=True)
    f.poly([(0, 0), (15, 0), (0, 8)], "rgba(232,169,12,.16)", LIGHT, 2.5)
    f.corner(0, 0, 1, 0, 0, 1, 1.1, LIGHT)
    f.text(7.5, -1.1, "15", 15, LIGHT, True)
    f.text(-1.1, 4, "8", 15, LIGHT, True)
    f.text(8.3, 5.2, "?", 20, GOLDQ, True)
    return f.svg()


def _cp_ii4():
    f = _Fig(250, 230, 25, 55, 205, "A square of side 7 whose sides are cut into 3 and 4: a 3 by 3 square, a 4 by 4 "
             "square and two rectangles marked with question marks", dark=True)
    a, b = 3, 4
    f.poly([(0, b), (a, b), (a, a + b), (0, a + b)], "rgba(58,93,168,.45)", LIGHT, 2)
    f.poly([(a, 0), (a + b, 0), (a + b, b), (a, b)], "rgba(232,169,12,.40)", LIGHT, 2)
    f.poly([(a, b), (a + b, b), (a + b, a + b), (a, a + b)], "rgba(176,48,48,.35)", LIGHT, 2)
    f.poly([(0, 0), (a, 0), (a, b), (0, b)], "rgba(176,48,48,.35)", LIGHT, 2)
    f.poly([(0, 0), (7, 0), (7, 7), (0, 7)], "none", LIGHT, 3)
    f.text(1.5, 5.5, "3 &#215; 3", 13, LIGHT, True)
    f.text(5, 2, "4 &#215; 4", 14, LIGHT, True)
    f.text(5, 5.5, "?", 19, GOLDQ, True)
    f.text(1.5, 2, "?", 19, GOLDQ, True)
    f.text(1.5, 7.45, "3", 13, LIGHT, halo=False)
    f.text(5, 7.45, "4", 13, LIGHT, halo=False)
    f.text(-0.45, 5.5, "3", 13, LIGHT, halo=False)
    f.text(-0.45, 2, "4", 13, LIGHT, halo=False)
    return f.svg()


def _cp_semicircle():
    R = 4.0
    C = _pol(R, 70)
    f = _Fig(340, 210, 36, 170, 180, "A triangle drawn in a semicircle, with the diameter as its long side. The angle at "
             "the left end is 35 degrees and the angle at the right end is marked with a question mark", dark=True)
    f.arc(0, 0, R, 0, 180, "#8fb0ff", 2)
    f.line(-R, 0, R, 0, "#8fb0ff", 2)
    f.poly([(-R, 0), (R, 0), C], "rgba(232,169,12,.16)", LIGHT, 2.5)
    ua = ((-R - C[0]) / math.hypot(-R - C[0], -C[1]), -C[1] / math.hypot(-R - C[0], -C[1]))
    ub = ((R - C[0]) / math.hypot(R - C[0], -C[1]), -C[1] / math.hypot(R - C[0], -C[1]))
    f.corner(C[0], C[1], ua[0], ua[1], ub[0], ub[1], 0.4, LIGHT)
    f.dot(0, 0, 3, LIGHT)
    f.arc(-R, 0, 1.0, 0, 35, "#8fb0ff", 2.5)
    f.text(-R + 1.55, 0.42, "35&#176;", 13, "#8fb0ff", True)
    f.text(R - 0.75, 0.55, "?", 19, GOLDQ, True)
    return f.svg()


def _cp_shadow():
    f = _Fig(360, 230, 1, 0, 0, "A 2 metre stick with a 3 metre shadow, and an obelisk with a 45 metre shadow and "
             "a question mark for its height. The sun's rays hit both at the same slant. Not to scale", dark=True)
    g = 200  # ground line, in pixels
    f.raw('<line x1="10" y1="%d" x2="350" y2="%d" stroke="#8f9cc4" stroke-width="2"/>' % (g, g))
    # stick: 2 m tall, 3 m shadow (24 px per metre)
    s = 24
    f.raw('<line x1="40" y1="%d" x2="40" y2="%d" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % (g, g - 2 * s, LIGHT))
    f.raw('<line x1="40" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>' % (g - 2 * s, 40 + 3 * s, g, GOLDQ))
    f.raw('<line x1="40" y1="%d" x2="%d" y2="%d" stroke="#5a6a9a" stroke-width="6"/>' % (g + 4, 40 + 3 * s, g + 4))
    # obelisk: 30 m tall, 45 m shadow (5 px per metre)
    k, x0 = 4, 160
    top = g - 30 * k
    f.raw('<polygon points="%d,%d %d,%d %d,%d %d,%d %d,%d" fill="rgba(232,169,12,.28)" stroke="%s" stroke-width="2"/>' % (
        x0 - 9, g, x0 + 9, g, x0 + 6, top + 10, x0, top, x0 - 6, top + 10, LIGHT))
    f.raw('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>' % (x0, top, x0 + 45 * k, g, GOLDQ))
    f.raw('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#5a6a9a" stroke-width="6"/>' % (x0, g + 4, x0 + 45 * k, g + 4))
    f.text(34, -(g - s), "2 m", 13, LIGHT, True, anchor="end")
    f.text(40 + 1.5 * s, -(g + 18), "3 m", 13, LIGHT, True)
    f.text(x0 - 16, -(g - 15 * k), "?", 20, GOLDQ, True, anchor="end")
    f.text(x0 + 22.5 * k, -(g + 18), "45 m", 13, LIGHT, True)
    f.text(345, -(30), "sun's rays", 11, GOLDQ, anchor="end", italic=True, halo=False)
    f.text(345, -(46), "not to scale", 10, "#8f9cc4", anchor="end", italic=True, halo=False)
    return f.svg()


def _cp_parallels():
    f = _Fig(340, 220, 42, 90, 170, "Two parallel lines crossed by a third line. Between the parallels, on the right of "
             "the crossing line, the lower angle is 65 degrees and the upper angle is marked with a question mark", dark=True)
    P = (1.0, 0.0)
    t = 3.0 / math.sin(math.radians(65))
    Q = (P[0] + t * math.cos(math.radians(65)), 3.0)
    f.line(-1.6, 0, 5.6, 0, LIGHT, 2.5)
    f.line(-1.6, 3, 5.6, 3, LIGHT, 2.5)
    for y in (0, 3):
        f.raw('<polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="2"/>' % (
            f.xy(4.6, y)[0] - 6, f.xy(4.6, y)[1] - 6, f.xy(4.6, y)[0], f.xy(4.6, y)[1],
            f.xy(4.6, y)[0] - 6, f.xy(4.6, y)[1] + 6, LIGHT))
    e1 = (P[0] - 0.9 * math.cos(math.radians(65)), -0.9 * math.sin(math.radians(65)))
    e2 = (Q[0] + 0.9 * math.cos(math.radians(65)), 3 + 0.9 * math.sin(math.radians(65)))
    f.line(e1[0], e1[1], e2[0], e2[1], "#8fb0ff", 2.5)
    f.arc(P[0], P[1], 0.6, 0, 65, B_COL, 2.5)
    f.arc(Q[0], Q[1], 0.55, 245, 360, GOLDQ, 2.5)
    f.text(P[0] + 1.05, 0.38, "65&#176;", 14, B_COL, True)
    f.text(Q[0] + 0.62, 3 - 0.6, "?", 19, GOLDQ, True)
    return f.svg()


# ---------------------------------------------------------------------------
# Live widgets
# ---------------------------------------------------------------------------
_BOX = 'background:#fdf9ee; border:1.5px solid #c9b57e; border-radius:12px; padding:14px 16px; margin:14px 0;'
_CAP = ('text-align:center; font-size:.8rem; letter-spacing:2px; text-transform:uppercase; '
        'color:#8a6400; font-weight:bold; margin-bottom:8px;')
_BTN = ('font-family:Georgia,serif; cursor:pointer; background:#fff8e6; border:1.5px solid #c9b57e; '
        'border-radius:8px; padding:7px 12px; font-size:.85rem; color:#5a4a1a;')
_GO = ('background:#e8a90c; color:#2a2005; font-weight:bold; font-size:1rem; border:none; border-radius:8px; '
       'padding:10px 20px; font-family:Georgia,serif; cursor:pointer;')

PROP1 = ('<div style="%s">\n  <div style="%s">Book I, Proposition 1 &middot; straightedge and compass</div>' % (_BOX, _CAP)) + r"""
  <div style="text-align:center;">
    <svg id="p1-svg" width="400" height="300" viewBox="0 0 400 300" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;" role="img" aria-label="Euclid's construction of an equilateral triangle, drawn one step at a time">
      <circle id="p1-c1" cx="150" cy="180" r="100" fill="rgba(58,93,168,.06)" stroke="#3a5da8" stroke-width="2" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1" style="opacity:0;"/>
      <circle id="p1-c2" cx="250" cy="180" r="100" fill="rgba(232,169,12,.07)" stroke="#8a6400" stroke-width="2" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1" style="opacity:0;"/>
      <line id="p1-ca" x1="200" y1="93.4" x2="150" y2="180" stroke="#b03030" stroke-width="3" stroke-linecap="round" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1"/>
      <line id="p1-cb" x1="200" y1="93.4" x2="250" y2="180" stroke="#b03030" stroke-width="3" stroke-linecap="round" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1"/>
      <line x1="150" y1="180" x2="250" y2="180" stroke="#22304f" stroke-width="3.5" stroke-linecap="round"/>
      <circle cx="150" cy="180" r="4.5" fill="#22304f"/><circle cx="250" cy="180" r="4.5" fill="#22304f"/>
      <text x="138" y="200" font-size="17" font-weight="bold" fill="#22304f" text-anchor="end" stroke="#fffdf4" stroke-width="4" paint-order="stroke">A</text>
      <text x="262" y="200" font-size="17" font-weight="bold" fill="#22304f" stroke="#fffdf4" stroke-width="4" paint-order="stroke">B</text>
      <g id="p1-c" style="opacity:0; transition:opacity .4s ease;">
        <circle cx="200" cy="93.4" r="5" fill="#b03030"/>
        <text x="200" y="78" font-size="17" font-weight="bold" fill="#b03030" text-anchor="middle" stroke="#fffdf4" stroke-width="4" paint-order="stroke">C</text>
      </g>
    </svg>
  </div>
  <div id="p1-step" style="text-align:center; font-size:.8rem; letter-spacing:1.5px; text-transform:uppercase; color:#8a6400; margin:8px 0 2px;">Step 0 of 4</div>
  <div id="p1-out" style="text-align:center; font-size:1rem; color:#3d3320; line-height:1.55; min-height:3.2em; max-width:560px; margin:0 auto 10px;"></div>
  <div style="text-align:center; display:flex; gap:8px; flex-wrap:wrap; justify-content:center;">
    <button type="button" id="p1-go" style="@@GO@@">Next step &#9654;</button>
    <button type="button" id="p1-reset" style="@@BTN@@">Start over</button>
  </div>
</div>
<script>
(function(){
  var go = document.getElementById('p1-go');
  if (!go) return;
  var step = 0;
  var MSG = [
    'You are given one straight line, <b>AB</b>. The job: build a triangle on it with all three sides equal. Your only tools are a straightedge (no markings) and a compass.',
    '<b>Postulate 3</b> lets you draw a circle with any centre and any radius. Put the compass point on <b>A</b> and open it to reach <b>B</b>. Draw.',
    'Now the same again the other way round: compass point on <b>B</b>, opened to reach <b>A</b>. Draw.',
    'The two circles cross. Call the top crossing point <b>C</b>.',
    '<b>Postulate 1</b> lets you draw a straight line between any two points. Join <b>C</b> to <b>A</b> and <b>C</b> to <b>B</b>. Euclid says triangle ABC has three equal sides. Can you say why? The checkpoint below asks.'
  ];
  function grow(id, on){
    var e = document.getElementById(id);
    e.style.transition = on ? 'stroke-dashoffset 1.1s ease, opacity .2s ease' : 'none';
    e.style.opacity = on ? 1 : (e.tagName === 'circle' ? 0 : 1);
    e.setAttribute('stroke-dashoffset', on ? 0 : 1);
  }
  function show(){
    grow('p1-c1', step >= 1);
    grow('p1-c2', step >= 2);
    document.getElementById('p1-c').style.opacity = step >= 3 ? 1 : 0;
    grow('p1-ca', step >= 4);
    grow('p1-cb', step >= 4);
    document.getElementById('p1-out').innerHTML = MSG[step];
    document.getElementById('p1-step').textContent = 'Step ' + step + ' of 4';
    go.disabled = step >= 4;
    go.style.opacity = step >= 4 ? 0.5 : 1;
    go.innerHTML = step >= 4 ? 'Done: Q.E.F.' : 'Next step &#9654;';
  }
  go.addEventListener('click', function(){ if (step < 4){ step++; show(); } });
  document.getElementById('p1-reset').addEventListener('click', function(){ step = 0; show(); });
  show();
})();
</script>"""

CROSSING = ('<div style="%s">\n  <div style="%s">Two crossing lines &middot; turn one of them</div>' % (_BOX, _CAP)) + r"""
  <div style="text-align:center;">
    <svg id="cx-svg" width="360" height="240" viewBox="0 0 360 240" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;" role="img" aria-label="Two straight lines crossing, with the four angles they make labelled"></svg>
  </div>
  <div id="cx-out" style="text-align:center; font-size:1rem; color:#3d3320; margin:8px 0 10px; line-height:1.6;"></div>
  <div style="max-width:440px; margin:0 auto;">
    <input id="cx-a" type="range" min="21" max="159" step="2" value="61" style="width:100%;" aria-label="turn the slanted line">
  </div>
</div>
<script>
(function(){
  var sl = document.getElementById('cx-a');
  if (!sl) return;
  var svg = document.getElementById('cx-svg'), NS = 'http://www.w3.org/2000/svg', CX = 180, CY = 120;
  function el(tag, attrs, text){
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    svg.appendChild(e); return e;
  }
  function pt(r, deg){ var a = deg * Math.PI / 180; return [CX + r * Math.cos(a), CY - r * Math.sin(a)]; }
  function wedge(r, a1, a2, fill, stroke){
    var p1 = pt(r, a1), p2 = pt(r, a2), large = (a2 - a1) > 180 ? 1 : 0;
    return el('path', {d: 'M' + CX + ',' + CY + ' L' + p1[0].toFixed(1) + ',' + p1[1].toFixed(1) + ' A' + r + ',' + r + ' 0 ' + large + ' 0 ' + p2[0].toFixed(1) + ',' + p2[1].toFixed(1) + ' Z',
      fill: fill, stroke: stroke, 'stroke-width': 2});
  }
  function label(r, deg, txt, fill){
    var p = pt(r, deg);
    return el('text', {x: p[0].toFixed(1), y: (p[1] + 6).toFixed(1), 'text-anchor': 'middle', 'font-size': 16, 'font-weight': 'bold', fill: fill,
      stroke: '#fffdf4', 'stroke-width': 4, 'paint-order': 'stroke'}, txt);
  }
  function draw(){
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    var t = Number(sl.value), u = 180 - t;
    var BLUE = '#3a5da8', GOLD = '#8a6400';
    wedge(46, 0, t, 'rgba(58,93,168,.22)', BLUE);
    wedge(46, t, 180, 'rgba(232,169,12,.28)', GOLD);
    wedge(46, 180, 180 + t, 'rgba(58,93,168,.22)', BLUE);
    wedge(46, 180 + t, 360, 'rgba(232,169,12,.28)', GOLD);
    el('line', {x1: 20, y1: CY, x2: 340, y2: CY, stroke: '#22304f', 'stroke-width': 3, 'stroke-linecap': 'round'});
    var p = pt(150, t), q = pt(150, t + 180);
    el('line', {x1: q[0].toFixed(1), y1: q[1].toFixed(1), x2: p[0].toFixed(1), y2: p[1].toFixed(1), stroke: '#22304f', 'stroke-width': 3, 'stroke-linecap': 'round'});
    el('circle', {cx: CX, cy: CY, r: 4, fill: '#22304f'});
    label(72, t / 2, t + '°', BLUE);
    label(72, t + u / 2, u + '°', GOLD);
    label(72, 180 + t / 2, t + '°', BLUE);
    label(72, 180 + t + u / 2, u + '°', GOLD);
    document.getElementById('cx-out').innerHTML =
      'Side by side (Prop 13): <span style="color:#3a5da8"><b>' + t + '°</b></span> + <span style="color:#8a6400"><b>' + u + '°</b></span> = <b>180°</b>' +
      '<br>Opposite angles (Prop 15): blue matches blue, gold matches gold.';
  }
  sl.addEventListener('input', draw);
  draw();
})();
</script>"""

SEMICIRCLE = ('<div style="%s">\n  <div style="%s">Book III, Proposition 31 &middot; slide the corner round the circle</div>' % (_BOX, _CAP)) + r"""
  <div style="text-align:center;">
    <svg id="sc-svg" width="380" height="230" viewBox="0 0 380 230" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;" role="img" aria-label="A triangle in a semicircle. Moving the top corner changes the other two angles, but the top angle stays a right angle"></svg>
  </div>
  <div id="sc-out" style="text-align:center; font-size:1rem; color:#3d3320; margin:8px 0 10px; line-height:1.6;"></div>
  <div style="max-width:440px; margin:0 auto;">
    <input id="sc-a" type="range" min="16" max="74" step="2" value="24" style="width:100%;" aria-label="move the corner round the semicircle">
  </div>
</div>
<script>
(function(){
  var sl = document.getElementById('sc-a');
  if (!sl) return;
  var svg = document.getElementById('sc-svg'), NS = 'http://www.w3.org/2000/svg', OX = 190, OY = 195, R = 150;
  function el(tag, attrs, text){
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    svg.appendChild(e); return e;
  }
  function txt(x, y, s, fill, size){
    return el('text', {x: x.toFixed(1), y: y.toFixed(1), 'text-anchor': 'middle', 'font-size': size || 15, 'font-weight': 'bold', fill: fill,
      stroke: '#fffdf4', 'stroke-width': 4, 'paint-order': 'stroke'}, s);
  }
  function draw(){
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    var a = Number(sl.value), b = 90 - a, t = 2 * a * Math.PI / 180;
    var Cx = OX + R * Math.cos(t), Cy = OY - R * Math.sin(t), Ax = OX - R, Bx = OX + R;
    el('path', {d: 'M' + Ax + ',' + OY + ' A' + R + ',' + R + ' 0 0 1 ' + Bx + ',' + OY, fill: 'rgba(58,93,168,.05)', stroke: '#3a5da8', 'stroke-width': 2});
    el('polygon', {points: Ax + ',' + OY + ' ' + Bx + ',' + OY + ' ' + Cx.toFixed(1) + ',' + Cy.toFixed(1), fill: '#e6d9b8', stroke: '#22304f', 'stroke-width': 2.5, 'stroke-linejoin': 'round'});
    el('line', {x1: OX, y1: OY, x2: Cx.toFixed(1), y2: Cy.toFixed(1), stroke: '#4a5878', 'stroke-width': 1.5, 'stroke-dasharray': '5 4'});
    var ux = Ax - Cx, uy = OY - Cy, vx = Bx - Cx, vy = OY - Cy, lu = Math.hypot(ux, uy), lv = Math.hypot(vx, vy), s = 14;
    ux = ux / lu * s; uy = uy / lu * s; vx = vx / lv * s; vy = vy / lv * s;
    el('polyline', {points: (Cx + ux).toFixed(1) + ',' + (Cy + uy).toFixed(1) + ' ' + (Cx + ux + vx).toFixed(1) + ',' + (Cy + uy + vy).toFixed(1) + ' ' + (Cx + vx).toFixed(1) + ',' + (Cy + vy).toFixed(1),
      fill: 'none', stroke: '#b03030', 'stroke-width': 2});
    el('circle', {cx: OX, cy: OY, r: 3.5, fill: '#22304f'});
    el('circle', {cx: Cx.toFixed(1), cy: Cy.toFixed(1), r: 5, fill: '#b03030'});
    var ha = a * Math.PI / 360, hb = b * Math.PI / 360;
    txt(Ax + 52 * Math.cos(ha), OY - 52 * Math.sin(ha) + 5, a + '°', '#3a5da8');
    txt(Bx - 52 * Math.cos(hb), OY - 52 * Math.sin(hb) + 5, b + '°', '#8a6400');
    var mx = (Ax + Bx) / 2 - Cx, my = OY - Cy, lm = Math.hypot(mx, my);
    txt(Cx + mx / lm * 34, Cy + my / lm * 34 + 5, '90°', '#b03030');
    txt(Ax - 2, OY + 20, 'A', '#22304f', 14); txt(Bx + 2, OY + 20, 'B', '#22304f', 14); txt(OX, OY + 20, 'O', '#4a5878', 13);
    document.getElementById('sc-out').innerHTML = '<span style="color:#3a5da8"><b>' + a + '°</b></span> + <span style="color:#8a6400"><b>' + b +
      '°</b></span> + <span style="color:#b03030"><b>90°</b></span> = 180° &nbsp;&middot;&nbsp; the corner on the circle never changes';
  }
  sl.addEventListener('input', draw);
  draw();
})();
</script>"""

ALGORITHM = ('<div style="%s">\n  <div style="%s">Euclid&#8217;s algorithm &middot; cut off the biggest square you can</div>' % (_BOX, _CAP)) + r"""
  <div style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center; align-items:center; margin-bottom:10px; font-size:.95rem; color:#3d3320;">
    <label>Width <input id="ea-w" type="number" min="1" max="150" value="21" style="width:64px; font-size:1rem; padding:4px 6px; font-family:Georgia,serif; border:1.5px solid #c9b57e; border-radius:6px;"></label>
    <label>Height <input id="ea-h" type="number" min="1" max="150" value="15" style="width:64px; font-size:1rem; padding:4px 6px; font-family:Georgia,serif; border:1.5px solid #c9b57e; border-radius:6px;"></label>
    <button type="button" id="ea-new" style="@@BTN@@">New rectangle</button>
  </div>
  <div style="display:flex; gap:8px; flex-wrap:wrap; justify-content:center; margin-bottom:10px;">
    <button type="button" class="ea-pre" data-w="21" data-h="15" style="@@BTN@@">21 &#215; 15</button>
    <button type="button" class="ea-pre" data-w="48" data-h="18" style="@@BTN@@">48 &#215; 18</button>
    <button type="button" class="ea-pre" data-w="13" data-h="8" style="@@BTN@@">13 &#215; 8</button>
  </div>
  <div style="text-align:center;">
    <svg id="ea-svg" width="520" height="300" viewBox="0 0 520 300" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;" role="img" aria-label="A rectangle being cut into squares, the biggest square possible each time"></svg>
  </div>
  <div id="ea-out" style="text-align:center; font-weight:bold; font-size:1.02rem; color:#22304f; margin:8px 0 4px; min-height:1.3em;"></div>
  <div id="ea-log" style="text-align:center; font-size:.95rem; color:#3d3320; line-height:1.6; min-height:1.4em; max-height:8.2em; overflow-y:auto; margin-bottom:10px;"></div>
  <div style="text-align:center; display:flex; gap:8px; flex-wrap:wrap; justify-content:center;">
    <button type="button" id="ea-step" style="@@GO@@">Cut off a square &#9654;</button>
    <button type="button" id="ea-all" style="@@BTN@@">Cut all the way</button>
  </div>
</div>
<script>
(function(){
  var svg = document.getElementById('ea-svg');
  if (!svg) return;
  var NS = 'http://www.w3.org/2000/svg';
  var W0, H0, x, y, w, h, cuts, done, sc, offX, offY, lastSide, shade;
  var FILLS = ['rgba(58,93,168,.30)', 'rgba(232,169,12,.40)', 'rgba(30,125,67,.28)', 'rgba(176,48,48,.25)'];
  function el(tag, attrs, text){
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    svg.appendChild(e); return e;
  }
  function start(W, H){
    W0 = W; H0 = H; x = 0; y = 0; w = W; h = H; cuts = []; done = false; lastSide = null; shade = -1;
    sc = Math.min(500 / W, 280 / H); offX = (520 - W * sc) / 2; offY = (300 - H * sc) / 2;
    document.getElementById('ea-log').innerHTML = '';
    document.getElementById('ea-out').textContent = 'A ' + W + ' by ' + H + ' rectangle. Which is the biggest square that fits?';
    draw();
  }
  function draw(){
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    el('rect', {x: offX, y: offY, width: W0 * sc, height: H0 * sc, fill: '#fff8e6'});
    cuts.forEach(function(c, i){
      var last = done && i === cuts.length - 1;
      el('rect', {x: (offX + c.x * sc).toFixed(1), y: (offY + c.y * sc).toFixed(1), width: (c.s * sc).toFixed(1), height: (c.s * sc).toFixed(1),
        fill: last ? 'rgba(232,169,12,.75)' : FILLS[c.shade % 4], stroke: '#22304f', 'stroke-width': last ? 3 : 1.5});
      if (c.s * sc >= 24) el('text', {x: (offX + (c.x + c.s / 2) * sc).toFixed(1), y: (offY + (c.y + c.s / 2) * sc + 6).toFixed(1), 'text-anchor': 'middle',
        'font-size': Math.min(18, c.s * sc / 2.2).toFixed(0), 'font-weight': 'bold', fill: '#22304f'}, c.s);
    });
    el('rect', {x: offX, y: offY, width: W0 * sc, height: H0 * sc, fill: 'none', stroke: '#22304f', 'stroke-width': 3});
    var b1 = document.getElementById('ea-step'), b2 = document.getElementById('ea-all');
    b1.disabled = b2.disabled = done; b1.style.opacity = b2.style.opacity = done ? 0.5 : 1;
  }
  function cut(){
    if (done) return;
    var s = Math.min(w, h), big = Math.max(w, h), line;
    if (s !== lastSide){ shade++; lastSide = s; }
    cuts.push({x: x, y: y, s: s, shade: shade});
    if (w === h){
      done = true;
      line = big + ' &#8722; ' + s + ' = 0';
      document.getElementById('ea-out').innerHTML = (s === 1)
        ? 'Down to 1 by 1 squares. Only 1 measures both numbers: Euclid calls them <i>prime to one another</i> (Prop 1).'
        : 'The last square is ' + s + ' by ' + s + '. It fits exactly into ' + W0 + ' and into ' + H0 + ': the greatest common measure is <b>' + s + '</b>.';
    } else {
      if (w > h){ x += s; w -= s; } else { y += s; h -= s; }
      line = big + ' &#8722; ' + s + ' = ' + (big - s);
      document.getElementById('ea-out').innerHTML = 'Left over: a ' + w + ' by ' + h + ' rectangle.';
    }
    var log = document.getElementById('ea-log');
    log.innerHTML += (log.innerHTML ? ' &nbsp;&middot;&nbsp; ' : '') + line;
    log.scrollTop = log.scrollHeight;
    draw();
  }
  function fromInputs(){
    var W = Math.round(Number(document.getElementById('ea-w').value)), H = Math.round(Number(document.getElementById('ea-h').value));
    if (!(W >= 1 && W <= 150 && H >= 1 && H <= 150)){
      document.getElementById('ea-out').textContent = 'Choose two whole numbers from 1 to 150.';
      return;
    }
    start(W, H);
  }
  document.getElementById('ea-new').addEventListener('click', fromInputs);
  document.getElementById('ea-step').addEventListener('click', cut);
  document.getElementById('ea-all').addEventListener('click', function(){ var n = 0; while (!done && n++ < 400) cut(); });
  [].forEach.call(document.querySelectorAll('.ea-pre'), function(b){
    b.addEventListener('click', function(){
      document.getElementById('ea-w').value = b.dataset.w; document.getElementById('ea-h').value = b.dataset.h; fromInputs();
    });
  });
  start(21, 15);
})();
</script>"""

CORNERS = ('<div style="%s">\n  <div style="%s">Build a corner &middot; can it fold up into a solid?</div>' % (_BOX, _CAP)) + r"""
  <div style="display:flex; gap:8px; flex-wrap:wrap; justify-content:center; margin-bottom:10px;">
    <button type="button" class="co-b" data-k="3" data-n="3" style="@@BTN@@">3 triangles</button>
    <button type="button" class="co-b" data-k="3" data-n="4" style="@@BTN@@">4 triangles</button>
    <button type="button" class="co-b" data-k="3" data-n="5" style="@@BTN@@">5 triangles</button>
    <button type="button" class="co-b" data-k="3" data-n="6" style="@@BTN@@">6 triangles</button>
    <button type="button" class="co-b" data-k="4" data-n="3" style="@@BTN@@">3 squares</button>
    <button type="button" class="co-b" data-k="4" data-n="4" style="@@BTN@@">4 squares</button>
  </div>
  <div style="text-align:center;">
    <svg id="co-svg" width="340" height="280" viewBox="0 0 340 280" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;" role="img" aria-label="Regular polygons laid flat around one corner point, with the gap that is left over"></svg>
  </div>
  <div id="co-sum" style="text-align:center; font-weight:bold; font-size:1.05rem; color:#22304f; margin:8px 0 2px;"></div>
  <div id="co-out" style="text-align:center; font-size:1rem; color:#3d3320; line-height:1.55; min-height:2.6em; max-width:560px; margin:0 auto;"></div>
  <div style="text-align:center; font-size:.8rem; color:#8a6400; margin-top:6px;">Pentagons and hexagons are yours to work out in the checkpoints below.</div>
</div>
<script>
(function(){
  var svg = document.getElementById('co-svg');
  if (!svg) return;
  var NS = 'http://www.w3.org/2000/svg', CX = 170, CY = 150;
  var NAMES = {'3,3': 'tetrahedron (4 triangle faces)', '3,4': 'octahedron (8 triangle faces)', '3,5': 'icosahedron (20 triangle faces)', '4,3': 'cube (6 square faces)'};
  function el(tag, attrs, text){
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    svg.appendChild(e); return e;
  }
  function P(r, deg){ var a = deg * Math.PI / 180; return [CX + r * Math.cos(a), CY - r * Math.sin(a)]; }
  function show(k, n){
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    var th = 180 - 360 / k, sum = n * th, gap = 360 - sum, L = (k === 3 ? 92 : 78);
    var start = 270 - n * th - gap / 2;
    var fills = ['rgba(58,93,168,.30)', 'rgba(232,169,12,.40)'];
    if (gap > 0){
      var g1 = P(110, start + n * th), g2 = P(110, start + 360), large = gap > 180 ? 1 : 0;
      el('path', {d: 'M' + CX + ',' + CY + ' L' + g1[0].toFixed(1) + ',' + g1[1].toFixed(1) + ' A110,110 0 ' + large + ' 0 ' + g2[0].toFixed(1) + ',' + g2[1].toFixed(1) + ' Z',
        fill: 'rgba(176,48,48,.14)', stroke: '#b03030', 'stroke-width': 1.5, 'stroke-dasharray': '5 4'});
      var gm = P(70, 270);
      el('text', {x: gm[0].toFixed(1), y: (gm[1] + 30).toFixed(1), 'text-anchor': 'middle', 'font-size': 14, 'font-weight': 'bold', fill: '#b03030',
        stroke: '#fffdf4', 'stroke-width': 4, 'paint-order': 'stroke'}, 'gap ' + gap + '°');
    }
    for (var i = 0; i < n; i++){
      var phi = start + i * th, px = CX, py = CY, pts = [], dir = phi;
      for (var j = 0; j < k; j++){
        pts.push(px.toFixed(1) + ',' + py.toFixed(1));
        px += L * Math.cos(dir * Math.PI / 180); py -= L * Math.sin(dir * Math.PI / 180);
        dir += 360 / k;
      }
      el('polygon', {points: pts.join(' '), fill: fills[i % 2], stroke: '#22304f', 'stroke-width': 2, 'stroke-linejoin': 'round'});
      var m = P(26, phi + th / 2);
      el('text', {x: m[0].toFixed(1), y: (m[1] + 4).toFixed(1), 'text-anchor': 'middle', 'font-size': 11, fill: '#22304f'}, th + '°');
    }
    el('circle', {cx: CX, cy: CY, r: 4, fill: '#22304f'});
    document.getElementById('co-sum').textContent = n + ' × ' + th + '° = ' + sum + '°';
    var out = document.getElementById('co-out');
    if (gap > 0) out.innerHTML = 'Less than 360°. Close the gap and the corner pops up into a point. This corner belongs to the <b>' + NAMES[k + ',' + n] + '</b>.';
    else out.innerHTML = 'Exactly 360°. No gap to close: the pieces lie <b>flat</b>, like floor tiles. No corner, no solid.';
    [].forEach.call(document.querySelectorAll('.co-b'), function(b){
      var on = Number(b.dataset.k) === k && Number(b.dataset.n) === n;
      b.style.background = on ? '#e8a90c' : '#fff8e6'; b.style.fontWeight = on ? 'bold' : 'normal';
    });
  }
  [].forEach.call(document.querySelectorAll('.co-b'), function(b){
    b.addEventListener('click', function(){ show(Number(b.dataset.k), Number(b.dataset.n)); });
  });
  show(3, 3);
})();
</script>"""



def _styled(w):
    return w.replace("@@GO@@", _GO).replace("@@BTN@@", _BTN)


PROP1, CROSSING, SEMICIRCLE, ALGORITHM, CORNERS = map(_styled, (PROP1, CROSSING, SEMICIRCLE, ALGORITHM, CORNERS))

# ---------------------------------------------------------------------------
EUCLID = dict(
    title="No Royal Road: Euclid and the Elements",
    h1="✦ No Royal Road ✦",
    sub="Euclid, the Elements, and twenty-one problems from the most successful math book ever written",
    footer="Every checkpoint is a proposition from the Elements · every legend is labeled as a legend<br>(there is still no royal road)",
    praise=["Q.E.D., {name}!", "Which was to be proved, {name}!", "Proved from the postulates, {name}!",
            "{name}, the straightedge never lies!", "Euclid would put that in the book, {name}!"],
    cert_org="The Society of the Straightedge and Compass",
    cert_of="the tale of Euclid's Elements",
    cert_rank="Keeper of the Elements",
    finale_title="The Chain Still Holds",
    finale_html="""
<p>Look back at what you have done. You started with a point, <i>that which has no part</i>, and a few rules about straight lines and circles. From those alone you built an equilateral triangle, proved that crossing lines make equal angles, found that every triangle holds exactly 180°, squared a sum with pictures, ran the oldest algorithm in the world, chased the primes forever, and showed why there can only ever be five perfect solids. Every step leaned on the steps before it, and every step can be checked by anyone, anywhere, without trusting anybody.</p>
<p>That way of working is Euclid's real gift, bigger than any single theorem. When Isaac Newton wrote his great book on gravity in 1687, he laid it out like the <i>Elements</i>: definitions first, then laws, then propositions, each one proved. Scientists, lawyers and computer programmers still argue the same way: say exactly what you are assuming, and then show that everything else follows.</p>
<p>The fifth postulate taught a second lesson. For two thousand years people tried to prove it and failed. When Lobachevsky and Bolyai finally asked <i>what if it is false?</i>, they did not find nonsense. They found new worlds. A starting assumption is a choice, and it is worth knowing which ones you have made.</p>
<p>Nobody knows what Euclid looked like, where he was born, or when he died. We have his book. After 2,300 years it is still being read, and every proof in it still works. There is no royal road. There never was. You walked the ordinary road, one step at a time, and you got there.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>&#9312; The <i>Elements</i> starts from definitions, five postulates and five common notions, and proves 465 propositions from them, each using only what came before.</p>
<p>&#9313; Angles side by side on a straight line make <b>180°</b>; crossing lines make equal opposite angles; every triangle's angles add up to <b>180°</b>; any two sides of a triangle are longer than the third.</p>
<p>&#9314; Euclid did algebra with shapes: (a + b)&#178; = a&#178; + 2ab + b&#178; is Book II, Proposition 4.</p>
<p>&#9315; Euclid's algorithm finds the greatest common measure of two numbers by subtracting, and computers still use it. There is no biggest prime. There are only five regular solids.</p>
<p>&#9316; The fifth postulate cannot be proved from the others. Change it, and you get a different geometry, one that Einstein needed to describe gravity.</p>
<p>&#9317; When you read <i>the story goes</i>, ask who wrote it down, and how long afterwards.</p>
</div>""",
    chapters=[
        # ------------------------------------------------------------------ 1
        dict(
            kicker="Chapter One · Alexandria · about 300 BC",
            title="The Man Nobody Knows",
            html="""
<p>In <b>331 BC</b>, Alexander the Great marched into Egypt and marked out a new city on the Mediterranean coast. He named it after himself: <b>Alexandria</b>. Eight years later Alexander was dead, and one of his generals, <b>Ptolemy</b>, took Egypt for himself and made Alexandria his capital. Ptolemy wanted a capital of ideas, not just of soldiers. He (or his son, who ruled after him) built the <b>Museum</b>, a "home of the Muses" where scholars were paid to study and teach, and beside it the <b>Library</b>, which tried to collect a copy of every book in the world.</p>
<p>Somewhere in that city, around <b>300 BC</b>, a teacher named <b>Euclid</b> wrote a book called the <i>Elements</i>. It became probably the most successful textbook in history. It was copied by hand for 1,800 years, printed over and over after that, and used in classrooms until about a hundred years ago.</p>
<p>The strange part is how little we know about the man. No portrait. No birthplace. No date of birth or death. Our main source is a philosopher named <b>Proclus</b>, who wrote about Euclid around <b>AD 450</b>, roughly <b>750 years later</b>. Even Proclus only knew that Euclid lived while the first Ptolemy was king: after Plato's students, and before Archimedes.</p>
<p>Two stories about him survive, and you should treat both with care. <b>The story goes</b> that King Ptolemy asked Euclid whether there was a shorter way to learn geometry than working through the whole <i>Elements</i>. Euclid answered: <b>"There is no royal road to geometry."</b> Proclus tells this story, but the very same line is also told about a different mathematician, Menaechmus, talking to Alexander. A good line tends to get passed around. The second story comes from a writer named <b>Stobaeus</b>, even later, around AD 500. A student who had just learned his first proposition asked, "What will I <i>get</i> from learning this?" Euclid called his servant and said, "Give him a coin, since he must make a profit from what he learns."</p>
<p>What we <i>do</i> have is the book. The <i>Elements</i> has <b>13 books</b> (we would call them chapters) and <b>465 propositions</b>: things to be built, and things to be proved. It does not start with a problem. It starts with <b>definitions</b>, so that everyone agrees on the words. Definition 1: <i>"A point is that which has no part."</i> Definition 2: <i>"A line is breadthless length."</i></p>
<p>Next come five <b>postulates</b>, things you are allowed to do or assume without proof. You may draw a straight line from any point to any point. You may extend a straight line as far as you like. You may draw a circle with any centre and any radius. All right angles are equal. The fifth postulate is long and odd, and it will cause trouble for two thousand years; we will meet it properly at the end. Last come five <b>common notions</b>, such as <i>"things which are equal to the same thing are also equal to one another"</i> and <i>"the whole is greater than the part."</i></p>
<p>After that, nothing is allowed in unless it is <b>proved</b>, using only the definitions, the postulates, the common notions and the propositions already proved before it. Much of the mathematics was not new. An earlier mathematician, Hippocrates of Chios, had written an <i>Elements</i> more than a century before (it is lost), and Euclid used the work of Eudoxus and Theaetetus, who had worked with Plato. Euclid's genius was the <b>order</b>: a single chain of reasoning where every link holds. It was so good that the older books stopped being copied, and vanished.</p>
""" + _circle_defs() + """
<p>Here is how the book defines a <b>circle</b> (Definitions 15 and 16): a round figure with a point inside, the <b>centre</b>, such that all the straight lines from the centre out to the edge are <b>equal</b>. We call each of those lines a <b>radius</b>. Definition 17: a <b>diameter</b> is a straight line through the centre that ends at the circle on both sides.</p>
<div class="bigidea">🌟 <b>Big Idea #1:</b> In the <i>Elements</i>, "it looks true" is never enough. Every claim must be proved from what came before, so anyone can check it, step by step, without having to trust the author.</div>""",
            cps=[dict(
                type="num",
                kicker="Book I, Definitions 15 to 17",
                q="""A circle has a radius of <b>7 cm</b>. How long is its <b>diameter</b>?""",
                answers=[14], unit="cm",
                hint="A diameter runs from the edge, through the centre, to the far edge: one radius in, one radius out.",
            )],
        ),
        # ------------------------------------------------------------------ 2
        dict(
            kicker="Chapter Two · Book I, Proposition 1",
            title="Two Circles and a Triangle",
            html="""
<p>Proposition 1 is the very first thing Euclid does with his rules: <i>"On a given finite straight line, to construct an equilateral triangle."</i> In plain words: you are handed a line. Build a triangle on it with all three sides equal.</p>
<p>Notice the tools. No ruler with numbers on it. No protractor. Postulates 1 to 3 allow exactly two tools: a <b>straightedge</b>, which only draws straight lines, and a <b>compass</b>, which only draws circles. Euclid never measures anything. He proves.</p>
""" + PROP1 + """
<p>Euclid's argument for why the sides are equal uses only two facts from the start of the book. The first is Definition 15: all the radii of one circle are equal. The second is Common Notion 1: things equal to the same thing are equal to each other. Look at the finished picture and see if you can put them together before you answer.</p>
<p>At the end of a construction Euclid writes, in Greek, <i>"which is what it was required to do."</i> Later Latin translators shortened this to <b>Q.E.F.</b> At the end of a proved theorem he writes <i>"which is what it was required to prove,"</i> in Latin <i>quod erat demonstrandum</i>: <b>Q.E.D.</b> Mathematicians still write Q.E.D. at the end of proofs today.</p>
<div class="funfact">🔎 An honest note. Euclid never proves that the two circles actually <i>cross</i>. It looks obvious in the picture. By his own rules, though, a picture is not a proof, and nothing in his postulates says that two circles must meet. Readers spotted gaps like this over the centuries. In <b>1899</b> the German mathematician <b>David Hilbert</b> wrote out a fuller set of starting rules for geometry that fills them. The chain was stronger than anyone had a right to expect, but it was not perfect.</div>""",
            cps=[dict(
                type="mc",
                kicker="Book I, Proposition 1 &middot; the proof",
                q="""In the finished figure, why must side <b>AC</b> be equal to side <b>AB</b>?""",
                mc=[("Because it looks that way in the drawing", False),
                    ("Both are radii of the circle with centre A", True),
                    ("Because C is at the top of the picture", False)],
                good="Exactly, {name}. AC and AB both run from the centre A out to the same circle. In the same way BC and BA are radii of the circle round B. That makes AC and BC each equal to AB, and by Common Notion 1 they are equal to each other. All three sides match.",
                bad="Euclid never trusts how a drawing looks, {name}. Which circle do A, B and C all sit on, and where is its centre?",
            ), dict(
                type="num",
                kicker="Book I, Proposition 1",
                q="""Suppose the line <b>AB</b> you start with is <b>6 cm</b> long. What is the <b>perimeter</b> of the equilateral triangle Euclid builds on it (all three sides added together)?""",
                answers=[18], unit="cm",
                hint="All three sides are equal to AB.",
            )],
        ),
        # ------------------------------------------------------------------ 3
        dict(
            kicker="Chapter Three · Book I, Propositions 13 and 15",
            title="Where Two Lines Cross",
            html="""
<p>Euclid never uses <b>degrees</b>. He measures angles in <b>right angles</b>, the square corner. Proposition 13 says: when one straight line stands on another, the two angles it makes beside each other add up to <b>two right angles</b>. In degrees, where a right angle is 90°, that is <b>180°</b>. A straight line is a half-turn.</p>
<p>Proposition 15 is about two straight lines that <b>cross</b>, like an X. They make four angles. The angles <b>opposite</b> each other (across the crossing point, not side by side) are always <b>equal</b>. Proclus says this fact was first discovered by <b>Thales</b>, a Greek thinker who lived around 600 BC, about three hundred years before Euclid. It was Euclid who gave it a proof.</p>
<p>The proof is short. Call the four angles, going round, <b>p</b>, <b>q</b>, <b>r</b> and <b>s</b>. Angles p and q sit side by side on one straight line, so by Proposition 13, p + q = 180°. Angles q and r sit side by side on the <i>other</i> straight line, so q + r = 180°. Now subtract q from both:</p>
<div class="bigidea">p + q = 180° &nbsp;so&nbsp; p = 180° &#8722; q<br>q + r = 180° &nbsp;so&nbsp; r = 180° &#8722; q<br>Both equal 180° &#8722; q, so <b>p = r</b>. (Common Notions 1 and 3.)</div>
<p>Turn the slanted line and watch the numbers.</p>
""" + CROSSING,
            cps=[dict(
                type="num",
                kicker="Book I, Proposition 13",
                q="""Two straight lines cross. One of the angles is <b>130°</b>. How big is the angle <b>x</b> right beside it?""",
                figure=_cp_cross(),
                answers=[50], unit="degrees",
                hint="The 130° angle and x sit side by side on one straight line. Together they make 180°.",
            ), dict(
                type="mc",
                kicker="Book I, Proposition 15",
                q="""Same crossing. How big is the angle <b>y</b>, opposite the 130° angle?""",
                mc=[("50°", False),
                    ("90°", False),
                    ("130°", True)],
                good="Yes, {name}: opposite angles are equal. You can check it with Proposition 13 too: y sits beside x, so y = 180° &#8722; 50° = 130°.",
                bad="Not that one, {name}. y is <i>across</i> the crossing from the 130° angle, not beside it. What does Proposition 15 say about opposite angles?",
            )],
        ),
        # ------------------------------------------------------------------ 4
        dict(
            kicker="Chapter Four · Book I, Propositions 5 and 32",
            title="The Bridge of Asses",
            html="""
<p>A triangle with two equal sides is called <b>isosceles</b> (eye-SOSS-uh-leez), Greek for "equal legs." Proposition 5 says that in an isosceles triangle, the two angles at the base (the angles where the equal sides meet the third side) are <b>equal</b>. Proclus says Thales knew this too.</p>
<p>Euclid's proof is famous for being tricky: he extends the two equal sides downward and compares two pairs of overlapping triangles. Generations of students got stuck right there. In the Middle Ages it earned a nickname: <i>pons asinorum</i>, Latin for <b>"the bridge of asses."</b> An ass is a donkey. If you could not get over this bridge, you were the donkey. (Euclid's drawing, with its extended sides, even looks a little like a bridge.)</p>
<p>Proposition 32 is one of the most useful facts in all of geometry: the three angles of any triangle add up to <b>two right angles</b>, 180°. Here is Euclid's idea. Through the top corner, draw a line <b>parallel</b> to the base. The parallel line makes an angle equal to <b>a</b> on the left and an angle equal to <b>b</b> on the right (that is Proposition 29). Now look at the top corner: a, c and b sit side by side along a straight line. By Proposition 13, they make 180°.</p>
""" + _i32() + """
<p>The same proposition gives a bonus. Extend one side of a triangle past a corner. The angle outside, the <b>exterior angle</b>, equals the two inside angles at the <i>other</i> two corners added together. Here is why, with the inside angles called a, b and c, and the exterior angle beside c called e:</p>
<div class="bigidea">e + c = 180° &nbsp;(side by side on a straight line, Prop 13)<br>a + b + c = 180° &nbsp;(the three angles of the triangle)<br>Both make 180°, so take c away from each: <b>e = a + b</b>.</div>
<div class="funfact">⚠️ Remember the odd fifth postulate from Chapter One? Proposition 29, the one about parallel lines, is the first place in the whole book where Euclid needs it. Every triangle in the world adding up to 180° depends on that postulate. Keep it in mind. It comes back at the end.</div>""",
            cps=[dict(
                type="num",
                kicker="Book I, Propositions 5 and 32",
                q="""An isosceles triangle has an angle of <b>40°</b> at the top, between its two equal sides. How big is <b>each</b> of the two base angles?""",
                figure=_cp_isosceles(),
                answers=[70], unit="degrees",
                hint="All three angles make 180°. Take away the 40° at the top, then share what is left equally between the two base angles (Proposition 5 says they are equal).",
            ), dict(
                type="num",
                kicker="Book I, Proposition 32",
                q="""A triangle has angles of <b>50°</b> and <b>60°</b> at its two bottom corners. One side is extended past the top corner. How big is the <b>exterior angle</b> there?""",
                figure=_cp_exterior(),
                answers=[110], unit="degrees",
                hint="The exterior angle equals the two inside angles at the other two corners, added together.",
            )],
        ),
        # ------------------------------------------------------------------ 5
        dict(
            kicker="Chapter Five · Book I, Proposition 20",
            title="What Every Donkey Knows",
            html="""
<p>Proposition 20: <i>in any triangle, any two sides added together are longer than the third side.</i> Put another way, a straight path is shorter than any path with a bend in it.</p>
<p>Some ancient Greeks thought proving this was silly. Proclus reports that followers of the philosopher Epicurus made fun of it: even a <b>donkey</b> knows it. Put the donkey at one corner of a triangle and the hay at another, and the donkey walks straight to the hay. It does not wander off to the third corner first.</p>
""" + _donkey() + """
<p>Proclus answered the joke. Knowing that something is true is not the same as knowing <i>why</i> it is true. The donkey can walk the short way, but it cannot explain it. There is a second, deeper reason. If Euclid let in one "obvious" fact without proof, which others would he let in? Some things that look obvious turn out to be false. The only safe rule is the hard one: prove everything.</p>
<p>The proposition is also practical. Proposition 22 shows how to build a triangle out of any three lengths, as long as each pair of them, added together, is longer than the third. If they are not, the two short sides cannot reach each other, or they lie flat along the long one.</p>""",
            cps=[dict(
                type="mc",
                kicker="Book I, Propositions 20 and 22",
                q="""You have three bundles of sticks. Which set of three lengths can be joined at the ends to make a <b>triangle</b>?""",
                mc=[("2 cm, 3 cm and 5 cm", False),
                    ("5 cm, 6 cm and 10 cm", True),
                    ("3 cm, 4 cm and 8 cm", False)],
                good="Right, {name}. 5 + 6 = 11, which is longer than 10, and every other pair is longer still. With 3 and 4, the two short sticks reach only 7, too short for 8. With 2 and 3 they make exactly 5, so they lie flat along the long stick: no triangle.",
                bad="Test the two shortest sticks, {name}. Added together, are they <i>longer</i> than the longest one? Exactly equal is not enough.",
            )],
        ),
        # ------------------------------------------------------------------ 6
        dict(
            kicker="Chapter Six · Book I, Propositions 47 and 48",
            title="The End of Book One",
            html="""
<p>All of Book I builds toward its last two propositions. Proposition 47: <i>in a right-angled triangle, the square on the side opposite the right angle equals the squares on the other two sides.</i> The two sides that make the square corner are the <b>legs</b>, and the long side across from it is the <b>hypotenuse</b>. With legs <b>a</b> and <b>b</b> and hypotenuse <b>c</b>:</p>
<div class="bigidea">📐 <b>Book I, Proposition 47:</b> a&#178; + b&#178; = c&#178;. (a&#178;, "a squared," means a &#215; a: the area of a square with side a.)</div>
<p>It carries the name of <b>Pythagoras</b>, who lived more than two hundred years before Euclid, though people in Babylon were using the rule more than a thousand years before Pythagoras. The proof in the <i>Elements</i> is a clever one. It cuts the big square into two rectangles and shows that each one matches one of the smaller squares. Proclus believed that this particular proof was Euclid's own.</p>
<p>Try the most famous example. With legs 3 and 4: 3 &#215; 3 = 9 and 4 &#215; 4 = 16, and 9 + 16 = 25. Since 5 &#215; 5 = 25, the hypotenuse is 5. Nobody had to measure the long side. It was <b>calculated</b>.</p>
<p>Proposition 48 runs the other way: if the squares on two sides add up to the square on the third, then the angle between those two sides <b>is</b> a right angle. A carpenter can check whether a corner is truly square by measuring 3 along one edge, 4 along the other, and checking that the diagonal is exactly 5.</p>""",
            cps=[dict(
                type="num",
                kicker="Book I, Proposition 47",
                q="""A right triangle has legs <b>8</b> and <b>15</b>. How long is its hypotenuse?""",
                figure=_cp_right(),
                answers=[17], unit="units",
                hint="8 &#215; 8 = 64 and 15 &#215; 15 = 225. Add them, then ask: what number times itself makes that? Try numbers just above 15.",
            )],
        ),
        # ------------------------------------------------------------------ 7
        dict(
            kicker="Chapter Seven · Book II, Proposition 4",
            title="Algebra Made of Squares",
            html="""
<p>The Greeks had no algebra symbols: no x, no little raised 2, no equals sign. They did their algebra with <b>shapes</b>. Book II of the <i>Elements</i> is full of it.</p>
<p>Proposition 4 says: cut a straight line anywhere into two pieces. The square on the whole line equals the squares on the two pieces, plus <b>twice</b> the rectangle made from the two pieces. That sounds like a mouthful until you see it:</p>
""" + _ii4() + """
<p>The whole square has side <b>a + b</b>. Inside it sit a square on a, a square on b, and two rectangles that are each a by b. In today's symbols:</p>
<div class="bigidea">(a + b)&#178; = a&#178; + 2ab + b&#178;</div>
<p>You can use it to square numbers in your head. Take 12 &#215; 12. Split 12 into 10 + 2. The big square is 10 &#215; 10 = 100, the small one 2 &#215; 2 = 4, and the two rectangles are 10 &#215; 2 = 20 each, so 40. Add them: 100 + 40 + 4 = 144.</p>
<p>In the 1890s two young scholars from Oxford, <b>Bernard Grenfell</b> and <b>Arthur Hunt</b>, dug through the ancient rubbish heaps of an Egyptian town called <b>Oxyrhynchus</b>, where the dry sand had preserved thousands of scraps of papyrus. One scrap, catalogued as <b>P.Oxy. I 29</b>, has the words of the very next proposition, Book II, Proposition 5, along with its diagram of a rectangle and a square. Experts disagree about its age; guesses run from about AD 75 to about AD 300. It is one of the oldest pieces of the <i>Elements</i> that survive, and it is now in the Penn Museum in Philadelphia.</p>""",
            cps=[dict(
                type="num",
                kicker="Book II, Proposition 4",
                q="""A square has side <b>7</b>, cut into <b>3 + 4</b>. Proposition 4 says<br>7&#178; = 3&#178; + (the two rectangles) + 4&#178;.<br>What is the area of the <b>two rectangles together</b>? Work it out both ways if you can.""",
                figure=_cp_ii4(),
                answers=[24], unit="square units",
                hint="One way: each rectangle is 3 by 4. Another way: 7&#178; = 49, 3&#178; = 9 and 4&#178; = 16, so 49 = 9 + (rectangles) + 16. What is 49 &#8722; 9 &#8722; 16?",
            )],
        ),
        # ------------------------------------------------------------------ 8
        dict(
            kicker="Chapter Eight · Book III, Proposition 31",
            title="The Corner in the Semicircle",
            html="""
<p>Book III is about circles. Proposition 31 holds a surprise. Draw a circle and a diameter across it. Pick <b>any</b> point on the curve and join it to both ends of the diameter. The angle at that point is always a <b>right angle</b>. Move the point anywhere you like along the half circle. It stays 90°.</p>
""" + SEMICIRCLE + """
<p>Why? Draw the dashed line from the centre O out to the corner. It is a radius, and so are OA and OB. That splits the big triangle into two isosceles triangles. By Proposition 5, each one has two equal base angles: call them a and a on the left, b and b on the right. The angle at the corner on the circle is a + b. Now add up all the angles of the big triangle:</p>
<div class="bigidea">a + a + b + b = 180° &nbsp;(Proposition 32)<br>2a + 2b = 180°<br>a + b = 90° &nbsp;(halve both sides)</div>
<p><b>The story goes</b> that Thales discovered this and was so delighted that he sacrificed an ox to the gods. That story comes from a writer named Diogenes Laertius, around AD 200 to 250, about 800 years after Thales lived. Even Diogenes admits that other writers gave the discovery, and the ox, to Pythagoras instead.</p>""",
            cps=[dict(
                type="num",
                kicker="Book III, Proposition 31",
                q="""A triangle is drawn in a semicircle with the diameter as its longest side. The angle at one end of the diameter is <b>35°</b>. How big is the angle at the <b>other</b> end?""",
                figure=_cp_semicircle(),
                answers=[55], unit="degrees",
                hint="The corner on the circle is 90°. The three angles make 180°: 180 &#8722; 90 &#8722; 35.",
            )],
        ),
        # ------------------------------------------------------------------ 9
        dict(
            kicker="Chapter Nine · Book IV, Proposition 15",
            title="Six Triangles in a Circle",
            html="""
<p>Book IV fits <b>regular</b> shapes (all sides equal, all angles equal) inside circles. Proposition 15 does it for the <b>hexagon</b>, the six-sided shape of a honeycomb cell. At the end of it Euclid adds a short note: the side of the hexagon is <b>equal to the radius</b> of the circle.</p>
<p>That means you can draw one with just a compass. Open the compass to the radius, put the point anywhere on the circle, and mark where it lands on the curve. Move the point to that mark and step again. After exactly six steps you are back where you started.</p>
""" + _hexagon() + """
<p>Here is why it works, using propositions you already know. Join the centre to all six corners. That makes six triangles that meet at the centre, sharing the full turn of 360°, so each one has <b>60°</b> at the centre (360 &#247; 6). Two sides of each triangle are radii, so each triangle is isosceles, and its two base angles are equal (Proposition 5). Together they make 180° &#8722; 60° = 120°, so each base angle is 60°. All three angles are 60°. A triangle with equal angles has equal sides (Proposition 6), so the outer side of each triangle, the side of the hexagon, is as long as a radius.</p>""",
            cps=[dict(
                type="num",
                kicker="Book IV, Proposition 15",
                q="""A regular hexagon is drawn inside a circle of radius <b>5 cm</b>, its corners touching the circle. What is the hexagon's <b>perimeter</b> (all six sides together)?""",
                answers=[30], unit="cm",
                hint="Each side equals the radius. There are six sides.",
            )],
        ),
        # ------------------------------------------------------------------ 10
        dict(
            kicker="Chapter Ten · Book VII, Propositions 1 and 2",
            title="The Oldest Algorithm",
            html="""
<p>Books VII, VIII and IX are about whole numbers, though Euclid still pictures every number as a length. Proposition 2 asks: given two numbers, find the biggest number that <b>measures</b> both of them exactly (divides into both with nothing left over). We call it the <b>greatest common divisor</b>. Euclid calls it the <b>greatest common measure</b>.</p>
<p>His method is beautifully simple. <b>Take the smaller number away from the larger.</b> Then do it again with the two numbers you now have. Keep going. When the two numbers are equal, that number is the answer.</p>
<p>Try 20 and 8. 20 &#8722; 8 = 12. Now 12 and 8: 12 &#8722; 8 = 4. Now 8 and 4: 8 &#8722; 4 = 4. Now 4 and 4: equal. So the greatest common measure of 20 and 8 is <b>4</b>. Check: 4 goes into 20 five times and into 8 twice.</p>
<p>You can see it as a picture. Make a rectangle 20 by 8. Cut off the biggest square you can, then the biggest square from what is left, and so on. The last square fits exactly into both sides. Try it:</p>
""" + ALGORITHM + """
<p>Proposition 1 covers the other ending: if the subtracting only stops when you reach <b>1</b>, then nothing bigger than 1 measures both numbers. Euclid calls such numbers <b>"prime to one another."</b> (Try 13 &#215; 8 above.)</p>
<p>A step-by-step recipe like this, one that always finishes with the right answer, is called an <b>algorithm</b>, and this is one of the oldest still in use. Computers use versions of it to simplify fractions. The encryption that keeps online shopping safe uses it too. The computer scientist <b>Donald Knuth</b> called it "the granddaddy of all algorithms."</p>""",
            cps=[dict(
                type="num",
                kicker="Book VII, Proposition 2",
                q="""Use Euclid's method to find the greatest common measure of <b>84</b> and <b>36</b>.""",
                answers=[12], unit="",
                hint="84 &#8722; 36 = 48. Then 48 &#8722; 36 = 12. Now you have 36 and 12. Keep taking the smaller from the larger until the two numbers match.",
            ), dict(
                type="num",
                kicker="Book VII, Proposition 2",
                q="""Now <b>91</b> and <b>35</b>. What is their greatest common measure?""",
                answers=[7], unit="",
                hint="91 &#8722; 35 = 56, then 56 &#8722; 35 = 21, then 35 &#8722; 21 = 14. Keep going.",
            )],
        ),
        # ------------------------------------------------------------------ 11
        dict(
            kicker="Chapter Eleven · Book IX, Proposition 20",
            title="The Primes Never Run Out",
            html="""
<p>A <b>prime number</b> is a number that only 1 and itself can measure: 2, 3, 5, 7, 11, 13, 17, 19, 23... Every other whole number above 1 can be built by multiplying primes together, like 12 = 2 &#215; 2 &#215; 3. Primes are the atoms of arithmetic.</p>
<p>As you count higher, primes get rarer. Between 1 and 100 there are 25 of them. Between 9,900 and 10,000 there are only 9. Do they eventually stop? Is there a biggest prime?</p>
<p>Proposition 20 of Book IX answers, in Euclid's careful words: <i>"Prime numbers are more than any assigned multitude of prime numbers."</i> Notice that he never says <b>infinite</b>. Greek mathematicians were wary of the infinite. Instead Euclid says: give me any list of primes you like, and I can show you a prime that is not on it.</p>
<p>Here is how. Multiply every prime on the list together, then <b>add 1</b>. Call the result N. Now try dividing N by any prime on your list. It always leaves a <b>remainder of 1</b>, because N is one more than a multiple of that prime. That means no prime on your list measures N. Then one of two things is true:</p>
<p>&#9312; N is prime itself. It is a new prime, not on your list.<br>&#9313; N is not prime. Then some prime measures it, and that prime cannot be on your list. Again, a new prime.</p>
<p>Either way, your list was missing a prime. No list can ever hold them all. Euclid's own proof uses a list of just three primes, but the argument works for any list at all. For example, with the list 2, 3, 5: 2 &#215; 3 &#215; 5 + 1 = 31, and 31 is a prime not on the list.</p>""",
            cps=[dict(
                type="num",
                kicker="Book IX, Proposition 20",
                q="""Take the list of primes <b>2, 3, 5, 7</b>. Follow Euclid's recipe: multiply them all together, then add 1. What number do you get? (It happens to be prime.)""",
                answers=[211], unit="",
                hint="2 &#215; 3 = 6, 6 &#215; 5 = 30, 30 &#215; 7 = 210. Then add 1.",
            ), dict(
                type="mc",
                kicker="Book IX, Proposition 20 &middot; testing the proof",
                q="""Now take the list <b>2, 3, 5, 7, 11, 13</b>. Multiply and add 1: you get <b>30,031</b>. But 30,031 = 59 &#215; 509, so it is <b>not</b> prime! Does that break Euclid's proof?""",
                mc=[("Yes: the new number was supposed to be prime", False),
                    ("No, because 2, 3, 5, 7, 11 and 13 all measure it after all", False),
                    ("No: 59 and 509 are primes that are not on the list", True)],
                good="Exactly, {name}. Euclid never claimed N itself must be prime. That is case &#9313;: N is not prime, but the primes that measure it, 59 and 509, are both missing from the list. The proof survives the test.",
                bad="Look again at the two cases, {name}. Did Euclid say N must be prime? Can 2, 3, 5, 7, 11 or 13 really measure a number that is one more than their product?",
            )],
        ),
        # ------------------------------------------------------------------ 12
        dict(
            kicker="Chapter Twelve · Book IX, Proposition 36",
            title="Perfect Numbers",
            html="""
<p>Book VII defines a <b>perfect number</b>: a number equal to the sum of its own <b>parts</b>, meaning all the numbers smaller than itself that measure it exactly. The smallest is 6. Its parts are 1, 2 and 3, and 1 + 2 + 3 = 6.</p>
<p>The next one is 28. Its parts are 1, 2, 4, 7 and 14 (try dividing 28 by each), and 1 + 2 + 4 + 7 + 14 = 28. After that they get rare very fast.</p>
<p>The last proposition of Book IX, Proposition 36, is a recipe for making them. Start at 1 and keep doubling: 1, 2, 4, 8, 16... Add them up as you go. Whenever the running total is a <b>prime</b>, multiply that total by the last number you added. The answer is a perfect number.</p>
<div class="bigidea">1 + 2 = 3, which is prime: 3 &#215; 2 = <b>6</b><br>1 + 2 + 4 = 7, which is prime: 7 &#215; 4 = <b>28</b><br>1 + 2 + 4 + 8 = 15, which is not prime (3 &#215; 5), so skip it<br>and carry on doubling...</div>
<p>About two thousand years later, in the 1700s, the Swiss mathematician <b>Leonhard Euler</b> proved that it works the other way round too: every <i>even</i> perfect number comes from Euclid's recipe. What about <b>odd</b> perfect numbers? Nobody has ever found one. Nobody has ever proved that none exist. It is one of the oldest unsolved problems in mathematics, and it is still open today. Maybe you will be the one to settle it.</p>""",
            cps=[dict(
                type="num",
                kicker="Book IX, Proposition 36",
                q="""Keep doubling: <b>1 + 2 + 4 + 8 + 16</b>. Add them up and check that the total is prime. Then follow Euclid's recipe: multiply the total by the last number you added. Which perfect number do you get?""",
                answers=[496], unit="",
                hint="1 + 2 + 4 + 8 + 16 = 31, which is prime. Now 31 &#215; 16: that is 31 &#215; 10 plus 31 &#215; 6.",
            )],
        ),
        # ------------------------------------------------------------------ 13
        dict(
            kicker="Chapter Thirteen · Book XIII, Propositions 13 to 18",
            title="Only Five",
            html="""
<p>The last book of the <i>Elements</i> climbs to the top of the mountain. A <b>regular solid</b> is a 3D shape whose faces are all the same regular polygon, with the same number meeting at every corner. Book XIII builds all five: the <b>tetrahedron</b> (4 triangles), the <b>octahedron</b> (8 triangles), the <b>icosahedron</b> (20 triangles), the <b>cube</b> (6 squares) and the <b>dodecahedron</b> (12 pentagons). Plato wrote about these five shapes, which is why they are often called the <b>Platonic solids</b>. Much of the work on them goes back to Plato's friend Theaetetus.</p>
<p>After Proposition 18, Euclid adds a remarkable claim: <b>there are no others</b>. Not "nobody has found another one yet." There cannot be another one, ever. Here is the reason, from Book XI, Proposition 21. At every corner of a solid, at least three faces must meet, and the flat angles that meet there must add up to <b>less than 360°</b>. If they add up to exactly 360°, the faces lie flat. With more than 360°, they will not fit at all.</p>
<p>Try it with the triangles and squares. Each corner of an equilateral triangle is 60°, and each corner of a square is 90°.</p>
""" + CORNERS + """
<p>Now the bigger shapes. Each corner of a regular <b>pentagon</b> is <b>108°</b>, and each corner of a regular <b>hexagon</b> is <b>120°</b>.</p>""",
            cps=[dict(
                type="num",
                kicker="Book XIII, after Proposition 18",
                q="""Three regular pentagons meet at one corner. Each corner of a pentagon is <b>108°</b>. What do the three angles add up to?""",
                answers=[324], unit="degrees",
                hint="3 &#215; 108 = 3 &#215; 100 + 3 &#215; 8.",
            ), dict(
                type="mc",
                kicker="Book XIII, after Proposition 18 &middot; the proof",
                q="""324° is less than 360°, so three pentagons <i>can</i> make a corner: that is the dodecahedron. Why can there be no regular solid made of <b>hexagons</b>?""",
                mc=[("Hexagons are too hard to cut out", False),
                    ("Three hexagon corners make 3 &#215; 120° = 360°, so they lie flat", True),
                    ("A solid can never have six-sided faces", False)],
                good="Q.E.D., {name}. Three hexagons fill exactly 360° and lie flat, like a honeycomb. Shapes with more sides have even bigger corners, so they are worse still. Count every possibility: 3, 4 or 5 triangles, 3 squares, 3 pentagons. Exactly five. Euclid's book ends here, at the top of the mountain.",
                bad="Not quite, {name}. Use the rule from Book XI: add up the angles meeting at the corner. Three hexagon corners at 120° each make what?",
            )],
        ),
        # ------------------------------------------------------------------ 14
        dict(
            kicker="Chapter Fourteen · Book VI, Proposition 4",
            title="Six Books by Candlelight",
            html="""
<p>Euclid's own copy of the <i>Elements</i> is long gone. The book survived because people kept <b>copying it by hand</b>, one scribe after another, for more than 1,700 years. In the 300s AD, <b>Theon of Alexandria</b> (the father of the mathematician Hypatia) made his own edition, adding small changes and fixes. Nearly every Greek copy that survives comes from Theon's version.</p>
<p>Around <b>AD 800</b>, in <b>Baghdad</b>, a scholar named <b>al-Hajjaj</b> translated the <i>Elements</i> into Arabic. Later in the same century <b>Ishaq ibn Hunayn</b> made a new translation, and the great mathematician <b>Thabit ibn Qurra</b> revised it. For centuries, mathematicians writing in Arabic studied the book, commented on it, and argued about it. In the 1120s, an Englishman named <b>Adelard of Bath</b>, who had travelled widely and learned Arabic, put it into Latin, the language of Europe's scholars.</p>
<p>In <b>1482</b>, in Venice, a printer named <b>Erhard Ratdolt</b> produced the first printed <i>Elements</i>, with its diagrams printed in the margins. Hundreds of editions followed. In <b>1847</b>, an Irish teacher named <b>Oliver Byrne</b> printed one where the diagrams and even the proofs were in red, yellow, blue and black instead of letters, "for the greater ease of learners," as his title page says.</p>
<p>One of the book's most famous students was a self-taught lawyer from Illinois. In a short life story he wrote in <b>1860</b> (in the third person, for a campaign biography), <b>Abraham Lincoln</b> said that after serving in Congress he <i>"studied and nearly mastered the six books of Euclid."</i> His law partner William Herndon remembered, many years later, Lincoln studying geometry late at night by candlelight while travelling from court to court.</p>
<p>"The six books" were the usual school course: Books I to VI, plane geometry. Book VI, the last of them, is about <b>similar</b> figures, shapes with the same angles but different sizes. Proposition 4 says that if two triangles have the same angles, their sides are in the same <b>proportion</b>. If one side of the big triangle is 3 times its partner in the small triangle, every side is 3 times its partner.</p>
<p>That lets you measure things you cannot reach. At the same moment, the sun's rays strike a stick and a tall tower at the same slant. Each one and its shadow make a right triangle, and the two triangles have the same angles. <b>The story goes</b> that Thales measured the height of an Egyptian pyramid this way, but that story was written down centuries after him. The geometry, though, is pure Book VI.</p>""",
            cps=[dict(
                type="num",
                kicker="Book VI, Proposition 4",
                q="""A stick <b>2 m</b> tall casts a shadow <b>3 m</b> long. At the same moment, an obelisk casts a shadow <b>45 m</b> long. The two triangles have the same angles. How tall is the obelisk?""",
                figure=_cp_shadow(),
                answers=[30], unit="metres",
                hint="The obelisk's shadow is 45 &#247; 3 = 15 times as long as the stick's shadow. By Proposition 4, its height is 15 times the stick's height too. Or: height &#247; 45 = 2 &#247; 3.",
            )],
        ),
        # ------------------------------------------------------------------ 15
        dict(
            kicker="Chapter Fifteen · Book I, Postulate 5 and Proposition 29",
            title="The Postulate That Would Not Behave",
            html="""
<p>Here, at last, is the fifth postulate, in plain words. Draw a straight line crossing two other straight lines. Look at the two inside angles on one side of it. If they add up to <b>less than two right angles</b> (less than 180°), then the two lines, if you extend them far enough, will <b>meet</b> on that side.</p>
<p>Compare that with the other four postulates, which are short and simple. This one reads more like a theorem, something that ought to be <i>proved</i>. Euclid himself seems to have avoided it as long as he could: he proves 28 propositions without it, and uses it for the first time in Proposition 29, to show what happens when a line crosses two <b>parallel</b> lines (lines that never meet). The alternate angles are equal, and the two inside angles on the same side add up to exactly two right angles, 180°.</p>
<p>For about two thousand years, mathematicians tried to prove the fifth postulate from the other four, so that it could be removed from the list. Proclus tried. In Persia, the poet and mathematician <b>Omar Khayyam</b> tried, and so did <b>Nasir al-Din al-Tusi</b>. In Italy in 1733, a priest named <b>Giovanni Saccheri</b> wrote a whole book claiming to have done it. Every attempt failed. Each "proof" quietly assumed something that turned out to be the fifth postulate in disguise.</p>
<p>Then, in the 1820s and 1830s, two young men tried something braver. In Russia, <b>Nikolai Lobachevsky</b>, and in Hungary, <b>János Bolyai</b>, each asked: what if the fifth postulate is simply <b>false</b>? What if, through a point next to a line, you could draw many lines that never meet it? They expected to run into a contradiction. They never did. Instead they found a whole new geometry, just as solid as Euclid's, in which the angles of a triangle add up to <b>less</b> than 180°. (The great German mathematician <b>Carl Friedrich Gauss</b> had reached similar ideas privately, and never published them.)</p>
<p>János's father, <b>Farkas Bolyai</b>, had spent years on the parallel problem himself. He wrote to his son begging him to leave it alone, warning that it could swallow up his whole life and all his happiness, as it had nearly done to him. János kept going anyway, and in 1832 his work was printed as an appendix to his father's book.</p>
<p>The fifth postulate, it turned out, cannot be proved. It is a genuine <b>choice</b>. Choose it, and you get Euclid's flat geometry. Choose something else, and you get curved geometries that are just as logical. In 1915, Albert Einstein used curved geometry to describe <b>gravity</b>: near heavy objects like the Sun, space itself does not follow Euclid's rules exactly. Euclid's chain of reasoning was so careful that, 2,000 years later, it showed exactly which link could be changed.</p>""",
            cps=[dict(
                type="num",
                kicker="Book I, Proposition 29",
                q="""A straight line crosses two <b>parallel</b> lines. Between the parallels, on the right of the crossing line, the lower angle is <b>65°</b>. How big is the upper angle on that same side, marked <b>?</b>""",
                figure=_cp_parallels(),
                answers=[115], unit="degrees",
                hint="Proposition 29: for parallel lines, the two inside angles on the same side add up to exactly 180°.",
            )],
        ),
    ],
    quiz=dict(
        title="&#10022; Ten More from the Elements &#10022;",
        intro="Ten more problems, every one taken from the <i>Elements</i>. One attempt per question, because a proof doesn't get a second guess either. Pencil and paper are allowed. A royal road is not.",
        verdicts=[
            dict(min=10, title="{score}: Q.E.D.", text="Flawless, {name}. Euclid would hand you the compass and let you teach the next class in Alexandria."),
            dict(min=7, title="{score}: A true student of the Museum", text="Strong work, {name}. Read the explanations under the ones that got away. Each one points back to a chapter you can revisit."),
            dict(min=4, title="{score}: Halfway across the bridge", text="You have the idea, {name}, and the rest is practice. Wipe the slate, keep a pencil handy, and draw a picture before you calculate anything. Euclid always did."),
            dict(min=0, title="{score}: Back to the postulates", text="Every one of these can be learned, {name}. There is no royal road, but there is a road. Go back through the chapters, then wipe the slate and try again."),
        ],
        questions=[
            dict(type="num", kicker="Book I, Proposition 32",
                 q="""A triangle has angles of <b>47°</b> and <b>68°</b>. How big is the third angle?""",
                 answers=[65], unit="degrees",
                 why="47 + 68 = 115, and 180 &#8722; 115 = 65. The three angles of every triangle make 180°."),
            dict(type="mc", kicker="Book I, Propositions 13 and 15",
                 q="""Two straight roads cross. One of the four angles is <b>72°</b>. What are the other three, going round?""",
                 mc=[("72°, 72° and 72°", False),
                     ("108°, 72° and 108°", True),
                     ("18°, 72° and 18°", False)],
                 why="The angles beside 72° make 180° with it, so each is 108° (Prop 13). The angle opposite is equal to it: 72° (Prop 15)."),
            dict(type="num", kicker="Book I, Proposition 20",
                 q="""Two sides of a triangle are <b>4 cm</b> and <b>9 cm</b>. The third side is a whole number of centimetres. What is the <b>shortest</b> it can be?""",
                 answers=[6], unit="cm",
                 why="4 plus the third side must be longer than 9, so the third side must be more than 5. The shortest whole number is 6. (With 5, the sides would lie flat.)"),
            dict(type="num", kicker="Book I, Proposition 47",
                 q="""A right triangle has legs <b>5</b> and <b>12</b>. How long is its hypotenuse?""",
                 answers=[13], unit="units",
                 why="25 + 144 = 169, and 13 &#215; 13 = 169."),
            dict(type="num", kicker="Book II, Proposition 4",
                 q="""Square <b>31</b> in your head, Euclid's way: split it into 30 + 1. Add the big square, the small square, and the two rectangles. What is 31 &#215; 31?""",
                 answers=[961], unit="",
                 why="30 &#215; 30 = 900, 1 &#215; 1 = 1, and the two rectangles are 30 &#215; 1 = 30 each, so 60. 900 + 60 + 1 = 961."),
            dict(type="mc", kicker="Book III, Proposition 31",
                 q="""A triangle has the diameter of a circle as one side, and its third corner on the circle. What can you say about the angle at that third corner?""",
                 mc=[("It is always 60°", False),
                     ("It depends on where the corner is", False),
                     ("It is always 90°", True)],
                 why="The angle in a semicircle is always a right angle, wherever the corner sits on the curve. The other two angles change, but they always add up to 90°."),
            dict(type="num", kicker="Book VII, Proposition 2",
                 q="""Find the greatest common measure of <b>98</b> and <b>56</b>.""",
                 answers=[14], unit="",
                 why="98 &#8722; 56 = 42. 56 &#8722; 42 = 14. 42 &#8722; 14 = 28. 28 &#8722; 14 = 14. Now both are 14."),
            dict(type="mc", kicker="Book IX, Proposition 36",
                 q="""In Euclid's recipe for perfect numbers, why do we skip the step <b>1 + 2 + 4 + 8</b>?""",
                 mc=[("Because 8 is too big", False),
                     ("Because the total, 15, is not prime: it is 3 &#215; 5", True),
                     ("Because the total is an even number", False)],
                 why="The recipe only works when the running total is prime. 15 = 3 &#215; 5, so we keep doubling until the total is prime again: 1 + 2 + 4 + 8 + 16 = 31."),
            dict(type="mc", kicker="Book XIII &middot; the five solids",
                 q="""How many squares meet at each corner of a regular solid made of squares?""",
                 mc=[("2", False),
                     ("4", False),
                     ("3", True)],
                 why="Three squares make 3 &#215; 90° = 270°, less than 360°: the corner of a cube. Four make exactly 360° and lie flat, and two cannot close up into a corner at all."),
            dict(type="num", kicker="Book I, Propositions 5 and 32",
                 q="""An isosceles triangle has two equal base angles of <b>50°</b> each. How big is the angle at the top?""",
                 answers=[80], unit="degrees",
                 why="50 + 50 = 100, and 180 &#8722; 100 = 80."),
        ],
    ),
)
