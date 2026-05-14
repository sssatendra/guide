import json
import re

with open('c:/Users/sssat/OneDrive/Documents/test/gen.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Insert diagram generation before full_html
insert_code = '''
for q in questions:
    diagram = "classDiagram\\n"
    classes = []
    for c in q["components"]:
        cls_names = [x.strip() for x in c[0].split("/")]
        safe_names = ["".join(filter(str.isalnum, x)) for x in cls_names]
        classes.append(safe_names)
        for i, safe_cls in enumerate(safe_names):
            if safe_cls:
                diagram += f"    class {safe_cls}\\n"
                if i > 0:
                    diagram += f"    {safe_names[i-1]} *-- {safe_cls}\\n"
    if len(classes) > 1:
        for i in range(1, len(classes)):
            if classes[i-1] and classes[i] and classes[i-1][-1] and classes[i][0]:
                diagram += f"    {classes[i-1][-1]} --> {classes[i][0]}\\n"
    q["diagram"] = diagram

'''
code = code.replace('full_html = html_template', insert_code + 'full_html = html_template')

# Add CSS
css_insert = '.mermaid-container { background: #1e2535; padding: 1rem; border-radius: 8px; border: 1px solid #2a3348; margin-bottom: 1.1rem; overflow-x: auto; text-align: center; }\\n</style>'
code = code.replace('</style>', css_insert)

# Add mermaidHtml
js_insert = '''
  let mermaidHtml = `<div class="slabel">System Flowchart / Class Diagram</div>
    <div class="mermaid-container"><pre class="mermaid" id="mermaid-canvas-${q.id}">${q.diagram}</pre></div>`;
  
  const content = `
    <div class="prog-strip"><div class="prog-fill" style="width:${pct}%"></div></div>
    <div class="badges">${badgesHTML}</div>
    <div class="qhead">
      <div class="qnum">${qn}</div>
      <div class="qtitle">${q.title}</div>
    </div>
    
    <div class="tldr"><strong>TL;DR:</strong> ${q.tldr}</div>
    
    <div class="slabel">Requirements</div>
    <div class="rgrid">
      <div class="rcard"><h4>Functional</h4><ul>${reqsHTML}</ul></div>
      <div class="rcard"><h4>Non-Functional / Scale</h4><ul>${nfreqsHTML}</ul></div>
    </div>
    
    ${mermaidHtml}
    
    <div class="slabel">Core Components (Class/Entity)</div>
    <div class="cgrid">${compHTML}</div>
    
    <div class="slabel">Design Decisions & Patterns</div>
    <div class="dlist">${decHTML}</div>
    
    <div class="navrow">${navHTML}</div>
  `;
'''

code = re.sub(r'const content = `.*?`;', js_insert.strip(), code, flags=re.DOTALL)

# Add window.renderMermaid logic
js_insert2 = '''
  document.getElementById('qcontent').innerHTML = content;
  document.getElementById('mainwrap').scrollTop = 0;
  
  if (window.renderMermaid) {
    setTimeout(() => window.renderMermaid(`mermaid-canvas-${q.id}`), 50);
  }
'''
code = code.replace("document.getElementById('qcontent').innerHTML = content;\n  document.getElementById('mainwrap').scrollTop = 0;", js_insert2)

# Add module script before closing body
module_script = '''
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: false, theme: 'dark' });
  window.renderMermaid = async function(id) {
    try {
      await mermaid.run({
        querySelector: '#' + id
      });
    } catch(e) {
      console.error(e);
    }
  };
</script>
</body>
'''
code = code.replace('</body>', module_script)

with open('c:/Users/sssat/OneDrive/Documents/test/gen.py', 'w', encoding='utf-8') as f:
    f.write(code)
print('gen.py modified successfully.')
