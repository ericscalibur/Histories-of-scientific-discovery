#!/usr/bin/env python3
"""Shared engine: builds a self-contained interactive story HTML from a story dict."""
import json

CSS = """
  :root{
    --night:#0b1230; --night2:#141c42; --parchment:#f9f3e4; --parchment2:#f1e7cf;
    --ink:#22304f; --ink-soft:#4a5878; --gold:#e8a90c; --gold-dark:#8a6400;
    --accent:#3a5da8; --good:#1e7d43; --bad:#b03030; --locked:#2a3560;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html{scroll-behavior:smooth;}
  body{background:linear-gradient(180deg,#070c22 0%, #0b1230 40%, #10173a 100%);
    color:var(--parchment); font-family:Georgia,'Times New Roman',serif;
    min-height:100vh; overflow-x:hidden;}
  .stars,.stars2{position:fixed; inset:0; pointer-events:none; z-index:0;}
  .stars{box-shadow:8vw 12vh 0 0 #fff,22vw 6vh 0 1px #ffe9b0,35vw 18vh 0 0 #fff,48vw 9vh 0 0 #cfe0ff,
    61vw 14vh 0 1px #fff,74vw 5vh 0 0 #ffe9b0,88vw 11vh 0 0 #fff,15vw 28vh 0 0 #cfe0ff,
    29vw 33vh 0 1px #fff,55vw 27vh 0 0 #fff,69vw 31vh 0 0 #ffe9b0,83vw 26vh 0 0 #fff,
    5vw 45vh 0 0 #fff,42vw 41vh 0 1px #cfe0ff,78vw 44vh 0 0 #fff,93vw 39vh 0 0 #ffe9b0,
    12vw 58vh 0 0 #fff,33vw 62vh 0 0 #fff,52vw 55vh 0 1px #ffe9b0,66vw 60vh 0 0 #cfe0ff,
    81vw 57vh 0 0 #fff,96vw 63vh 0 0 #fff,9vw 74vh 0 1px #fff,27vw 79vh 0 0 #ffe9b0,
    45vw 72vh 0 0 #fff,63vw 77vh 0 0 #cfe0ff,87vw 74vh 0 1px #fff,18vw 90vh 0 0 #fff,
    38vw 87vh 0 0 #ffe9b0,58vw 92vh 0 0 #fff,76vw 88vh 0 0 #fff,94vw 91vh 0 1px #cfe0ff;
    width:1px; height:1px; border-radius:50%; background:#fff; opacity:.8;}
  .stars2{box-shadow:4vw 20vh 0 0 #fff8,19vw 15vh 0 0 #fff6,44vw 23vh 0 0 #fff7,71vw 19vh 0 0 #fff6,
    91vw 16vh 0 0 #fff8,25vw 48vh 0 0 #fff6,49vw 46vh 0 0 #fff7,73vw 50vh 0 0 #fff5,
    7vw 66vh 0 0 #fff7,36vw 69vh 0 0 #fff6,60vw 66vh 0 0 #fff8,85vw 68vh 0 0 #fff6,
    14vw 83vh 0 0 #fff7,47vw 82vh 0 0 #fff5,69vw 84vh 0 0 #fff7,90vw 81vh 0 0 #fff6;
    width:1px; height:1px; border-radius:50%; background:#fff; opacity:.6;}
  .wrap{position:relative; z-index:1; max-width:860px; margin:0 auto; padding:24px 16px 80px;}
  header{text-align:center; padding:36px 8px 10px;}
  header h1{font-size:clamp(1.6rem,4.2vw,2.4rem); color:var(--gold); letter-spacing:.5px;
    text-shadow:0 2px 12px rgba(232,169,12,.35);}
  header .sub{font-style:italic; color:#cdd6ee; margin-top:8px; font-size:1.05rem;}
  header .byline{color:#8f9cc4; font-size:.85rem; margin-top:6px;}
  #tracker{position:sticky; top:0; z-index:5; background:rgba(7,12,34,.92);
    backdrop-filter:blur(4px); border-bottom:1px solid #2a3560; padding:6px 0 2px; margin:18px -16px 8px;}
  #tracker svg{display:block; margin:0 auto;}
  #tracker .tlabel{fill:#8f9cc4; font-size:10px; font-family:Georgia,serif;}
  .card{background:var(--parchment); color:var(--ink); border-radius:14px; padding:28px 30px;
    margin:26px 0; box-shadow:0 10px 34px rgba(0,0,0,.45), inset 0 0 60px rgba(180,140,60,.08);
    border:1px solid #d9c9a3;}
  .card, .checkpoint{scroll-margin-top:88px;}
  .card.locked{display:none;}
  .checkpoint.locked{display:none;}
  .chap-kicker{font-size:.8rem; letter-spacing:2.5px; text-transform:uppercase;
    color:var(--gold-dark); font-weight:bold;}
  .card h2{font-size:1.55rem; margin:6px 0 14px; color:var(--ink);}
  .card p{line-height:1.65; margin:0 0 13px; font-size:1.04rem;}
  .card .funfact{background:#fff8e6; border-left:4px solid var(--gold);
    padding:10px 14px; border-radius:0 8px 8px 0; font-size:.95rem; margin:14px 0; color:#5a4a1a;}
  .bigidea{background:#eef2fb; border:1.5px solid #b9c7e8; border-radius:10px;
    padding:12px 16px; margin:16px 0; color:#22304f; font-size:1rem;}
  .bigidea b{color:var(--accent);}
  .illus{display:block; margin:16px auto; max-width:100%;}
  .checkpoint{background:linear-gradient(180deg,#1b2450,#141c42); color:#eef1fb;
    border-radius:12px; padding:20px 22px; margin:20px -8px -6px; border:1.5px solid #3a4a86;}
  .checkpoint + .checkpoint{margin-top:16px;}
  .checkpoint .cp-kicker{color:var(--gold); font-weight:bold; letter-spacing:1.5px;
    font-size:.8rem; text-transform:uppercase;}
  .checkpoint .question{font-size:1.08rem; line-height:1.55; margin:8px 0 14px;}
  .answer-row{display:flex; gap:10px; flex-wrap:wrap; align-items:center;}
  .answer-row input[type=text]{font-size:1.15rem; padding:9px 13px; border-radius:8px;
    border:2px solid #3a4a86; width:140px; background:#0d1330; color:#ffe9b0;
    font-family:Georgia,serif; text-align:center;}
  .answer-row input[type=text]:focus{outline:2px solid var(--gold);}
  button{font-family:Georgia,serif; cursor:pointer;}
  .check-btn{background:var(--gold); color:#2a2005; font-weight:bold; font-size:1rem;
    border:none; border-radius:8px; padding:10px 20px;}
  .check-btn:hover{background:#f7bb2b;}
  .hint-btn{background:transparent; color:#aebadf; border:1.5px dashed #4a5a9a;
    border-radius:8px; padding:9px 14px; font-size:.9rem;}
  .hint-btn:hover{color:#fff;}
  .mc-btn{background:#0d1330; color:#eef1fb; border:2px solid #3a4a86; border-radius:8px;
    padding:10px 16px; font-size:.98rem;}
  .mc-btn:hover{border-color:var(--gold);}
  .hint{display:none; margin-top:10px; color:#ffd97a; font-size:.95rem;}
  .feedback{margin-top:12px; font-size:1rem; min-height:1.2em;}
  .feedback.good{color:#7fe0a7;}
  .feedback.bad{color:#ff9d9d;}
  .unit{color:#aebadf; font-size:.95rem;}
  .shake{animation:shake .4s;}
  @keyframes shake{0%,100%{transform:translateX(0)} 25%{transform:translateX(-6px)} 75%{transform:translateX(6px)}}
  .solved-glow{animation:glow 1.2s;}
  @keyframes glow{0%{box-shadow:0 0 0 rgba(232,169,12,0)} 40%{box-shadow:0 0 40px rgba(232,169,12,.8)} 100%{box-shadow:0 0 0 rgba(232,169,12,0)}}
  #finale{text-align:center;}
  #finale h2{color:var(--gold-dark);}
  #finale p{text-align:left;}
  .cert{border:3px double var(--gold-dark); border-radius:12px; padding:22px; margin:18px 0; background:#fffdf4;}
  .cert .cname{font-size:1.4rem; color:var(--accent); font-weight:bold;}
  .laws{text-align:left; background:#eef2fb; border-radius:10px; padding:14px 18px; margin:14px 0;}
  .laws p{margin:8px 0;}
  .name-row{margin:14px 0 4px;}
  .name-row input{font-size:1.05rem; padding:8px 12px; border-radius:8px;
    border:2px solid #b9c7e8; font-family:Georgia,serif; width:240px;}
  footer{color:#8f9cc4; text-align:center; font-size:.85rem; margin-top:40px; line-height:1.6;}
"""

