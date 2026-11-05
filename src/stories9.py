# -*- coding: utf-8 -*-
"""Story data: Descartes. Doubt, the Cogito, the fly on the ceiling and the coordinate plane."""

INK = "#22304f"
BLUE, GOLD, RED = "#3a5da8", "#8a6400", "#b03030"


# ---------------------------------------------------------------------------
# Small static coordinate-plane figure for checkpoints
# ---------------------------------------------------------------------------
def _plane(xmin, xmax, ymin, ymax, s, pts=(), segs=(), dashes=(), label="coordinate grid"):
    """pts: (x, y, label, colour, dx, dy). segs / dashes: (x1, y1, x2, y2, colour)."""
    pad = 22
    w = (xmax - xmin) * s + 2 * pad
    h = (ymax - ymin) * s + 2 * pad

    def X(x):
        return pad + (x - xmin) * s

    def Y(y):
        return pad + (ymax - y) * s

    o = ['<svg width="%d" height="%d" viewBox="0 0 %d %d" font-family="Georgia,serif" '
         'style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%%; '
         'height:auto; display:block; margin:10px auto;" role="img" aria-label="%s">' % (w, h, w, h, label)]
    for gx in range(xmin, xmax + 1):
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#e6d9b8" stroke-width="1"/>'
                 % (X(gx), Y(ymin), X(gx), Y(ymax)))
    for gy in range(ymin, ymax + 1):
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#e6d9b8" stroke-width="1"/>'
                 % (X(xmin), Y(gy), X(xmax), Y(gy)))
    ax0, ay0 = max(xmin, min(xmax, 0)), max(ymin, min(ymax, 0))
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'
             % (X(xmin), Y(ay0), X(xmax), Y(ay0), INK))
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'
             % (X(ax0), Y(ymin), X(ax0), Y(ymax), INK))
    for gx in range(xmin, xmax + 1):
        if gx != 0 and (gx % 2 == 0 or xmax - xmin <= 8):
            o.append('<text x="%.1f" y="%.1f" font-size="11" fill="#4a5878" text-anchor="middle">%d</text>'
                     % (X(gx), Y(ay0) + 14, gx))
    for gy in range(ymin, ymax + 1):
        if gy != 0 and (gy % 2 == 0 or ymax - ymin <= 8):
            o.append('<text x="%.1f" y="%.1f" font-size="11" fill="#4a5878" text-anchor="end">%d</text>'
                     % (X(ax0) - 5, Y(gy) + 4, gy))
    for x1, y1, x2, y2, col in dashes:
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2" '
                 'stroke-dasharray="5 4"/>' % (X(x1), Y(y1), X(x2), Y(y2), col))
    for x1, y1, x2, y2, col in segs:
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3.5" '
                 'stroke-linecap="round"/>' % (X(x1), Y(y1), X(x2), Y(y2), col))
    for x, y, lab, col, dx, dy in pts:
        o.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (X(x), Y(y), col))
        if lab:
            o.append('<text x="%.1f" y="%.1f" font-size="14" font-weight="bold" fill="%s" '
                     'stroke="#fffdf4" stroke-width="4" paint-order="stroke">%s</text>'
                     % (X(x) + dx, Y(y) + dy, col, lab))
    o.append('</svg>')
    return "".join(o)


def _cp_walk():
    return _plane(0, 6, 0, 4, 44,
                  pts=[(1, 2, "A", BLUE, -16, -10), (4, 2, "B", RED, 8, -10)],
                  segs=[(1, 2, 4, 2, RED)],
                  label="A fly at address (1, 2) crawls along a straight row to address (4, 2)")


def _cp_diag():
    return _plane(0, 6, 0, 6, 40,
                  pts=[(1, 1, "A", BLUE, -16, 16), (4, 5, "B", RED, 8, -8)],
                  segs=[(1, 1, 4, 5, RED)],
                  dashes=[(1, 1, 4, 1, GOLD), (4, 1, 4, 5, GOLD)],
                  label="A fly crawls straight from address (1, 1) to address (4, 5)")


def _cp_origin():
    return _plane(-8, 2, 0, 9, 32,
                  pts=[(-6, 8, "P", RED, -22, -8), (0, 0, "O", BLUE, 8, 16)],
                  segs=[(0, 0, -6, 8, RED)],
                  dashes=[(-6, 0, -6, 8, GOLD), (-6, 0, 0, 0, GOLD)],
                  label="A point P at address (-6, 8), with a straight line back to the origin O")


# ---------------------------------------------------------------------------
# Live widgets
# ---------------------------------------------------------------------------
_BOX = 'background:#fdf9ee; border:1.5px solid #c9b57e; border-radius:12px; padding:14px 16px; margin:14px 0;'
_CAP = ('text-align:center; font-size:.8rem; letter-spacing:2px; text-transform:uppercase; '
        'color:#8a6400; font-weight:bold; margin-bottom:8px;')
_BTN = ('font-family:Georgia,serif; cursor:pointer; background:#fff8e6; border:1.5px solid #c9b57e; '
        'border-radius:8px; padding:7px 12px; font-size:.85rem; color:#5a4a1a;')

