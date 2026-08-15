import os

html_files = ['home.html', 'product.html', 'laptops.html', 'desktops.html', 'printers.html', 'accessories.html']
old_lines = """const originalUrl = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS9B8RWH-SMmDwX11nBAhR3FddNQp_I9iTDT3nwT4dbMM0jTY3MtBGUtgPXCRtvpgWVI2h-oFQ-srsJ/pub?output=csv";
            const SHEET_URL = "https://api.allorigins.win/raw?url=" + encodeURIComponent(originalUrl);"""
new_line = 'const SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS9B8RWH-SMmDwX11nBAhR3FddNQp_I9iTDT3nwT4dbMM0jTY3MtBGUtgPXCRtvpgWVI2h-oFQ-srsJ/pub?output=csv";'

for f in html_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace(old_lines, new_line)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

print("Proxy removed.")
