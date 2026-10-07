# -*- coding: utf-8 -*-
"""Story data: Pythagoras and the theorem that wears his name."""

# ---------------------------------------------------------------------------
# Diagram helpers. Every figure is drawn from real coordinates (math y-axis up),
# so the pictures are true to the numbers in the text.
# Colour code, used everywhere: square on leg a = blue, on leg b = gold,
# on the hypotenuse c = red.
# ---------------------------------------------------------------------------
A_COL, B_COL, C_COL = "#3a5da8", "#e8a90c", "#b03030"
A_FILL, B_FILL, C_FILL = "rgba(58,93,168,.22)", "rgba(232,169,12,.30)", "rgba(176,48,48,.18)"
INK, TRI = "#22304f", "#e6d9b8"
LIGHT = "#eef1fb"  # for figures that sit on the dark checkpoint panels


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

    def grid(self, x0, y0, x1, y1, stroke, step=1):
        k = x0 + step
        while k < x1:
            self.line(k, y0, k, y1, stroke, 1)
            k += step
        k = y0 + step
        while k < y1:
            self.line(x0, k, x1, k, stroke, 1)
            k += step
        return self

    def corner(self, x, y, dx1, dy1, dx2, dy2, size=0.4, stroke=INK):
        """Right-angle marker at (x, y) opening along the two unit directions."""
        pts = [(x + dx1 * size, y + dy1 * size),
               (x + (dx1 + dx2) * size, y + (dy1 + dy2) * size),
               (x + dx2 * size, y + dy2 * size)]
        p = " ".join("%.1f,%.1f" % self.xy(a, b) for a, b in pts)
        self.parts.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.5"/>' % (p, stroke))
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


def _vocab():
    f = _Fig(340, 190, 40, 80, 160, "A right triangle with its two legs and its hypotenuse labelled")
    f.poly([(0, 0), (4, 0), (0, 3)], TRI, INK, 2.5)
    f.corner(0, 0, 1, 0, 0, 1, 0.35)
    f.text(-0.25, 1.5, "leg a", 15, A_COL, True, "end")
    f.text(2, -0.4, "leg b", 15, "#8a6400", True)
    f.text(2.35, 1.85, "hypotenuse c", 15, C_COL, True, "start")
    f.text(0.95, 0.75, "square corner", 11, "#4a5878", italic=True, anchor="start", halo=False)
    return f.svg()


def _tetractys():
    f = _Fig(220, 170, 36, 110, 150, "The tetractys: ten dots in rows of one, two, three and four")
    for row in range(4):            # row 0 = bottom row of four
        n = 4 - row
        for i in range(n):
            f.dot(-(n - 1) / 2.0 + i, row * 0.9 + 0.1, 8, "#8a6400")
    for row, n in enumerate([4, 3, 2, 1]):
        f.text(2.45, row * 0.9 + 0.1, str(n), 14, "#4a5878", anchor="start", halo=False)
    return f.svg()


def _xian_tu():
    """Zhao Shuang's diagram for the 3-4-5 triangle, in the colours his text names."""
    f = _Fig(380, 270, 44, 50, 245, "A square of side 5 cut into four right triangles and one small central square")
    red, yel = "rgba(190,60,40,.30)", "rgba(232,169,12,.55)"
    P = [(0, 0), (5, 0), (5, 5), (0, 5)]
    Q = [(3.2, 2.4), (2.6, 3.2), (1.8, 2.6), (2.4, 1.8)]
    for i in range(4):
        f.poly([P[i], P[(i + 1) % 4], Q[i]], red, "#8a2d1c", 2)
    f.poly(Q, yel, "#8a6400", 2)
    f.poly(P, "none", INK, 3)
    f.text(2.5, -0.3, "c = 5", 14, C_COL, True)
    for i in range(4):  # area label at each red triangle's centre (centroid)
        tri = [P[i], P[(i + 1) % 4], Q[i]]
        f.text(sum(t[0] for t in tri) / 3, sum(t[1] for t in tri) / 3, "6", 15, "#8a2d1c", True)
    f.text(2.5, 2.5, "1", 14, "#5a4a1a", True, halo=False)
    f.text(5.2, 3.9, "red: four", 12, "#8a2d1c", anchor="start", halo=False)
    f.text(5.2, 3.5, "triangles", 12, "#8a2d1c", anchor="start", halo=False)
    f.text(5.2, 2.7, "yellow:", 12, "#8a6400", anchor="start", halo=False)
    f.text(5.2, 2.3, "the square", 12, "#8a6400", anchor="start", halo=False)
    f.text(5.2, 1.9, "left over", 12, "#8a6400", anchor="start", halo=False)
    return f.svg()


def _windmill():
    """Euclid I.47 for the 3-4-5 triangle: hypotenuse on the bottom, squares outward."""
    f = _Fig(360, 380, 30, 110, 205, "Euclid's windmill: a right triangle with a square on each side, "
             "and a line from the right angle cutting the big square into two rectangles")
    A, B, C = (0, 0), (5, 0), (1.8, 2.4)
    f.poly([A, C, (-0.6, 4.2), (-2.4, 1.8)], A_FILL, A_COL, 2)
    f.poly([C, B, (7.4, 3.2), (4.2, 5.6)], B_FILL, B_COL, 2)
    f.poly([(0, 0), (1.8, 0), (1.8, -5), (0, -5)], A_FILL, A_COL, 2)
    f.poly([(1.8, 0), (5, 0), (5, -5), (1.8, -5)], B_FILL, B_COL, 2)
    f.poly([(0, 0), (5, 0), (5, -5), (0, -5)], "none", C_COL, 3)
    f.poly([A, B, C], TRI, INK, 2.5)
    f.line(1.8, 2.4, 1.8, -5, INK, 1.5, "5 4")
    f.text(-0.3, 2.1, "9", 17, A_COL, True)
    f.text(4.7, 2.8, "16", 17, "#8a6400", True)
    f.text(0.9, -2.5, "9", 17, A_COL, True)
    f.text(3.4, -2.5, "16", 17, "#8a6400", True)
    f.text(0.9, -5.4, "1.8", 12, "#4a5878", halo=False)
    f.text(3.4, -5.4, "3.2", 12, "#4a5878", halo=False)
    f.text(5.3, -2.5, "5", 12, "#4a5878", anchor="start", halo=False)
    f.text(0.6, 1.55, "3", 12, INK, halo=False)
    f.text(3.75, 1.55, "4", 12, INK, halo=False)
    return f.svg()


def _garfield():
    f = _Fig(360, 230, 40, 40, 195, "Garfield's trapezoid, built from two copies of a right triangle and "
             "half of a square on the hypotenuse")
    f.poly([(0, 0), (4, 0), (0, 3)], TRI, INK, 2)
    f.poly([(4, 0), (7, 0), (7, 4)], TRI, INK, 2)
    f.poly([(0, 3), (4, 0), (7, 4)], C_FILL, C_COL, 2)
    f.poly([(0, 0), (7, 0), (7, 4), (0, 3)], "none", INK, 3)
    f.corner(0, 0, 1, 0, 0, 1, 0.3)
    f.corner(7, 0, -1, 0, 0, 1, 0.3)
    f.corner(4, 0, -0.8, 0.6, 0.6, 0.8, 0.35, C_COL)
    f.text(1.2, 0.9, "6", 16, INK, True, halo=False)
    f.text(6.0, 1.1, "6", 16, INK, True, halo=False)
    f.text(3.7, 2.3, "half of c&#178;", 14, C_COL, True)
    f.text(-0.25, 1.5, "3", 13, "#4a5878", anchor="end", halo=False)
    f.text(7.25, 2, "4", 13, "#4a5878", anchor="start", halo=False)
    f.text(2, -0.35, "4", 13, "#4a5878", halo=False)
    f.text(5.5, -0.35, "3", 13, "#4a5878", halo=False)
    f.text(1.75, 1.95, "5", 13, C_COL, halo=True)
    f.text(5.75, 1.75, "5", 13, C_COL, halo=True)
    return f.svg()


def _einstein():
    f = _Fig(360, 190, 56, 40, 160, "A right triangle split by a line from its right angle into two "
             "smaller triangles of the same shape")
    A, B, C, F = (0, 0), (5, 0), (1.8, 2.4), (1.8, 0)
    f.poly([A, F, C], A_FILL, A_COL, 2)
    f.poly([F, B, C], B_FILL, B_COL, 2)
    f.poly([A, B, C], "none", INK, 2.5)
    f.corner(1.8, 0, 1, 0, 0, 1, 0.22)
    f.corner(1.8, 2.4, -0.6, -0.8, 0.8, -0.6, 0.22)
    f.text(1.15, 0.75, "2.16", 14, A_COL, True)
    f.text(2.95, 0.8, "3.84", 14, "#8a6400", True)
    f.text(0.65, 1.4, "3", 14, A_COL, True, halo=False)
    f.text(3.65, 1.4, "4", 14, "#8a6400", True, halo=False)
    f.text(2.5, -0.28, "5", 14, C_COL, True, halo=False)
    return f.svg()


def _unit_square():
    f = _Fig(240, 210, 130, 50, 175, "A one by one square with its diagonal drawn")
    f.poly([(0, 0), (1, 0), (1, 1), (0, 1)], "#fff8e6", INK, 2)
    f.poly([(0, 0), (1, 0), (1, 1)], TRI, INK, 2.5)
    f.corner(1, 0, -1, 0, 0, 1, 0.09)
    f.text(0.5, -0.1, "1", 15, INK, True, halo=False)
    f.text(1.08, 0.5, "1", 15, INK, True, anchor="start", halo=False)
    f.text(0.42, 0.56, "?", 20, C_COL, True)
    return f.svg()


# ---- figures for the dark checkpoint panels ----
def _angles():
    f = _Fig(320, 200, 40, 70, 170, "A right triangle with a square corner, one angle marked 35 degrees, "
             "and the third angle marked with a question mark", dark=True)
    f.poly([(0, 0), (5, 0), (0, 3.5)], "rgba(232,169,12,.16)", LIGHT, 2.5)
    f.corner(0, 0, 1, 0, 0, 1, 0.35, LIGHT)
    f.text(0.55, 0.75, "90&#176;", 13, LIGHT, anchor="start", halo=False)
    f.text(3.55, 0.35, "35&#176;", 14, LIGHT, True, halo=False)
    f.text(0.42, 2.45, "?", 20, "#ffd97a", True, halo=False)
    return f.svg()


def _ladder():
    f = _Fig(300, 230, 7.5, 70, 205, "A ladder leaning against a wall, its foot 7 metres from the wall", dark=True)
    f.raw('<rect x="40" y="18" width="30" height="187" fill="rgba(238,241,251,.10)" stroke="#5a6a9a"/>')
    f.line(-4, 0, 26, 0, "#5a6a9a", 2)
    f.line(7, 0, 0, 24, B_COL, 4)
    f.corner(0, 0, 1, 0, 0, 1, 1.6, LIGHT)
    f.text(3.5, -1.6, "7 m", 14, LIGHT, True)
    f.text(5.2, 13, "25 m ladder", 14, B_COL, True, anchor="start")
    f.text(-1.2, 12, "?", 20, "#ffd97a", True, anchor="end")
    return f.svg()


def _diamond():
    f = _Fig(300, 270, 1.3, 150, 250, "A baseball diamond: a square with 90 foot sides, "
             "with the throw from home plate to second base marked", dark=True)
    h = 63.64  # half the diagonal of a 90 ft square
    home, first, second, third = (0, 0), (h, h), (0, 2 * h), (-h, h)
    f.poly([home, first, second, third], "rgba(30,125,67,.30)", LIGHT, 2)
    f.line(0, 0, 0, 2 * h, "#ffd97a", 2.5, "6 5")
    for p, name, dx, dy, anc in [(home, "home", 0, -9, "middle"), (first, "1st", 8, 0, "start"),
                                 (second, "2nd", 0, 9, "middle"), (third, "3rd", -8, 0, "end")]:
        f.dot(p[0], p[1], 5, "#fff")
        f.text(p[0] + dx, p[1] + dy, name, 13, LIGHT, anchor=anc, halo=False)
    f.text(38, 26, "90 ft", 13, LIGHT, anchor="start")
    f.text(-38, 26, "90 ft", 13, LIGHT, anchor="end")
    f.text(5, h, "?", 20, "#ffd97a", True, anchor="start")
    return f.svg()


