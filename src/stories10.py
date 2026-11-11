# -*- coding: utf-8 -*-
"""Story data: Fraunhofer, Kirchhoff and Bunsen. The dark lines in sunlight and the bright lines in the lab."""

# ---------------------------------------------------------------------------
# Live widgets and the one checkpoint figure
# ---------------------------------------------------------------------------
_BOX = 'background:#fdf9ee; border:1.5px solid #c9b57e; border-radius:12px; padding:14px 16px; margin:14px 0;'
_CAP = ('text-align:center; font-size:.8rem; letter-spacing:2px; text-transform:uppercase; '
        'color:#8a6400; font-weight:bold; margin-bottom:8px;')
_BTN = ('font-family:Georgia,serif; cursor:pointer; background:#fff8e6; border:1.5px solid #c9b57e; '
        'border-radius:8px; padding:7px 12px; font-size:.85rem; color:#5a4a1a;')


def _cp_table():
    td = 'style="padding:4px 10px; border:1px solid #d9c9a3;"'
    th = 'style="padding:4px 10px; border:1px solid #d9c9a3; background:#f1e7cf;"'
    rows = [("Sodium", "589.0 and 589.6"), ("Lithium", "670.8"), ("Strontium", "460.7"), ("Potassium", "766.5")]
    body = "".join("<tr><td %s>%s</td><td %s>%s</td></tr>" % (td, a, td, b) for a, b in rows)
    return ('<div style="background:#fffdf4; color:#22304f; border-radius:10px; padding:10px 12px; margin:10px 0; '
            'font-size:.95rem;"><div style="text-align:center; font-weight:bold; margin-bottom:6px;">'
            'Reference fingerprints (bright lines, in nm)</div>'
            '<table style="border-collapse:collapse; margin:0 auto;"><tr><th %s>Element</th><th %s>Bright lines</th></tr>%s</table>'
            '<div style="text-align:center; margin-top:8px;">Mystery flame, lines seen: <b>460.7, 589.0, 589.6, 670.8</b></div></div>'
            % (th, th, body))


REVERSAL = ('<div style="%s">\n  <div style="%s">Kirchhoff&rsquo;s sodium flame &middot; slide the background lamp</div>' % (_BOX, _CAP)) + r"""
  <div style="text-align:center;">
    <svg id="rv-svg" width="420" height="282" viewBox="0 0 420 282" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;" role="img" aria-label="Above: a lump of hot lime glowing more or less brightly, a sodium flame, and a prism. Below: a strip of yellow light near 589 nanometres with the sodium D pair of lines shown brighter, darker or invisible depending on how bright the lime is"></svg>
  </div>
  <div id="rv-out" style="text-align:center; font-size:1rem; color:#3d3320; margin:8px 0 8px; line-height:1.6; min-height:5.2em;"></div>
  <div style="max-width:440px; margin:0 auto; display:grid; grid-template-columns:auto 1fr auto; gap:6px 10px; align-items:center; font-size:.9rem; color:#3d3320;">
    <label for="rv-b">Background lamp (hot lime)</label><input id="rv-b" type="range" min="0" max="100" step="5" value="80" style="width:100%;"><span id="rv-bv" style="min-width:2.2em; text-align:right;"><b>80</b></span>
  </div>
  <div style="text-align:center; margin-top:10px;"><label style="font-size:.9rem; color:#3d3320; cursor:pointer;"><input type="checkbox" id="rv-on" checked> sodium flame in the beam (glows at 50, soaks up 60% of the light behind it)</label></div>
</div>
<script>
(function(){
  var svg = document.getElementById('rv-svg');
  if (!svg) return;
  var NS = 'http://www.w3.org/2000/svg', F = 50, A = 0.6;
  var sb = document.getElementById('rv-b'), on = document.getElementById('rv-on');
  function el(tag, attrs, text){
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    svg.appendChild(e); return e;
  }
  function shade(v){ var k = Math.max(0, Math.min(100, v)) / 100; return 'rgb(' + Math.round(255 * k) + ',' + Math.round(205 * k) + ',' + Math.round(20 * k) + ')'; }
  function X(nm){ return 30 + (nm - 585) / 8 * 360; }
  function glow(id, cx, cy, r, color, op){
    var g = el('radialGradient', {id: id});
    [[0, op], [0.45, op * 0.55], [1, 0]].forEach(function(st){
      var s = document.createElementNS(NS, 'stop');
      s.setAttribute('offset', st[0]); s.setAttribute('stop-color', color); s.setAttribute('stop-opacity', st[1]);
      g.appendChild(s);
    });
    el('circle', {cx: cx, cy: cy, r: r, fill: 'url(#' + id + ')'});
  }
  function bench(B, flame){
    var Y = 58;
    el('rect', {x: 10, y: 8, width: 400, height: 112, rx: 8, fill: '#0d1330'});
    // beam: as bright as the lime
    el('line', {x1: 60, y1: Y, x2: 318, y2: Y, stroke: '#fff3c0', 'stroke-width': 3, opacity: (0.08 + 0.8 * B / 100).toFixed(2)});
    // hot lime: glow and core follow the slider
    var k = B / 100;
    glow('rv-gl', 60, Y, 8 + 34 * k, '#fff2b0', 0.15 + 0.85 * k);
    var c = function(a, b){ return Math.round(a + (b - a) * k); };
    el('rect', {x: 52, y: Y - 8, width: 16, height: 16, rx: 2, fill: 'rgb(' + c(70, 255) + ',' + c(66, 251) + ',' + c(60, 232) + ')'});
    el('text', {x: 60, y: 108, 'text-anchor': 'middle', 'font-size': 11, fill: '#aebadf'}, 'hot lime: ' + B);
    // sodium flame: fixed glow of F
    el('rect', {x: 186, y: Y + 12, width: 8, height: 26, fill: '#8a8f9a'});
    if (flame){
      glow('rv-gf', 190, Y - 2, 8 + 34 * F / 100, '#ffd23a', 0.15 + 0.85 * F / 100);
      el('path', {d: 'M190 ' + (Y - 24) + ' C202 ' + (Y - 6) + ' 199 ' + (Y + 12) + ' 190 ' + (Y + 12) +
                     ' C181 ' + (Y + 12) + ' 178 ' + (Y - 6) + ' 190 ' + (Y - 24) + ' z', fill: '#ffd23a', 'fill-opacity': 0.9});
      el('path', {d: 'M190 ' + (Y - 10) + ' C195 ' + Y + ' 194 ' + (Y + 10) + ' 190 ' + (Y + 10) +
                     ' C186 ' + (Y + 10) + ' 185 ' + Y + ' 190 ' + (Y - 10) + ' z', fill: '#fff4a0'});
      el('text', {x: 190, y: 108, 'text-anchor': 'middle', 'font-size': 11, fill: '#aebadf'}, 'sodium flame: ' + F);
    } else {
      el('text', {x: 190, y: 108, 'text-anchor': 'middle', 'font-size': 11, fill: '#aebadf'}, 'flame out');
    }
    // prism, then the light heads down to the strip
    el('polygon', {points: '320,' + (Y - 20) + ' 305,' + (Y + 14) + ' 335,' + (Y + 14), fill: '#9fc6e8', 'fill-opacity': 0.2, stroke: '#cfe3f5', 'stroke-width': 1.5});
    el('text', {x: 320, y: 108, 'text-anchor': 'middle', 'font-size': 11, fill: '#aebadf'}, 'prism');
    el('text', {x: 372, y: Y + 4, 'text-anchor': 'middle', 'font-size': 18, fill: '#aebadf'}, '\u2193');
  }
  function draw(){
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    var B = Number(sb.value), flame = on.checked;
    var L = flame ? Math.round((B * (1 - A) + A * F) * 10) / 10 : B;
    bench(B, flame);
    var T = 142;
    el('rect', {x: 30, y: T, width: 360, height: 70, fill: shade(B), stroke: '#22304f', 'stroke-width': 2});
    if (flame){
      [589.0, 589.6].forEach(function(nm){ el('rect', {x: X(nm) - 3, y: T, width: 6, height: 70, fill: shade(L)}); });
    }
    [585, 587, 589, 591, 593].forEach(function(nm){
      el('line', {x1: X(nm), y1: T + 70, x2: X(nm), y2: T + 76, stroke: '#4a5878', 'stroke-width': 1});
      el('text', {x: X(nm), y: T + 90, 'text-anchor': 'middle', 'font-size': 11, fill: '#4a5878'}, nm);
    });
    el('text', {x: 210, y: T + 110, 'text-anchor': 'middle', 'font-size': 11, fill: '#4a5878'}, 'wavelength (nm), zoomed in on the sodium D pair');
    var verdict, col;
    if (!flame){ verdict = 'No flame in the beam: a smooth, even glow.'; col = '#4a5878'; }
    else if (L > B + 0.05){ verdict = 'A BRIGHT pair of lines: the flame glows more than the lamp behind it.'; col = '#1e7d43'; }
    else if (L < B - 0.05){ verdict = 'A DARK pair of lines: the flame soaks up more than it adds.'; col = '#b03030'; }
    else { verdict = 'The lines VANISH: the flame and the lamp are exactly equally bright.'; col = '#8a6400'; }
    document.getElementById('rv-bv').innerHTML = '<b>' + B + '</b>';
    document.getElementById('rv-out').innerHTML =
      (flame ? 'Line brightness = ' + B + ' &times; 0.4 + 0.6 &times; ' + F + ' = <b>' + L + '</b> &nbsp;(background = <b>' + B + '</b>)<br>' : '') +
      '<b style="color:' + col + ';">' + verdict + '</b>';
  }
  sb.addEventListener('input', draw);
  on.addEventListener('change', draw);
  draw();
})();
</script>"""

