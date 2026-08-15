import os
import re

# 1. Add Proxy to Google Sheets URL across all HTML files
html_files = ['home.html', 'product.html', 'laptops.html', 'desktops.html', 'printers.html', 'accessories.html']
old_url_line = 'const SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS9B8RWH-SMmDwX11nBAhR3FddNQp_I9iTDT3nwT4dbMM0jTY3MtBGUtgPXCRtvpgWVI2h-oFQ-srsJ/pub?output=csv";'
new_url_line = """const originalUrl = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS9B8RWH-SMmDwX11nBAhR3FddNQp_I9iTDT3nwT4dbMM0jTY3MtBGUtgPXCRtvpgWVI2h-oFQ-srsJ/pub?output=csv";
            const SHEET_URL = "https://api.allorigins.win/raw?url=" + encodeURIComponent(originalUrl);"""

for f in html_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace(old_url_line, new_url_line)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

# 2. Add Search Logic to home.html
with open('home.html', 'r', encoding='utf-8') as file:
    home_content = file.read()

# adding an ID to the search input so we can reference it
old_input = """<input
                    class="w-full h-14 pl-12 md:pl-14 pr-24 md:pr-28 rounded-full border border-outline-variant/30 bg-transparent focus:bg-white focus:ring-2 focus:ring-primary text-body-lg placeholder:text-outline outline-none"
                    placeholder="Search for services, products, or issues..." type="text">"""
new_input = """<input id="home-search-input"
                    class="w-full h-14 pl-12 md:pl-14 pr-24 md:pr-28 rounded-full border border-outline-variant/30 bg-transparent focus:bg-white focus:ring-2 focus:ring-primary text-body-lg placeholder:text-outline outline-none"
                    placeholder="Search for services, products, or issues..." type="text">"""

if old_input in home_content:
    home_content = home_content.replace(old_input, new_input)
else:
    # fallback regex
    home_content = re.sub(r'<input\s+class="w-full h-14 pl-12[^"]*"\s+placeholder="Search for services, products, or issues..." type="text">', new_input, home_content)

# injecting the script
script_injection = """
            // Home Page Search Logic
            const homeSearchInput = document.getElementById('home-search-input');
            if (homeSearchInput) {
                homeSearchInput.addEventListener('keypress', function (e) {
                    if (e.key === 'Enter') {
                        const query = this.value.toLowerCase().trim();
                        if (!query) return;
                        
                        // Service Keywords
                        if (query.includes('repair') || query.includes('service') || query.includes('fix')) {
                            window.location.href = 'service.html';
                            return;
                        }

                        // Product Keywords
                        if (query.includes('laptop') || query.includes('macbook')) {
                            window.location.href = `laptops.html?search=${encodeURIComponent(query)}`;
                        } else if (query.includes('desktop') || query.includes('pc') || query.includes('computer')) {
                            window.location.href = `desktops.html?search=${encodeURIComponent(query)}`;
                        } else if (query.includes('printer') || query.includes('epson') || query.includes('canon') || query.includes('ink')) {
                            window.location.href = `printers.html?search=${encodeURIComponent(query)}`;
                        } else if (query.includes('mouse') || query.includes('keyboard') || query.includes('accessory') || query.includes('accessories') || query.includes('cable')) {
                            window.location.href = `accessories.html?search=${encodeURIComponent(query)}`;
                        } else {
                            // Default redirect to main product page for broad searching
                            window.location.href = `product.html?search=${encodeURIComponent(query)}`;
                        }
                    }
                });
            }
"""

if "Home Page Search Logic" not in home_content:
    home_content = home_content.replace('// Mic Recording Logic', script_injection + '\n            // Mic Recording Logic')

with open('home.html', 'w', encoding='utf-8') as file:
    file.write(home_content)

print("Modifications done!")