def _stargrid():
    f = _Fig(320, 300, 26, 110, 275, "A coordinate grid with one star at negative 2, 1 and another at 4, 9", dark=True)
    for k in range(-3, 8):
        f.line(k, 0, k, 10, "rgba(238,241,251,.16)", 1)
    for k in range(0, 11):
        f.line(-3, k, 7, k, "rgba(238,241,251,.16)", 1)
    f.line(-3, 0, 7, 0, "#8f9cc4", 1.5)
    f.line(0, 0, 0, 10, "#8f9cc4", 1.5)
    f.line(-2, 1, 4, 1, "#aebadf", 2, "5 4")
    f.line(4, 1, 4, 9, "#aebadf", 2, "5 4")
    f.line(-2, 1, 4, 9, "#ffd97a", 2.5)
    f.corner(4, 1, -1, 0, 0, 1, 0.4, LIGHT)
    for x, y in [(-2, 1), (4, 9)]:
        f.raw('<path transform="translate(%.1f %.1f)" d="M0,-9 L2.6,-2.8 9,-2.8 3.8,1.4 5.6,8 0,4 -5.6,8 -3.8,1.4 -9,-2.8 -2.6,-2.8Z" '
              'fill="#e8a90c" stroke="#ffe9b0"/>' % f.xy(x, y))
    f.text(-2, 0.15, "(&#8722;2, 1)", 12, LIGHT)
    f.text(4.4, 9.2, "(4, 9)", 12, LIGHT, anchor="start")
    f.text(0.4, 5.4, "?", 20, "#ffd97a", True)
    for k in (-2, 2, 4, 6):
        f.text(k, -0.45, str(k).replace("-", "&#8722;"), 10, "#8f9cc4", halo=False)
    for k in (2, 4, 6, 8, 10):
        f.text(-0.3, k, str(k), 10, "#8f9cc4", anchor="end", halo=False)
    return f.svg()


def _horizon():
    f = _Fig(340, 280, 1, 150, 250, "The Earth's curve with the space station above it; the line of sight "
             "just touches the Earth at the horizon, making a right angle with the radius there", dark=True)
    f.raw('<circle cx="150" cy="250" r="120" fill="rgba(58,93,168,.35)" stroke="#8fb0ff" stroke-width="2"/>')
    iss, tan = (0, 180), (89.44, 80)
    f.line(0, 0, 0, 180, "#aebadf", 2)
    f.line(0, 0, tan[0], tan[1], "#aebadf", 2)
    f.line(iss[0], iss[1], tan[0], tan[1], "#ffd97a", 2.5)
    f.corner(tan[0], tan[1], -0.7454, -0.6667, -0.6667, 0.7454, 11, LIGHT)
    f.dot(0, 0, 3.5, "#fff")
    f.dot(tan[0], tan[1], 4, "#fff")
    f.raw('<g transform="translate(150 70)"><rect x="-13" y="-3" width="9" height="6" fill="#8fb0ff"/>'
          '<rect x="4" y="-3" width="9" height="6" fill="#8fb0ff"/><rect x="-4" y="-4" width="8" height="8" fill="#fff"/></g>')
    f.text(-8, 196, "space station", 12, LIGHT, anchor="end", halo=False)
    f.text(-6, 90, "6,771 km", 12, LIGHT, anchor="end")
    f.text(52, 30, "6,371 km", 12, LIGHT, anchor="start")
    f.text(55, 140, "?", 20, "#ffd97a", True, anchor="start")
    f.text(98, 78, "horizon", 12, LIGHT, anchor="start", halo=False)
    f.text(0, -16, "centre of the Earth", 11, LIGHT, halo=False)
    f.text(182, 236, "not to scale", 10, "#8f9cc4", anchor="end", italic=True, halo=False)
    return f.svg()


# ---------------------------------------------------------------------------
# Live widgets
# ---------------------------------------------------------------------------
_BOX = 'background:#fdf9ee; border:1.5px solid #c9b57e; border-radius:12px; padding:14px 16px; margin:14px 0;'
_CAP = ('text-align:center; font-size:.8rem; letter-spacing:2px; text-transform:uppercase; '
        'color:#8a6400; font-weight:bold; margin-bottom:8px;')
_BTN = ('font-family:Georgia,serif; cursor:pointer; background:#fff8e6; border:1.5px solid #c9b57e; '
        'border-radius:8px; padding:7px 12px; font-size:.85rem; color:#5a4a1a;')

MONOCHORD = ('<div style="%s">\n  <div style="%s">Your monochord &middot; one string, one movable bridge</div>' % (_BOX, _CAP)) + r"""
  <div style="text-align:center;">
    <svg id="mc-svg" width="560" height="150" viewBox="0 0 560 150" font-family="Georgia,serif" style="max-width:100%; height:auto; cursor:pointer; touch-action:manipulation;" role="group" aria-label="A monochord. Choose a mark to move the bridge there and hear the note.">
      <text id="mc-len" x="280" y="16" text-anchor="middle" font-size="14" fill="#22304f">whole string: 120 cm</text>
      <rect x="20" y="54" width="520" height="84" rx="6" fill="#c9a24a" stroke="#5c3d15" stroke-width="2"/>
      <rect x="21" y="55" width="518" height="8" rx="4" fill="#e8c97a"/>
      <rect x="36" y="34" width="6" height="22" fill="#5c3d15"/><rect x="518" y="34" width="6" height="22" fill="#5c3d15"/>
      <line x1="40" y1="38" x2="520" y2="38" stroke="#b9a66e" stroke-width="2"/>
      <line id="mc-live" x1="40" y1="38" x2="520" y2="38" stroke="#22304f" stroke-width="3"/>
      <g id="mc-marks"></g>
      <polygon id="mc-bridge" points="-9,54 0,33 9,54" fill="#b03030" stroke="#5c1a1a" style="display:none; transition:transform .25s ease;"/>
    </svg>
  </div>
  <div id="mc-out" style="text-align:center; font-weight:bold; font-size:1.02rem; color:#3d3320; margin:4px 0 6px; min-height:1.3em;">Click the string above any mark, and listen.</div>
  <div style="text-align:center; font-size:.8rem; color:#8a6400;">Each click plays the whole string, then the shortened string, then both together. Turn your sound on.</div>
</div>
<script>
(function(){
  var svg = document.getElementById('mc-svg');
  if (!svg) return;
  var NS = 'http://www.w3.org/2000/svg', X0 = 40, LEN = 480, BASE = 220, FULL = 120, ctx = null;
  var MARKS = [
    {n: 1,  d: 2,  name: 'octave', say: 'an octave', row: 0},
    {n: 2,  d: 3,  name: 'fifth',  say: 'a fifth',   row: 1},
    {n: 3,  d: 4,  name: 'fourth', say: 'a fourth',  row: 0},
    {n: 15, d: 16, name: 'clumsy', say: '',          row: 1},
    {n: 1,  d: 1,  name: 'whole',  say: '',          row: 0}
  ];
  var out = document.getElementById('mc-out'), live = document.getElementById('mc-live'),
      bridge = document.getElementById('mc-bridge'), len = document.getElementById('mc-len'),
      holder = document.getElementById('mc-marks');
  function el(tag, attrs, text){
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    return e;
  }
  MARKS.forEach(function(m, i){
    m.x = X0 + LEN * m.n / m.d;
    var y = m.row ? 118 : 96;
    var g = el('g', {tabindex: '0', role: 'button',
      'aria-label': (m.n === m.d ? 'Whole string' : m.n + ' ' + m.d + 'ths of the string, ' + m.name)});
    g.appendChild(el('line', {x1: m.x, y1: 56, x2: m.x, y2: y - 15, stroke: '#5c3d15', 'stroke-width': 1.5}));
    g.appendChild(el('text', {x: m.x, y: y, 'text-anchor': 'middle', 'font-size': 15, 'font-weight': 'bold', fill: '#3d2a0c'},
      m.n === m.d ? '1' : m.n + '/' + m.d));
    g.appendChild(el('text', {x: m.x, y: y + 14, 'text-anchor': 'middle', 'font-size': 11, 'font-style': 'italic', fill: '#3d2a0c'}, m.name));
    g.addEventListener('keydown', function(ev){
      if (ev.key === 'Enter' || ev.key === ' '){ ev.preventDefault(); choose(i); }
    });
    m.g = g; holder.appendChild(g);
  });
  function pluck(freq, when, dur){
    var o = ctx.createOscillator(), g = ctx.createGain();
    o.type = 'triangle'; o.frequency.value = freq;
    g.gain.setValueAtTime(0.0001, when);
    g.gain.exponentialRampToValueAtTime(0.3, when + 0.012);
    g.gain.exponentialRampToValueAtTime(0.0001, when + dur);
    o.connect(g); g.connect(ctx.destination);
    o.start(when); o.stop(when + dur + 0.05);
  }
  function play(n, d){
    var AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return false;
    try {
      if (!ctx) ctx = new AC();
      if (ctx.state === 'suspended') ctx.resume();
      var t = ctx.currentTime + 0.03, f = BASE * d / n;
      if (n === d){ pluck(BASE, t, 1.6); return true; }
      pluck(BASE, t, 0.9); pluck(f, t + 0.75, 0.9);
      pluck(BASE, t + 1.5, 1.8); pluck(f, t + 1.5, 1.8);
      return true;
    } catch (e) { return false; }
  }
  function choose(i){
    var m = MARKS[i], whole = (m.n === m.d);
    live.setAttribute('x2', m.x.toFixed(1));
    bridge.style.display = whole ? 'none' : 'block';
    bridge.style.transform = 'translate(' + m.x.toFixed(1) + 'px,0px)';
    MARKS.forEach(function(k){
      var on = (k === m), t = k.g.getElementsByTagName('text');
      for (var j = 0; j < t.length; j++) t[j].setAttribute('fill', on ? '#8a1f1f' : '#3d2a0c');
    });
    var cm = Math.round(FULL * m.n / m.d * 10) / 10;
    len.textContent = whole ? 'whole string: 120 cm' : 'sounding part: ' + cm + ' cm of 120';
    var ok = play(m.n, m.d), msg;
    if (whole) msg = 'The whole string: your starting note.';
    else if (m.d > 10) msg = 'A clumsy fraction, and a sour, restless sound. No simple ratio, no sweetness.';
    else msg = m.n + '/' + m.d + ' of the string gives ' + m.say + ': a simple ratio, a sweet sound.';
    out.textContent = msg + (ok ? '' : ' (No sound on this device, but the ratios are just as true.)');
  }
  svg.addEventListener('click', function(ev){
    var r = svg.getBoundingClientRect();
    if (!r.width) return;
    var x = (ev.clientX - r.left) * 560 / r.width, best = 0;
    for (var i = 1; i < MARKS.length; i++)
      if (Math.abs(MARKS[i].x - x) < Math.abs(MARKS[best].x - x)) best = i;
    choose(best);
  });
})();
</script>"""