SPECTRA = ('<div style="%s">\n  <div style="%s">Three kinds of spectrum &middot; pick an element and compare it with the Sun</div>' % (_BOX, _CAP)) + r"""
  <div id="sp-el" style="text-align:center; margin-bottom:8px; display:flex; gap:6px; flex-wrap:wrap; justify-content:center;"></div>
  <div id="sp-mode" style="text-align:center; margin-bottom:8px; display:flex; gap:6px; flex-wrap:wrap; justify-content:center;"></div>
  <div style="text-align:center;">
    <svg id="sp-svg" width="680" height="260" viewBox="0 0 680 260" font-family="Georgia,serif" style="background:#fffdf4; border:1px solid #d9c9a3; border-radius:10px; max-width:100%; height:auto;" role="img" aria-label="A strip showing the spectrum of the chosen element, optionally above a strip showing the Sun with dark lines"></svg>
  </div>
  <div id="sp-out" style="text-align:center; font-size:1rem; color:#3d3320; margin:8px 0 6px; line-height:1.6; min-height:5.4em;"></div>
  <div style="text-align:center;"><label style="font-size:.92rem; color:#3d3320; cursor:pointer;"><input type="checkbox" id="sp-cmp"> compare with the Sun&rsquo;s spectrum</label></div>
</div>
<script>
(function(){
  var svg = document.getElementById('sp-svg');
  if (!svg) return;
  var NS = 'http://www.w3.org/2000/svg', LO = 380, HI = 720, X0 = 20, W = 640;
  var EL = {
    'Hydrogen': [410.2, 434.0, 486.1, 656.3],
    'Sodium': [589.0, 589.6],
    'Iron': [404.6, 438.4, 466.8, 495.8, 527.0, 532.8],
    'Calcium': [393.4, 396.8, 422.7, 616.2],
    'Magnesium': [383.8, 516.7, 517.3, 518.4],
    'Helium': [447.1, 501.6, 587.6, 667.8]
  };
  var SUNSET = ['Hydrogen', 'Sodium', 'Iron', 'Calcium', 'Magnesium'];
  var sunLines = [];
  SUNSET.forEach(function(k){ EL[k].forEach(function(nm){ sunLines.push(nm); }); });
  var cur = 'Hydrogen', mode = 'emit', cmp = document.getElementById('sp-cmp');
  var elRow = document.getElementById('sp-el'), moRow = document.getElementById('sp-mode');
  var BTN = '@@BTN@@';
  function el(tag, attrs, text){
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    svg.appendChild(e); return e;
  }
  function X(nm){ return X0 + (nm - LO) / (HI - LO) * W; }
  function rgb(nm){
    var r = 0, g = 0, b = 0;
    if (nm >= 380 && nm < 440){ r = -(nm - 440) / 60; b = 1; }
    else if (nm < 490){ g = (nm - 440) / 50; b = 1; }
    else if (nm < 510){ g = 1; b = -(nm - 510) / 20; }
    else if (nm < 580){ r = (nm - 510) / 70; g = 1; }
    else if (nm < 645){ r = 1; g = -(nm - 645) / 65; }
    else { r = 1; }
    var f = 1;
    if (nm < 420) f = 0.3 + 0.7 * (nm - 380) / 40; else if (nm > 700) f = 0.3 + 0.7 * (720 - nm) / 20;
    f = Math.max(0.3, f);
    return 'rgb(' + Math.round(255 * r * f) + ',' + Math.round(255 * g * f) + ',' + Math.round(255 * b * f) + ')';
  }
  function rainbow(y, h){
    for (var nm = LO; nm < HI; nm += 2) el('rect', {x: X(nm), y: y, width: X(nm + 2) - X(nm) + 0.6, height: h, fill: rgb(nm + 1)});
  }
  function strip(y, h, kind, lines){
    if (kind === 'emit'){
      el('rect', {x: X0, y: y, width: W, height: h, fill: '#0a0a12'});
      lines.forEach(function(nm){ el('rect', {x: X(nm) - 1.4, y: y, width: 2.8, height: h, fill: rgb(nm)}); });
    } else if (kind === 'cont'){
      rainbow(y, h);
    } else {
      rainbow(y, h);
      lines.forEach(function(nm){ el('rect', {x: X(nm) - 1.4, y: y, width: 2.8, height: h, fill: 'rgba(10,10,18,.92)'}); });
    }
    el('rect', {x: X0, y: y, width: W, height: h, fill: 'none', stroke: '#22304f', 'stroke-width': 2});
  }
  function draw(){
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    var lines = EL[cur], kindTitle = {emit: 'Hot thin gas (a flame, a glowing tube)', cont: 'Glowing solid (a lamp filament)', abs: 'Cool gas in front of a glowing solid'};
    el('text', {x: X0, y: 18, 'font-size': 13, fill: '#8a6400', 'font-weight': 'bold'}, kindTitle[mode] + (mode === 'cont' ? '' : ': ' + cur));
    strip(26, 56, mode, lines);
    var cmpOn = cmp.checked, bottom = 100;
    if (cmpOn){
      el('text', {x: X0, y: 118, 'font-size': 13, fill: '#8a6400', 'font-weight': 'bold'}, 'The Sun (only five elements’ lines drawn; the real Sun shows thousands)');
      strip(126, 56, 'abs', sunLines);
      lines.forEach(function(nm){ el('line', {x1: X(nm), y1: 22, x2: X(nm), y2: 186, stroke: '#e8a90c', 'stroke-width': 1.5, 'stroke-dasharray': '4 3'}); });
      bottom = 186;
    }
    for (var nm = 400; nm <= 700; nm += 50){
      el('line', {x1: X(nm), y1: bottom + 2, x2: X(nm), y2: bottom + 8, stroke: '#4a5878', 'stroke-width': 1});
      el('text', {x: X(nm), y: bottom + 22, 'text-anchor': 'middle', 'font-size': 11, fill: '#4a5878'}, nm);
    }
    el('text', {x: X(560), y: bottom + 40, 'text-anchor': 'middle', 'font-size': 11, fill: '#4a5878'}, 'wavelength (nm), violet to red');
    var list = lines.map(function(n){ return n.toFixed(1); }).join(', '), msg;
    if (mode === 'cont') msg = 'A hot solid or liquid glows with <b>every</b> colour at once: a smooth rainbow with no gaps. (Pick any element: this one never changes.)';
    else if (mode === 'emit') msg = '<b>' + cur + '</b> glowing as a hot thin gas shows <b>bright lines</b> at about <b>' + list + ' nm</b>, and nothing else.';
    else msg = 'The same <b>' + cur + '</b> as a cool gas in front of a glowing lamp takes out <b>exactly the same colours</b>: dark lines at <b>' + list + ' nm</b>.';
    if (cmpOn){
      var hit = lines.filter(function(nm){ return sunLines.indexOf(nm) !== -1; }).length;
      msg += '<br>Dashed gold lines: <b>' + hit + ' of ' + lines.length + '</b> sit on a dark line in the Sun.' +
        (hit === 0 ? ' Helium is not among the dark lines Fraunhofer and Kirchhoff mapped. It was found in 1868, glowing (see Chapter Eight).' : (hit === lines.length ? ' <b>' + cur + '</b> is in the Sun.' : ''));
    }
    document.getElementById('sp-out').innerHTML = msg;
    Array.prototype.forEach.call(elRow.children, function(b){ b.style.background = b.dataset.k === cur ? '#e8a90c' : '#fff8e6'; b.style.fontWeight = b.dataset.k === cur ? 'bold' : 'normal'; });
    Array.prototype.forEach.call(moRow.children, function(b){ b.style.background = b.dataset.k === mode ? '#e8a90c' : '#fff8e6'; b.style.fontWeight = b.dataset.k === mode ? 'bold' : 'normal'; });
  }
  Object.keys(EL).forEach(function(k){
    var b = document.createElement('button'); b.type = 'button'; b.dataset.k = k; b.textContent = k; b.setAttribute('style', BTN);
    b.addEventListener('click', function(){ cur = k; draw(); }); elRow.appendChild(b);
  });
  [['emit', 'Hot thin gas'], ['cont', 'Glowing solid'], ['abs', 'Cool gas in front']].forEach(function(p){
    var b = document.createElement('button'); b.type = 'button'; b.dataset.k = p[0]; b.textContent = p[1]; b.setAttribute('style', BTN);
    b.addEventListener('click', function(){ mode = p[0]; draw(); }); moRow.appendChild(b);
  });
  cmp.addEventListener('change', draw);
  draw();
})();
</script>""".replace("@@BTN@@", _BTN)

RULES = """<div class="bigidea"><b>Kirchhoff&rsquo;s three kinds of spectrum</b> (the rules, as people usually state them today):<br>
<b>1. Continuous.</b> A hot solid, a hot liquid or a hot dense gas glows with every colour: a smooth rainbow.<br>
<b>2. Emission lines.</b> A hot <i>thin</i> gas glows only at certain colours: bright lines on a dark background.<br>
<b>3. Absorption lines.</b> If a rainbow shines through a <i>cooler</i> thin gas, that gas takes out the same colours it would glow with: dark lines on the rainbow.</div>"""