FLY = ('<div style="%s">\n  <div style="%s">The ceiling corner &middot; click to move the fly</div>' % (_BOX, _CAP)) + r"""
  <div style="text-align:center;">
    <svg id="fl-svg" width="400" height="330" viewBox="0 0 400 330" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto; cursor:crosshair; touch-action:manipulation;" role="img" aria-label="A ceiling seen from below, with a grid measured from one corner and a fly sitting on one grid point"></svg>
  </div>
  <div id="fl-out" style="text-align:center; font-size:1.02rem; color:#3d3320; margin:8px 0 8px; line-height:1.6; min-height:3.2em;"></div>
  <div style="max-width:420px; margin:0 auto; display:grid; grid-template-columns:auto 1fr; gap:6px 10px; align-items:center; font-size:.9rem; color:#3d3320;">
    <label for="fl-x">across (x)</label><input id="fl-x" type="range" min="0" max="6" step="1" value="4" style="width:100%;">
    <label for="fl-y">along (y)</label><input id="fl-y" type="range" min="0" max="5" step="1" value="2" style="width:100%;">
  </div>
  <div style="text-align:center; margin-top:10px;"><button type="button" id="fl-clear" style="@@BTN@@">Clear the trail</button></div>
</div>
<script>
(function(){
  var svg = document.getElementById('fl-svg');
  if (!svg) return;
  var NS = 'http://www.w3.org/2000/svg', S = 52, OX = 44, OY = 290, NX = 6, NY = 5;
  var sx = document.getElementById('fl-x'), sy = document.getElementById('fl-y');
  var trail = [[4, 2]];
  function el(tag, attrs, text){
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    svg.appendChild(e); return e;
  }
  function X(x){ return OX + x * S; }
  function Y(y){ return OY - y * S; }
  function draw(){
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    el('rect', {x: X(0), y: Y(NY), width: NX * S, height: NY * S, fill: '#f6efdc', stroke: '#22304f', 'stroke-width': 3});
    for (var i = 0; i <= NX; i++) el('line', {x1: X(i), y1: Y(0), x2: X(i), y2: Y(NY), stroke: '#d9c9a3', 'stroke-width': 1});
    for (var j = 0; j <= NY; j++) el('line', {x1: X(0), y1: Y(j), x2: X(NX), y2: Y(j), stroke: '#d9c9a3', 'stroke-width': 1});
    for (i = 0; i <= NX; i++) el('text', {x: X(i), y: Y(0) + 18, 'text-anchor': 'middle', 'font-size': 12, fill: '#4a5878'}, i);
    for (j = 1; j <= NY; j++) el('text', {x: X(0) - 9, y: Y(j) + 4, 'text-anchor': 'end', 'font-size': 12, fill: '#4a5878'}, j);
    el('text', {x: X(0) - 9, y: Y(0) + 18, 'text-anchor': 'end', 'font-size': 12, fill: '#b03030', 'font-weight': 'bold'}, '0');
    el('text', {x: X(NX / 2), y: 322, 'text-anchor': 'middle', 'font-size': 12, fill: '#8a6400'}, 'steps along the long wall from the corner');
    el('text', {x: 12, y: Y(NY / 2), 'text-anchor': 'middle', 'font-size': 12, fill: '#8a6400', transform: 'rotate(-90 12 ' + Y(NY / 2) + ')'}, 'steps along the short wall');
    el('circle', {cx: X(0), cy: Y(0), r: 6, fill: '#b03030'});
    el('text', {x: X(0) + 10, y: Y(0) - 8, 'font-size': 12, fill: '#b03030', 'font-weight': 'bold'}, 'corner');
    if (trail.length > 1){
      var pts = trail.map(function(p){ return X(p[0]) + ',' + Y(p[1]); }).join(' ');
      el('polyline', {points: pts, fill: 'none', stroke: '#3a5da8', 'stroke-width': 2.5, 'stroke-dasharray': '6 4', 'stroke-linejoin': 'round'});
      trail.forEach(function(p){ el('circle', {cx: X(p[0]), cy: Y(p[1]), r: 3.5, fill: '#3a5da8'}); });
    }
    var cur = trail[trail.length - 1], fx = X(cur[0]), fy = Y(cur[1]);
    el('line', {x1: fx, y1: fy, x2: fx, y2: Y(0), stroke: '#e8a90c', 'stroke-width': 2.5, 'stroke-dasharray': '5 4'});
    el('line', {x1: fx, y1: fy, x2: X(0), y2: fy, stroke: '#e8a90c', 'stroke-width': 2.5, 'stroke-dasharray': '5 4'});
    var g = el('g', {transform: 'translate(' + fx + ',' + fy + ')'});
    var parts = [['ellipse', {cx: -7, cy: -6, rx: 8, ry: 4, fill: 'rgba(120,160,220,.55)', stroke: '#3a5da8', 'stroke-width': 1, transform: 'rotate(-30 -7 -6)'}],
                 ['ellipse', {cx: 7, cy: -6, rx: 8, ry: 4, fill: 'rgba(120,160,220,.55)', stroke: '#3a5da8', 'stroke-width': 1, transform: 'rotate(30 7 -6)'}],
                 ['ellipse', {cx: 0, cy: 0, rx: 5, ry: 8, fill: '#22304f'}],
                 ['circle', {cx: 0, cy: -9, r: 4, fill: '#22304f'}]];
    parts.forEach(function(p){
      var e = document.createElementNS(NS, p[0]);
      for (var k in p[1]) e.setAttribute(k, p[1][k]);
      g.appendChild(e);
    });
    sx.value = cur[0]; sy.value = cur[1];
    document.getElementById('fl-out').innerHTML =
      'The fly is <b>' + cur[0] + '</b> steps across and <b>' + cur[1] + '</b> steps along.<br>' +
      'Its address: <span style="font-size:1.25rem; color:#b03030;"><b>(' + cur[0] + ', ' + cur[1] + ')</b></span>';
  }
  function put(x, y){
    x = Math.max(0, Math.min(NX, x)); y = Math.max(0, Math.min(NY, y));
    var last = trail[trail.length - 1];
    if (last[0] === x && last[1] === y) return;
    trail.push([x, y]);
    if (trail.length > 12) trail.shift();
    draw();
  }
  svg.addEventListener('click', function(ev){
    var r = svg.getBoundingClientRect(), k = 400 / r.width;
    put(Math.round(((ev.clientX - r.left) * k - OX) / S), Math.round((OY - (ev.clientY - r.top) * k) / S));
  });
  sx.addEventListener('input', function(){ put(Number(sx.value), trail[trail.length - 1][1]); });
  sy.addEventListener('input', function(){ put(trail[trail.length - 1][0], Number(sy.value)); });
  document.getElementById('fl-clear').addEventListener('click', function(){ trail = [trail[trail.length - 1]]; draw(); });
  draw();
})();
</script>""".replace("@@BTN@@", _BTN)

