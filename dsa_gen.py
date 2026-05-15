import json
import data_dsa

questions = data_dsa.questions

# Assign continuous IDs
for i, q in enumerate(questions):
    q["id"] = i + 1

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Data Structures & Algorithms Interview Guide</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Syne:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0f1117;color:#ffffff;font-family:'Syne',sans-serif;min-height:100vh}
.topbar{background:#161b27;border-bottom:1px solid #2a3348;padding:.65rem 1rem;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:.5rem;position:sticky;top:0;z-index:300}
.logo{font-size:.95rem;font-weight:700;color:#10b981}
.logo span{color:#ffffff;font-weight:400;font-size:.78rem}
.topbar-right{display:flex;gap:.4rem;align-items:center;flex-wrap:wrap}
.srch{background:#1e2535;border:1px solid #2a3348;border-radius:8px;padding:.38rem .75rem;color:#ffffff;font-family:'Syne',sans-serif;font-size:.8rem;width:200px;outline:none}
.srch:focus{border-color:#10b981}
.srch::placeholder{color:#ffffff}
.fbtn{background:#1e2535;border:1px solid #2a3348;border-radius:8px;padding:.36rem .65rem;color:#ffffff;font-size:.7rem;cursor:pointer;font-family:'Syne',sans-serif;transition:all .15s;white-space:nowrap}
.fbtn:hover,.fbtn.on{background:#252d40;color:#10b981;border-color:#10b98155}
.mob-toggle{display:none;background:#10b981;border:none;border-radius:8px;padding:.38rem .75rem;color:#fff;font-size:.75rem;font-weight:700;cursor:pointer;font-family:'Syne',sans-serif;align-items:center;white-space:nowrap}
.layout{display:flex;height:calc(100vh - 50px)}
.sidebar{width:320px;min-width:320px;background:#161b27;border-right:1px solid #2a3348;overflow-y:auto;height:100%;position:sticky;top:50px}
.sb-inner{padding:.4rem .35rem}
.main{flex:1;overflow-y:auto}
.wrap{padding:1.5rem 2rem 3rem;max-width:960px}
.mob-overlay{display:none;position:fixed;inset:0;background:#0f1117;z-index:400;flex-direction:column}
.mob-overlay.open{display:flex}
.mob-header{background:#161b27;border-bottom:1px solid #2a3348;padding:.65rem 1rem;display:flex;align-items:center;justify-content:space-between;gap:.5rem}
.mob-title{font-size:.9rem;font-weight:700;color:#ffffff}
.mob-close{background:#1e2535;border:1px solid #2a3348;border-radius:8px;padding:.35rem .7rem;color:#ffffff;font-size:.75rem;cursor:pointer;font-family:'Syne',sans-serif}
.mob-search{padding:.6rem .75rem;background:#161b27;border-bottom:1px solid #2a3348}
.mob-search input{width:100%;background:#1e2535;border:1px solid #2a3348;border-radius:8px;padding:.4rem .75rem;color:#ffffff;font-family:'Syne',sans-serif;font-size:.82rem;outline:none}
.mob-search input:focus{border-color:#10b981}
.mob-list{flex:1;overflow-y:auto;padding:.4rem .5rem}
.qi{display:flex;align-items:flex-start;gap:.45rem;padding:.52rem .6rem;border-radius:7px;cursor:pointer;border:1px solid transparent;transition:all .12s;margin-bottom:2px}
.qi:hover{background:#1e2535;border-color:#2a3348}
.qi.active{background:#1e2535;border-left:3px solid #10b981;border-color:#10b98133}
.qi.hidden{display:none}
.qn{min-width:20px;font-size:.67rem;font-weight:700;color:#ffffff;margin-top:2px;font-family:'JetBrains Mono',monospace;flex-shrink:0}
.qi.active .qn{color:#10b981}
.qt{font-size:.75rem;color:#ffffff;line-height:1.4;flex:1;font-weight:500}
.qi.active .qt{color:#ffffff;font-weight:600}
.fdot{width:5px;height:5px;border-radius:50%;margin-top:5px;flex-shrink:0}
.welcome{text-align:center;padding:3.5rem 1rem}
.welcome h2{font-size:1.5rem;font-weight:700;color:#ffffff;margin-bottom:.6rem}
.welcome p{font-size:.9rem;color:#9ca3af;line-height:1.75}
.prog-strip{background:#1e2535;border-radius:4px;height:3px;margin-bottom:1rem;overflow:hidden}
.prog-fill{height:100%;background:linear-gradient(90deg,#10b981,#3b82f6);border-radius:4px;transition:width .4s}
.qhead{display:flex;align-items:flex-start;gap:.65rem;margin-bottom:.85rem;flex-wrap:wrap}
.qnum{background:#10b981;color:#fff;font-size:.7rem;font-weight:700;padding:3px 8px;border-radius:10px;font-family:'JetBrains Mono',monospace;margin-top:3px;flex-shrink:0}
.qtitle{font-size:1.2rem;font-weight:700;color:#ffffff;line-height:1.35;flex:1}
.badges{display:flex;flex-wrap:wrap;gap:.3rem;margin-bottom:1rem;align-items:center}
.fbadge{font-size:.66rem;padding:3px 9px;border-radius:10px;border:1px solid;font-weight:600}
.tldr{background:#1e2535;border-left:3px solid #10b981;border-radius:0 8px 8px 0;padding:1rem;font-size:.85rem;line-height:1.6;color:#e5e7eb;margin-bottom:1.5rem}
.slabel{font-size:.7rem;font-weight:700;letter-spacing:.1em;color:#9ca3af;text-transform:uppercase;margin:1.5rem 0 .75rem;border-bottom:1px solid #2a3348;padding-bottom:.4rem}
.explanation{font-size:.85rem;color:#d1d5db;line-height:1.7;margin-bottom:1.5rem}
.explanation p{margin-bottom:.8rem}
.explanation code{background:#1e2535;color:#f472b6;padding:2px 6px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:.75rem;border:1px solid #2a3348}

/* Test Cases Table */
.test-cases{width:100%;border-collapse:collapse;margin:1rem 0 1.5rem;font-size:.8rem}
.test-cases th{background:#1e2535;color:#fff;font-weight:600;padding:.75rem;text-align:left;border:1px solid #2a3348}
.test-cases td{padding:.75rem;border:1px solid #2a3348;color:#d1d5db;line-height:1.5; font-family:'JetBrains Mono',monospace;}

/* Language Toggle */
.lang-toggle{display:flex;gap:.5rem;margin-bottom:1rem;}
.btn-lang{background:#161b27;border:1px solid #2a3348;border-radius:6px;padding:.4rem 1rem;color:#d1d5db;font-size:.75rem;cursor:pointer;font-family:'Syne',sans-serif;font-weight:600;transition:all 0.15s;}
.btn-lang:hover{border-color:#10b981;}
.btn-lang.active{background:#10b981;color:#fff;border-color:#10b981;}

/* Code Wrap */
.code-wrap{background:#1e2535;padding:1rem;border-radius:8px;border:1px solid #2a3348;font-family:'JetBrains Mono',monospace;font-size:.85rem;overflow-x:auto;margin-bottom:1.5rem;}
.code-wrap pre{color:#e5e7eb;margin:0;}
.code-block{display:none;}

/* Solution explanation box */
.sol-exp{background:#1e2535;padding:1rem;border-radius:8px;border-left:3px solid #3b82f6;font-size:.85rem;line-height:1.6;color:#d1d5db;margin-bottom:1.5rem;}

.navrow{display:flex;gap:.5rem;margin-top:2rem;padding-top:1.5rem;border-top:1px solid #2a3348}
.nbtn{background:#1e2535;border:1px solid #2a3348;border-radius:8px;padding:.6rem 1rem;color:#ffffff;font-size:.8rem;cursor:pointer;font-family:'Syne',sans-serif;transition:all .15s;flex:1;text-align:center;line-height:1.45}
.nbtn:hover{background:#252d40;color:#ffffff;border-color:#ffffff}
.nbtn.off{opacity:.25;pointer-events:none}
.mermaid-container{background:transparent;padding:1.5rem 1rem;margin-bottom:1.5rem;overflow-x:auto;display:flex;justify-content:center;border-radius:12px;border:1px dashed #2a3348}
.mermaid-container pre{margin:0; width:100%; display:flex; justify-content:center;}
.mermaid-container svg{max-width:100%; height:auto !important; min-height:250px;}

@media(max-width:768px){
  .sidebar{display:none}
  .mob-toggle{display:flex}
  .srch{display:none}
  .layout{height:auto;flex-direction:column}
  .main{overflow-y:visible}
  .wrap{padding:1.25rem 1rem 3rem}
  .welcome{padding:2rem .5rem}
  .topbar{padding:.55rem .75rem}
  .logo span{display:none}
}
</style>
</head>
<body>
<div class="topbar">
  <div style="display:flex;align-items:center;gap:.6rem">
    <button class="mob-toggle" onclick="openMob()">☰ Menu</button>
    <div class="logo">DSA <span>· Interview Guide</span></div>
  </div>
  <div class="topbar-right">
    <a href="index.html" class="fbtn" style="text-decoration:none">🏠 Home</a>
    <input class="srch" id="dsrch" type="text" placeholder="Search problems…" oninput="doSearch(this.value,'desk')">
  </div>
</div>

<div class="mob-overlay" id="moboverlay">
  <div class="mob-header">
    <div class="mob-title">📋 Problems</div>
    <button class="mob-close" onclick="closeMob()">✕ Close</button>
  </div>
  <div class="mob-search"><input type="text" id="msrch" placeholder="Search…" oninput="doSearch(this.value,'mob')"></div>
  <div class="mob-list" id="moblist"></div>
</div>

<div class="layout">
  <div class="sidebar"><div class="sb-inner" id="deskqlist"></div></div>
  <div class="main"><div class="wrap" id="mainwrap">
    <div id="welcome">
      <div class="welcome">
        <h2>Data Structures & Algorithms</h2>
        <p>Master top FAANG problems with deep explanations, visualizations, and code in JS & Python.</p>
        <div style="margin-top: 2.5rem; text-align: left; background: #1e2535; padding: 1.5rem; border-radius: 12px; border: 1px solid #2a3348;">
            <h3 style="color: #10b981; font-size: 1rem; margin-bottom: 1rem;">Why this guide?</h3>
            <p style="font-size:0.85rem; line-height: 1.6; margin-bottom: 1rem;">This guide avoids rote memorization. Instead, it focuses on <strong>pattern recognition</strong>. Once you master the underlying patterns (Sliding Window, Two Pointers, BFS/DFS, DP), you can solve hundreds of derived questions.</p>
        </div>
      </div>
    </div>
    <div id="qcontent"></div>
  </div></div>
</div>

<script>
const QS = """

js_code = """
let curQ = 0;
let currentLang = localStorage.getItem('dsa_lang') || 'js';

function getCatColor(cat) {
  if(cat.includes('Array')) return '#10b981';
  if(cat.includes('Sliding Window') || cat.includes('Pointer')) return '#3b82f6';
  if(cat.includes('List')) return '#f59e0b';
  if(cat.includes('Graph') || cat.includes('Tree')) return '#8b5cf6';
  if(cat.includes('Dynamic')) return '#ef4444';
  if(cat.includes('Stack') || cat.includes('Queue')) return '#06b6d4';
  return '#ffffff';
}

function getDiffColor(diff) {
    if(diff === 'Easy') return '#10b981';
    if(diff === 'Medium') return '#f59e0b';
    if(diff === 'Hard') return '#ef4444';
    return '#9ca3af';
}

function initList() {
  const ml = document.getElementById('moblist');
  const dl = document.getElementById('deskqlist');
  ml.innerHTML = ''; dl.innerHTML = '';
  
  let curCat = '';
  
  QS.forEach(q => {
    if (q.category !== curCat) {
      curCat = q.category;
      const catHTML = `<div style="font-size:0.65rem;font-weight:700;color:#9ca3af;text-transform:uppercase;margin:1rem 0 0.3rem 0.6rem;letter-spacing:0.05em">${curCat}</div>`;
      dl.innerHTML += catHTML;
      ml.innerHTML += catHTML;
    }
  
    const qn = q.id < 10 ? '0'+q.id : q.id;
    const diffColor = getDiffColor(q.difficulty);
    
    const html = `<div class="qi" id="qi-${q.id}" onclick="showQ(${q.id})" data-cat="${q.category}">
      <span class="qn">${qn}</span>
      <span class="qt">${q.title}</span>
      <span class="fdot" style="background:${diffColor}"></span>
    </div>`;
    dl.innerHTML += html;
    
    const mhtml = `<div class="qi mob-qi" id="mqi-${q.id}" onclick="showQ(${q.id})" data-cat="${q.category}">
      <span class="qn">${qn}</span>
      <span class="qt">${q.title}</span>
      <span class="fdot" style="background:${diffColor}"></span>
    </div>`;
    ml.innerHTML += mhtml;
  });
}

function setLang(lang) {
    currentLang = lang;
    localStorage.setItem('dsa_lang', lang);
    
    document.querySelectorAll('.btn-lang').forEach(btn => btn.classList.remove('active'));
    const activeBtn = document.getElementById('btn-lang-' + lang);
    if(activeBtn) activeBtn.classList.add('active');
    
    document.querySelectorAll('.code-js').forEach(el => el.style.display = lang === 'js' ? 'block' : 'none');
    document.querySelectorAll('.code-py').forEach(el => el.style.display = lang === 'py' ? 'block' : 'none');
    document.querySelectorAll('.walk-js').forEach(el => el.style.display = lang === 'js' ? 'block' : 'none');
    document.querySelectorAll('.walk-py').forEach(el => el.style.display = lang === 'py' ? 'block' : 'none');
}

function showQ(id) {
  curQ = id;
  const q = QS.find(x => x.id === id);
  if (!q) return;
  
  closeMob();
  document.getElementById('welcome').style.display = 'none';
  
  document.querySelectorAll('.qi').forEach(el => el.classList.remove('active'));
  const dqi = document.getElementById('qi-'+id);
  const mqi = document.getElementById('mqi-'+id);
  if(dqi) dqi.classList.add('active');
  if(mqi) mqi.classList.add('active');
  
  const qn = q.id < 10 ? '0'+q.id : q.id;
  const pct = Math.round((q.id / QS.length) * 100);
  const diffColor = getDiffColor(q.difficulty);
  const catColor = getCatColor(q.category);
  
  let badgesHTML = `<span class="fbadge" style="color:${catColor};border-color:${catColor}55;background:${catColor}15">${q.category}</span>`;
  badgesHTML += `<span class="fbadge" style="color:${diffColor};border-color:${diffColor}55;background:${diffColor}15">${q.difficulty}</span>`;
  
  let navHTML = '';
  if (id > 1) {
    const prev = QS.find(x => x.id === id - 1);
    navHTML += `<button class="nbtn" onclick="showQ(${id-1})">&larr; Previous<br><span style="color:#8b949e;font-size:0.65rem">${prev.title}</span></button>`;
  } else {
    navHTML += `<button class="nbtn off">&larr; Previous</button>`;
  }
  
  if (id < QS.length) {
    const next = QS.find(x => x.id === id + 1);
    navHTML += `<button class="nbtn" onclick="showQ(${id+1})">Next &rarr;<br><span style="color:#8b949e;font-size:0.65rem">${next.title}</span></button>`;
  } else {
    navHTML += `<button class="nbtn off">Next &rarr;</button>`;
  }
  
  let mermaidHtml = '';
  if (q.diagram) {
     mermaidHtml = `<div class="slabel">Visualization</div>
     <div class="mermaid-container"><pre class="mermaid" id="mermaid-canvas-${q.id}">${q.diagram}</pre></div>`;
  }
  
  let testCasesHtml = '';
  if (q.test_cases && q.test_cases.length > 0) {
      testCasesHtml += `<table class="test-cases"><tr><th>Input</th><th>Output</th></tr>`;
      q.test_cases.forEach(tc => {
          testCasesHtml += `<tr><td>${tc.input.replace(/</g, "&lt;").replace(/>/g, "&gt;")}</td><td style="color:#10b981">${tc.output.replace(/</g, "&lt;").replace(/>/g, "&gt;")}</td></tr>`;
      });
      testCasesHtml += `</table>`;
  }
  
  // Format code blocks replacing < and >
  const jsEscaped = q.js_code.replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const pyEscaped = q.py_code.replace(/</g, "&lt;").replace(/>/g, "&gt;");
  
  const content = `
    <div class="prog-strip"><div class="prog-fill" style="width:${pct}%"></div></div>
    <div class="badges">${badgesHTML}</div>
    <div class="qhead">
      <div class="qnum">${qn}</div>
      <div class="qtitle">${q.title}</div>
    </div>
    
    <div class="slabel">Problem Statement & Intuition</div>
    <div class="explanation">${q.explanation.replace(/\\n/g, "<br>")}</div>
    
    ${mermaidHtml}
    
    <div class="slabel">Test Cases</div>
    ${testCasesHtml}
    
    <div class="slabel">Implementation</div>
    <div class="lang-toggle">
        <button class="btn-lang" id="btn-lang-js" onclick="setLang('js')">JavaScript</button>
        <button class="btn-lang" id="btn-lang-py" onclick="setLang('py')">Python</button>
    </div>
    
    <div class="code-wrap code-block code-js">
        <pre>${jsEscaped}</pre>
    </div>
    
    <div class="code-wrap code-block code-py">
        <pre>${pyEscaped}</pre>
    </div>
    
    <div class="sol-exp">
        <strong>Complexity & Walkthrough:</strong><br><br>
        <div class="walk-js">${q.js_walkthrough || ''}</div>
        <div class="walk-py">${q.py_walkthrough || ''}</div>
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #2a3348;">
            ${q.solution_explanation}
        </div>
    </div>
    
    <div class="navrow">${navHTML}</div>
  `;
  
  document.getElementById('qcontent').innerHTML = content;
  document.getElementById('mainwrap').scrollTop = 0;
  
  // Apply current language choice
  setLang(currentLang);
  
  if (q.diagram && window.renderMermaid) {
    setTimeout(() => window.renderMermaid(`mermaid-canvas-${q.id}`), 50);
  }
  
  if(dqi) {
    const sb = document.querySelector('.sidebar');
    const offset = dqi.offsetTop - sb.offsetTop;
    if (offset < sb.scrollTop || offset > sb.scrollTop + sb.clientHeight - 40) {
      sb.scrollTop = offset - 100;
    }
  }
}

function openMob() {
  document.getElementById('moboverlay').classList.add('open');
}
function closeMob() {
  document.getElementById('moboverlay').classList.remove('open');
}

function doSearch(val, source) {
  if (source === 'desk') {
    document.getElementById('msrch').value = val;
  } else {
    document.getElementById('dsrch').value = val;
  }
  val = val.toLowerCase();
  
  document.querySelectorAll('.qi').forEach(el => {
    const qid = parseInt(el.id.replace('qi-','').replace('mqi-',''));
    const q = QS.find(x => x.id === qid);
    if(!q) return;
    
    if (val && !q.title.toLowerCase().includes(val) && !q.category.toLowerCase().includes(val)) {
      el.classList.add('hidden');
    } else {
      el.classList.remove('hidden');
    }
  });
}

document.addEventListener('keydown', (e) => {
  if (curQ > 0) {
    if (e.key === 'ArrowDown' || e.key === 'j') {
      if (curQ < QS.length) { showQ(curQ + 1); e.preventDefault(); }
    } else if (e.key === 'ArrowUp' || e.key === 'k') {
      if (curQ > 1) { showQ(curQ - 1); e.preventDefault(); }
    }
  }
});

initList();
</script>
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ 
    startOnLoad: false, 
    theme: 'base',
    themeVariables: {
      background: 'transparent',
      primaryColor: '#1e2535',
      primaryTextColor: '#ffffff',
      primaryBorderColor: '#10b981',
      lineColor: '#10b981',
      secondaryColor: '#161b27',
      tertiaryColor: '#161b27',
      fontFamily: '"JetBrains Mono", monospace'
    },
    flowchart: { curve: 'basis', padding: 25 }
  });
  window.renderMermaid = async function(id) {
    try {
      await mermaid.run({ querySelector: '#' + id });
    } catch(e) { console.error(e); }
  };
</script>
</body>
</html>
"""

full_html = html_template + json.dumps(questions) + ";" + js_code

with open("c:\\Users\\sssat\\OneDrive\\Documents\\test\\dsa-guide.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print("DSA guide generated successfully.")