# ---------------------------------------------------------------------------
# The story
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Static illustrations for Chapter Two (prism and Wollaston's slit)
# ---------------------------------------------------------------------------
_WL_STOPS = [(400, (139, 0, 255)), (440, (60, 70, 255)), (480, (0, 170, 255)), (510, (0, 210, 120)),
             (550, (120, 230, 40)), (575, (245, 225, 20)), (600, (255, 150, 0)), (640, (255, 40, 10)),
             (700, (170, 0, 0))]


def _wl_rgb(nm):
    """Rough display colour for a wavelength in nm (400 to 700)."""
    s = _WL_STOPS
    if nm <= s[0][0]:
        c = s[0][1]
    elif nm >= s[-1][0]:
        c = s[-1][1]
    else:
        for (a, ca), (b, cb) in zip(s, s[1:]):
            if a <= nm <= b:
                t = (nm - a) / float(b - a)
                c = tuple(round(ca[i] + (cb[i] - ca[i]) * t) for i in range(3))
                break
    return "#%02x%02x%02x" % c


def _prism_fig():
    """White sunlight enters a prism and fans out: red bends least, violet most."""
    cols = [_wl_rgb(nm) for nm in (680, 610, 578, 530, 480, 445, 410)]   # red ... violet
    ex, ey0, ey1 = (260.9, 270.3), 112, 134          # exit points on the right face
    o = ['<svg class="illus" width="480" height="230" viewBox="0 0 480 230" font-family="Georgia,serif" '
         'role="img" aria-label="A thin beam of white sunlight passes through a hole in a shutter, enters a '
         'triangular glass prism, and leaves as a fan of colours from red at the top to violet at the bottom: '
         'red is bent the least and violet the most">',
         '<rect width="480" height="230" fill="#0d1330" rx="10"/>',
         # shutter with hole
         '<rect x="22" y="40" width="10" height="70" fill="#5a4630"/>',
         '<rect x="22" y="122" width="10" height="70" fill="#5a4630"/>',
         '<text x="27" y="30" fill="#aebadf" font-size="11" text-anchor="middle">shutter</text>',
         '<text x="27" y="210" fill="#aebadf" font-size="11" text-anchor="middle">hole</text>',
         '<line x1="27" y1="196" x2="27" y2="120" stroke="#aebadf" stroke-width="1" stroke-dasharray="2 3"/>',
         # white beam in
         '<line x1="34" y1="116" x2="196" y2="120" stroke="#fffbe8" stroke-width="4"/>',
         '<text x="110" y="106" fill="#fffbe8" font-size="12" text-anchor="middle">white sunlight</text>']
    # inside the prism: a narrow wedge from the entry point
    for i, c in enumerate(cols):
        t = i / 6.0
        x = ex[0] + (ex[1] - ex[0]) * t
        y = ey0 + (ey1 - ey0) * t
        o.append('<line x1="196" y1="120" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6" opacity=".9"/>' % (x, y, c))
    # prism body on top of the inner rays, slightly transparent
    o.append('<polygon points="230,40 165,190 295,190" fill="#9fc6e8" fill-opacity=".18" stroke="#cfe3f5" stroke-width="2"/>')
    o.append('<text x="230" y="208" fill="#cfe3f5" font-size="12" text-anchor="middle">glass prism</text>')
    # the fan out to the screen
    for i, c in enumerate(cols):
        t = i / 6.0
        x = ex[0] + (ex[1] - ex[0]) * t
        y = ey0 + (ey1 - ey0) * t
        yend = 92 + 104 * t
        o.append('<line x1="%.1f" y1="%.1f" x2="432" y2="%.1f" stroke="%s" stroke-width="2.4"/>' % (x, y, yend, c))
        o.append('<rect x="432" y="%.1f" width="12" height="17.4" fill="%s"/>' % (yend - 8.7, c))
    o += ['<rect x="432" y="83" width="12" height="122" fill="none" stroke="#6f80b8" stroke-width="1"/>',
          '<text x="438" y="72" fill="#aebadf" font-size="11" text-anchor="middle">screen</text>',
          '<text x="360" y="86" fill="%s" font-size="12" text-anchor="middle">red bends least</text>' % '#ff7a6a',
          '<text x="350" y="214" fill="%s" font-size="12" text-anchor="middle">violet bends most</text>' % '#c39bff',
          '</svg>']
    return "\n".join(o)


def _slit_fig():
    """Round hole versus narrow slit: the slit gives each colour its own thin line, so the dark gaps show."""
    X0, W, LO, HI = 174, 270, 390, 700
    gaps = [397, 431, 486, 527, 589, 656, 687]          # seven strong solar lines (Fraunhofer's H, G, F, E, D, C, B)

    def X(nm):
        return X0 + W * (nm - LO) / float(HI - LO)

    o = ['<svg class="illus" width="480" height="250" viewBox="0 0 480 250" font-family="Georgia,serif" '
         'role="img" aria-label="Two spectra of sunlight compared. Top: light through a round hole makes a row of '
         'overlapping coloured circles, and the dark gaps are filled in by the neighbouring colours. Bottom: light '
         'through a narrow slit makes a row of thin coloured lines side by side, and seven thin dark lines can be '
         'seen crossing the band">',
         '<rect width="480" height="250" fill="#0d1330" rx="10"/>',
         '<defs><linearGradient id="wl-band" x1="0" x2="1" y1="0" y2="0">']
    for nm in range(400, 701, 20):
        o.append('<stop offset="%.3f" stop-color="%s"/>' % ((nm - LO) / float(HI - LO), _wl_rgb(nm)))
    o.append('</linearGradient></defs>')

    # ---- row 1: round hole
    o += ['<text x="20" y="24" fill="#ffd97a" font-size="13" font-weight="bold">Through a round hole</text>',
          '<rect x="40" y="44" width="46" height="62" fill="#5a4630" rx="3"/>',
          '<circle cx="63" cy="75" r="9" fill="#fffbe8"/>',
          '<line x1="94" y1="75" x2="132" y2="75" stroke="#fffbe8" stroke-width="2"/>',
          '<path d="M132 70 L141 75 L132 80 z" fill="#fffbe8"/>']
    for nm in range(392, 701, 6):
        if any(abs(nm - g) < 4 for g in gaps):
            continue                                   # a missing colour: its circle is simply absent
        o.append('<circle cx="%.1f" cy="75" r="22" fill="%s" fill-opacity=".38"/>' % (X(nm), _wl_rgb(nm)))
    o.append('<text x="245" y="120" fill="#aebadf" font-size="11" text-anchor="middle">'
             'each colour is a blurry circle; neighbours overlap and cover the gaps</text>')

    # ---- row 2: narrow slit
    o += ['<text x="20" y="150" fill="#ffd97a" font-size="13" font-weight="bold">Through a narrow slit (Wollaston, 1802)</text>',
          '<rect x="40" y="168" width="46" height="62" fill="#5a4630" rx="3"/>',
          '<rect x="61" y="174" width="4" height="50" fill="#fffbe8"/>',
          '<line x1="94" y1="199" x2="132" y2="199" stroke="#fffbe8" stroke-width="2"/>',
          '<path d="M132 194 L141 199 L132 204 z" fill="#fffbe8"/>',
          '<rect x="%d" y="176" width="%d" height="46" fill="url(#wl-band)"/>' % (X0, W)]
    for g in gaps:
        o.append('<line x1="%.1f" y1="176" x2="%.1f" y2="222" stroke="#05081a" stroke-width="2"/>' % (X(g), X(g)))
    o += ['<text x="245" y="240" fill="#aebadf" font-size="11" text-anchor="middle">'
          'each colour is its own thin line, so a missing colour leaves a dark line</text>',
          '</svg>']
    return "\n".join(o)


def _dline_fig():
    """The Sun's dark D pair sits exactly where a salted flame shows its bright yellow pair.
    The Sun strip also carries hydrogen's C line and magnesium's b group, which the flame lacks."""
    X0, W, LO, HI = 40, 400, 400, 700

    def X(nm):
        return X0 + W * (nm - LO) / float(HI - LO)

    d = X(589.3)
    pair = (d - 2.5, d + 2.5)                           # 589.0 and 589.6, spread out so the eye can see two
    b = X(517.5)
    bgrp = (b - 3, b, b + 3)                            # 516.7, 517.3, 518.4, spread out likewise
    c = X(656.3)
    o = ['<svg class="illus" width="480" height="264" viewBox="0 0 480 264" font-family="Georgia,serif" '
         'role="img" aria-label="Two spectra one above the other. Top: sunlight, a full rainbow crossed by dark '
         'lines: a group of three in the green from magnesium, a pair in the yellow from sodium, and a strong '
         'single line in the red from hydrogen. Bottom: a lamp flame with salt in it, black except for a bright '
         'yellow pair of lines. A dashed guide shows that the sodium pairs sit at exactly the same place, '
         '589 nanometres">',
         '<rect width="480" height="264" fill="#0d1330" rx="10"/>',
         '<defs><linearGradient id="wl-band-d" x1="0" x2="1" y1="0" y2="0">']
    for nm in range(400, 701, 20):
        o.append('<stop offset="%.3f" stop-color="%s"/>' % ((nm - LO) / float(HI - LO), _wl_rgb(nm)))
    o += ['</linearGradient></defs>',
          # Sun
          '<text x="%d" y="22" fill="#ffd97a" font-size="13" font-weight="bold">Sunlight</text>' % X0,
          '<text x="%d" y="22" fill="#aebadf" font-size="11" text-anchor="end">dark lines (Fraunhofer)</text>' % (X0 + W),
          '<rect x="%d" y="50" width="%d" height="50" fill="url(#wl-band-d)"/>' % (X0, W)]
    for x in bgrp:
        o.append('<line x1="%.1f" y1="50" x2="%.1f" y2="100" stroke="#05081a" stroke-width="1.6"/>' % (x, x))
    for x in pair:
        o.append('<line x1="%.1f" y1="50" x2="%.1f" y2="100" stroke="#05081a" stroke-width="2.2"/>' % (x, x))
    o.append('<line x1="%.1f" y1="50" x2="%.1f" y2="100" stroke="#05081a" stroke-width="3.2"/>' % (c, c))
    for x, letter, who in ((b, "b", "magnesium"), (d, "D", "sodium"), (c, "C", "hydrogen")):
        o.append('<text x="%.1f" y="38" fill="#fffbe8" font-size="11.5" text-anchor="middle">'
                 '<tspan font-weight="bold">%s</tspan> %s</text>' % (x, letter, who))
        o.append('<line x1="%.1f" y1="41" x2="%.1f" y2="48" stroke="#aebadf" stroke-width="1"/>' % (x, x))
    # flame
    o += ['<text x="%d" y="150" fill="#ffd97a" font-size="13" font-weight="bold">Lamp flame with salt in it</text>' % X0,
          '<text x="%d" y="150" fill="#aebadf" font-size="11" text-anchor="end">bright lines</text>' % (X0 + W),
          '<rect x="%d" y="160" width="%d" height="50" fill="#000" stroke="#3a4a86" stroke-width="1"/>' % (X0, W)]
    for x in pair:
        o.append('<line x1="%.1f" y1="160" x2="%.1f" y2="210" stroke="#ffe14d" stroke-width="2.4"/>' % (x, x))
    # guide
    o += ['<line x1="%.1f" y1="102" x2="%.1f" y2="158" stroke="#fffbe8" stroke-width="1.2" stroke-dasharray="4 4"/>' % (d, d),
          '<text x="%.1f" y="126" fill="#fffbe8" font-size="12">same place, 589 nm</text>' % (d + 10),
          '<text x="%d" y="228" fill="#aebadf" font-size="11" text-anchor="middle">400 nm</text>' % X0,
          '<text x="%d" y="228" fill="#aebadf" font-size="11" text-anchor="middle">700 nm</text>' % (X0 + W),
          '<text x="240" y="252" fill="#aebadf" font-size="11" text-anchor="middle">'
          'the D pair and the b group are drawn further apart than true scale</text>',
          '</svg>']
    return "\n".join(o)

def _theodolite_fig():
    """Fraunhofer's 1814 arrangement: slit in a shutter, prism before a theodolite's objective."""
    cols = [_wl_rgb(nm) for nm in (680, 610, 578, 530, 480, 445, 410)]
    o = ['<svg class="illus" width="480" height="250" viewBox="0 0 480 250" font-family="Georgia,serif" '
         'role="img" aria-label="Diagram of Fraunhofer\'s 1814 set-up. Sunlight comes through a narrow slit in a '
         'window shutter, travels several metres across a dark room to a flint-glass prism, and the spread-out '
         'colours enter a small telescope mounted on a divided circle, a theodolite, through which Fraunhofer '
         'looks and reads off the angle of each dark line">',
         '<rect width="480" height="250" fill="#0d1330" rx="10"/>',
         # shutter and slit
         '<rect x="22" y="40" width="10" height="66" fill="#5a4630"/>',
         '<rect x="22" y="110" width="10" height="70" fill="#5a4630"/>',
         '<text x="14" y="200" fill="#aebadf" font-size="11">slit in the</text>',
         '<text x="14" y="214" fill="#aebadf" font-size="11">window shutter</text>',
         '<text x="14" y="28" fill="#ffd97a" font-size="11">sunlight</text>',
         # beam with a break
         '<line x1="34" y1="108" x2="118" y2="108" stroke="#fffbe8" stroke-width="2.5"/>',
         '<line x1="132" y1="108" x2="226" y2="108" stroke="#fffbe8" stroke-width="2.5"/>',
         '<path d="M114 98 l8 20 M128 98 l8 20" stroke="#aebadf" stroke-width="1.4"/>',
         '<text x="125" y="90" fill="#aebadf" font-size="11" text-anchor="middle">several metres</text>',
         '<text x="125" y="134" fill="#aebadf" font-size="11" text-anchor="middle">of dark room</text>']
    # divided circle (drawn first so the telescope sits on top)
    cx, cy, r = 362, 151, 46
    o.append('<circle cx="%d" cy="%d" r="%d" fill="#16204a" stroke="#cfe3f5" stroke-width="1.5"/>' % (cx, cy, r))
    import math
    for k in range(0, 360, 10):
        a = math.radians(k)
        r2 = r - (7 if k % 30 == 0 else 4)
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#cfe3f5" stroke-width="1"/>'
                 % (cx + r * math.cos(a), cy + r * math.sin(a), cx + r2 * math.cos(a), cy + r2 * math.sin(a)))
    o.append('<line x1="%d" y1="%d" x2="%d" y2="232" stroke="#cfe3f5" stroke-width="3"/>' % (cx, cy + r, cx))
    o.append('<line x1="%d" y1="232" x2="%d" y2="232" stroke="#cfe3f5" stroke-width="3"/>' % (cx - 30, cx + 30))
    o.append('<text x="%d" y="246" fill="#aebadf" font-size="11" text-anchor="middle">divided circle: read the angle</text>' % cx)
    # colour fan from prism to objective
    for i, c in enumerate(cols):
        t = i / 6.0
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.8"/>'
                 % (262 + 3 * t, 114 + 6 * t, 298, 124 + 18 * t, c))
    # prism
    o.append('<polygon points="246,74 222,140 270,140" fill="#9fc6e8" fill-opacity=".2" stroke="#cfe3f5" stroke-width="2"/>')
    o.append('<text x="246" y="62" fill="#cfe3f5" font-size="11" text-anchor="middle">flint-glass prism</text>')
    # telescope, tilted to follow the bent light
    o.append('<g transform="rotate(16 300 133)">'
             '<rect x="300" y="122" width="130" height="22" rx="3" fill="#8a6a3a" stroke="#d9c9a3" stroke-width="1.5"/>'
             '<ellipse cx="301" cy="133" rx="4" ry="13" fill="#9fc6e8" stroke="#cfe3f5" stroke-width="1.5"/>'
             '<rect x="430" y="127" width="16" height="12" fill="#6a522c" stroke="#d9c9a3" stroke-width="1"/>'
             '</g>')
    o.append('<circle cx="%d" cy="%d" r="3.5" fill="#d9c9a3" stroke="#5a4630"/>' % (cx, cy))
    o.append('<text x="338" y="96" fill="#cfe3f5" font-size="11" text-anchor="middle">theodolite telescope</text>')
    o.append('<text x="300" y="168" fill="#aebadf" font-size="10" text-anchor="end">objective</text>')
    o.append('<text x="462" y="196" fill="#ffd97a" font-size="11" text-anchor="end">eye</text>')
    o.append('</svg>')
    return "\n".join(o)