GRAPH = ('<div style="%s">\n  <div style="%s">The plane &middot; an equation draws a picture</div>' % (_BOX, _CAP)) + r"""
  <div style="text-align:center; margin-bottom:8px;">
    <button type="button" id="gr-line" style="@@BTN@@ background:#e8a90c; font-weight:bold;">Line: y = mx + b</button>
    <button type="button" id="gr-circ" style="@@BTN@@">Circle: x&#178; + y&#178; = r&#178;</button>
  </div>
  <div style="text-align:center;">
    <svg id="gr-svg" width="400" height="400" viewBox="0 0 400 400" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;" role="img" aria-label="A coordinate plane with four quadrants showing the graph of the chosen equation"></svg>
  </div>
  <div id="gr-out" style="text-align:center; font-size:1rem; color:#3d3320; margin:8px 0 10px; line-height:1.6; min-height:4.8em;"></div>
  <div id="gr-lc" style="max-width:420px; margin:0 auto; display:grid; grid-template-columns:auto 1fr; gap:6px 10px; align-items:center; font-size:.9rem; color:#3d3320;">
    <label for="gr-m">m (steepness)</label><input id="gr-m" type="range" min="-3" max="3" step="1" value="1" style="width:100%;">
    <label for="gr-b">b (start height)</label><input id="gr-b" type="range" min="-4" max="4" step="1" value="1" style="width:100%;">
  </div>
  <div id="gr-cc" style="max-width:420px; margin:0 auto; display:none; grid-template-columns:auto 1fr; gap:6px 10px; align-items:center; font-size:.9rem; color:#3d3320;">
    <label for="gr-r">r (radius)</label><input id="gr-r" type="range" min="1" max="6" step="1" value="5" style="width:100%;">
  </div>
</div>
<script>
(function(){
  var svg = document.getElementById('gr-svg');
  if (!svg) return;
  var NS = 'http://www.w3.org/2000/svg', S = 30, C = 200, R = 6, mode = 'line';
  var sm = document.getElementById('gr-m'), sb = document.getElementById('gr-b'), sr = document.getElementById('gr-r');
  function el(tag, attrs, text){
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    svg.appendChild(e); return e;
  }
  function X(x){ return C + x * S; }
  function Y(y){ return C - y * S; }
  function sign(n){ return n < 0 ? '−' + Math.abs(n) : String(n); }
  function draw(){
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    for (var i = -R; i <= R; i++){
      el('line', {x1: X(i), y1: Y(-R), x2: X(i), y2: Y(R), stroke: '#e6d9b8', 'stroke-width': 1});
      el('line', {x1: X(-R), y1: Y(i), x2: X(R), y2: Y(i), stroke: '#e6d9b8', 'stroke-width': 1});
    }
    el('line', {x1: X(-R), y1: Y(0), x2: X(R), y2: Y(0), stroke: '#22304f', 'stroke-width': 2});
    el('line', {x1: X(0), y1: Y(-R), x2: X(0), y2: Y(R), stroke: '#22304f', 'stroke-width': 2});
    for (i = -R; i <= R; i++){
      if (i === 0 || i % 2 !== 0) continue;
      el('text', {x: X(i), y: Y(0) + 14, 'text-anchor': 'middle', 'font-size': 11, fill: '#4a5878'}, sign(i));
      el('text', {x: X(0) - 5, y: Y(i) + 4, 'text-anchor': 'end', 'font-size': 11, fill: '#4a5878'}, sign(i));
    }
    el('text', {x: X(R) - 4, y: Y(0) - 6, 'text-anchor': 'end', 'font-size': 13, fill: '#22304f', 'font-style': 'italic'}, 'x');
    el('text', {x: X(0) + 8, y: Y(R) + 12, 'font-size': 13, fill: '#22304f', 'font-style': 'italic'}, 'y');
    var lab = [['x>0, y>0', 3, 5.3], ['x<0, y>0', -3, 5.3], ['x<0, y<0', -3, -5.6], ['x>0, y<0', 3, -5.6]];
    lab.forEach(function(q){ el('text', {x: X(q[1]), y: Y(q[2]), 'text-anchor': 'middle', 'font-size': 10, fill: '#a99a70'}, q[0]); });
    var out = '', pts = [];
    if (mode === 'line'){
      var m = Number(sm.value), b = Number(sb.value);
      el('line', {x1: X(-R), y1: Y(m * -R + b), x2: X(R), y2: Y(m * R + b), stroke: '#b03030', 'stroke-width': 3.5, 'stroke-linecap': 'round'});
      for (var x = -R; x <= R; x++){ var y = m * x + b; if (Math.abs(y) <= R) pts.push([x, y]); }
      var eq = 'y = ' + (m === 0 ? '' : (m === 1 ? 'x' : m === -1 ? '−x' : sign(m) + 'x')) +
               (m === 0 ? sign(b) : (b === 0 ? '' : (b < 0 ? ' − ' + Math.abs(b) : ' + ' + b)));
      var rows = [-2, -1, 0, 1, 2].map(function(x){ return 'x=' + sign(x) + ' &rarr; y=' + sign(m * x + b); }).join(' &nbsp;&middot;&nbsp; ');
      out = '<b style="font-size:1.15rem; color:#b03030;">' + eq + '</b><br>' + rows;
    } else {
      var r = Number(sr.value);
      el('circle', {cx: X(0), cy: Y(0), r: r * S, fill: 'rgba(232,169,12,.10)', stroke: '#b03030', 'stroke-width': 3.5});
      for (var a = -r; a <= r; a++) for (var c = -r; c <= r; c++) if (a * a + c * c === r * r) pts.push([a, c]);
      var shown = pts.filter(function(p){ return p[0] > 0 && p[1] >= 0; }).map(function(p){ return '(' + p[0] + ', ' + p[1] + ')'; }).join(' ');
      out = '<b style="font-size:1.15rem; color:#b03030;">x&#178; + y&#178; = ' + (r * r) + '</b><br>Whole-number points on the first quarter: ' + shown +
            '<br>Check one: ' + (function(){ var p = pts.filter(function(p){ return p[0] > 0 && p[1] > 0; })[0]; return p ? p[0] + '&#178; + ' + p[1] + '&#178; = ' + (p[0]*p[0]) + ' + ' + (p[1]*p[1]) + ' = ' + (r*r) : 'no corner-cutting points, only the four axis points'; })();
    }
    pts.forEach(function(p){ el('circle', {cx: X(p[0]), cy: Y(p[1]), r: 4.5, fill: '#3a5da8', stroke: '#fffdf4', 'stroke-width': 1.5}); });
    document.getElementById('gr-out').innerHTML = out;
  }
  function setMode(mm){
    mode = mm;
    document.getElementById('gr-lc').style.display = mm === 'line' ? 'grid' : 'none';
    document.getElementById('gr-cc').style.display = mm === 'line' ? 'none' : 'grid';
    document.getElementById('gr-line').style.background = mm === 'line' ? '#e8a90c' : '#fff8e6';
    document.getElementById('gr-circ').style.background = mm === 'line' ? '#fff8e6' : '#e8a90c';
    draw();
  }
  document.getElementById('gr-line').addEventListener('click', function(){ setMode('line'); });
  document.getElementById('gr-circ').addEventListener('click', function(){ setMode('circ'); });
  [sm, sb, sr].forEach(function(s){ s.addEventListener('input', draw); });
  draw();
})();
</script>""".replace("@@BTN@@", _BTN)

QUOTES = ('<div style="%s">\n  <div style="%s">Lines he is remembered for</div>' % (_BOX, _CAP)) + """
  <ol style="margin:0 0 0 1.2em; padding:0; line-height:1.6; font-size:.98rem; color:#3d3320;">
    <li style="margin-bottom:9px;"><b>&ldquo;I think, therefore I am.&rdquo;</b> (<i>Je pense, donc je suis</i>, Discourse on Method, 1637; <i>Cogito, ergo sum</i>, Principles of Philosophy, 1644.) The one fact the demon cannot take away.</li>
    <li style="margin-bottom:9px;"><b>&ldquo;It is not enough to have a good mind; the main thing is to use it well.&rdquo;</b> (Discourse, Part 1.) Brains are not the scarce thing. Method is.</li>
    <li style="margin-bottom:9px;"><b>&ldquo;Divide each of the difficulties under examination into as many parts as possible.&rdquo;</b> (Discourse, Part 2.) His second rule of method, and the engine of all later science.</li>
    <li style="margin-bottom:9px;"><b>&ldquo;It is necessary, once in the course of our life, to doubt, as far as possible, all things.&rdquo;</b> (Principles of Philosophy, Part 1, 1644.) Doubt as a one-time house-cleaning, not a way of life.</li>
    <li style="margin-bottom:9px;"><b>&ldquo;The reading of all good books is like a conversation with the finest minds of past centuries.&rdquo;</b> (Discourse, Part 1.)</li>
    <li style="margin-bottom:9px;"><b>&ldquo;Good sense is the best shared thing in the world.&rdquo;</b> (The opening line of the Discourse.) He added, with a straight face, that everyone is sure they already have enough of it.</li>
    <li style="margin-bottom:9px;"><b>&ldquo;Always try to master myself rather than fortune, and to change my desires rather than the order of the world.&rdquo;</b> (Discourse, Part 3.)</li>
    <li style="margin-bottom:9px;"><b><i>Larvatus prodeo</i>: &ldquo;Masked, I advance.&rdquo;</b> (A note from his early private papers, around 1619.)</li>
    <li><b><i>Bene vixit, bene qui latuit</i>: &ldquo;He lives well who hides well.&rdquo;</b> (A line of the Roman poet Ovid, which Descartes took to heart after Galileo&rsquo;s trial.)</li>
  </ol>
  <div style="font-size:.82rem; color:#6b5a30; margin-top:10px; font-style:italic;">Descartes wrote in French and Latin, so every English version is a translation. Wording varies a little from book to book.</div>
</div>"""