JS = """
(function(){
  var TOTAL = @@TOTAL@@;
  var solved = 0;
  var answers = @@ANSWERS@@;
  var unlocks = @@UNLOCKS@@;
  var praise = @@PRAISE@@;
  var path = document.getElementById('cometPath');
  var g = document.getElementById('trackStars');
  var L = path.getTotalLength();
  for (var i=0;i<TOTAL;i++){
    var p = path.getPointAtLength(L*(i+0.5)/TOTAL);
    var s = document.createElementNS('http://www.w3.org/2000/svg','path');
    var r1=8, r2=3.4, d='';
    for (var k=0;k<10;k++){
      var rr = (k%2===0)?r1:r2, an = -Math.PI/2 + k*Math.PI/5;
      d += (k===0?'M':'L') + (p.x+rr*Math.cos(an)).toFixed(1) + ' ' + (p.y+rr*Math.sin(an)).toFixed(1) + ' ';
    }
    s.setAttribute('d', d+'Z');
    s.setAttribute('fill', '#2a3560');
    s.setAttribute('stroke', '#3a4a86');
    s.setAttribute('id', 'tstar'+(i+1));
    g.appendChild(s);
  }
  var starOrder = @@STARORDER@@;
  function lightStar(cpid){
    var s = document.getElementById('tstar'+(starOrder.indexOf(cpid)+1));
    if(s){ s.setAttribute('fill','#e8a90c'); s.setAttribute('stroke','#ffe9b0'); }
  }
  function reveal(id){
    var el = document.getElementById(id);
    if(!el) return;
    el.classList.remove('locked');
    el.classList.add('solved-glow');
    setTimeout(function(){ el.scrollIntoView({behavior:'smooth', block:'start'}); }, 250);
  }
  function parseNum(v){
    v = (v||'').replace(/[,\\s]/g,'').replace(/[^0-9.\\-]/g,'');
    return v === '' ? NaN : Number(v);
  }
  function pname(){
    var nm = (document.getElementById('playerName').value || '').trim();
    return nm !== '' ? nm : 'astronomer';
  }
  function withName(msg){ return msg.replace(/\\{name\\}/g, pname()); }
  function solve(cpid){
    solved++; lightStar(cpid); reveal(unlocks[cpid]);
    if (solved >= TOTAL) finish();
  }
  var tries = {};
  window.check = function(n){
    var input = document.getElementById('a'+n);
    var fb = document.getElementById('f'+n);
    var val = parseNum(input.value);
    var ok = answers[n].indexOf(val) !== -1;
    if (ok){
      if (!input.dataset.done){
        input.dataset.done = '1';
        fb.className = 'feedback good';
        fb.textContent = '\\u2713 ' + withName(praise[Math.floor(Math.random()*praise.length)]);
        input.disabled = true;
        solve(n);
      }
    } else {
      tries[n] = (tries[n]||0)+1;
      fb.className = 'feedback bad';
      fb.textContent = isNaN(val) ? withName('\\u2717 Type a number first, {name}!') :
        (tries[n] >= 2 ? withName('\\u2717 Not yet, {name} \\u2014 try the Hint button. Real scientists redo their math all the time.') :
         withName('\\u2717 Not quite, {name} \\u2014 measure again!'));
      input.classList.add('shake');
      setTimeout(function(){input.classList.remove('shake');}, 450);
      if (tries[n] >= 2) { var h=document.getElementById('h'+n); if(h) h.style.display='block'; }
    }
  };
  var mcMsgs = @@MCMSGS@@;
  var mcDone = {};
  window.checkMC = function(n, btn, correct){
    var fb = document.getElementById('f'+n);
    if (mcDone[n]) return;
    if (correct){
      mcDone[n] = true;
      btn.style.borderColor = '#7fe0a7'; btn.style.color = '#7fe0a7';
      fb.className = 'feedback good';
      fb.textContent = '\\u2713 ' + withName(mcMsgs[n].good);
      solve(n);
    } else {
      fb.className = 'feedback bad';
      fb.textContent = '\\u2717 ' + withName(mcMsgs[n].bad);
      btn.classList.add('shake');
      setTimeout(function(){btn.classList.remove('shake');}, 450);
    }
  };
  function finish(){
    var nm = (document.getElementById('playerName').value || '').trim();
    document.getElementById('certName').textContent = nm !== '' ? nm : 'Astronomer';
  }
})();
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@TITLE@@</title>
<style>@@CSS@@</style>
</head>
<body>
<div class="stars"></div><div class="stars2"></div>
<div class="wrap">
<header>
  <h1>@@H1@@</h1>
  <div class="sub">@@SUB@@</div>
  <div class="byline">An interactive adventure &middot; solve each problem to unlock the next chapter</div>
  <div class="name-row"><input id="playerName" type="text" placeholder="Write your name, astronomer&hellip;" aria-label="Your name"></div>
</header>
<div id="tracker" aria-label="progress">
  <svg width="760" height="64" viewBox="0 0 760 64" preserveAspectRatio="xMidYMid meet" style="max-width:100%">
    <path id="cometPath" d="M 30 48 C 160 14, 300 56, 420 30 S 660 40, 730 18" fill="none" stroke="#2a3560" stroke-width="1.5" stroke-dasharray="3 5"/>
    <g id="trackStars"></g>
    <text class="tlabel" x="30" y="62" text-anchor="middle">start</text>
    <text class="tlabel" x="730" y="34" text-anchor="middle">&#9732;</text>
  </svg>
</div>
@@BODY@@
<footer>@@FOOTER@@</footer>
</div>
<script>@@JS@@</script>
</body>
</html>
"""