def _kirchhoff_exp_fig():
    """Kirchhoff, October 1859: sunlight, then limelight, sent through a sodium flame."""
    X0, W, LO, HI = 178, 278, 400, 700

    def X(nm):
        return X0 + W * (nm - LO) / float(HI - LO)

    d = X(589.3)
    pair = (d - 2.2, d + 2.2)
    sun_other = [X(517.5) - 2.5, X(517.5), X(517.5) + 2.5, X(656.3)]
    o = ['<svg class="illus" width="480" height="330" viewBox="0 0 480 330" font-family="Georgia,serif" '
         'role="img" aria-label="Kirchhoff\'s two experiments of October 1859. Top: sunlight alone shows a dark D '
         'pair; sunlight sent through a sodium flame shows the D pair darker and sharper. Bottom: light from '
         'glowing lime alone is a smooth rainbow with no dark lines; sent through a sodium flame, a dark pair '
         'appears exactly at the D position">',
         '<rect width="480" height="330" fill="#0d1330" rx="10"/>',
         '<defs><linearGradient id="wl-band-k" x1="0" x2="1" y1="0" y2="0">']
    for nm in range(400, 701, 20):
        o.append('<stop offset="%.3f" stop-color="%s"/>' % ((nm - LO) / float(HI - LO), _wl_rgb(nm)))
    o += ['</linearGradient>',
          '<radialGradient id="lime-glow"><stop offset="0" stop-color="#fffbe8"/>'
          '<stop offset=".5" stop-color="#fff2b0" stop-opacity=".6"/><stop offset="1" stop-color="#fff2b0" stop-opacity="0"/></radialGradient>',
          '</defs>']

    def flame(x, y):
        return ['<rect x="%d" y="%d" width="8" height="22" fill="#8a8f9a"/>' % (x - 4, y + 14),
                '<path d="M%d %d C%d %d %d %d %d %d C%d %d %d %d %d %d z" fill="#ffd23a" fill-opacity=".85"/>'
                % (x, y - 22, x + 12, y - 4, x + 9, y + 14, x, y + 14, x - 9, y + 14, x - 12, y - 4, x, y - 22),
                '<path d="M%d %d C%d %d %d %d %d %d C%d %d %d %d %d %d z" fill="#fff4a0"/>'
                % (x, y - 8, x + 5, y + 2, x + 4, y + 12, x, y + 12, x - 4, y + 12, x - 5, y + 2, x, y - 8),
                '<text x="%d" y="%d" fill="#aebadf" font-size="10" text-anchor="middle">sodium flame</text>' % (x, y + 50)]

    def prism(x, y):
        return ['<polygon points="%d,%d %d,%d %d,%d" fill="#9fc6e8" fill-opacity=".2" stroke="#cfe3f5" stroke-width="1.5"/>'
                % (x, y - 16, x - 12, y + 12, x + 12, y + 12),
                '<text x="%d" y="%d" fill="#aebadf" font-size="10" text-anchor="middle">prism</text>' % (x, y + 50)]

    def strip(y, label, sun, dstyle):
        out = ['<text x="%d" y="%d" fill="#fffbe8" font-size="11">%s</text>' % (X0, y - 5, label),
               '<rect x="%d" y="%d" width="%d" height="30" fill="url(#wl-band-k)"/>' % (X0, y, W)]
        if sun:
            for x in sun_other:
                out.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#05081a" stroke-width="1.5" opacity=".75"/>' % (x, y, x, y + 30))
        if dstyle:
            w, op = dstyle
            for x in pair:
                out.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#05081a" stroke-width="%s" opacity="%s"/>' % (x, y, x, y + 30, w, op))
        return out

    # ---- row 1: the Sun
    o.append('<text x="18" y="24" fill="#ffd97a" font-size="13" font-weight="bold">1 &#183; Sunlight through a sodium flame</text>')
    o += ['<circle cx="34" cy="92" r="14" fill="#ffd23a"/>',
          '<text x="34" y="142" fill="#aebadf" font-size="10" text-anchor="middle">Sun</text>',
          '<line x1="50" y1="92" x2="136" y2="92" stroke="#fffbe8" stroke-width="2" opacity=".8"/>']
    o += flame(88, 92) + prism(140, 92)
    o += strip(52, "Sun alone", True, (1.4, .7))
    o += strip(110, "Sun through the flame: D darker and sharper", True, (2.6, 1))
    o.append('<line x1="18" y1="166" x2="462" y2="166" stroke="#3a4a86" stroke-width="1"/>')
    # ---- row 2: limelight
    o.append('<text x="18" y="190" fill="#ffd97a" font-size="13" font-weight="bold">2 &#183; Limelight through a sodium flame</text>')
    o += ['<circle cx="34" cy="258" r="20" fill="url(#lime-glow)"/>',
          '<rect x="28" y="252" width="12" height="12" fill="#fffbe8" rx="2"/>',
          '<text x="34" y="308" fill="#aebadf" font-size="10" text-anchor="middle">hot lime</text>',
          '<line x1="50" y1="258" x2="136" y2="258" stroke="#fffbe8" stroke-width="2" opacity=".8"/>']
    o += flame(88, 258) + prism(140, 258)
    o += strip(218, "Limelight alone: no dark lines at all", False, None)
    o += strip(276, "Through the flame: a dark D pair appears", False, (2.6, 1))
    o += ['<text x="%.1f" y="321" fill="#ffd97a" font-size="11" text-anchor="middle">D, made in the lab</text>' % d,
          '</svg>']
    return "\n".join(o)


