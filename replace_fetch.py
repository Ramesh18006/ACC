import os
import re

files = ['laptops.html', 'desktops.html', 'printers.html', 'accessories.html']
for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace the top part
    regex_start = re.compile(r"Papa\.parse\(\s*SHEET_URL\s*,\s*\{\s*download:\s*true\s*,\s*header:\s*true\s*,\s*complete:\s*function\s*\([^)]*\)\s*\{")
    
    replace_start = """fetch(SHEET_URL, { cache: 'no-store' })
                .then(response => {
                    if (!response.ok) throw new Error("Network response was not ok");
                    return response.text();
                })
                .then(csvData => {
                    Papa.parse(csvData, {
                        header: true,
                        complete: function (results) {"""
                        
    content = regex_start.sub(replace_start, content, count=1)
    
    # 2. Replace the bottom part
    regex_end = re.compile(r"\}\s*,\s*error:\s*function\s*\([^)]*\)\s*\{(.*?)\}\s*\}\);", re.DOTALL)
    
    def repl_end(match):
        body = match.group(1)
        return """}
                    });
                })
                .catch(err => {""" + body + """});"""
                
    content = regex_end.sub(repl_end, content, count=1)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Fetch replacements executed!")