def cp_html(cp, first_in_chapter):
    n = cp["n"]
    lock = "" if first_in_chapter else " locked"
    out = ['<div class="checkpoint%s" id="cp%d">' % (lock, n)]
    out.append('<div class="cp-kicker">&#9733; Checkpoint %d &middot; %s</div>' % (n, cp["kicker"]))
    out.append('<div class="question">%s</div>' % cp["q"])
    if cp.get("figure"):
        out.append(cp["figure"])
    if cp["type"] == "num":
        out.append('<div class="answer-row">')
        out.append('<input type="text" inputmode="numeric" id="a%d" aria-label="answer %d">' % (n, n))
        out.append('<span class="unit">%s</span>' % cp.get("unit", ""))
        out.append('<button class="check-btn" onclick="check(%d)">Check &#10022;</button>' % n)
        out.append('<button class="hint-btn" onclick="document.getElementById(\'h%d\').style.display=\'block\'">Hint?</button>' % n)
        out.append('</div>')
        out.append('<div class="hint" id="h%d">%s</div>' % (n, cp["hint"]))
    else:  # mc
        out.append('<div class="answer-row">')
        for label, correct in cp["mc"]:
            out.append(
                '<button class="mc-btn" onclick="checkMC(%d,this,%s)">%s</button>' %
                (n, "true" if correct else "false", label))
        out.append('</div>')
    out.append('<div class="feedback" id="f%d" aria-live="polite"></div>' % n)
    out.append('</div>')
    return "\n".join(out)