PRISM_FIG = _prism_fig()
SLIT_FIG = _slit_fig()
DLINE_FIG = _dline_fig()
THEO_FIG = _theodolite_fig()
KEXP_FIG = _kirchhoff_exp_fig()


KIRCHHOFF = dict(
    title="The Dark Lines in the Rainbow: Fraunhofer, Kirchhoff and Bunsen",
    h1="✦ The Dark Lines in the Rainbow ✦",
    sub="How a glassmaker's puzzle and a flame in Heidelberg showed what the Sun is made of",
    footer="Every date is checked · every quote is labeled with where it comes from<br>(the Sun is still 150 million kilometres away, and we still know what is in it)",
    praise=["Well matched, {name}!", "Bright line, dark line, same place, {name}!", "Kirchhoff would nod, {name}!",
            "Right on the D line, {name}!", "Spectroscopist's eyes, {name}!"],
    cert_org="The Heidelberg Society of Spectral Analysis",
    cert_of="the tale of the Sun's dark lines",
    cert_rank="Reader of Starlight",
    finale_title="A Message Written in Light",
    finale_html="""
<p>Think about how strange the achievement is. In 1835, a famous philosopher said that people would never learn what the stars are made of. Twenty-four years later, two professors in a small German university town put a salt in a flame, looked through a prism, and read the answer off a ruler. They did not go to the Sun. They did not need a sample. They only needed to learn how to read the light that was already arriving.</p>
<p>The key was a pair of facts that had been sitting side by side for decades. A glowing gas gives out certain colours. A cool gas takes the same colours away. Fraunhofer had measured the dark lines. Foucault had seen the dark and bright lines trade places. Kirchhoff saw why, and Bunsen saw at once what it meant.</p>
<p>Almost at once the method began to pay off. Hydrogen turned out to be all through the Sun. Two new elements, caesium and rubidium, were spotted in a flame before anyone had a pure sample. And helium was found in the Sun 27 years before anyone found it on Earth. In 1925 a 25-year-old astronomer named Cecilia Payne used the same lines to show that the Sun and the stars are made mostly of hydrogen and helium. Today astronomers read the colour barcodes of galaxies, the air of planets around other stars, and the speed at which distant galaxies are flying away.</p>
<p>It all grew from one habit: look closely at a small thing nobody explains, and keep measuring until it does. Those dark lines in the rainbow were there for anyone to see, ever since Newton&rsquo;s prism. They were waiting for someone to ask why.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>&#9312; A prism spreads sunlight into a <b>spectrum</b>. Each colour is a different <b>wavelength</b>, measured in nanometres (billionths of a metre): violet is about 400, red about 700.</p>
<p>&#9313; The Sun's spectrum is crossed by hundreds of dark lines. <b>Wollaston</b> saw a few in 1802. <b>Fraunhofer</b> mapped 574 of them in 1814 and used them as measuring marks.</p>
<p>&#9314; Every element, heated until it glows, gives out its own bright lines, a <b>fingerprint</b> that no other element shares.</p>
<p>&#9315; In 1859 <b>Kirchhoff</b> showed that a cool gas absorbs the same colours it gives out when hot. So the Sun's dark lines are <b>elements in its cooler outer layers</b>.</p>
<p>&#9316; Kirchhoff and Bunsen found <b>caesium</b> and <b>rubidium</b> by their lines. <b>Helium</b> was found in the Sun in 1868 and on Earth in 1895.</p>
<p>&#9317; Balmer found a formula for hydrogen's lines in 1885. Bohr explained why it works in 1913: electrons jump between fixed energy levels.</p>
</div>""",
    chapters=[
        # ------------------------------------------------------------------ 1
        dict(
            kicker="Chapter One · Paris · 1835",
            title="The Thing We Will Never Know",
            html="""
<p>In <b>1835</b> the French philosopher <b>Auguste Comte</b> published a long book on how knowledge works. In it he gave an example of a question that science would never answer. He wrote that we could imagine finding the <b>shapes</b>, <b>distances</b>, <b>sizes</b> and <b>motions</b> of the stars, but that we could never, by any means, study their <b>chemical make-up</b>. (That is a paraphrase of his French; he said it flatly and he meant it.)</p>
<p>It was a reasonable thing to think. To find out what something is made of, a chemist needs a <b>sample</b>: a pinch to heat, to dissolve, to weigh. Nobody could fetch a pinch of the Sun. Even the nearest star is trillions of kilometres away. The Sun itself is about <b>150 million kilometres</b> from Earth. Light, the fastest thing there is, travels about <b>300,000 kilometres every second</b>, and still takes a good while to make the trip.</p>
<p>Comte had missed one thing. The Sun may be out of reach, but its <b>light</b> is not. Light comes all the way from the Sun to your window. Every ray that arrives has been through the Sun&rsquo;s outer layers on its way out, and it might carry some record of what it passed through. All anyone needed was a way to read it.</p>
<p>The way to read light had been around for nearly two hundred years. In 1666 a young <b>Isaac Newton</b>, home from Cambridge during the plague, had let a thin beam of sunlight through a hole in a shutter and through a glass prism, and found that it fanned out into a band of colours. (If you have done the Newton lesson, you were there.) The story of this lesson begins with that band of colours, and with a few thin dark lines that nobody could explain.</p>
<div class="bigidea">🌟 <b>Big Idea #1:</b> Sometimes the thing you are told you can never know is only hard to reach. If a message is arriving anyway, ask what it might be carrying, and how you could read it.</div>""",
            cps=[dict(
                type="num",
                kicker="Why the Sun is out of reach",
                q="""The Sun is about <b>150,000,000 km</b> away. Light travels about <b>300,000 km every second</b>. How many <b>seconds</b> does sunlight take to reach Earth?""",
                answers=[500], unit="seconds",
                hint="Divide the distance by the speed: 150,000,000 &#247; 300,000. (Cancel five zeros first: 1,500 &#247; 3.) That is 8 minutes and 20 seconds.",
            )],
        ),
        # ------------------------------------------------------------------ 2
        dict(
            kicker="Chapter Two · From Newton to a London Doctor · 1666 to 1802",
            title="Splitting the Light",
            html="""
<p>Newton&rsquo;s discovery was that white sunlight is not a pure thing. It is a <b>mixture</b> of all the colours, and a prism pulls them apart because it bends some colours more than others: violet the most, red the least. The result is a fan of colour from red through orange, yellow, green and blue to violet. In a paper of 1672 he called the band a <b>spectrum</b>, from a Latin word that means an &ldquo;appearance&rdquo; (the same root gives us <i>spectre</i>, a ghost).</p>
""" + PRISM_FIG + """
<p>By the early 1800s, scientists understood that light behaves like a <b>wave</b>, and that each colour is a different <b>wavelength</b>: the distance from one crest to the next. Wavelengths of light are tiny. They are measured in <b>nanometres</b> (nm): one nanometre is a <b>billionth of a metre</b>. Red light is about <b>700 nm</b> long and violet about <b>400 nm</b>. For comparison, a human hair is about <b>80,000 nm</b> wide.</p>
<p>In <b>1802</b>, an English doctor and chemist named <b>William Hyde Wollaston</b> tried something new. Instead of a round hole, he let the sunlight in through a very <b>narrow slit</b>, and then looked at it through a prism. The colours came out much sharper, and to his surprise he saw a few thin <b>dark lines</b> crossing the rainbow, like gaps in a comb. He counted about seven.</p>
<p>Wollaston guessed that the lines marked the natural <b>borders between colours</b>, and he did not look further. He was wrong about that, but he was the first person to see them. Nobody knew what the lines were. Hardly anyone noticed.</p>
<div class="funfact">🔎 Why a slit? A round hole makes a smeared stack of overlapping coloured circles. A thin slit makes a thin line of light, and each colour lands in its own thin line, side by side. A sharp line can be noticed at a very exact position, and that is what turned out to matter.</div>
""" + SLIT_FIG,
            cps=[dict(
                type="num",
                kicker="How small is a wavelength?",
                q="""A human hair is about <b>80,000 nm</b> wide. Light of wavelength <b>500 nm</b> (green) has crests <b>500 nm</b> apart. About how many green wavelengths fit across the width of one hair?""",
                answers=[160], unit="wavelengths",
                hint="Divide: 80,000 &#247; 500. (Cancel two zeros first: 800 &#247; 5.)",
            )],
        ),
        # ------------------------------------------------------------------ 3
        dict(
            kicker="Chapter Three · Munich and Benediktbeuern · 1801 to 1826",
            title="The Orphan Who Counted the Lines",
            html="""
<p>The man who really put the lines on the map was a glassmaker. <b>Joseph Fraunhofer</b> was born in <b>1787</b> in the Bavarian town of Straubing, the youngest of eleven children of a glazier. Both parents died when he was <b>eleven</b>. He was sent to Munich to work as an apprentice to a mirror-maker and glass-cutter, a master who, the tellers say, was harsh and did not let him go to school.</p>
<p>In <b>July 1801</b>, when Joseph was fourteen, the house where he worked <b>collapsed</b> with him inside. He was dug out of the rubble after hours. The ruler of Bavaria, Prince-Elector <b>Maximilian Joseph</b>, was at the scene, and (the story goes) he gave the boy a gift of money, about 18 ducats. Fraunhofer spent it on books and a glass-cutting machine. A few years later an optical firm in the abbey of <b>Benediktbeuern</b> took him on, and within a few years he was running its glassworks. He was a self-taught genius at making lenses.</p>
<p>His problem was colour. In the telescopes of the time, a lens bent the different colours by different amounts, so every star came with a coloured fringe, like a faint rainbow. Opticians call this fault <b>chromatic aberration</b>. The cure is an <b>achromatic</b> lens, which pairs two kinds of glass, <b>crown</b> and <b>flint</b>, so that their colour errors cancel. To design one, a lens-maker has to know <b>exactly</b> how much each kind of glass bends each colour. But &ldquo;red&rdquo; and &ldquo;yellow&rdquo; are vague words. He needed one precise, repeatable colour to measure with.</p>
<p>He found one in a lamp flame. When he looked at the flame through a prism, there was a bright <b>yellow line</b> that was always in exactly the same place. Next he turned the prism toward the <b>Sun</b>, hoping to find the same line there. Instead, at <b>exactly the same place</b>, he found a thin <b>dark</b> line. And in the rest of the rainbow there were hundreds more.</p>
<p>His instrument was not a special machine. It was a <b>theodolite</b>, a surveyor&rsquo;s telescope mounted on a finely <b>divided circle</b>, so that the angle it pointed at could be read to a tiny fraction of a degree. In a darkened room he let sunlight in through a <b>narrow slit</b> in the window shutter, several metres away. In front of the telescope&rsquo;s <b>objective</b> (the big lens at the front) he set a prism of his own flint glass, turned to the angle of <b>minimum deviation</b>, where the colours come out sharpest. Then he swung the telescope slowly across the spectrum and read off the angle of each dark line from the circle.</p>
""" + THEO_FIG + """
<p>In <b>1814</b> Fraunhofer carefully mapped <b>574</b> dark lines. He gave the strongest ones capital letters, working from the red end: <b>A, B, C, D, E, F, G, H</b>. The dark pair he labelled <b>D</b> was where the lamp flame&rsquo;s bright line lay. Look at his own drawing from 1817 in the margin: the dark line D stands out like a pencil stroke in the yellow.</p>
<p>Fraunhofer tested whether the lines could be a trick of the prism or of Earth&rsquo;s air. He pointed his instrument at <b>moonlight</b> and at the <b>planets</b>, which only shine by reflecting sunlight, and found the same lines. For the stars he fixed a prism over the objective of a telescope, so that each star became a tiny spectrum in the eyepiece. Astronomers still call this an <b>objective prism</b>. But the light of bright <b>stars</b> showed different patterns of lines. So the lines were not made by the prism or the atmosphere. They belonged to each light source itself. In 1821 he built a <b>diffraction grating</b>: hundreds of fine wires stretched side by side, evenly spaced, a fraction of a millimetre apart. Light passing through the gaps <b>interferes</b> with itself, and each colour comes out at its own angle. Because he knew the spacing of the wires, the angle told him the <b>wavelength</b>. Later he ruled even finer gratings with a diamond on glass. The D line came out at about <b>589 nm</b>.</p>
<p>Fraunhofer died in <b>1826</b>, aged only <b>39</b>. Years of breathing the fumes of the glassworks probably played a part. On his grave in Munich are written the Latin words <i>Approximavit sidera</i>: &ldquo;He brought the stars closer.&rdquo; He knew the lines were important. He never found out why they were there.</p>""",
            cps=[dict(
                type="num",
                kicker="Counting the lines",
                q="""Wollaston saw about <b>7</b> dark lines in 1802. In 1814 Fraunhofer mapped <b>574</b>. How many <b>times as many</b> lines did Fraunhofer find?""",
                answers=[82], unit="times",
                hint="Divide: 574 &#247; 7. Try 7 &times; 80 = 560, and see how much is left over.",
            )],
        ),
        # ------------------------------------------------------------------ 4
        dict(
            kicker="Chapter Four · Paris and Sweden · 1814 to 1859",
            title="Forty-Five Years of Not Knowing",
            html="""
<p>After Fraunhofer, the puzzle sat there. People <b>suspected</b> that the lines were a message of some sort. Nobody could read it.</p>
<p>The clue was the <b>coincidence of position</b>. Why should a dark line in sunlight be at <b>exactly the same place</b> as the bright line from a lamp flame? Salt put in a flame (which turns the flame yellow) is a compound of the metal <b>sodium</b>. So perhaps sodium was involved. But how could the same stuff make a bright line here and a dark line there?</p>
""" + DLINE_FIG + """
<p>In <b>1849</b> in Paris, a young physicist named <b>L&eacute;on Foucault</b> (later famous for his pendulum, which proved the Earth turns) came very close to the answer. He used a strong electric <b>arc lamp</b>, a glowing spark between two carbon rods. The arc showed the bright yellow D pair. Then he shone <b>sunlight</b> straight through the arc into his prism. Now the D pair in the sunlight got <b>darker</b> than before. The arc, which could <b>give out</b> the D colours, was also <b>soaking them up</b> from the sunlight passing through it.</p>
<p>It was a remarkable observation. Foucault wrote it up in a short note and moved on to other things, and nobody built on it. In 1853 the Swedish physicist <b>Anders &Aring;ngstr&ouml;m</b> suggested in print that a glowing gas gives out just the colours it can absorb. That idea, too, was set aside.</p>
<p>Others had other pieces. In 1826 the English photography pioneer <b>William Henry Fox Talbot</b> noticed that different salts gave different coloured flames, and suggested that a prism might be used to tell the substances apart. But nobody had put these pieces together, or measured carefully enough to be sure. The dark lines of the Sun and the bright lines of the flame remained two puzzles, not one.</p>
<div class="funfact">🔎 This is a common pattern in science. Sometimes the evidence lies about for years, in pieces, in different heads. What is missing is not data. It is someone who has the time, the instruments and the nerve to pull the pieces together and say: <i>these are the same thing</i>.</div>""",
            cps=[dict(
                type="num",
                kicker="A long wait",
                q="""Fraunhofer mapped the dark lines in <b>1814</b>. The explanation came in <b>1859</b>. How many <b>years</b> did the lines sit unexplained?""",
                answers=[45], unit="years",
                hint="Subtract: 1859 &#8722; 1814.",
            )],
        ),
        # ------------------------------------------------------------------ 5
        dict(
            kicker="Chapter Five · Heidelberg, Germany · 1859",
            title="A Burner, a Prism, and Two Professors",
            html="""
<p>The answer came from the university town of <b>Heidelberg</b>, from two very different men. <b>Robert Bunsen</b>, born in 1811, was a chemist. He was known for doing dangerous experiments (an explosion in his twenties cost him the sight of one eye) and for a gas burner, built with the help of a workshop technician named Peter Desaga, which gave a very hot, nearly <b>colourless flame</b>. <b>Gustav Kirchhoff</b>, born in 1824, thirteen years younger, was a physicist and a brilliant mathematician.</p>
<p>Bunsen used his burner to identify chemicals by <b>flame colour</b>. Put a pinch of sodium salt in the flame and it burns yellow. Potassium gives a pale violet. Lithium and strontium both give a red. That last pair was the trouble: the two reds looked so alike that Bunsen could not tell them apart by eye, especially in a mixture.</p>
<p>Kirchhoff made a suggestion: <b>look at the flame through a prism</b>. Perhaps what looked like one colour to the eye would turn out to be made of separate thin lines. They built a simple instrument: a slit to let the flame&rsquo;s light in, a prism to spread it out, and a small telescope to look at the result. (You can see their drawing in the margin.)</p>
<p>It worked beautifully. Each element, in the flame, gave its own <b>pattern of bright lines</b>, at its own fixed colours. Sodium gave the familiar yellow pair. Lithium gave a red line and a faint orange one. Strontium gave a blue line. The two &ldquo;similar&rdquo; reds were now <b>completely different</b> when spread by the prism. Bunsen and Kirchhoff called the method <b>spectral analysis</b>. Each element had a <b>fingerprint of light</b> that no other element shared.</p>
<p>The method was astonishingly sensitive. By Bunsen&rsquo;s own figures it could detect less than a <b>three-millionth of a milligram</b> of sodium. Reportedly, the sodium line flickered into view whenever somebody dusted a book at the far end of the room, because sodium dust floats everywhere.</p>
<p>And now try it yourself. Here are four elements&rsquo; fingerprints. A mystery flame has been put through the spectroscope.</p>""",
            cps=[dict(
                type="num",
                kicker="Reading a fingerprint",
                q="""A mystery flame shows bright lines at <b>460.7, 589.0, 589.6 and 670.8 nm</b>. Use the reference table. How many <b>different elements</b> are in the flame?""",
                figure=_cp_table(),
                answers=[3], unit="elements",
                hint="Match each line to the table. Notice that the two lines at 589.0 and 589.6 belong to the <i>same</i> element. Count the elements, not the lines.",
            )],
        ),
        # ------------------------------------------------------------------ 6
        dict(
            kicker="Chapter Six · Heidelberg · October 1859",
            title="The Experiment That Connected Everything",
            html="""
<p>Kirchhoff was now thinking about Fraunhofer&rsquo;s D line. If sodium in a flame gave a <b>bright</b> pair of lines at exactly the position of the Sun&rsquo;s <b>dark</b> pair, there had to be a connection. In <b>October 1859</b> he tried an experiment much like Foucault&rsquo;s of ten years before, but carried it through with care.</p>
<p>First he let <b>sunlight</b> go through a flame with sodium in it, and then into his spectroscope. He expected that the flame&rsquo;s bright D lines would <b>fill in</b> the dark D lines of the Sun, at least a bit. Instead, the dark lines became <b>darker and sharper</b>.</p>
<p>Next he replaced the Sun with an artificial source, a glowing lump of heated lime, which gives a smooth rainbow with <b>no</b> dark lines at all. He sent that light through the sodium flame, and a pair of <b>dark</b> lines appeared in the rainbow, right at the D position. He had <b>manufactured Fraunhofer&rsquo;s D lines</b> in the laboratory.</p>
""" + KEXP_FIG + """
<p>The conclusion followed. Sodium vapour that <b>gives out</b> yellow light at those two colours when hot will also <b>take in</b> light of those same two colours that pass through it. And the Sun&rsquo;s dark D lines must therefore be caused by <b>sodium in the Sun&rsquo;s atmosphere</b>: a layer of cooler gas above a hotter, glowing body, soaking up its own colours from the light that comes from below. The Sun was not a solid chunk of one thing. It had a surface hot enough to glow with every colour, and above it a layer of cooler gases. Each gas in that layer absorbs its own set of colours, so each one leaves its own pattern of dark lines across the spectrum.</p>
<p>Bunsen understood at once. In a letter to a friend in November 1859 he wrote that Kirchhoff had made a wonderful, quite unexpected discovery, finding the cause of the dark lines in the solar spectrum, and that now the way was open to determine the make-up of the Sun and the fixed stars with the <b>same certainty</b> with which a chemist tests for sulphuric acid or chlorine in the lab. (This is a close paraphrase of his letter to Henry Roscoe.) Comte&rsquo;s impossible question had been answered 24 years after it was called impossible.</p>
""" + RULES + """
<p>There is a catch that makes the picture more interesting: whether the lines look bright or dark depends on <b>how bright the background is compared with the gas</b>. Try the sodium flame yourself. The flame glows at a brightness of 50 and soaks up 60% of whatever light passes through it. Slide the lamp behind it from dim to bright.</p>
""" + REVERSAL + """
<p>At the point where the lamp is exactly as bright as the flame, the lines vanish. Brighter lamp, dark lines. Dimmer lamp, bright lines. For the Sun, the glowing surface is <b>hotter</b> than the gas above it, so the lines come out dark. This also tells us something: the gas above the Sun&rsquo;s surface must be <b>cooler</b> than the surface below.</p>
<p>Now try all three kinds of spectrum for six elements, and compare each with the Sun.</p>
""" + SPECTRA,
            cps=[dict(
                type="num",
                kicker="Kirchhoff&rsquo;s reversal, by numbers",
                q="""A lamp behind the sodium flame has brightness <b>80</b>. The flame has brightness <b>50</b> and soaks up <b>60%</b> (0.6) of the light behind it, so it lets through 0.4 of it. The brightness of the D line is <b>80 &times; 0.4 + 0.6 &times; 50</b>. What is it?""",
                answers=[62], unit="",
                hint="80 &times; 0.4 = 32 and 0.6 &times; 50 = 30. Add them: 32 + 30. Compare with the background of 80: is the line brighter or darker?",
            ), dict(
                type="mc",
                kicker="Bright line or dark line?",
                q="""Same flame (brightness 50, soaks up 60%), but now the lamp behind it is dim, only <b>30</b>. The D line has brightness 30 &times; 0.4 + 0.6 &times; 50. How would the lines appear?""",
                mc=[("Darker than the background: 12", False),
                    ("Brighter than the background: 42", True),
                    ("No change: 30", False)],
                good="Right, {name}. 12 + 30 = 42, which is more than the background of 30, so the flame shows as a bright line. A dim background with a hotter, glowing gas in front gives bright lines. The Sun is the other way round.",
                bad="Work it out, {name}: 30 &times; 0.4 = 12 and 0.6 &times; 50 = 30, so the line is 12 + 30. Compare that total with the background of 30.",
            )],
        ),
        # ------------------------------------------------------------------ 7
        dict(
            kicker="Chapter Seven · Heidelberg · 1860 to 1862",
            title="Reading the Sun, Finding New Elements",
            html="""
<p>Kirchhoff set out to read the Sun systematically. He drew a huge, careful <b>map of the solar spectrum</b>, with thousands of dark lines, to compare, line by line, with the bright lines of the elements. For <b>iron</b>, which has a great many lines, he found that more than sixty bright lines in the lab lay exactly on dark lines in the Sun. The chances of this happening by luck were absurdly small. By 1860 he had named <b>sodium, iron, calcium, magnesium, nickel and chromium</b> as elements of the Sun, and he suspected a few more.</p>
<p>A few years later, <b>hydrogen</b> was found too. The bright lines of hydrogen in a lab tube lie at <b>656.3 nm</b> (red) and <b>486.1 nm</b> (blue-green). They matched Fraunhofer&rsquo;s dark lines <b>C</b> and <b>F</b>. Hydrogen, the simplest element, was in the Sun.</p>
<p>The same flame method worked for finding <b>new</b> elements. A chemist who sees a line that matches <b>no known element</b> knows there is something new in the sample. In 1860 Bunsen and Kirchhoff boiled down tens of thousands of litres of water from a mineral spring at D&uuml;rkheim, not far from Heidelberg, and examined what was left. In the spectrum of the residue they saw two bright <b>blue</b> lines that belonged to nothing known. They named the new element <b>caesium</b>, from the Latin <i>caesius</i>, &ldquo;sky blue&rdquo;. The lines lie at <b>455.5 nm</b> and <b>459.3 nm</b>. The next year, in a mineral called lepidolite, they saw two deep <b>red</b> lines and named another new element <b>rubidium</b>, from the Latin <i>rubidus</i>, &ldquo;deep red&rdquo;.</p>
<p>It was a remarkable moment for science. For the first time, chemists could say that an element was there before they had ever held a pinch of it. And the Sun and a mineral spring could be analysed by the same method.</p>
<div class="funfact">🔎 The photograph in the margin shows the two professors with their former student <b>Henry Roscoe</b> in 1862. Roscoe later became a professor in Manchester and helped to bring spectral analysis to Britain. It was Roscoe who kept Bunsen&rsquo;s letters and told much of this story.</div>""",
            cps=[dict(
                type="num",
                kicker="Caesium&rsquo;s two blue lines",
                q="""Caesium&rsquo;s two bright blue lines lie at <b>455.5 nm</b> and <b>459.3 nm</b>. How many <b>nanometres apart</b> are they?""",
                answers=[3.8], unit="nm",
                hint="Subtract: 459.3 &#8722; 455.5. (Line them up by decimal point: 459.3 &#8722; 455.5 = 3.8.)",
            )],
        ),
        # ------------------------------------------------------------------ 8
        dict(
            kicker="Chapter Eight · India and England · 1868",
            title="The Element Found in the Sun",
            html="""
<p>The next triumph was the strangest. On <b>18 August 1868</b> there was a total eclipse of the Sun visible from India. The French astronomer <b>Pierre Janssen</b> went to the town of Guntur, and aimed a spectroscope at the red flames of glowing gas that leap from the Sun&rsquo;s edge, the <b>prominences</b>. Their light was not a rainbow. It was a few <b>bright lines</b>: the signature of a hot, thin, glowing gas. By Kirchhoff&rsquo;s rule, that is exactly what such a gas should give. Among the lines was a <b>bright yellow one</b>.</p>
<p>Janssen realised that lines this bright could be seen <b>without an eclipse</b>, if the spectroscope was set up carefully. He tried the next day, in full daylight, and saw them. Two months later, an English astronomer, <b>Norman Lockyer</b>, who had been working on the same idea, saw the same yellow line from England in October. The two reports reached Paris within days of each other.</p>
<p>The yellow line was close to Fraunhofer&rsquo;s <b>D</b>, but not at the same place. It lay at <b>587.6 nm</b>, while the sodium D lines are at 589.0 and 589.6 nm. So it was not sodium. Lockyer compared it to every known element. It matched <b>nothing</b>. He and the chemist Edward Frankland concluded that it was a new element, and named it <b>helium</b>, from <i>helios</i>, the Greek word for the Sun. (The &ldquo;-ium&rdquo; ending is the way metals were named. They assumed it would be one.)</p>
<p>Many scientists did not believe it. An element that had been found in the Sun, and had never been seen on Earth? It sounded like a mistake. For years helium stayed in doubt. Then in <b>1895</b> the Scottish chemist <b>William Ramsay</b> treated a uranium mineral called cleveite with acid and collected a gas that came off. When he put it in a spectroscope, there it was: a bright yellow line at <b>587.6 nm</b>. Helium was on Earth after all. It had been found in the Sun first.</p>
<p>Today we know that helium is the <b>second most common element in the universe</b>, after hydrogen. It fills the stars, and it gave us the first sign that the dark lines could do more than confirm what we knew. They could point to something new.</p>""",
            cps=[dict(
                type="num",
                kicker="First in the Sun, then on Earth",
                q="""Helium was spotted in the Sun in <b>1868</b> and found on Earth in <b>1895</b>. How many <b>years later</b> was it found on Earth?""",
                answers=[27], unit="years",
                hint="Subtract: 1895 &#8722; 1868.",
            )],
        ),
        # ------------------------------------------------------------------ 9
        dict(
            kicker="Chapter Nine · Basel and Copenhagen · 1885 to 1913",
            title="The Rule Behind the Lines",
            html="""
<p>One big question was left: <b>why</b>? Why does each element have its own set of lines, and why does a gas take out the very colours it gives out?</p>
<p>The first clue came from a most unexpected person. <b>Johann Balmer</b> was a Swiss mathematics teacher at a girls&rsquo; school in Basel. In <b>1885</b>, at the age of 60, he looked at the four known visible lines of hydrogen, at 656.3, 486.1, 434.0 and 410.2 nm, and wondered whether numbers like those could follow a pattern. They did. He found a simple formula:</p>
<div class="bigidea"><b>wavelength = 364.6 nm &times; n&#178; &#247; (n&#178; &#8722; 4)</b><br>for n = 3, 4, 5, 6, ...<br>With n = 3, you get the red line. With n = 4, the blue-green. And so on.</div>
<p>Balmer had no idea why it worked. He had found a <b>rule</b> without a reason. Hydrogen&rsquo;s lines were not a random scatter. They followed a pattern, and the pattern had to mean something about the atom inside.</p>
<p>In <b>1913</b> the Danish physicist <b>Niels Bohr</b> supplied the reason. In his picture of the atom, an electron can only sit at certain fixed energy levels, like standing on the steps of a staircase, never between steps. When an electron drops from a higher step to a lower one, the atom gives out a little packet of light with an exact colour, which is an <b>emission line</b>. When light of exactly that colour passes by, an electron can <b>absorb</b> it and jump up the same step, which is an <b>absorption line</b>. Same steps, same colours, up or down. That is what Kirchhoff had found in the flame in 1859.</p>
<p>In <b>1925</b>, a 25-year-old astronomer called <b>Cecilia Payne</b>, using what had been learned about lines and atoms, worked out how much of each element is in the Sun and found that it is made mostly of <b>hydrogen and helium</b>, which astronomers had not expected. And the lines in starlight can do more: when a star moves toward us or away from us, its lines shift slightly in colour, and that shift measures how fast it moves. The dark lines in the rainbow became one of the most useful tools in all of astronomy.</p>""",
            cps=[dict(
                type="num",
                kicker="Balmer&rsquo;s formula",
                q="""Use Balmer&rsquo;s formula with <b>n = 3</b>: wavelength = 364.6 &times; 9 &#247; 5 (since 3&#178; = 9 and 9 &#8722; 4 = 5). What is the wavelength to the nearest whole nanometre? (It is hydrogen&rsquo;s red line, Fraunhofer&rsquo;s C.)""",
                answers=[656, 656.3, 656.28], unit="nm",
                hint="364.6 &times; 9 = 3281.4. Then divide by 5 to get 656.28, which rounds to 656.",
            )],
        ),
    ],
    quiz=dict(
        title="&#10022; Ten Problems in the Light of the Sun &#10022;",
        intro="Ten problems from the history of the Sun&rsquo;s dark lines. One attempt per question, because a spectrum does not give a second look either. A pencil and a steady eye are allowed.",
        verdicts=[
            dict(min=10, title="{score}: A perfect spectrum", text="Flawless, {name}. Fraunhofer, Kirchhoff and Bunsen would let you hold the prism."),
            dict(min=7, title="{score}: A sharp-eyed analyst", text="Strong work, {name}. Read the explanations under the ones that got away, and play with the widgets once more."),
            dict(min=4, title="{score}: Lines coming into focus", text="You have the idea, {name}. Go back to the Kirchhoff chapter, slide the lamp, and try again."),
            dict(min=0, title="{score}: Back to the slit", text="Every one of these can be learned, {name}. Return to Newton&rsquo;s prism, then wipe the slate and try again."),
        ],
        questions=[
            dict(type="num", kicker="Light speed",
                 q="""Light travels about <b>300,000 km</b> in one second. How many kilometres does it travel in <b>2 seconds</b>?""",
                 answers=[600000], unit="km",
                 why="2 &times; 300,000 = 600,000 km. In 500 seconds it would reach the Sun&rsquo;s distance."),
            dict(type="num", kicker="Tiny waves",
                 q="""A hair is about <b>80,000 nm</b> wide. How many violet wavelengths of <b>400 nm</b> fit across it?""",
                 answers=[200], unit="wavelengths",
                 why="80,000 &#247; 400 = 200."),
            dict(type="num", kicker="Counting lines",
                 q="""Fraunhofer mapped <b>574</b> dark lines. Wollaston had seen about <b>7</b>. How many <b>more</b> lines did Fraunhofer find?""",
                 answers=[567], unit="lines",
                 why="574 &#8722; 7 = 567."),
            dict(type="num", kicker="Years",
                 q="""Wollaston saw the dark lines in <b>1802</b>, and Kirchhoff explained them in <b>1859</b>. How many years apart?""",
                 answers=[57], unit="years",
                 why="1859 &#8722; 1802 = 57."),
            dict(type="mc", kicker="Fingerprints",
                 q="""A flame shows bright lines at <b>589.0 nm and 589.6 nm</b>. (Reference: hydrogen 656.3, lithium 670.8, sodium 589.0 and 589.6.) Which element is it?""",
                 mc=[("Hydrogen", False),
                     ("Sodium", True),
                     ("Lithium", False)],
                 why="Only sodium has a pair of lines at 589.0 and 589.6 nm: the pair that matches Fraunhofer&rsquo;s dark D lines."),
            dict(type="num", kicker="Kirchhoff&rsquo;s reversal",
                 q="""A lamp has brightness <b>100</b>. A flame of brightness <b>40</b> that absorbs <b>50%</b> (0.5) is in front of it. The line brightness is <b>100 &times; 0.5 + 0.5 &times; 40</b>. What is it?""",
                 answers=[70], unit="",
                 why="100 &times; 0.5 = 50 and 0.5 &times; 40 = 20. 50 + 20 = 70."),
            dict(type="mc", kicker="Bright or dark?",
                 q="""In the last problem, the lamp is 100 and the line comes out at 70. Compared with the background, the line looks:""",
                 mc=[("Brighter than the background", False),
                     ("The same as the background", False),
                     ("Darker than the background", True)],
                 why="70 is less than 100, so the line is a dark line. That is the case for the Sun: a glowing surface hotter than the gas above it."),
            dict(type="num", kicker="Caesium",
                 q="""Caesium has lines at <b>455.5 nm</b> and <b>459.3 nm</b>. What is the gap between them?""",
                 answers=[3.8], unit="nm",
                 why="459.3 &#8722; 455.5 = 3.8."),
            dict(type="num", kicker="Helium",
                 q="""The helium line is at <b>587.6 nm</b>. The nearer sodium line is at <b>589.0 nm</b>. How many nm apart?""",
                 answers=[1.4], unit="nm",
                 why="589.0 &#8722; 587.6 = 1.4. Close enough to confuse a careless eye, far enough to prove a new element."),
            dict(type="num", kicker="Balmer&rsquo;s formula",
                 q="""Balmer&rsquo;s formula is 364.6 &times; n&#178; &#247; (n&#178; &#8722; 4). With <b>n = 4</b>, work out 364.6 &times; 16 &#247; 12 to the nearest whole nanometre.""",
                 answers=[486, 486.1, 486.13], unit="nm",
                 why="364.6 &times; 16 = 5833.6, and 5833.6 &#247; 12 = 486.13, which rounds to 486. It is hydrogen&rsquo;s blue-green line, Fraunhofer&rsquo;s F."),
        ],
    ),
)