MACHINE = ('<div style="%s">\n  <div style="%s">Your theorem machine &middot; build any right triangle</div>' % (_BOX, _CAP)) + r'''
  <div style="text-align:center;">
    <svg id="pm-svg" width="360" height="330" viewBox="0 0 360 330" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;"></svg>
  </div>
  <div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap; margin:10px 0 0; font-size:1.05rem; color:#3d3320;">
    <span style="color:#3a5da8;">a&#178; = <b id="pm-a2">9</b></span>
    <span style="color:#8a6400;">b&#178; = <b id="pm-b2">16</b></span>
    <span style="color:#b03030;">a&#178; + b&#178; = <b id="pm-c2">25</b></span>
  </div>
  <div id="pm-verdict" style="text-align:center; font-weight:bold; font-size:1.05rem; margin:6px 0 12px; min-height:1.3em;">&nbsp;</div>
  <div style="max-width:480px; margin:0 auto;">
    <label style="display:block; font-size:.92rem; color:#3a5da8; margin-bottom:2px;">Leg a: <b id="pm-al">3</b></label>
    <input id="pm-a" type="range" min="1" max="12" value="3" style="width:100%;" aria-label="leg a">
    <label style="display:block; font-size:.92rem; color:#8a6400; margin:8px 0 2px;">Leg b: <b id="pm-bl">4</b></label>
    <input id="pm-b" type="range" min="1" max="12" value="4" style="width:100%;" aria-label="leg b">
  </div>
  <div style="text-align:center; margin-top:12px; display:flex; gap:8px; flex-wrap:wrap; justify-content:center;">
    <button type="button" class="pm-preset" data-a="3" data-b="4">3 and 4</button>
    <button type="button" class="pm-preset" data-a="6" data-b="8">6 and 8</button>
    <button type="button" class="pm-preset" data-a="5" data-b="12">5 and 12</button>
    <button type="button" class="pm-preset" data-a="1" data-b="1">1 and 1</button>
    <button type="button" class="pm-preset" data-a="4" data-b="5">4 and 5</button>
  </div>
</div>
<script>
(function(){
  var sa = document.getElementById('pm-a'), sb = document.getElementById('pm-b');
  if (!sa) return;
  var svg = document.getElementById('pm-svg'), W = 360, H = 330, M = 16;
  function draw(){
    var a = Number(sa.value), b = Number(sb.value), c2 = a*a + b*b, c = Math.sqrt(c2);
    var whole = Math.abs(c - Math.round(c)) < 1e-9;
    var s = Math.min((W - 2*M) / (2*a + b), (H - 2*M) / (a + 2*b));
    var ox = (W - (2*a + b)*s) / 2 + a*s, oy = (H - (a + 2*b)*s) / 2 + (a + b)*s;
    function X(x){ return (ox + x*s).toFixed(1); }
    function Y(y){ return (oy - y*s).toFixed(1); }
    function poly(p, fill, stroke, sw){
      var t = '';
      for (var i = 0; i < p.length; i++) t += X(p[i][0]) + ',' + Y(p[i][1]) + ' ';
      return '<polygon points="' + t + '" fill="' + fill + '" stroke="' + stroke + '" stroke-width="' + sw + '" stroke-linejoin="round"/>';
    }
    function line(x1, y1, x2, y2, col){
      return '<line x1="' + X(x1) + '" y1="' + Y(y1) + '" x2="' + X(x2) + '" y2="' + Y(y2) + '" stroke="' + col + '" stroke-width="1"/>';
    }
    function label(x, y, txt, col, side){
      if (side * s < 26) return '';
      var fs = Math.max(12, Math.min(22, side * s * 0.3));
      return '<text x="' + X(x) + '" y="' + (Number(Y(y)) + fs*0.35).toFixed(1) + '" font-size="' + fs.toFixed(0) +
        '" font-weight="bold" text-anchor="middle" fill="' + col + '" stroke="#fffdf4" stroke-width="4" paint-order="stroke" stroke-linejoin="round">' + txt + '</text>';
    }
    var h = '', k;
    h += poly([[0,0],[0,a],[-a,a],[-a,0]], 'rgba(58,93,168,.22)', '#3a5da8', 2);
    for (k = 1; k < a; k++) h += line(-k, 0, -k, a, 'rgba(58,93,168,.4)') + line(-a, k, 0, k, 'rgba(58,93,168,.4)');
    h += poly([[0,0],[b,0],[b,-b],[0,-b]], 'rgba(232,169,12,.30)', '#e8a90c', 2);
    for (k = 1; k < b; k++) h += line(k, 0, k, -b, 'rgba(138,100,0,.35)') + line(0, -k, b, -k, 'rgba(138,100,0,.35)');
    h += poly([[b,0],[0,a],[a,a+b],[a+b,b]], 'rgba(176,48,48,.18)', '#b03030', 2);
    if (whole){
      var ux = -b/c, uy = a/c, nx = a/c, ny = b/c;
      for (k = 1; k < Math.round(c); k++){
        h += line(b + k*nx, k*ny, k*nx, a + k*ny, 'rgba(176,48,48,.35)');
        h += line(b + k*ux, k*uy, b + k*ux + c*nx, k*uy + c*ny, 'rgba(176,48,48,.35)');
      }
    }
    h += poly([[0,0],[b,0],[0,a]], '#e6d9b8', '#22304f', 2.5);
    var q = Math.min(0.45, 11 / s);
    h += '<polyline points="' + X(q) + ',' + Y(0) + ' ' + X(q) + ',' + Y(q) + ' ' + X(0) + ',' + Y(q) + '" fill="none" stroke="#22304f" stroke-width="1.5"/>';
    h += label(-a/2, a/2, a*a, '#3a5da8', a) + label(b/2, -b/2, b*b, '#8a6400', b) + label((a+b)/2, (a+b)/2, c2, '#b03030', c);
    svg.innerHTML = h;
    document.getElementById('pm-al').textContent = a;
    document.getElementById('pm-bl').textContent = b;
    document.getElementById('pm-a2').textContent = a*a;
    document.getElementById('pm-b2').textContent = b*b;
    document.getElementById('pm-c2').textContent = c2;
    var v = document.getElementById('pm-verdict');
    if (whole){
      v.textContent = '★ The hypotenuse is exactly ' + Math.round(c) + ', because ' + Math.round(c) + ' × ' + Math.round(c) + ' = ' + c2 + '. A whole-number triangle!';
      v.style.color = '#1e7d43';
    } else {
      v.textContent = 'The hypotenuse is the number that squares to ' + c2 + ': about ' + c.toFixed(2) + '. Real, but not whole.';
      v.style.color = '#b03030';
    }
  }
  sa.addEventListener('input', draw);
  sb.addEventListener('input', draw);
  var ps = document.querySelectorAll('.pm-preset');
  for (var i = 0; i < ps.length; i++){
    ps[i].setAttribute('style', '@@BTN@@');
    ps[i].addEventListener('click', function(){ sa.value = this.dataset.a; sb.value = this.dataset.b; draw(); });
  }
  draw();
})();
</script>'''.replace("@@BTN@@", _BTN)

SLIDER_PROOF = ('<div style="%s">\n  <div style="%s">The sliding proof &middot; four triangles in a square tray</div>' % (_BOX, _CAP)) + r"""
  <div style="display:flex; gap:18px; flex-wrap:wrap; justify-content:center;">
    <div style="text-align:center;">
      <svg id="rp-left" width="300" height="300" viewBox="0 0 332 332" font-family="Georgia,serif" style="max-width:100%; height:auto;" role="img" aria-label="Before: four triangles in the corners of the tray, leaving one tilted square of side c"></svg>
      <div style="font-size:.9rem; color:#b03030; font-weight:bold;">Before: one tilted square, side c</div>
    </div>
    <div style="text-align:center;">
      <svg id="rp-right" width="300" height="300" viewBox="0 0 332 332" font-family="Georgia,serif" style="max-width:100%; height:auto;" role="img" aria-label="The same tray and triangles, which slide to leave two squares of sides a and b"></svg>
      <div id="rp-rcap" style="font-size:.9rem; color:#4a5878; font-weight:bold;">The same tray, the same triangles</div>
    </div>
  </div>
  <div style="text-align:center; margin:12px 0 10px;">
    <button type="button" id="rp-go" style="background:#e8a90c; color:#2a2005; font-weight:bold; font-size:1rem; border:none; border-radius:8px; padding:10px 20px; font-family:Georgia,serif; cursor:pointer;">Slide the triangles &#9654;</button>
  </div>
  <div id="rp-out" style="text-align:center; font-size:1rem; color:#3d3320; margin:4px 0 2px; line-height:1.6;"></div>
  <div id="rp-verdict" style="text-align:center; font-weight:bold; font-size:1.05rem; margin:4px 0 12px; min-height:1.3em; color:#22304f;"></div>
  <div style="max-width:480px; margin:0 auto;">
    <label style="display:block; font-size:.92rem; color:#3d3320; margin-bottom:2px;">Change the triangle: legs a = <b id="rp-al">3</b> and b = <b id="rp-bl">4</b></label>
    <input id="rp-a" type="range" min="2" max="12" value="6" style="width:100%;" aria-label="shape of the triangle">
    <div style="display:flex; justify-content:space-between; font-size:.76rem; color:#8a6400;"><span>long and thin</span><span>the tray stays 7 &times; 7</span><span>long and thin</span></div>
  </div>
</div>
<script>
(function(){
  var sl = document.getElementById('rp-a');
  if (!sl) return;
  var NS = 'http://www.w3.org/2000/svg', U = 40, O = 26, S = 7, slid = false;
  function el(tag, attrs, parent, text){
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    parent.appendChild(e);
    return e;
  }
  function label(parent, txt, size, fill){
    return el('text', {'text-anchor': 'middle', 'font-size': size, 'font-weight': 'bold', fill: fill,
      stroke: '#fffdf4', 'stroke-width': 4, 'paint-order': 'stroke', 'stroke-linejoin': 'round'}, parent, txt);
  }
  function Tray(id, animated){
    var svg = document.getElementById(id), T = this;
    el('rect', {x: O, y: O, width: S*U, height: S*U, fill: '#fffdf4'}, svg);
    T.c = el('polygon', {fill: 'rgba(176,48,48,.28)'}, svg);
    T.a2 = el('rect', {fill: 'rgba(58,93,168,.30)'}, svg);
    T.b2 = el('rect', {fill: 'rgba(232,169,12,.40)'}, svg);
    T.t = [0,1,2,3].map(function(i){
      var t = el('polygon', {fill: '#cdb98a', stroke: '#22304f', 'stroke-width': 2, 'stroke-linejoin': 'round'}, svg);
      if (animated) t.style.transition = 'transform .9s ease ' + (i * 0.12) + 's';
      return t;
    });
    el('rect', {x: O, y: O, width: S*U, height: S*U, fill: 'none', stroke: '#22304f', 'stroke-width': 3}, svg);
    T.big = {c: label(svg, 'c²', 26, '#b03030'), a: label(svg, 'a²', 22, '#3a5da8'), b: label(svg, 'b²', 22, '#8a6400')};
    T.cs = [0,1,2,3].map(function(){ return label(svg, 'c', 17, '#b03030'); });
    T.edge = [0,1,2,3].map(function(){ return label(svg, '', 16, '#22304f'); });
    if (animated) [T.c, T.a2, T.b2, T.big.c, T.big.a, T.big.b].concat(T.cs).forEach(function(e){ e.style.transition = 'opacity .45s ease'; });
  }
  function pts(p){ return p.map(function(q){ return (O + q[0]*U) + ',' + (O + q[1]*U); }).join(' '); }
  function put(e, x, y, show){ e.setAttribute('x', O + x*U); e.setAttribute('y', O + y*U + 6); e.style.opacity = show ? 1 : 0; }
  function fmt(v){ return String(Math.round(v * 100) / 100); }
  function paint(T, a, b, after){
    T.t[0].setAttribute('points', pts([[0,0],[a,0],[0,b]]));
    T.t[1].setAttribute('points', pts([[S,0],[a,0],[S,a]]));
    T.t[2].setAttribute('points', pts([[S,S],[S,a],[b,S]]));
    T.t[3].setAttribute('points', pts([[0,S],[b,S],[0,b]]));
    T.t[0].style.transform = after ? 'translate(0px,' + (a*U) + 'px)' : 'translate(0px,0px)';
    T.t[2].style.transform = after ? 'translate(' + (-b*U) + 'px,0px)' : 'translate(0px,0px)';
    T.t[3].style.transform = after ? 'translate(' + (a*U) + 'px,' + (-b*U) + 'px)' : 'translate(0px,0px)';
    T.c.setAttribute('points', pts([[a,0],[S,a],[b,S],[0,b]]));
    T.a2.setAttribute('x', O); T.a2.setAttribute('y', O); T.a2.setAttribute('width', a*U); T.a2.setAttribute('height', a*U);
    T.b2.setAttribute('x', O + a*U); T.b2.setAttribute('y', O + a*U); T.b2.setAttribute('width', b*U); T.b2.setAttribute('height', b*U);
    T.c.style.opacity = after ? 0 : 1; T.a2.style.opacity = after ? 1 : 0; T.b2.style.opacity = after ? 1 : 0;
    put(T.big.c, S/2, S/2, !after); put(T.big.a, a/2, a/2, after); put(T.big.b, a + b/2, a + b/2, after);
    // the letter c sits on every hypotenuse, nudged off the line toward open space
    var hyp = after ? [[[a,a],[0,S]], [[a,0],[S,a]]] : [[[a,0],[0,b]], [[a,0],[S,a]], [[S,a],[b,S]], [[b,S],[0,b]]];
    for (var i = 0; i < 4; i++){
      if (!hyp[i]){ T.cs[i].style.opacity = 0; continue; }
      var mx = (hyp[i][0][0] + hyp[i][1][0]) / 2, my = (hyp[i][0][1] + hyp[i][1][1]) / 2, dx, dy;
      if (after){ dx = (i === 0 ? -1 : 1) * a; dy = (i === 0 ? -1 : 1) * -b; var n = Math.sqrt(dx*dx + dy*dy); dx = 0.32*dx/n; dy = -0.32*dy/n; if (i === 0){ dx = -Math.abs(dx); dy = -Math.abs(dy); } else { dx = Math.abs(dx); dy = -Math.abs(dy); } }
      else { dx = S/2 - mx; dy = S/2 - my; var m = Math.sqrt(dx*dx + dy*dy) || 1; dx = 0.34*dx/m; dy = 0.34*dy/m; }
      put(T.cs[i], mx + dx, my + dy, true);
    }
    // a and b along the top and left edges of the tray
    var top = [['a', a/2], ['b', a + b/2]], left = after ? [['a', a/2], ['b', a + b/2]] : [['b', b/2], ['a', b + a/2]];
    T.edge[0].textContent = top[0][0];  put(T.edge[0], top[0][1], -0.42, true);
    T.edge[1].textContent = top[1][0];  put(T.edge[1], top[1][1], -0.42, true);
    T.edge[2].textContent = left[0][0]; put(T.edge[2], -0.38, left[0][1], true);
    T.edge[3].textContent = left[1][0]; put(T.edge[3], -0.38, left[1][1], true);
  }
  var L = new Tray('rp-left', false), R = new Tray('rp-right', true);
  function draw(){
    var a = Number(sl.value) / 2, b = S - a, tri = 2*a*b, hole = S*S - tri;
    paint(L, a, b, false);
    paint(R, a, b, slid);
    document.getElementById('rp-al').textContent = fmt(a);
    document.getElementById('rp-bl').textContent = fmt(b);
    var cap = document.getElementById('rp-rcap');
    cap.textContent = slid ? 'After: two squares, sides a and b' : 'The same tray, the same triangles';
    cap.style.color = slid ? '#3a5da8' : '#4a5878';
    document.getElementById('rp-out').innerHTML = 'Each tray: 7 × 7 = <b>49</b> &nbsp;&middot;&nbsp; four triangles: 4 × (' +
      fmt(a) + ' × ' + fmt(b) + ' ÷ 2) = <b>' + fmt(tri) + '</b> &nbsp;&middot;&nbsp; empty space: 49 − ' + fmt(tri) + ' = <b>' + fmt(hole) + '</b>';
    document.getElementById('rp-verdict').innerHTML = slid
      ? '<span style="color:#b03030">c² = ' + fmt(hole) + '</span> &nbsp;and&nbsp; <span style="color:#3a5da8">a² + b² = ' + fmt(a*a) + ' + ' + fmt(b*b) + ' = ' + fmt(hole) + '</span>'
      : '<span style="color:#b03030">The empty space is c² = ' + fmt(hole) + '</span>';
    document.getElementById('rp-go').innerHTML = slid ? '&#9664; Slide them back' : 'Slide the triangles &#9654;';
  }
  sl.addEventListener('input', draw);
  document.getElementById('rp-go').addEventListener('click', function(){ slid = !slid; draw(); });
  draw();
})();
</script>"""