def build(story, outpath):
    # assign checkpoint numbers and unlock chain
    cps = []
    for ch_i, ch in enumerate(story["chapters"]):
        for cp_i, cp in enumerate(ch["cps"]):
            cps.append((ch_i, cp_i, cp))
    for i, (_, _, cp) in enumerate(cps):
        cp["n"] = i + 1
    unlocks, answers, mcmsgs = {}, {}, {}
    for i, (ch_i, cp_i, cp) in enumerate(cps):
        if i + 1 < len(cps):
            nch_i, ncp_i, ncp = cps[i + 1]
            unlocks[cp["n"]] = ("cp%d" % ncp["n"]) if nch_i == ch_i else ("ch%d" % (nch_i + 1))
        else:
            unlocks[cp["n"]] = "finale"
        if cp["type"] == "num":
            answers[cp["n"]] = cp["answers"]
        else:
            mcmsgs[cp["n"]] = {"good": cp["good"], "bad": cp["bad"]}
    body = []
    for ch_i, ch in enumerate(story["chapters"]):
        lock = "" if ch_i == 0 else " locked"
        body.append('<section class="card%s" id="ch%d">' % (lock, ch_i + 1))
        body.append('<div class="chap-kicker">%s</div>' % ch["kicker"])
        body.append('<h2>%s</h2>' % ch["title"])
        body.append(ch["html"])
        for cp_i, cp in enumerate(ch["cps"]):
            body.append(cp_html(cp, cp_i == 0))
        body.append('</section>')
    body.append('<section class="card locked" id="finale">')
    body.append('<div class="chap-kicker">Epilogue</div>')
    body.append('<h2>&#10022; %s &#10022;</h2>' % story["finale_title"])
    body.append(story["finale_html"])
    body.append("""<div class="cert">
    <div style="font-size:.85rem; letter-spacing:2px; color:#8a6400; text-transform:uppercase;">%s</div>
    <div style="margin:10px 0 4px;">certifies that</div>
    <div class="cname" id="certName">Astronomer</div>
    <div style="margin:6px 0 10px;">has completed all %d checkpoints of %s<br>and is hereby granted the rank of</div>
    <div style="font-size:1.25rem; color:#8a6400; font-weight:bold;">&#11088; %s &#11088;</div>
  </div>""" % (story["cert_org"], len(cps), story["cert_of"], story["cert_rank"]))
    body.append(story.get("takeaways", ""))
    body.append('</section>')

    js = (JS.replace("@@TOTAL@@", str(len(cps)))
            .replace("@@ANSWERS@@", json.dumps(answers))
            .replace("@@UNLOCKS@@", json.dumps({str(k): v for k, v in unlocks.items()}))
            .replace("@@PRAISE@@", json.dumps(story["praise"]))
            .replace("@@MCMSGS@@", json.dumps(mcmsgs))
            .replace("@@STARORDER@@", json.dumps([cp["n"] for _, _, cp in cps])))
    # unlocks keys are numbers in JS lookups; JSON string keys work with JS obj[n] coercion
    html = (PAGE.replace("@@TITLE@@", story["title"])
                .replace("@@CSS@@", CSS)
                .replace("@@H1@@", story["h1"])
                .replace("@@SUB@@", story["sub"])
                .replace("@@BODY@@", "\n".join(body))
                .replace("@@FOOTER@@", story["footer"])
                .replace("@@JS@@", js))
    with open(outpath, "w") as f:
        f.write(html)
    # return test plan: ordered list of (n, type, first-correct-answer or correct-mc-index)
    plan = []
    for _, _, cp in cps:
        if cp["type"] == "num":
            plan.append({"n": cp["n"], "type": "num", "val": str(cp["answers"][0])})
        else:
            idx = [i for i, (_, c) in enumerate(cp["mc"]) if c][0]
            plan.append({"n": cp["n"], "type": "mc", "idx": idx})
    return plan