# ---------------------------------------------------------------------------
# The story
# ---------------------------------------------------------------------------
DESCARTES = dict(
    title="I Think, Therefore I Am: Descartes and the Fly on the Ceiling",
    h1="✦ I Think, Therefore I Am ✦",
    sub="René Descartes, the man who doubted everything, and the fly that gave us the coordinate plane",
    footer="Every quote is labeled with where it comes from · every legend is labeled as a legend<br>(the fly is still unproven, and still the best way to remember the grid)",
    praise=["Cogito, {name}!", "Clearly and distinctly right, {name}!", "The demon could not fool you, {name}!",
            "Descartes would add that to his notebook, {name}!", "Well divided and well conquered, {name}!"],
    cert_org="The Society of Honest Doubters",
    cert_of="the tale of René Descartes",
    cert_rank="Master of the Grid",
    finale_title="One Sure Point, and a Grid to Put It On",
    finale_html="""
<p>Look at the two things Descartes left us, side by side. One is a way of thinking: doubt everything you can, find the single thing you cannot doubt, and then build upward one careful step at a time. The other is a way of drawing: pick a corner, measure two distances, and every spot in the world gets a two-number address. They are really the same idea. Both start from one fixed point (<i>I think</i>, or the corner of the ceiling) and both build a whole world from there by clear, checkable steps.</p>
<p>The grid changed science more than the doubt did. Once any curve can be written as an equation, you can describe the path of a cannonball, a planet, or a stock price with a rule, and then use algebra to answer questions about it. Isaac Newton studied Descartes&rsquo;s geometry as a student at Cambridge. When Newton worked out the orbit of the Moon, he was walking on the road Descartes had paved. Every graph in every textbook, every map on your phone, every video game that places a character at <i>(x, y)</i>, is a descendant of that idea.</p>
<p>The doubt did not disappear either. Whenever someone asks &ldquo;how do you know?&rdquo; and will not accept &ldquo;because everyone says so,&rdquo; that is Descartes in the room. He would also want you to remember the second half of his method, which is easy to forget: after you doubt, you <i>rebuild</i>. Doubt is the demolition. Reasoning is the construction.</p>
<p>And the fly? Maybe it was there, maybe it was not. The story is probably a tale told long after his death. But you have just spent a lesson placing a fly at (4, 2), crawling it to (4, 5), and measuring the distance with the Pythagorean theorem. Whoever the first person was who thought of it, you now think like them.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>&#9312; Descartes (1596 to 1650) set out to doubt everything he could and keep only what survived. His <b>method</b> has four rules, the second being to divide every difficulty into as many parts as needed.</p>
<p>&#9313; The <b>dream argument</b> and the <b>evil demon</b> were thought experiments. He did not believe he was being tricked. He wanted to see what was left standing.</p>
<p>&#9314; The one thing left was <b>&ldquo;I think, therefore I am&rdquo;</b>: even a deceived mind must exist to be deceived. (Saint Augustine had a similar thought 1,200 years earlier.)</p>
<p>&#9315; <b>The fly on the ceiling</b> is a legend, but its idea is real. A point's position can be given by two numbers, such as <b>(4, 2)</b>, and the distance between two points comes from a&#178; + b&#178; = c&#178;.</p>
<p>&#9316; <b>La G&eacute;om&eacute;trie</b> (1637) joined algebra to geometry: an equation such as y = 2x + 1 or x&#178; + y&#178; = 25 draws a line or a circle on the plane.</p>
<p>&#9317; The plane is called <b>Cartesian</b> after his Latin name, <i>Cartesius</i>. Negative numbers and all four quadrants came into general use after him.</p>
</div>""",
    chapters=[
        # ------------------------------------------------------------------ 1
        dict(
            kicker="Chapter One · La Haye, France · 1596 to 1614",
            title="The Boy Who Stayed in Bed",
            html="""
<p>René Descartes was born on <b>31 March 1596</b> in a small French town called La Haye en Touraine. (Today the town is named <i>Descartes</i> in his honour.) His mother died when he was still a baby, and he grew up thin, pale and often ill, with a dry cough. His father, a judge, is said to have called him his &ldquo;little philosopher&rdquo; because he asked questions about everything.</p>
<p>Around <b>1606</b>, when René was about ten, he was sent to one of the best schools in Europe: the Jesuit college of <b>La Fl&egrave;che</b>, founded by King Henri IV. For about eight years he studied Latin, Greek, logic, philosophy, and mathematics. <b>The story goes</b> that because he was so frail, the headmaster allowed him to stay in bed in the morning while the other boys went to class. It is told in a biography by Adrien Baillet, published in <b>1691</b>, forty-one years after Descartes died, so treat it with care. What does seem true is that he kept the habit all his life. Lying warm in bed, thinking, was where he did his best work.</p>
<p>School left him unhappy in a strange way. He later wrote that the books taught him a great deal, but that on every question, the learned men disagreed. He observed that there is nothing so strange or hard to believe that some philosopher has not said it. If the cleverest people alive could not agree about anything, how was a student to know what was true?</p>
<p>There was one exception: <b>mathematics</b>. He wrote that he was delighted by it because of the <i>certainty</i> of its proofs. Nobody shouted about a triangle or about two plus two, and nobody stayed unconvinced once the steps were laid out. That was the feeling he wanted for the rest of knowledge. (If you read the Euclid lesson, you know exactly what he meant.)</p>
<p>He finished at La Fl&egrave;che about <b>1614</b>, studied law at the University of Poitiers, and earned his degree in <b>1616</b>. Then he did something unusual for a young man with a law degree: he decided he had learned all he could from books, and that the rest of the learning would have to come from &ldquo;the great book of the world.&rdquo; He went out to see it.</p>
<div class="bigidea">🌟 <b>Big Idea #1:</b> When clever people disagree about everything, how do you decide what to believe? Descartes&rsquo;s answer was to copy mathematics: accept only what you can see clearly for yourself, step by step.</div>""",
            cps=[dict(
                type="num",
                kicker="La Fl&egrave;che",
                q="""Descartes arrived at the college of La Fl&egrave;che around the year <b>1606</b> and left about <b>1614</b>. About how many <b>years</b> did he spend there?""",
                answers=[8], unit="years",
                hint="Subtract the start year from the finish year: 1614 &#8722; 1606.",
            )],
        ),
        # ------------------------------------------------------------------ 2
        dict(
            kicker="Chapter Two · Breda and Germany · 1618 to 1619",
            title="A Soldier, a Stove, and Three Dreams",
            html="""
<p>In <b>1618</b>, the twenty-two-year-old Descartes joined the army of Prince Maurice of Nassau, in the Dutch town of <b>Breda</b>. He was a gentleman-volunteer, not much of a fighter. There was a pause in the war at the time, and the young Frenchman had plenty of free hours.</p>
<p>One story, again from Baillet, says that he saw a crowd reading a poster in Dutch, a language he did not know. The poster was a maths puzzle. He asked a bystander to translate it into French or Latin. The bystander turned out to be <b>Isaac Beeckman</b>, a Dutch scientist and schoolmaster, who set him a harder problem as a joke. Descartes is said to have solved it in a few hours. True or not, the two did become close friends, and Beeckman reawakened Descartes&rsquo;s love of mathematics and of explaining nature with numbers.</p>
<p>The next year the great religious war that we now call the <b>Thirty Years&rsquo; War</b> was blazing, and Descartes joined another army, in Germany. On <b>10 November 1619</b>, snowed in at winter quarters near the Danube, he shut himself into a room heated by a large stove. That night, as he later recorded in a notebook, he had <b>three vivid dreams</b>. He came away convinced that he had found &ldquo;the foundations of a wonderful science.&rdquo; The notebook is lost. We know of it only through Baillet&rsquo;s summary seventy years later, so the details are uncertain. What we do know is that this was the moment he decided what to do with his life.</p>
<p>Where did the idea come from? Look at what mathematicians do. They take a huge, scary problem and cut it into small steps, each so simple that nobody can doubt it. Then they chain the steps together. Descartes noticed that this is exactly how Euclid proved everything. Why not use the same chain for <i>all</i> questions? He later wrote it down as four short rules in his <b>Discourse on Method</b> (1637):</p>
<div class="bigidea"><b>1.</b> Accept nothing as true unless you see it so clearly that you cannot doubt it.<br>
<b>2.</b> <b>Divide</b> each difficulty into as many small parts as you can.<br>
<b>3.</b> Think in order, starting with the simplest things and climbing step by step to the complex ones.<br>
<b>4.</b> Check everything so thoroughly, with lists and reviews, that you are sure nothing has been missed.</div>
<p>Rule 2 is the one you will use most. Here it is on a multiplication problem. To work out <b>13 &times; 15</b>, don&rsquo;t try to do it all at once. Split 15 into 10 + 5. Then 13 &times; 10 = 130, and 13 &times; 5 = 65, and the answer is 130 + 65 = <b>195</b>. A hard thing became two easy things.</p>""",
            cps=[dict(
                type="num",
                kicker="Rule 2 &middot; divide the difficulty",
                q="""Use Descartes&rsquo;s second rule. Split <b>24</b> into <b>20 + 4</b> and work out <b>17 &times; 24</b>.""",
                answers=[408], unit="",
                hint="17 &times; 20 = 340, and 17 &times; 4 = 68. Add the two pieces together.",
            )],
        ),
        # ------------------------------------------------------------------ 3
        dict(
            kicker="Chapter Three · The Netherlands · the 1630s and 1640s",
            title="Can I Trust My Eyes?",
            html="""
<p>In <b>1628</b> Descartes moved to the Dutch Republic, and there he stayed, with a few moves from town to town, for about twenty years. The Dutch Republic was one of the freest and busiest places in Europe. It had printing presses, good lenses, and few people watching what you thought. He liked it so much that he said he walked through the crowds of Amsterdam as calmly as if he were walking in a forest.</p>
<p>Here he began the project that made him famous, and it started with a very odd job: <b>doubting everything he could</b>. The idea is easiest to see with a basket of apples. Suppose you have a basket, and you fear some of the apples are rotten. The sensible thing to do is to tip them all out, look at each one, and put back only the good ones. In his mind, Descartes tipped out <i>every belief he had</i> and put back only those that survived.</p>
<p>First to go were beliefs that come from the senses. A stick half in water <i>looks</i> bent, but it is straight. A square tower seen from far away <i>looks</i> round. Your eyes have fooled you before, and he thought it unwise to trust completely something that has ever fooled you.</p>
<p>But surely, he thought, I can trust my senses about things that are right in front of me, such as that I am sitting here by the fire with a paper in my hand? Then he stopped himself. His own words, from the <b>Meditations on First Philosophy</b> (1641): how often, asleep at night, am I sure of just such familiar facts, that I am sitting by the fire in my dressing gown, when in fact I am lying undressed in bed! In a dream, everything feels real. And he could find <i>no sure sign</i> that would tell waking from dreaming.</p>
<p>That is the <b>dream argument</b>. Think about how much time is involved. You spend about one-third of your life asleep. If dreams can feel real, and you spend a third of your life in them, can you be sure you are not dreaming right now?</p>
<div class="funfact">🔎 About 1,900 years earlier, the Chinese thinker Zhuangzi told of dreaming he was a butterfly, and waking up unsure whether he was a man who had dreamed of being a butterfly, or a butterfly now dreaming it was a man. The puzzle is very old. Descartes made it sharp.</div>
<p>You are probably thinking, &ldquo;But this is silly. I know I&rsquo;m awake!&rdquo; Descartes would nod. He did not <i>believe</i> he was dreaming. He used the idea like a crowbar to test which beliefs would hold up if someone pushed hard. In everyday life, he said, you should keep acting normally, eat dinner, and go to bed. The doubt was something he did in his study, on purpose, for a short time.</p>""",
            cps=[dict(
                type="num",
                kicker="The dream argument",
                q="""Suppose a person sleeps <b>8 hours</b> out of every 24, which is one-third of their time. If they live to be <b>75</b>, how many <b>years</b> of their life do they spend asleep?""",
                answers=[25], unit="years",
                hint="One-third of 75 is 75 &#247; 3.",
            )],
        ),
        # ------------------------------------------------------------------ 4
        dict(
            kicker="Chapter Four · Meditation One",
            title="The Evil Demon",
            html="""
<p>The dream argument shook the senses. But what about things you know without looking at anything? Surely <b>2 + 3 = 5</b>, and a square has four sides, whether I am dreaming or awake. These are as safe as anything can be.</p>
<p>Descartes was not satisfied. He imagined something stranger and more frightening. His words: suppose that some malicious demon of the utmost power and cunning has used all of his energy to deceive me. Suppose the sky, the air, the earth, colours, shapes and sounds are nothing but tricks the demon uses to catch my belief. I will think of myself as having no hands, no eyes, no flesh, and no blood. This is the <b>evil demon</b> (he also called it a &ldquo;malicious genius&rdquo;), and it is one of the most famous thought experiments in history.</p>
<p>What could the demon do to mathematics? Descartes pushed the thought as far as it would go. If a demon were powerful enough, it might arrange for you to go wrong <i>every single time</i> you add two and three, or count the sides of a square. There would be no feeling of being wrong. The mistake would look perfectly clear to you. So even sums could be doubted.</p>
<p>This idea has come back many times. In 1981 the American philosopher Hilary Putnam asked what if you were a <b>brain in a vat</b>, fed all of your experiences by a computer. Movies like <i>The Matrix</i> use the same thought. All of them go back to Descartes&rsquo;s demon.</p>
<p>Why would anyone do this to themselves? Remember the apple basket. Descartes wanted a foundation that nothing could shake, not even a demon. If he could find one single thing that survived all of this, he could build everything else on it. If he could not, then all his knowledge was sand. It was a test of strength, applied as hard as he could.</p>
<div class="funfact">🔎 Descartes did not stay in the dark forever. After he found his first solid fact, he went on to argue that a good God exists and would not let him be tricked all the time. Many readers, then and now, think that step is the weakest part of his chain. Even his friends argued with him about it. Descartes would have been the first to tell you to check his work.</div>
<p>A practical lesson from the demon is that when something matters, you should <b>check it a second way</b>. If a demon might be rigging your adding, add in a different order, or subtract to see if you get back to where you started.</p>""",
            cps=[dict(
                type="num",
                kicker="Doubting the sum",
                q="""Descartes would say: check your work by a second route. Work out <b>478 + 356</b>. Then check by adding 356 to 478 the other way round (or subtract to get back).""",
                answers=[834], unit="",
                hint="478 + 300 = 778. Then 778 + 56 = 834. Check: 834 &#8722; 356 should give 478.",
            )],
        ),
        # ------------------------------------------------------------------ 5
        dict(
            kicker="Chapter Five · Discourse Part 4 and Meditation Two",
            title="I Think, Therefore I Am",
            html="""
<p>Now Descartes had thrown away the senses, the body, the sky, even arithmetic. Was anything left? He went hunting for any single fact that the demon could not touch.</p>
<p>Then he saw it. Suppose the demon is tricking me about <i>everything</i>. Then there must be a <i>me</i> that is being tricked. To be fooled, I have to exist. The more power the demon uses to deceive me, the more certain it becomes that I am here. In the <b>Meditations</b> he wrote that the statement <b>&ldquo;I am, I exist&rdquo;</b> is necessarily true each time I say it or think it.</p>
<p>Put into one sentence, that is the most famous line in philosophy. It first appeared in print in French in the <b>Discourse on Method</b> (1637): <b>&ldquo;Je pense, donc je suis.&rdquo;</b> In 1644, in the Latin <i>Principles of Philosophy</i>, it became the version we know best: <b>&ldquo;Cogito, ergo sum.&rdquo;</b> In English: <b>I think, therefore I am.</b></p>
<p>Notice how modest the claim is. He had not proved the sky exists, or his body, or other people. He had found only that <b>there is thinking going on, so there is a thinker</b>. He wrote that his &ldquo;I&rdquo; at this stage was only &ldquo;a thing that thinks&rdquo;: something that doubts, understands, affirms, denies, wishes, imagines and feels. It was a tiny island. But he said it was solid, and he would build on it.</p>
<p>That is exactly what Euclid does with a few postulates. A system of knowledge needs a point where you stand. Descartes found his.</p>
<div class="funfact">🔎 Was Descartes the first to think of it? No. About AD 420, <b>Saint Augustine</b> wrote &ldquo;<i>si fallor, sum</i>&rdquo;: if I am mistaken, I am. Descartes&rsquo;s contemporaries pointed this out to him. He answered politely that he had not read the passage, and that he used the idea for a different purpose: not to prove the soul, but to begin a whole new chain of knowledge from scratch.</div>
<p>Count how the demolition went. He began with a long list of things he believed. The senses fell to the dream argument. The body fell with them. Mathematics fell to the demon. What stood at the end was a very short list.</p>
<div class="bigidea">🌟 <b>Big Idea #2:</b> A certain starting point is worth more than a thousand likely guesses. Find one thing you cannot doubt, then build outward with clear steps, checking each one.</div>""",
            cps=[dict(
                type="num",
                kicker="What is left standing?",
                q="""Descartes starts with <b>10</b> beliefs on his list. The dream argument knocks out <b>4</b> (beliefs from the senses). The loss of the body knocks out <b>3</b> more. The evil demon knocks out <b>2</b> (the mathematics). How many beliefs survive? (It is the one he is famous for.)""",
                answers=[1], unit="belief",
                hint="10 &#8722; 4 &#8722; 3 &#8722; 2. What is left over?",
            )],
        ),
        # ------------------------------------------------------------------ 6
        dict(
            kicker="Chapter Six · The Legend",
            title="The Fly on the Ceiling",
            html="""
<p>Now to the story you came for. <b>The story goes</b> that Descartes was lying in bed one morning, as usual, with nothing to do but think. A fly was crawling about on the ceiling. He watched it. And a question formed: <i>how could I tell someone exactly where that fly is?</i></p>
<p>You could say &ldquo;near the lamp.&rdquo; But that is vague. You could say &ldquo;a hand&rsquo;s width from the window.&rdquo; Better, but whose hand? Then he realised: pick one corner of the ceiling. Two walls meet there. Measure how far the fly is <b>along one wall</b>. Then measure how far it is <b>along the other wall</b>. Two numbers, and the fly&rsquo;s position is exactly fixed. The fly could crawl anywhere, and at every moment you could describe where it was with just two numbers.</p>
<p>The path of the fly, then, is a list of number pairs. If the fly moves in a straight line, the numbers follow a pattern. If it moves in a circle, they follow a different pattern. <i>The pattern is an equation.</i> That is the secret. A shape becomes a rule, and a rule becomes a shape.</p>
<div class="funfact">🔎 <b>Is the fly story true?</b> Probably not as told. The story is repeated in many books, but we cannot find it in Descartes&rsquo;s own writings, and we do not know who first told it. Historians of mathematics also note that Descartes did not write coordinates as modern number pairs. The real idea is unmistakable in his book, though. The fly is a good way to remember the idea, and the project&rsquo;s rule is to call a story a story.</div>
<p>Mathematicians now write a fly&rsquo;s address as an <b>ordered pair</b>, <b>(x, y)</b>. The first number is always across (x), and the second is always along (y). Order matters: (4, 2) is not the same spot as (2, 4). The corner where you start is called the <b>origin</b>, and its address is (0, 0).</p>
<p>The pair of measuring lines is called a <b>Cartesian plane</b>, after Descartes&rsquo;s Latin name, <i>Cartesius</i>. (A &ldquo;plane&rdquo; here means a flat surface that goes on as far as you like.) Try the fly yourself. Click on the ceiling, or use the sliders, and watch the address change. Move the fly several times and the trail it leaves is a path made of addresses.</p>
""" + FLY + """
<p>Once you have addresses, you can ask: how far apart are two spots? If the fly walks straight along a row, it is easy. You just subtract. If it walks <i>diagonally</i>, imagine a right triangle: one leg across, one leg along. The fly&rsquo;s straight path is the hypotenuse. That is Pythagoras: <b>a&#178; + b&#178; = c&#178;</b>. Descartes was combining two ancient ideas, the grid and the right triangle, and they fit together perfectly.</p>""",
            cps=[dict(
                type="num",
                kicker="Distance along a row",
                q="""A fly sits at <b>A = (1, 2)</b> and crawls straight along the row to <b>B = (4, 2)</b>. How many steps did it crawl?""",
                figure=_cp_walk(),
                answers=[3], unit="steps",
                hint="Both spots are on the same row (y = 2). Only the x-number changes: 4 &#8722; 1.",
            ), dict(
                type="num",
                kicker="Distance on a diagonal",
                q="""Now a fly crawls in a straight line from <b>A = (1, 1)</b> to <b>B = (4, 5)</b>. The dashed lines make a right triangle. How many steps long is the straight path AB?""",
                figure=_cp_diag(),
                answers=[5], unit="steps",
                hint="The legs are 4 &#8722; 1 = 3 across and 5 &#8722; 1 = 4 up. Then 3&#178; + 4&#178; = 9 + 16 = 25, and the square root of 25 is 5.",
            ), dict(
                type="mc",
                kicker="Reading an address",
                q="""A fly is <b>5 steps across</b> and <b>2 steps along</b> from the corner. What is its address?""",
                mc=[("(2, 5)", False),
                    ("(5, 2)", True),
                    ("(7, 0)", False)],
                good="Yes, {name}. Across comes first, so the address is (5, 2). Swap them and you get a different spot, (2, 5), a long way off.",
                bad="Careful, {name}. The first number is the steps across (x), and the second is the steps along (y). Order matters.",
            )],
        ),
        # ------------------------------------------------------------------ 7
        dict(
            kicker="Chapter Seven · La G&eacute;om&eacute;trie · 1637",
            title="Where Algebra Met Geometry",
            html="""
<p>In <b>1637</b>, Descartes published his first book. Its full title was long: <i>Discourse on the Method of Rightly Conducting One&rsquo;s Reason and Seeking Truth in the Sciences</i>. Three &ldquo;essays&rdquo; followed it as examples of the method at work: one on optics (<i>La Dioptrique</i>), one on weather (<i>Les M&eacute;t&eacute;ores</i>), and one on geometry: <b>La G&eacute;om&eacute;trie</b>. It was printed in the Dutch city of Leiden, in <b>French</b> instead of Latin, so that ordinary educated readers could follow, and his name did not appear on the title page.</p>
<p>Before this book, <b>geometry</b> and <b>algebra</b> lived in separate houses. Geometry was about shapes, drawn with ruler and compass, like Euclid&rsquo;s. Algebra was about unknown numbers and rules for finding them. Few people thought of using one to help the other.</p>
<p>Descartes connected them. Pick a reference line. Then a point on a curve can be described by how far along the line it is, and how far away from the line it is. Call these two lengths <b>x</b> and <b>y</b>. A curve is simply every point where x and y obey some rule. An <b>equation</b> that mixes x and y is a description of a curve. And if you can describe a curve by an equation, you can solve geometry problems with algebra, without drawing a thing.</p>
<p>He also tidied up how maths is written. He used letters from the <b>start</b> of the alphabet (a, b, c) for numbers that are known, and letters from the <b>end</b> (x, y, z) for the unknowns. That habit has stuck for nearly 400 years. He wrote powers with small raised numbers, such as x&#179;, for x &times; x &times; x. Before him, maths was often written in long sentences.</p>
<p>The French lawyer and mathematician <b>Pierre de Fermat</b> had the same idea at about the same time, working alone. Fermat did not publish his, so the credit went to Descartes. And Descartes&rsquo;s own plane was not quite the modern one. He mostly used distances measured in one direction, and the full picture with two axes crossing at the middle and negative numbers going left and down was filled in by those who came after him. Isaac Newton studied the Latin edition of <i>La G&eacute;om&eacute;trie</i> as a student, and he helped carry the idea forward.</p>
<p>Play with the plane below. Move the sliders and watch an equation draw a line, or draw a circle. Notice the four <b>quadrants</b>. In the top left, x is negative (it is to the <i>left</i> of the middle). In the bottom right, y is negative (<i>below</i> the middle).</p>
""" + GRAPH + """
<p>A <b>line</b> has the form <b>y = mx + b</b>. The number b says where the line crosses the up-down axis, and m says how steeply it climbs. Take the line <b>y = 2x + 1</b>. When x = 0, y = 1. When x = 1, y = 3. When x = 2, y = 5. Every time x goes up by 1, y goes up by 2.</p>
<p>A <b>circle</b> centred on the origin has the form <b>x&#178; + y&#178; = r&#178;</b>, where r is the radius. This is Pythagoras again. A point (x, y) is exactly r steps from the origin when x&#178; + y&#178; = r&#178;. For example, (3, 4) is on the circle with r = 5, because 9 + 16 = 25.</p>""",
            cps=[dict(
                type="num",
                kicker="Reading a line",
                q="""A line has the equation <b>y = 2x + 1</b>. When <b>x = 3</b>, what is <b>y</b>?""",
                answers=[7], unit="",
                hint="Put 3 in place of x: 2 &times; 3 + 1.",
            ), dict(
                type="mc",
                kicker="Reading a circle",
                q="""Which of these points lies on the circle <b>x&#178; + y&#178; = 25</b>?""",
                mc=[("(4, 4)", False),
                    ("(2, 5)", False),
                    ("(3, 4)", True)],
                good="Yes, {name}. 3&#178; + 4&#178; = 9 + 16 = 25. The others give 32 and 29.",
                bad="Try squaring both numbers and adding, {name}. The answer must come to exactly 25.",
            ), dict(
                type="num",
                kicker="Negative addresses",
                q="""A point <b>P</b> sits at <b>(&#8722;6, 8)</b>: six steps to the <i>left</i> of the origin and eight steps up. How many steps is P from the origin <b>O</b> in a straight line?""",
                figure=_cp_origin(),
                answers=[10], unit="steps",
                hint="Ignore the minus sign for the distance: the legs are 6 and 8. Then 36 + 64 = 100.",
            ), dict(
                type="num",
                kicker="Descartes&rsquo;s notation",
                q="""Using his habit of writing powers, find the value of <b>x&#178; &#8722; 2x</b> when <b>x = 5</b>.""",
                answers=[15], unit="",
                hint="x&#178; means x &times; x, which is 25. Then 2x is 10. Subtract.",
            )],
        ),
        # ------------------------------------------------------------------ 8
        dict(
            kicker="Chapter Eight · Egmond, Stockholm · 1633 to 1650",
            title="The Man Who Hid",
            html="""
<p>In <b>1633</b>, Descartes was nearly finished with a book called <i>The World</i>, which explained the universe as a machine, with the Earth moving around the Sun. Then news came from Italy: the Church had put <b>Galileo</b> on trial for saying exactly that, and had forced him to take it back. Descartes put <i>The World</i> in a drawer. It was not printed until after he died. He kept as his motto a line of the Roman poet Ovid: <i>bene vixit, bene qui latuit</i>, &ldquo;he lives well who hides well.&rdquo; (A note in his early papers read, <i>larvatus prodeo</i>: &ldquo;masked, I advance.&rdquo;)</p>
<p>Still, his ideas got out. He wrote in 1641 the <b>Meditations</b>, and in 1644 the <b>Principles of Philosophy</b>. He compared all knowledge to a tree: the <b>roots</b> are the first questions (what can I be sure of?), the <b>trunk</b> is physics, and the <b>branches</b> are the useful sciences, such as medicine and mechanics.</p>
<p>He also defended a strong idea about the mind and the body: that they are two different kinds of thing, one made of thought and the other of matter. A clever young woman, <b>Princess Elisabeth of Bohemia</b>, wrote him letters from 1643 asking the hard question: if the mind is not a physical thing, how can it move the body? He did not have a good answer, and they kept writing.</p>
<p>In 1649, <b>Queen Christina of Sweden</b>, who was only twenty-two and fiercely eager to learn, invited him to Stockholm to teach her. He went. The tale told is that she wanted her lessons at <b>five in the morning</b>, in a cold library, and that the late-sleeping philosopher, now in a Swedish winter, caught pneumonia. He died on <b>11 February 1650</b>, aged <b>53</b>. (Some historians have wondered whether the story is exaggerated, but the sudden death in a northern winter is a fact.)</p>
<p>Here are the words he is best remembered for. They come from his books and letters, but he wrote in French and Latin, so the English is a translation.</p>
""" + QUOTES + """
<p>After he died, the word <b>Cartesian</b> came to mean both his philosophy and his grid. Even now, when you find a spot on a map by two numbers, or plot a graph in science class, you are using his idea.</p>""",
            cps=[dict(
                type="num",
                kicker="A lifetime of ideas",
                q="""Descartes published <i>La G&eacute;om&eacute;trie</i> in <b>1637</b> and died in <b>1650</b>. How many years after the book appeared did he die?""",
                answers=[13], unit="years",
                hint="1650 &#8722; 1637.",
            )],
        ),
    ],
    quiz=dict(
        title="&#10022; Ten Problems in the Cartesian Style &#10022;",
        intro="Ten questions for a Cartesian mind. One attempt each, because a demon never gives a second guess either. Divide each difficulty into parts, draw a grid if it helps, and check your answer a second way.",
        verdicts=[
            dict(min=10, title="{score}: Clear and distinct", text="Flawless, {name}. Descartes would be satisfied that nothing was missed. (Rule 4!)"),
            dict(min=7, title="{score}: A sound builder", text="Strong work, {name}. Read the explanations under the ones that got away, then try the fly widget again."),
            dict(min=4, title="{score}: Doubt, then rebuild", text="You have the idea, {name}. Sketch a grid for each problem, split it into small parts, and try again."),
            dict(min=0, title="{score}: Back to the corner", text="Every one of these can be learned, {name}. Start again at the corner of the ceiling, (0, 0), and count your steps."),
        ],
        questions=[
            dict(type="num", kicker="Rule 2 &middot; divide the difficulty",
                 q="""Split <b>14</b> into <b>10 + 4</b> and work out <b>23 &times; 14</b>.""",
                 answers=[322], unit="",
                 why="23 &times; 10 = 230, and 23 &times; 4 = 92. 230 + 92 = 322."),
            dict(type="num", kicker="Lines",
                 q="""A line has the equation <b>y = 3x &#8722; 2</b>. When <b>x = 4</b>, what is <b>y</b>?""",
                 answers=[10], unit="",
                 why="3 &times; 4 = 12, and 12 &#8722; 2 = 10."),
            dict(type="num", kicker="Distance from the origin",
                 q="""How far is the point <b>(&#8722;3, 4)</b> from the origin?""",
                 answers=[5], unit="units",
                 why="The legs are 3 and 4. 9 + 16 = 25, and the square root of 25 is 5."),
            dict(type="mc", kicker="Quadrants",
                 q="""Which point is to the <b>left</b> of the up-down axis and <b>above</b> the across axis?""",
                 mc=[("(3, &#8722;4)", False),
                     ("(&#8722;3, 4)", True),
                     ("(&#8722;3, &#8722;4)", False)],
                 why="Left means x is negative. Above means y is positive. That is (&#8722;3, 4), in the top-left quadrant."),
            dict(type="num", kicker="The fly",
                 q="""A fly crawls in a straight line from <b>(2, 1)</b> to <b>(5, 5)</b>. How many steps long is its path?""",
                 answers=[5], unit="steps",
                 why="The legs are 5 &#8722; 2 = 3 across and 5 &#8722; 1 = 4 up. 9 + 16 = 25, so the path is 5."),
            dict(type="mc", kicker="Circles",
                 q="""Which point lies on the circle <b>x&#178; + y&#178; = 100</b>?""",
                 mc=[("(7, 7)", False),
                     ("(10, 1)", False),
                     ("(6, 8)", True)],
                 why="6&#178; + 8&#178; = 36 + 64 = 100. The others give 98 and 101."),
            dict(type="num", kicker="The dream argument",
                 q="""A student sleeps <b>9 hours</b> out of every 24. In <b>80 years</b>, how many years is that asleep?""",
                 answers=[30], unit="years",
                 why="9 out of 24 is 3 out of 8. Then 80 &#247; 8 = 10, and 10 &times; 3 = 30."),
            dict(type="num", kicker="Powers",
                 q="""Using Descartes&rsquo;s raised numbers, what is <b>x&#179;</b> when <b>x = 3</b>?""",
                 answers=[27], unit="",
                 why="x&#179; means x &times; x &times; x = 3 &times; 3 &times; 3 = 27."),
            dict(type="mc", kicker="Lines",
                 q="""Which point lies on the line <b>y = x + 2</b>?""",
                 mc=[("(2, 2)", False),
                     ("(3, 5)", True),
                     ("(0, 3)", False)],
                 why="3 + 2 = 5, so (3, 5) is on the line. The others need y to be 4 and 2."),
            dict(type="num", kicker="A lifetime",
                 q="""Descartes was born on 31 March 1596 and died on 11 February 1650. How many <b>full years</b> old was he when he died?""",
                 answers=[53], unit="years",
                 why="1650 &#8722; 1596 = 54, but he died before his March birthday, so he had completed 53 years."),
        ],
    ),
)