BOWSTRING = ('<div style="%s">\n  <div style="%s">Your bowstring diagram &middot; choose any two legs</div>' % (_BOX, _CAP)) + r"""
  <div style="text-align:center;">
    <svg id="bw-svg" width="330" height="330" viewBox="0 0 330 330" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;" role="img" aria-label="A square on the hypotenuse filled by four red right triangles and a small yellow square in the middle"></svg>
  </div>
  <div id="bw-out" style="text-align:center; font-size:1rem; color:#3d3320; margin:10px 0 2px; line-height:1.7;"></div>
  <div id="bw-verdict" style="text-align:center; font-weight:bold; font-size:1.05rem; margin:2px 0 12px; color:#1e7d43;"></div>
  <div style="max-width:480px; margin:0 auto;">
    <label style="display:block; font-size:.92rem; color:#3d3320; margin-bottom:2px;">Leg a: <b id="bw-al">3</b></label>
    <input id="bw-a" type="range" min="1" max="12" value="3" style="width:100%;" aria-label="leg a">
    <label style="display:block; font-size:.92rem; color:#3d3320; margin:8px 0 2px;">Leg b: <b id="bw-bl">4</b></label>
    <input id="bw-b" type="range" min="1" max="12" value="4" style="width:100%;" aria-label="leg b">
  </div>
  <div style="text-align:center; margin-top:12px; display:flex; gap:8px; flex-wrap:wrap; justify-content:center;">
    <button type="button" class="bw-preset" data-a="3" data-b="4">3 and 4</button>
    <button type="button" class="bw-preset" data-a="5" data-b="12">5 and 12</button>
    <button type="button" class="bw-preset" data-a="2" data-b="9">2 and 9</button>
    <button type="button" class="bw-preset" data-a="6" data-b="6">6 and 6</button>
  </div>
</div>
<script>
(function(){
  var sa = document.getElementById('bw-a'), sb = document.getElementById('bw-b');
  if (!sa) return;
  var svg = document.getElementById('bw-svg'), BOX = 250, OX = 40, OY = 32;
  function txt(x, y, t, size, fill){
    return '<text x="' + x.toFixed(1) + '" y="' + (y + size * 0.35).toFixed(1) + '" font-size="' + size + '" font-weight="bold" text-anchor="middle" fill="' + fill +
      '" stroke="#fffdf4" stroke-width="4" paint-order="stroke" stroke-linejoin="round">' + t + '</text>';
  }
  function poly(p, fill, stroke, sw){
    return '<polygon points="' + p.map(function(q){ return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' ') +
      '" fill="' + fill + '" stroke="' + stroke + '" stroke-width="' + sw + '" stroke-linejoin="round"/>';
  }
  function fmt(v){ return String(Math.round(v * 100) / 100); }
  function draw(){
    var a = Number(sa.value), b = Number(sb.value), c2 = a*a + b*b, c = Math.sqrt(c2), k = BOX / c;
    // corners of the big square, screen coordinates, going round anticlockwise as seen on screen
    var P = [[OX, OY + BOX], [OX + BOX, OY + BOX], [OX + BOX, OY], [OX, OY]];
    var Q = [], h = '';
    for (var i = 0; i < 4; i++){
      var p0 = P[i], p1 = P[(i + 1) % 4];
      var ux = (p1[0] - p0[0]) / BOX, uy = (p1[1] - p0[1]) / BOX;   // along the side
      var nx = uy, ny = -ux;                                           // pointing into the square
      Q.push([p0[0] + k * (b*b/c * ux + a*b/c * nx), p0[1] + k * (b*b/c * uy + a*b/c * ny)]);
    }
    for (i = 0; i < 4; i++) h += poly([P[i], P[(i + 1) % 4], Q[i]], 'rgba(190,60,40,.30)', '#8a2d1c', 2);
    if (a !== b) h += poly([Q[0], Q[1], Q[2], Q[3]], 'rgba(232,169,12,.55)', '#8a6400', 2);
    h += poly(P, 'none', '#22304f', 3);
    var tri = a * b / 2, mid = (b - a) * (b - a);
    var triPx = tri * k * k, midSide = Math.abs(b - a) * k;
    for (i = 0; i < 4; i++){
      if (triPx < 650) break;
      var g = [P[i], P[(i + 1) % 4], Q[i]];
      h += txt((g[0][0] + g[1][0] + g[2][0]) / 3, (g[0][1] + g[1][1] + g[2][1]) / 3, fmt(tri), Math.min(16, 10 + triPx / 900), '#8a2d1c');
    }
    if (midSide > 22) h += txt((Q[0][0] + Q[2][0]) / 2, (Q[0][1] + Q[2][1]) / 2, fmt(mid), Math.min(15, 9 + midSide / 12), '#5a4a1a');
    // name the sides of the bottom triangle
    h += txt(OX + BOX / 2, OY + BOX + 18, (Math.abs(c - Math.round(c)) < 1e-9) ? String(Math.round(c)) : '\u2248 ' + c.toFixed(2), 15, '#b03030');
    var mB = [(P[0][0] + Q[0][0]) / 2, (P[0][1] + Q[0][1]) / 2], mA = [(P[1][0] + Q[0][0]) / 2, (P[1][1] + Q[0][1]) / 2];
    if (b * k > 34) h += txt(mB[0] - 9, mB[1] - 9, 'b', 14, '#22304f');
    if (a * k > 34) h += txt(mA[0] + 9, mA[1] - 9, 'a', 14, '#22304f');
    svg.innerHTML = h;
    document.getElementById('bw-al').textContent = a;
    document.getElementById('bw-bl').textContent = b;
    document.getElementById('bw-out').innerHTML =
      'Four red triangles: 4 × (' + a + ' × ' + b + ' ÷ 2) = <b>' + fmt(4 * tri) + '</b>' +
      ' &nbsp;&middot;&nbsp; yellow square: (' + Math.max(a, b) + ' − ' + Math.min(a, b) + ')² = <b>' + fmt(mid) + '</b><br>' +
      'Big square: ' + fmt(4 * tri) + ' + ' + fmt(mid) + ' = <b style="color:#b03030">' + fmt(4 * tri + mid) + '</b>' +
      ' &nbsp;&middot;&nbsp; a² + b² = ' + (a*a) + ' + ' + (b*b) + ' = <b style="color:#3a5da8">' + c2 + '</b>';
    document.getElementById('bw-verdict').textContent = (a === b)
      ? '✓ They match. (With equal legs the yellow square shrinks to nothing, and it still works.)'
      : '✓ They match: the big square is always a² + b².';
  }
  sa.addEventListener('input', draw);
  sb.addEventListener('input', draw);
  var ps = document.querySelectorAll('.bw-preset');
  for (var j = 0; j < ps.length; j++){
    ps[j].setAttribute('style', '@@BTN@@');
    ps[j].addEventListener('click', function(){ sa.value = this.dataset.a; sb.value = this.dataset.b; draw(); });
  }
  draw();
})();
</script>""".replace("@@BTN@@", _BTN)

SHEAR = ('<div style="%s">\n  <div style="%s">Euclid&#8217;s moves &middot; slide, turn, slide</div>' % (_BOX, _CAP)) + r"""
  <div style="text-align:center;">
    <svg id="sh-svg" width="360" height="390" viewBox="0 0 360 390" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;" role="img" aria-label="Animation: each small square slides into a slanted shape, turns a quarter-turn about a corner of the triangle, and slides into its rectangle inside the big square, keeping its area"></svg>
  </div>
  <div id="sh-step" style="text-align:center; font-weight:bold; font-size:1.02rem; color:#22304f; margin:8px 0 2px; min-height:1.3em;"></div>
  <div id="sh-why" style="text-align:center; font-size:.95rem; color:#3d3320; margin:0 0 10px; min-height:2.6em; line-height:1.45;"></div>
  <div style="text-align:center; margin-bottom:10px;">
    <button type="button" id="sh-play" style="background:#e8a90c; color:#2a2005; font-weight:bold; font-size:1rem; border:none; border-radius:8px; padding:10px 20px; font-family:Georgia,serif; cursor:pointer;">&#9654; Play</button>
  </div>
  <div style="max-width:480px; margin:0 auto;">
    <input id="sh-t" type="range" min="0" max="600" value="0" style="width:100%;" aria-label="move through the animation by hand">
    <div style="display:flex; justify-content:space-between; font-size:.76rem;"><span style="color:#8a6400;">start</span><span style="color:#3a5da8;">blue: slide &middot; turn &middot; slide</span><span style="color:#8a6400;">gold: slide &middot; turn &middot; slide</span></div>
  </div>
</div>
<script>
(function(){
  var svg = document.getElementById('sh-svg'), sl = document.getElementById('sh-t');
  if (!svg) return;
  var S = 30, OX = 110, OY = 210;
  function X(x){ return OX + x * S; }
  function Y(y){ return OY - y * S; }
  function poly(p, fill, stroke, sw, dash){
    return '<polygon points="' + p.map(function(q){ return X(q[0]).toFixed(1) + ',' + Y(q[1]).toFixed(1); }).join(' ') +
      '" fill="' + fill + '" stroke="' + stroke + '" stroke-width="' + sw + '"' + (dash ? ' stroke-dasharray="' + dash + '"' : '') + ' stroke-linejoin="round"/>';
  }
  function txt(x, y, t, size, fill, halo){
    return '<text x="' + X(x).toFixed(1) + '" y="' + (Y(y) + size * 0.35).toFixed(1) + '" font-size="' + size + '" font-weight="bold" text-anchor="middle" fill="' + fill + '"' +
      (halo ? ' stroke="#fffdf4" stroke-width="4" paint-order="stroke" stroke-linejoin="round"' : '') + '>' + t + '</text>';
  }
  function lerp(p, q, k){ return [p[0] + (q[0] - p[0]) * k, p[1] + (q[1] - p[1]) * k]; }
  function rot(p, c, ang){
    var dx = p[0] - c[0], dy = p[1] - c[1], co = Math.cos(ang), si = Math.sin(ang);
    return [c[0] + dx * co - dy * si, c[1] + dx * si + dy * co];
  }
  function ease(k){ return k < 0.5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; }
  var A = [0, 0], B = [5, 0], C = [1.8, 2.4], F = [1.8, 0];
  // Each shape: fixed corner, the two moving corners for each slide, and the turn.
  // Left square on AC (area 9): slide keeps side A-D, top edge slides along its own line until it reaches B.
  var L = { pivot: A, ang: -Math.PI / 2, fill: 'rgba(58,93,168,.32)', stroke: '#3a5da8', label: '9', lc: '#3a5da8',
    sq: [A, C, [-0.6, 4.2], [-2.4, 1.8]],
    s1: [A, B, [2.6, 1.8], [-2.4, 1.8]],
    s3: [A, [0, -5], [1.8, -5], F] };
  // Right square on CB (area 16): slide keeps side B-E, top edge slides until it reaches A.
  var R = { pivot: B, ang: Math.PI / 2, fill: 'rgba(232,169,12,.40)', stroke: '#b8860b', label: '16', lc: '#8a6400',
    sq: [B, C, [4.2, 5.6], [7.4, 3.2]],
    s1: [B, A, [2.4, 3.2], [7.4, 3.2]],
    s3: [B, [5, -5], [1.8, -5], F] };
  function shape(o, t){
    var k, i, out = [];
    if (t <= 1){ k = ease(t); for (i = 0; i < 4; i++) out.push(lerp(o.sq[i], o.s1[i], k)); return out; }
    var turned = o.s1.map(function(p){ return rot(p, o.pivot, o.ang); });
    if (t <= 2){ k = ease(t - 1); return o.s1.map(function(p){ return rot(p, o.pivot, o.ang * k); }); }
    k = ease(t - 2);
    for (i = 0; i < 4; i++) out.push(lerp(turned[i], o.s3[i], k));
    return out;
  }
  var NAME = {L: ['blue', 'A'], R: ['gold', 'B']};
  function steps(o, k){
    var n = NAME[o];
    return [
      ['Step 1. Slide the ' + n[0] + ' square.', 'Its top edge slides along its own line, so the shape leans over. Same base, same height: the area stays the same.'],
      ['Step 2. Turn it.', 'A quarter-turn around corner ' + n[1] + ' of the triangle. Turning never changes area.'],
      ['Step 3. Slide again.', 'One more lean, straight down this time, and it fits exactly into its own part of the big square.']
    ][k];
  }
  function draw(t){
    var tl = Math.min(3, Math.max(0, t)), tr = Math.min(3, Math.max(0, t - 3)), h = '';
    h += poly([A, B, [5, -5], [0, -5]], 'none', '#b03030', 2.5);
    h += poly(L.sq, 'none', '#3a5da8', 1.2, '4 4') + poly(R.sq, 'none', '#b8860b', 1.2, '4 4');
    h += '<line x1="' + X(1.8) + '" y1="' + Y(0) + '" x2="' + X(1.8) + '" y2="' + Y(-5) + '" stroke="#22304f" stroke-width="1.2" stroke-dasharray="5 4"/>';
    h += poly([A, B, C], '#e6d9b8', 'none', 0);
    [[L, tl], [R, tr]].forEach(function(pair){
      var o = pair[0], p = shape(o, pair[1]), cx = 0, cy = 0;
      h += poly(p, o.fill, o.stroke, 2);
      p.forEach(function(q){ cx += q[0] / 4; cy += q[1] / 4; });
      o.c = [cx, cy];
    });
    h += poly([A, B, C], 'none', '#22304f', 2.5);
    h += txt(L.c[0], L.c[1], L.label, 18, L.lc, true) + txt(R.c[0], R.c[1], R.label, 18, R.lc, true);
    h += txt(-0.35, -0.3, 'A', 14, '#22304f', true) + txt(5.35, -0.3, 'B', 14, '#22304f', true) + txt(1.8, 2.85, 'C', 14, '#22304f', true);
    h += txt(2.5, -5.45, 'square on the hypotenuse: 25', 12, '#b03030', false);
    svg.innerHTML = h;
    var st;
    if (t <= 0.001) st = ['The two squares on the legs: 9 and 16.', 'Watch the blue square first, then the gold one. Each area label rides along with its shape.'];
    else if (t >= 5.999) st = ['Done: 9 + 16 fill the square on the hypotenuse.', 'Nothing was stretched, squashed, added or cut away. So a² + b² = c².'];
    else if (t < 3) st = steps('L', Math.min(2, Math.floor(t - 0.0001)));
    else if (t <= 3.001) st = ['The blue 9 has landed in the big square.', 'Now the gold square makes the same three moves.'];
    else st = steps('R', Math.min(2, Math.floor(t - 3.0001)));
    document.getElementById('sh-step').textContent = st[0];
    document.getElementById('sh-why').textContent = st[1];
  }
  var playing = false, raf = null, btn = document.getElementById('sh-play'), MAX = 600;
  function setBtn(){ btn.innerHTML = playing ? '&#10074;&#10074; Pause' : (Number(sl.value) >= MAX ? '&#8635; Play again' : '&#9654; Play'); }
  function stop(){ playing = false; if (raf) cancelAnimationFrame(raf); setBtn(); }
  function play(){
    if (Number(sl.value) >= MAX) sl.value = 0;
    playing = true; setBtn();
    var last = null, rested = 0, restingAt = -1;
    function frame(ts){
      if (!playing) return;
      if (last === null) last = ts;
      var dt = ts - last, v = Number(sl.value); last = ts;
      var whole = Math.round(v / 100) * 100;
      // pause for a moment at each step boundary so the eye can catch up
      if (Math.abs(v - whole) < 0.01 && whole > 0 && whole < MAX && restingAt !== whole){
        rested += dt;
        if (rested < 650){ raf = requestAnimationFrame(frame); return; }
        restingAt = whole; rested = 0;
      }
      v = Math.min(MAX, v + dt / 14);
      var next = (Math.floor(Number(sl.value) / 100) + 1) * 100;
      if (v > next && next < MAX) v = next;          // land exactly on the boundary, then rest
      sl.value = v; draw(v / 100);
      if (v >= MAX){ stop(); return; }
      raf = requestAnimationFrame(frame);
    }
    raf = requestAnimationFrame(frame);
  }
  btn.addEventListener('click', function(){ playing ? stop() : play(); });
  sl.addEventListener('input', function(){ stop(); draw(Number(sl.value) / 100); setBtn(); });
  draw(0);
})();
</script>"""

PYTHAGORAS = dict(
    title="The Secret in the Squares: Pythagoras and the Most-Proved Theorem in the World",
    h1="✦ The Secret in the Squares ✦",
    sub="Pythagoras, a clay tablet a thousand years older than he was, and the theorem that has been proved some 370 different ways",
    footer="Every date, number and proof is real · every legend is labeled as a legend<br>(the beans remain a mystery)",
    praise=["Q.E.D., {name}!", "Proved beyond doubt, {name}!", "Square on the mark, {name}!",
            "{name}, the brotherhood would let you past the curtain!",
            "Exactly right, {name}. All is number!"],
    cert_org="The Order of the Right Angle",
    cert_of="the tale of the secret in the squares",
    cert_rank="Master of the Hypotenuse",
    dev_skip=True,  # press \ to solve the next checkpoint (teacher shortcut)
    finale_title="The Proof Goes On",
    finale_html="""
<p>In 1927 an American teacher named <b>Elisha Loomis</b> published a whole book containing nothing but proofs of this one theorem. By its second edition it held about <b>370</b> of them: sliding proofs, windmill proofs, a president's trapezoid, proofs by people famous and unknown. No other theorem in mathematics has been proved so many ways. In the same book Loomis laid down a rule: there could never be a proof using <b>trigonometry</b>, the mathematics of angles, because trigonometry, he said, is itself built on the Pythagorean theorem. You'd be using the thing to prove the thing.</p>
<p>In <b>2023</b>, two high-school students from New Orleans, <b>Calcea Johnson</b> and <b>Ne'Kiya Jackson</b>, stood up at a meeting of professional mathematicians and presented a proof using trigonometry, one that carefully never leans on the theorem it is proving. It had started as a bonus question in a school math contest. Their work was published in a mathematics journal in 2024, with more new proofs added. The book said it couldn't be done. They checked anyway.</p>
<p>So count the chain. A scribe pressing wedges into wet clay in Babylon. Rope-stretchers in India, a commentator in China painting triangles red and yellow. A brotherhood in Italy who swore by a triangle of ten dots. Euclid in Alexandria. A congressman doodling a trapezoid. A boy in Munich who wouldn't take his uncle's word for it. Two teenagers in Louisiana. <b>Nearly four thousand years, and the same triangle.</b></p>
<p>That is what a proof buys you. Kings, empires and whole languages have vanished since the clay tablets were written. In all that time, a² + b² = c² has not changed by a hair. It was true before anyone noticed it. It will be true when every book about it has crumbled. And it never belonged to Pythagoras, or to Babylon, or to anyone: it belongs to whoever takes the trouble to prove it again. As of today, that includes you.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① In every right triangle, <b>a² + b² = c²</b>: the squares on the two legs add up to the square on the hypotenuse. Know two sides and you can calculate the third.</p>
<p>② Pythagoras didn't discover it. Babylonian scribes were using it around <b>1800 BC</b>, more than a thousand years before he was born. India and China found it too.</p>
<p>③ A rule that has worked every time you tried it is <i>evidence</i>. A <b>proof</b> covers every case at once, forever. You have now seen five: the sliding triangles, the bowstring diagram, Euclid's windmill, Garfield's trapezoid, and the schoolboy's similar triangles.</p>
<p>④ The diagonal of a 1 × 1 square is a number that <b>no fraction can ever equal</b>. The theorem broke its own discoverers' favourite belief, and they had to follow the proof anyway.</p>
<p>⑤ When you read <i>the story goes</i>, ask who wrote it down, and how long afterwards.</p>
</div>""",
    chapters=[
        # ------------------------------------------------------------------ 1
        dict(
            kicker="Chapter One · Samos and Croton · about 570–495 BC",
            title="The Man Behind the Curtain",
            html="""
<p>Around <b>530 BC</b>, a ship from the Greek island of Samos docked at <b>Croton</b>, a rich port near the toe of Italy's boot. Off stepped a man named <b>Pythagoras</b>. Within a few years he was the most talked-about person in the city, and the leader of something the world had not seen before: part school, part secret society. His followers shared their belongings, lived by his rules, and kept his teachings to themselves. New members, the old stories say, spent their first years in silence, listening to the master speak from <b>behind a curtain</b>. They were allowed to hear him, but not to see him.</p>
<p>Members were expected to adhere to strict rules <b>Never eat beans.</b> Never stir a fire with a knife. Don't pick up what has fallen from the table. When you get out of bed, smooth the sheets so your body leaves no print. Don't let swallows nest under your roof. Nobody is sure what the rules were <i>for</i>. His critics were already arguing about the beans. But the Pythagoreans kept to the rules without question.</p>
<p>They also believed that souls are born again, into new people and into animals. A poet named <b>Xenophanes</b>, who was alive at the same time, made a joke of it: Pythagoras sees a man beating a puppy and cries out to stop, because that's the soul of a friend, and he recognized the voice!</p>
<p>Because here is the trouble with Pythagoras. <b>He left no writings.</b> Not one line in his own words survives. His followers were sworn to secrecy, and they had a habit of crediting every discovery to the master; their way of ending an argument was <i>"He himself said it."</i> The detailed biographies we have were written <b>seven or eight hundred years after he died</b>, by admirers, and they are stuffed with wonders: a thigh made of gold, a river that greeted him by name, a day when he was seen in two cities at once. So all through this lesson, watch for three little words: <b><i>the story goes</i></b>. When you see them, a legend is coming, and your job is to ask how anybody could know.</p>
<p>And behind the curtain, they did <b>geometry</b>. Later Greek writers credit the Pythagoreans with one of the first facts every geometry student learns: the three angles of <i>any</i> triangle, added together, always make exactly two square corners, or <b>180 degrees</b>. Fat triangle, thin triangle, it makes no difference. You can test it with scissors: tear the three corners off a paper triangle, lay them point to point, and they line up along a straight edge every time.</p>
<div class="funfact">🫘 Even his death comes in three versions. In one, enemies chase him to the edge of a bean field; he refuses to trample the beans, and is caught. In another he starves in a temple. In a third he simply dies, old, in the town of Metapontum. The ancient writers who tell these stories tell all of them, which shows you how much anyone really knew.</div>""",
            cps=[dict(
                type="num",
                kicker="Countdown arithmetic",
                q="""Pythagoras was born about <b>570 BC</b> and landed in Croton about <b>530 BC</b>. Roughly how old was he when he stepped off the ship? (Careful: BC years count <i>down</i> as time moves forward.)""",
                answers=[40], unit="years old",
                hint="BC counts backwards, like a rocket countdown: 570 − 530.",
            ), dict(
                type="mc",
                kicker="The brotherhood's triangle rule",
                q="""The three angles of any triangle add up to <b>180°</b>. This triangle has a square corner, which is <b>90°</b>, and another angle of <b>35°</b>. How big is the third angle?""",
                figure=_angles(),
                mc=[("145°", False),
                    ("35°", False),
                    ("55°", True)],
                good="Right, {name}: 90 + 35 = 125, and 180 − 125 = 55. Notice something else: the two sharp angles, 35 and 55, make 90 between them. In a right triangle they always do. You will need that in Chapter Five.",
                bad="Add up what you already have, {name}: the square corner and the 35°. Then ask how much is still missing from 180°.",
            )],
        ),
        # ------------------------------------------------------------------ 2
        dict(
            kicker="Chapter Two · Croton · about 520 BC",
            title="All Is Number",
            html="""
<p>What did the brotherhood actually <i>study</i> behind that curtain? Numbers, but not the way a shopkeeper studies them. The Pythagoreans had noticed something that stunned them, and it came out of <b>music</b>.</p>
<p>Stretch a string tight and pluck it: you get a note. Now press the string down at exactly its <b>halfway</b> point and pluck again. The new note is higher, yet somehow it is the <i>same</i> note, the jump musicians call an <b>octave</b>. Let <b>two-thirds</b> of the string sound instead, and you get the strong, sweet jump called a <b>fifth</b>. Let <b>three-quarters</b> sound, and you get a <b>fourth</b>. The notes that belong together come from the simplest fractions there are: 1/2, 2/3, 3/4. Press just anywhere, and mostly you get mud.</p>
""" + MONOCHORD + """
<p>Think about how strange that is. Your <i>ear</i>, which has never heard of fractions, can tell a two-thirds string from a clumsy one. Beauty was obeying arithmetic. The Pythagoreans drew the wildest conclusion they could: if number rules music, maybe number rules <b>everything</b>: the planets, the seasons, the world itself. Their creed comes down to us as <b>"All is number."</b> It was a guess, and an enormous one. It is also, more or less, the guess that all of physics has been built on ever since.</p>
<p>Their holiest symbol was a triangle of ten dots called the <b>tetractys</b> (tet-RAK-tiss): rows of 1, 2, 3 and 4. Look at neighbouring rows and you'll find the music hiding inside: 2 to 1, 3 to 2, 4 to 3. Pythagoreans swore their oaths by it.</p>
""" + _tetractys() + """
<p>The story goes that Pythagoras found the musical ratios while walking past a <b>blacksmith's forge</b>: he heard the hammers ringing in harmony, weighed them, and found their weights stood in the ratios 12, 9, 8 and 6. It is a wonderful story, and it was copied from book to book for more than a thousand years. It is also <b>false</b>, and anyone with two hammers could have found that out. A hammer twice as heavy does not ring an octave lower. Nobody checked; they trusted the book. When an Italian lute player named Vincenzo Galilei finally hung real weights on real strings in the 1580s, he found the old numbers wrong there too: to raise a string one octave you need <b>four</b> times the weight, not two. (His son Galileo picked up the habit of checking.)</p>
<p>The <i>string lengths</i>, though, are true. And unlike the scholars who copied the hammer story, you have just tested them with your own ears.</p>
<div class="bigidea">🌟 <b>Big Idea #1:</b> A story can be repeated for a thousand years and still be wrong. What made the string ratios <i>knowledge</i> and the hammers a <i>legend</i> was not who told them or how often. It was that one of them survives being tested.</div>""",
            cps=[dict(
                type="num",
                kicker="Tune the string",
                q="""The monochord's rule works on any string. A harp string is <b>90 cm</b> long. To sound the <b>fifth</b> above its note, exactly <b>two-thirds</b> of it must vibrate. How many centimeters is that?""",
                answers=[60], unit="cm",
                hint="One third of 90 is 30. Two thirds is twice that.",
            ), dict(
                type="num",
                kicker="Grow the tetractys",
                q="""The tetractys has rows of 1, 2, 3 and 4 dots, ten in all. Add one more row underneath, with <b>5</b> dots. How many dots does the bigger triangle have?""",
                answers=[15], unit="dots",
                hint="1 + 2 + 3 + 4 + 5. (Numbers you can stack into triangles like this are called triangular numbers: 1, 3, 6, 10, 15. The Pythagoreans loved them.)",
            )],
        ),
        # ------------------------------------------------------------------ 3
        dict(
            kicker="Chapter Three · The theorem itself",
            title="The Secret in the Squares",
            html="""
<p>Now for the thing with his name on it. Start with a <b>right triangle</b>: a triangle with one perfectly square corner, like the corner of this page. The two sides that make the square corner are the <b>legs</b>. The third side, the long slanting one across from the corner, is the <b>hypotenuse</b> (hy-POT-en-ooss), from Greek words meaning "stretched underneath."</p>
""" + _vocab() + """
<p>Here is the secret. Build a square on each of the three sides, like three square fields, each fenced along one edge of the triangle. Then, for every right triangle that ever was or ever will be:</p>
<div class="bigidea">📐 <b>The Pythagorean Theorem:</b> the square on one leg <b>plus</b> the square on the other leg <b>equals</b> the square on the hypotenuse. With legs <b>a</b> and <b>b</b> and hypotenuse <b>c</b>, that is: <b>a² + b² = c²</b>.</div>
<p>(The little raised 2 is read "squared." <b>a²</b> means a × a, the area of a square whose side is a. That is exactly why multiplying a number by itself is called <i>squaring</i> it.)</p>
<p>Try the most famous triangle of all, with legs 3 and 4. The squares on the legs hold 9 and 16 little unit squares. (Count them in the machine below.) Together that makes 25. And 25 is 5 × 5, so the hypotenuse is exactly <b>5</b>. Notice what just happened: nobody measured that slanting side. We <i>calculated</i> it from the other two. That is the whole power of the theorem: <b>know two sides of a right triangle, and the third can't hide from you.</b></p>
""" + MACHINE + """
<p>Drag the sliders for a while and you'll notice something. Most triangles give a messy hypotenuse. Legs 4 and 5 make a square of 41, and no whole number times itself is 41. Whole-number triangles like 3-4-5 are rare treasures. They have a name: <b>Pythagorean triples</b>. Hold on to the word "rare." It matters in the next chapter.</p>""",
            cps=[dict(
                type="num",
                kicker="Count the squares",
                q="""A right triangle has legs <b>3</b> and <b>4</b>. The squares on its legs have areas 3 × 3 = 9 and 4 × 4 = 16. What is the area of the square on its <b>hypotenuse</b>?""",
                answers=[25], unit="unit squares",
                hint="The theorem says: just add the two smaller squares. 9 + 16.",
            ), dict(
                type="num",
                kicker="Find the hidden side",
                q="""Now one on your own. The legs are <b>6</b> and <b>8</b>. How long is the hypotenuse? (Square each leg, add, then ask: what number times itself gives that?)""",
                answers=[10], unit="units",
                hint="6 × 6 = 36 and 8 × 8 = 64. Together, 100. What times itself is 100?",
            ), dict(
                type="num",
                kicker="A bigger treasure",
                q="""Set your theorem machine to legs <b>5</b> and <b>12</b>, or work it by hand. How long is the hypotenuse?""",
                answers=[13], unit="units",
                hint="25 + 144 = 169. Try 13 × 13.",
            )],
        ),
        # ------------------------------------------------------------------ 4
        dict(
            kicker="Chapter Four · Babylon, India, China · from 1800 BC",
            title="A Thousand Years Too Early",
            html="""
<p>After all that, here is a fact that may come as a shock: <b>Pythagoras did not discover the Pythagorean theorem.</b> He wasn't even close to first.</p>
<p>Around 1922 a New York publisher named George Plimpton bought a broken clay tablet, smaller than a postcard, from a dealer in antiquities. The price is said to have been about ten dollars. It had been written in what is now southern Iraq around <b>1800 BC</b>, in wedge-shaped <b>cuneiform</b> pressed into wet clay with a cut reed. Scholars call it <b>Plimpton 322</b>. When its numbers were finally worked out in 1945, the tablet turned out to be a table: fifteen rows, and every row belongs to a right triangle with whole-number sides. Not just baby ones like 3-4-5. One row gives <b>119, 120, 169</b>. Another gives <b>12,709, 13,500, 18,541</b>. You just learned how rare such triples are. Nobody stumbles on fifteen of them by luck. Whoever wrote that tablet knew the rule, and knew it cold.</p>
<p>A second tablet from about the same age, small and round, the kind a student held in one palm, shows a square with its diagonals scratched in, and along the diagonal a string of numbers. They give the diagonal's length correct to better than <b>one part in a million</b>. It looks very much like somebody's homework.</p>
<p>And Babylon was not alone. In India, the <i>Sulba Sutras</i> ("the rules of the cord") were handbooks for laying out altars with stretched ropes. The oldest goes under the name of <b>Baudhayana</b>, was composed perhaps between 800 and 500 BC, and says it plainly: the rope stretched along the diagonal of a rectangle makes an area equal to what the two sides make together. In China, an old book of astronomy and mathematics called the <i>Zhoubi Suanjing</i> works the 3-4-5 triangle as a conversation between a duke and a wise man. The Chinese names for the three sides are <b>gou</b>, <b>gu</b> and <b>xian</b>, meaning "hook," "thigh" and "bowstring," and Chinese students today learn the rule as the <b>gougu theorem</b>. Pythagoras's name isn't on it at all.</p>
<p>So why do <i>we</i> call it Pythagoras's? Because the Greeks who came after him gave him, or his school, the credit for something new. Not the rule. The <b>proof</b>. A Babylonian scribe had a recipe that worked every time anyone tried it. But "it has always worked" and "it cannot ever fail" are two different claims, and the space between them is the whole of mathematics. A proof is an argument so airtight that it covers every right triangle at once: the big ones, the skinny ones, the ones nobody has drawn yet.</p>
<p>And now the honest part. We have <b>no proof in Pythagoras's own hand</b>, and no writer from his own century says he made one. The story goes that when he found it, he sacrificed an ox to the gods. In some versions it was a hundred oxen. A man whose followers believed animals carried the souls of their friends? Even ancient writers raised an eyebrow at that. What we can say is this: by the time the Greeks wrote their mathematics down, the proof was there. The next four chapters will show you five of them.</p>
<div class="funfact">🪢 You may read that Egyptian builders made their square corners with a rope knotted into 12 equal parts, pulled tight into a 3-4-5 triangle. The trick really works, and carpenters still use it. But no Egyptian text or picture shows anyone doing it. A historian suggested the idea in the 1800s as a guess, and it has been repeated ever since until it sounds like a fact. It might even be true. It just isn't <i>known</i>.</div>
<div class="bigidea">🌟 <b>Big Idea #2:</b> A rule that has worked every time is <b>evidence</b>. A <b>proof</b> is a different kind of thing: it rules out the exception before anyone goes looking for it. Evidence says "so far." Proof says "always."</div>""",
            cps=[dict(
                type="num",
                kicker="How late was Pythagoras?",
                q="""Plimpton 322 was written about <b>1800 BC</b>. Pythagoras was born about <b>570 BC</b>. How many years <i>before his birth</i> was the tablet already sitting in Babylon?""",
                answers=[1230], unit="years",
                hint="Both dates are BC, so just subtract: 1800 − 570.",
            ), dict(
                type="num",
                kicker="Read a row of the tablet",
                q="""One row of Plimpton 322 belongs to a triangle with legs <b>45</b> and <b>60</b>. The scribe's squares would be 45 × 45 = <b>2,025</b> and 60 × 60 = <b>3,600</b>. How long is the hypotenuse the tablet records?""",
                answers=[75], unit="units",
                hint="2,025 + 3,600 = 5,625. Now hunt for the number that squares to 5,625: 70 × 70 is 4,900 and 80 × 80 is 6,400, and the answer must end in 5. (Divide all three sides by 15 and see which old friend appears.)",
            ), dict(
                type="mc",
                kicker="What was left to do?",
                q="""Babylonian scribes were using the rule more than a thousand years before the Greeks. So what did the Greeks add that was truly new?""",
                mc=[("Bigger and harder examples than the Babylonians had found", False),
                    ("A proof: an argument showing the rule can never fail, for any right triangle at all", True),
                    ("Nothing at all. They only put a Greek name on it", False)],
                good="Exactly, {name}. A million examples still leave room for example one-million-and-one to go wrong. A proof closes that door for good, which is why it was worth more than every row on the tablet.",
                bad="Think about what examples can and can't do, {name}. Fifteen triangles that obey the rule tell you about fifteen triangles. What kind of argument could tell you about all of them at once?",
            )],
        ),
        # ------------------------------------------------------------------ 5
        dict(
            kicker="Chapter Five · Proof One · older than its own history",
            title="The Sliding Triangles",
            html="""
<p>Here is the first proof, and many people think it is the most beautiful. Nobody knows who saw it first. Some historians guess that it is the kind of proof the early Pythagoreans would have used, scratched in sand; pictures like it turn up in China and India too. It needs no algebra and almost no words.</p>
<p>Cut out <b>four copies</b> of the same right triangle. Any right triangle will do; call its legs a and b. Make a square tray just big enough that one a and one b fit along each side. Now lay the four triangles in the four corners, each turned a quarter-turn from the last.</p>
<p>Look at the empty space in the middle. Every one of its four sides is a hypotenuse, so all four sides have length c. And its corners are true square corners. (Where two triangles meet on the tray's edge, three angles share one straight line: a sharp angle from each triangle, and the corner of the hole between them. A straight line is worth two square corners. The two sharp angles of a right triangle always add up to one. So the hole's corner gets the other.) So the hole is a <b>tilted square with side c</b>. Its area is <b>c²</b>.</p>
<p>Below are two copies of that tray. Press the button and watch the triangles in the right-hand one slide. The left-hand one stays put, so you can compare.</p>
""" + SLIDER_PROOF + """
<p>The triangles pair up into two rectangles, and the empty space becomes <b>two squares</b>: one with side a, one with side b. But <i>nothing was added and nothing was taken away</i>. It is the same tray. They are the same four triangles. So the empty space must be exactly as big as it was before:</p>
<div class="bigidea">📐 empty space before = empty space after, so &nbsp;<b>c² = a² + b²</b>. &nbsp;That's the whole proof.</div>
<p>Now drag the slider and change the triangle. Make it fat, thin, nearly flat, and slide them again. It works every time, and you can <i>see</i> that it has to.</p>""",
            cps=[dict(
                type="num",
                kicker="Check it with numbers",
                q="""Use the 3-4-5 triangle. The tray is 7 × 7, so its area is <b>49</b>. Each triangle has area 3 × 4 ÷ 2 = <b>6</b>, and there are four of them. How much empty space is left in the tray?""",
                answers=[25], unit="unit squares",
                hint="Four triangles cover 4 × 6 = 24. Take that from 49. (And notice: 25 is both 5 × 5 and 9 + 16.)",
            ), dict(
                type="mc",
                kicker="Why is this a proof, and not just another example?",
                q="""You checked the tray with a 3-4-5 triangle. Why does the sliding argument settle the question for <b>every</b> right triangle?""",
                mc=[("Because 3-4-5 is the most important triangle, so the others must follow it", False),
                    ("It doesn't. Each triangle would have to be checked separately", False),
                    ("Because nothing in it depends on the numbers: any four matching right triangles fit a tray a + b wide, and slide in exactly the same way", True)],
                good="That's the heart of it, {name}. The 3, the 4 and the 5 never did any work. They were only passengers. The argument runs on 'a' and 'b', whatever they happen to be, and that is what makes it a proof.",
                bad="Go back to the slider under the tray, {name}, and change the triangle. Did the argument ever need to know the lengths, or only that the four triangles were the same as each other?",
            )],
        ),
        # ------------------------------------------------------------------ 6
        dict(
            kicker="Chapter Six · Proof Two · China · written down by the 200s AD",
            title="The Bowstring Diagram",
            html="""
<p>The <i>Zhoubi Suanjing</i> is a Chinese book about two thousand years old, and some of the ideas in it are older still. In the <b>200s AD</b> a scholar named <b>Zhao Shuang</b> wrote notes to explain it, and in those notes he drew a picture: the <i>xian tu</i>, the <b>"bowstring diagram."</b> His notes even say what colours to paint it: the triangles <b>red</b>, the little square in the middle <b>yellow</b>.</p>
<p>This time, start with the big square, the one on the hypotenuse with side c, and fill it up. Four copies of the triangle fit inside like the blades of a pinwheel, each with its hypotenuse lying along one side of the square. They don't quite fill it. In the very middle a small square is left over, and its side is the <i>difference</i> between the two legs: b − a.</p>
""" + _xian_tu() + """
<p>For the 3-4-5 triangle, each red triangle has area 6, and the yellow square has side 4 − 3 = 1, so its area is 1. Add it all up: 6 + 6 + 6 + 6 + 1 = <b>25</b>. And 25 is exactly 9 + 16.</p>
<p>That worked for one triangle. To prove it works for <i>every</i> right triangle, do the same sum with letters instead of numbers. Call the short leg <b>a</b>, the long leg <b>b</b>, and the hypotenuse <b>c</b>.</p>
<div class="bigidea" style="line-height:1.9;">
<b>Step 1. The four red triangles.</b> Each one has area a × b ÷ 2. Four of them make 4 × (a × b ÷ 2) = <b>2ab</b>.<br>
<b>Step 2. The yellow square.</b> Its side is b − a, so its area is (b − a) × (b − a). Multiply each part of the first bracket by each part of the second:<br>
<span style="display:block; text-align:center;">b × b &nbsp;−&nbsp; b × a &nbsp;−&nbsp; a × b &nbsp;+&nbsp; a × a</span>
b × a and a × b are the same number, so the two of them together make 2ab:<br>
<span style="display:block; text-align:center;"><b>b² − 2ab + a²</b></span>
<b>Step 3. Add the pieces.</b> Red plus yellow:<br>
<span style="display:block; text-align:center;">2ab &nbsp;+&nbsp; b² − 2ab + a²</span>
The <b>+2ab</b> and the <b>−2ab</b> cancel each other out, and what is left is <b>a² + b²</b>.<br>
<b>Step 4. Compare.</b> The pieces fill the big square exactly, and the big square's area is <b>c²</b>. So:<br>
<span style="display:block; text-align:center; font-size:1.15rem;"><b>c² = a² + b²</b></span>
</div>
""" + BOWSTRING + """
<p>Put the two proofs side by side. In the last chapter the triangles sat <i>outside</i> the tilted square. Here they sit <i>inside</i> it. It is the same idea, seen from the other side of the world.</p>
<div class="funfact">📜 The same picture appears in India around AD 1150, in the work of the great mathematician Bhaskara. The story goes that he drew the figure and wrote beside it one single word of proof: <i>"Behold!"</i> It's a marvellous story, told in many books. But historians who have gone looking for that word in what Bhaskara actually wrote have come back without it. He explained his figure with a calculation, like everybody else.</div>""",
            cps=[dict(
                type="num",
                kicker="Fill a bigger square",
                q="""Try the bowstring diagram on the <b>5-12-13</b> triangle. Each triangle has area 5 × 12 ÷ 2 = <b>30</b>, and there are four. The little middle square has side 12 − 5 = 7, so its area is <b>49</b>. What is the area of the whole big square?""",
                answers=[169], unit="unit squares",
                hint="4 × 30 = 120, plus the 49 in the middle. (Then check: is your answer 13 × 13? Is it 25 + 144?)",
            )],
        ),
        # ------------------------------------------------------------------ 7
        dict(
            kicker="Chapter Seven · Proof Three · Alexandria · about 300 BC",
            title="Euclid's Windmill",
            html="""
<p>Around <b>300 BC</b>, in the new city of Alexandria in Egypt, a teacher named <b>Euclid</b> wrote the most successful textbook of all time. The <i>Elements</i> starts from a handful of statements so plain that nobody could doubt them, such as <i>you can draw a straight line between any two points</i>. Then it builds, step by locked step, each new result resting only on the ones before it. It was still being used in schoolrooms more than two thousand years later.</p>
<p>The first of its thirteen books climbs through forty-six propositions like a staircase. At the top stands <b>Proposition 47</b>: the theorem of Pythagoras. Generations of students gave its diagram nicknames: the <b>windmill</b>, the <b>bride's chair</b>, the <b>peacock's tail</b>.</p>
""" + _windmill() + """
<p>Euclid's idea is different from the sliding proofs, and cleverer. He drops a line from the square corner straight down through the big square, slicing it into <b>two rectangles</b>. Then, using triangles that he slides and turns without changing their area, he proves that the left rectangle is exactly as big as the square on the left leg, and the right rectangle exactly as big as the square on the right leg.</p>
<p>Here are his moves, played out. Euclid works with triangles that are exactly half of each shape below, but the moves are the same, and so is the reason they work: sliding a shape along its own line, or turning it, never changes how much space it covers.</p>
""" + SHEAR + """
<p>So the two small squares don't merely <i>add up</i> to the big one. Each has its own <b>place</b> inside it. Euclid shows you where the 9 goes, and where the 16 goes.</p>
<p>His very next proposition, number 48, runs the theorem backwards: if a triangle's sides obey a² + b² = c², then it <i>must</i> have a square corner. That is what makes the carpenter's knotted rope work. And there the first book ends.</p>
<div class="funfact">😲 Around 1629, an Englishman named Thomas Hobbes, forty years old and no mathematician, saw a copy of Euclid lying open in a library at Proposition 47. He read the claim and said out loud, with a swear word, <i>"This is impossible!"</i> So he read the proof. It sent him back to an earlier proposition, which sent him back to another, and another, all the way to the beginning, until he was convinced. His friend John Aubrey, who wrote the story down, says: "This made him in love with geometry."</div>""",
            cps=[dict(
                type="num",
                kicker="Where does the 9 go?",
                q="""In the windmill for the 3-4-5 triangle, the big square is 5 tall. Euclid's line cuts off a rectangle on the left that is <b>1.8</b> wide and <b>5</b> tall. What is its area, and which square does that match?""",
                answers=[9], unit="unit squares",
                hint="1.8 × 5. Think of it as 18 × 5 = 90, then put the decimal point back. (The other rectangle is 3.2 × 5 = 16. There are your two squares.)",
            )],
        ),
        # ------------------------------------------------------------------ 8
        dict(
            kicker="Chapter Eight · Proofs Four and Five · 1876 and about 1891",
            title="The Congressman and the Schoolboy",
            html="""
<p>You don't have to be a mathematician to prove the theorem. You have to be stubborn, and you have to like it.</p>
<p><b>James A. Garfield</b> had been a schoolteacher and the head of a small Ohio college before he became a general in the Civil War and then a congressman. In <b>1876</b>, passing the time with other members of Congress, he found a proof of his own. It was printed that April in the <i>New-England Journal of Education</i>. Five years later he was sworn in as the <b>twentieth President of the United States</b>. He is the only one, so far, to have published a proof of the Pythagorean theorem.</p>
<p>Garfield's trick is to stand two copies of the triangle on one straight line, toe to toe, and join their tops. The shape you get is a <b>trapezoid</b>, a four-sided figure with two parallel sides, and it is made of exactly three triangles: the two copies, and between them a big one with two sides of length c and a square corner. That middle triangle is <b>half of a square with side c</b>.</p>
""" + _garfield() + """
<p>Now measure the trapezoid two ways. As one whole shape, its area is the average of its two parallel sides, times the distance between them. As three pieces, its area is triangle + triangle + half of c². The two answers must agree, and out falls the theorem. You'll run the numbers yourself below.</p>
<p>The fifth proof belongs to a boy. In Munich, around <b>1891</b>, an engineer named Jakob Einstein told his nephew <b>Albert</b>, who was eleven or twelve, about the theorem of Pythagoras. Albert did not look the proof up. He decided to find one. Many years later he remembered: <i>"After much effort I succeeded in 'proving' this theorem on the basis of the similarity of triangles."</i></p>
<p><b>Similar</b> triangles are triangles with the same shape in different sizes: scale models of each other. We don't have the boy's notebook, so nobody can say exactly which steps he took. But here is a proof of just the kind he describes. Drop a line from the square corner straight to the hypotenuse:</p>
""" + _einstein() + """
<p>The triangle splits into two smaller ones, and both are <b>scale models of the whole</b>, with the same angles and the same shape. Look at their longest sides. The blue one's hypotenuse is the old leg <b>a</b>. The gold one's is the old leg <b>b</b>. The whole triangle's is <b>c</b>.</p>
<p>Now a fact about scale models: area grows as the <i>square</i> of the size. Double every length and the area is four times as big; triple them and it is nine times. So for triangles of this one shape, the area is always the same fixed fraction of the square on the hypotenuse. For the 3-4-5 shape that fraction happens to be 0.24: the whole triangle has area 0.24 × 25 = 6.</p>
<p>So the three areas are 0.24 × a², 0.24 × b² and 0.24 × c². But the two small triangles <i>are</i> the big one, cut in two. Their areas add up to its area. Divide away the 0.24, and what is left says a² + b² = c². No squares were drawn at all.</p>
<div class="bigidea">🌟 <b>Big Idea #3:</b> Nobody asked Garfield for a proof, and the theorem had been settled for two thousand years when Einstein's uncle mentioned it. They proved it anyway, because being told something is true and <i>seeing for yourself why</i> are not the same experience.</div>""",
            cps=[dict(
                type="num",
                kicker="Garfield's trapezoid, measured whole",
                q="""For the 3-4-5 triangle, the trapezoid's two parallel sides are <b>3</b> and <b>4</b> long, and they stand <b>7</b> apart. Area of a trapezoid = (average of the parallel sides) × (distance between them). What is the area?""",
                answers=[24.5], unit="unit squares",
                hint="The average of 3 and 4 is 3.5. Then 3.5 × 7.",
            ), dict(
                type="num",
                kicker="Garfield's trapezoid, measured in pieces",
                q="""The whole trapezoid is 24.5. Take away the two triangles, which have area <b>6</b> each. What remains is <b>half</b> of the square on the hypotenuse. So what is the area of the <i>whole</i> square on the hypotenuse?""",
                answers=[25], unit="unit squares",
                hint="24.5 − 6 − 6 = 12.5. That is half of c². Double it.",
            ), dict(
                type="num",
                kicker="The schoolboy's proof, checked",
                q="""In the 3-4-5 shape, a triangle's area is always <b>0.24</b> × the square on its hypotenuse. The small blue triangle has area 0.24 × 9 = <b>2.16</b>. The gold one has area 0.24 × 16 = <b>3.84</b>. Add them. What do you get?""",
                answers=[6], unit="unit squares",
                hint="2.16 + 3.84. (And the whole 3-4-5 triangle's area is 3 × 4 ÷ 2. The pieces make the whole. That was the entire proof.)",
            )],
        ),
        # ------------------------------------------------------------------ 9
        dict(
            kicker="Chapter Nine · Southern Italy · the 400s BC",
            title="The Number That Would Not Behave",
            html="""
<p>Remember the creed: <i>All is number.</i> By "number" the Pythagoreans meant whole numbers (1, 2, 3) and the ratios between them, like 3/2 or 17/12. Every length in the world, they believed, could be written as one of those. And then their own theorem turned on them.</p>
<p>Take the simplest right triangle there is: both legs exactly <b>1</b>. It is half of a square, cut corner to corner.</p>
""" + _unit_square() + """
<p>The theorem says c² = 1 + 1 = <b>2</b>. So the diagonal is whatever number, multiplied by itself, makes 2. We call it <b>the square root of 2</b> and write it <b>√2</b>. Fine. Which fraction is it?</p>
<p>Try 7/5, which is 1.4. Squared, it falls a little short of 2. Try 17/12: squared, it lands a hair the other side. Try 41/29, try 99/70: closer, and closer, and never there. Look at how they miss. For a fraction to equal √2, the top number squared would have to be <i>exactly double</i> the bottom number squared:</p>
<p style="text-align:center; line-height:1.9;">7 × 7 = <b>49</b> &nbsp;but&nbsp; 2 × 5 × 5 = <b>50</b><br>
17 × 17 = <b>?</b> &nbsp;but&nbsp; 2 × 12 × 12 = <b>288</b> &nbsp;<i>(that one is yours, below)</i><br>
41 × 41 = <b>1,681</b> &nbsp;but&nbsp; 2 × 29 × 29 = <b>1,682</b><br>
99 × 99 = <b>9,801</b> &nbsp;but&nbsp; 2 × 70 × 70 = <b>9,800</b></p>
<p>Off by one. Every time. The Greeks went further and found a <b>proof</b> that no fraction will ever hit it, not even with numbers a mile long. The diagonal of a square is a perfectly real length; you can draw it in two seconds. But it cannot be written as a ratio of whole numbers. Such numbers are called <b>irrational</b>, which means "without a ratio." Written as a decimal, √2 begins 1.41421356… and runs on forever without ever settling into a repeating pattern.</p>
<p>The story goes that the man who let this secret out was a Pythagorean named <b>Hippasus</b>, and that he was drowned at sea for it, thrown overboard by the brotherhood, or punished by the gods, depending on who is telling it. The tellers lived centuries afterwards, and they do not even agree about what his crime was. So: a legend. But somebody did make the discovery, and it must have landed like a thunderclap. The creed said all is number. The theorem said: <i>not this.</i></p>
<div class="funfact">🧱 The Babylonian student's round tablet gives the diagonal as 1, then 24 sixtieths, then 51 parts of 3,600, then 10 parts of 216,000. The Babylonians counted in sixties, which is why your hour still has 60 minutes. Add the pieces and you get 1.41421296. The true value starts 1.41421356. Not bad for wet clay and a reed.</div>
<div class="bigidea">🌟 <b>Big Idea #4:</b> The Pythagoreans' own best theorem broke the Pythagoreans' favourite belief. They could keep the belief or keep the proof, but not both. Mathematics kept the proof. When a good argument and a cherished idea collide, that is always the right way round.</div>""",
            cps=[dict(
                type="num",
                kicker="A near miss",
                q="""Try <b>1.4</b> as a guess for the diagonal. What is 1.4 × 1.4? (If the guess were perfect, you would get exactly 2.)""",
                answers=[1.96], unit="",
                hint="14 × 14 = 196. Now put the decimal point back: two decimal places.",
            ), dict(
                type="num",
                kicker="Off by one",
                q="""Now try the fraction <b>17/12</b>. For it to equal √2, 17 × 17 would have to equal 2 × 12 × 12, which is <b>288</b>. What is 17 × 17 really?""",
                answers=[289], unit="",
                hint="17 × 17 = 17 × 10 + 17 × 7 = 170 + 119. So close to 288, and that gap of one never closes, no matter how big the numbers get.",
            )],
        ),
        # ----------------------------------------------------------------- 10
        dict(
            kicker="Chapter Ten · Everywhere · today",
            title="Put It to Work",
            html="""
<p>A theorem proved is a tool earned. This one may be the most-used tool in all of mathematics. Carpenters square the corners of a house with a 3-4-5 triangle. A phone finding its position, a video game deciding whether the arrow hit the dragon, a telescope working out how far apart two stars sit on a photograph: deep inside, each of them is squaring two numbers, adding, and taking a square root.</p>
<p>The recipe never changes:</p>
<div class="bigidea">🧭 <b>1.</b> Find the right triangle, and its square corner. &nbsp;<b>2.</b> The side <i>across from</i> the square corner is the hypotenuse, c. &nbsp;<b>3.</b> Looking for the hypotenuse? <b>Add</b> the squares of the legs. Looking for a leg? <b>Subtract</b>: c² − a² = b². &nbsp;<b>4.</b> Take the square root.</div>
<p>Four jobs are waiting below. For the last three you may use a calculator's <b>√</b> key. The Babylonian scribes kept tables of squares beside them for exactly the same purpose, and nobody called it cheating.</p>""",
            cps=[dict(
                type="num",
                kicker="Job one · the fire ladder",
                q="""A fire crew's ladder is <b>25 m</b> long. Its foot stands <b>7 m</b> out from the wall. How high up the wall does the top reach? (Careful: the ladder is the <i>hypotenuse</i>. You are hunting for a leg.)""",
                figure=_ladder(),
                answers=[24], unit="m",
                hint="25 × 25 = 625 and 7 × 7 = 49. Subtract this time: 625 − 49 = 576. Now, what times itself is 576? (Try 24.)",
            ), dict(
                type="num",
                kicker="Job two · the catcher's throw",
                q="""A baseball diamond is a square with bases <b>90 feet</b> apart. A runner is stealing second, and the catcher throws from home plate straight across the diamond. How long is the throw, to the nearest foot?""",
                figure=_diamond(),
                answers=[127, 127.3, 127.28, 127.279], unit="feet",
                hint="Home, first and second make a right triangle with both legs 90. 90 × 90 = 8,100, twice: 16,200. Press √ on 16,200. (The official rule book says 127 feet 3⅜ inches. It got there the same way.)",
            ), dict(
                type="num",
                kicker="Job three · the distance between two stars",
                q="""On a star chart, one star is plotted at <b>(−2, 1)</b> and another at <b>(4, 9)</b>. How far apart are they on the chart, in grid units? (Walk across, then up: those are your two legs.)""",
                figure=_stargrid(),
                answers=[10], unit="grid units",
                hint="Across: from −2 to 4 is 6 steps. Up: from 1 to 9 is 8 steps. Legs 6 and 8: you have met this triangle before.",
            ), dict(
                type="num",
                kicker="Job four · the view from orbit",
                q="""The Earth's radius is about <b>6,371 km</b>. The International Space Station flies about 400 km up, so it is <b>6,771 km</b> from the Earth's centre. An astronaut's line of sight just grazes the Earth at the horizon, and there it meets the Earth's radius at a <b>square corner</b>. How far away is the astronaut's horizon, to the nearest kilometer?""",
                figure=_horizon(),
                answers=[2293, 2292.8, 2292.77, 2292], unit="km",
                hint="The long side, 6,771, is the hypotenuse. 6,771² = 45,846,441 and 6,371² = 40,589,641. Subtract: 5,256,800. Then press √.",
            )],
        ),
    ],
    quiz=dict(
        title="&#10022; Ten Triangles &#10022;",
        intro="Ten more jobs for your new tool, plus a little history. One attempt per question, because a proof doesn't get a second guess either. Pencil, paper and the √ key are all allowed.",
        verdicts=[
            dict(min=10, title="{score}: Q.E.D.", text="Flawless, {name}. Euclid would nod, Garfield would shake your hand, and the brotherhood would probably swear you to secrecy. Go and find a right triangle in the room you are sitting in."),
            dict(min=7, title="{score}: Past the curtain", text="Strong work, {name}. Read the explanations under the ones that got away. Most of them turn on one question: which side is the hypotenuse?"),
            dict(min=4, title="{score}: Still in the listening years", text="You have the idea, {name}, and the rest is practice. Wipe the slate, keep the recipe from Chapter Ten beside you, and draw the triangle before you calculate anything."),
            dict(min=0, title="{score}: Back to the theorem machine", text="Every one of these can be learned, {name}. Go back to Chapter Three, play with the sliders until the squares feel obvious, then wipe the slate and try again. Einstein said his proof took 'much effort' too."),
        ],
        questions=[
            dict(type="num", kicker="Find the hypotenuse",
                 q="""A right triangle has legs <b>9</b> and <b>12</b>. How long is its hypotenuse?""",
                 answers=[15], unit="units",
                 why="81 + 144 = 225, and 15 &times; 15 = 225. It is the 3-4-5 triangle again, three times bigger."),
            dict(type="num", kicker="Find a leg",
                 q="""A right triangle has hypotenuse <b>10</b> and one leg <b>6</b>. How long is the other leg?""",
                 answers=[8], unit="units",
                 why="Hunting for a leg, you subtract: 100 &minus; 36 = 64, and 8 &times; 8 = 64."),
            dict(type="mc", kicker="Euclid's Proposition 48",
                 q="""A carpenter measures a triangular frame: its sides are <b>5</b>, <b>6</b> and <b>8</b>. Does it have a square corner?""",
                 mc=[("Yes: every triangle obeys the theorem", False),
                     ("No: 25 + 36 = 61, but 8 &times; 8 = 64", True),
                     ("Yes: 5 + 6 is bigger than 8", False)],
                 why="Only right triangles obey a&#178; + b&#178; = c&#178;, and only triangles that obey it are right. 61 is not 64, so the corner is not square. (It is a little wider than square.)"),
            dict(type="num", kicker="The shortcut",
                 q="""A rectangular field is <b>30 m</b> by <b>40 m</b>. Instead of walking along two sides, you cut straight across the diagonal. How many meters of walking do you save?""",
                 answers=[20], unit="m",
                 why="The diagonal is 50 m (900 + 1,600 = 2,500). Around the edge is 30 + 40 = 70 m. You save 20."),
            dict(type="num", kicker="The ship",
                 q="""A ship sails <b>9 km</b> due east and then <b>40 km</b> due north. How far is it from the harbour, in a straight line?""",
                 answers=[41], unit="km",
                 why="81 + 1,600 = 1,681, and 41 &times; 41 = 1,681. East and north meet at a square corner, so the theorem applies."),
            dict(type="num", kicker="The screen",
                 q="""Television screens are sold by their <b>diagonal</b>. A screen is <b>48 inches</b> wide and <b>27 inches</b> tall. What size will the box say, to the nearest inch?""",
                 answers=[55, 55.1, 55.07], unit="inches",
                 why="2,304 + 729 = 3,033, and the square root of 3,033 is about 55.07. It's a 55-inch television."),
            dict(type="num", kicker="The number that would not behave",
                 q="""A square has sides exactly <b>1</b> long. You build a new square on its diagonal. What is the <i>area</i> of the new square?""",
                 answers=[2], unit="unit squares",
                 why="c&#178; = 1 + 1 = 2. The area is a perfectly tidy 2. It is only the <i>side</i>, &radic;2, that no fraction can ever equal."),
            dict(type="mc", kicker="Chapter Four &middot; who knew it first?",
                 q="""Which of these is the <b>oldest</b> evidence that people knew the rule?""",
                 mc=[("Euclid's <i>Elements</i>", False),
                     ("The clay tablet Plimpton 322, from Babylon", True),
                     ("A book written by Pythagoras", False)],
                 why="Plimpton 322 dates from about 1800 BC. Euclid wrote about 300 BC. And not one line written by Pythagoras himself survives."),
            dict(type="mc", kicker="Chapter Two &middot; test the story",
                 q="""The story of Pythagoras and the blacksmith's hammers was copied from book to book for over a thousand years. What was wrong with it?""",
                 mc=[("Blacksmiths hadn't been invented yet", False),
                     ("Nothing: it has been checked, and it is true", False),
                     ("It is false, and anyone with two hammers could have found that out by trying", True)],
                 why="A hammer twice as heavy does not ring an octave lower. The string lengths are true; the hammers are a legend that nobody tested. Being repeated is not the same as being right."),
            dict(type="mc", kicker="Chapter Eight &middot; the proofs",
                 q="""A future President of the United States proved the theorem in 1876. What shape did he build his proof on?""",
                 mc=[("A circle", False),
                     ("A trapezoid made of three triangles", True),
                     ("A triangle of ten dots", False)],
                 why="James A. Garfield measured one trapezoid two ways, whole and in three pieces, and the theorem fell out. The ten dots are the tetractys."),
        ],
    ),
)
