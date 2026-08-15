import os
import glob
import re

html_files = glob.glob('*.html')

translate_css = """
    <style>
        /* Google Translate specific styling */
        body { top: 0 !important; }
        .goog-te-banner-frame { display: none !important; }
        .goog-te-gadget-icon { display: none; }
        .goog-te-combo {
            border-radius: 12px;
            padding: 8px 12px;
            font-size: 13px;
            font-weight: bold;
            font-family: inherit;
            border: 1px solid rgba(194, 198, 212, 0.5);
            background-color: #f8f9fa;
            color: #1a1b1e;
            cursor: pointer;
            outline: none;
        }
        .goog-te-combo:focus { border-color: #004d99; box-shadow: 0 0 0 1px #004d99; }
        #google_translate_element { margin-left: auto; }
        .goog-logo-link { display: none !important; }
        .goog-te-gadget { color: transparent !important; font-size:0; }
    </style>
</head>
"""

translate_script = """
    <!-- Google Translate Script -->
    <script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({
                pageLanguage: 'en',
                includedLanguages: 'en,ta',
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE
            }, 'google_translate_element');
        }
    </script>
    <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</body>
"""

translate_button = '<div id="google_translate_element"></div>'

btn_pattern = re.compile(r'<button class="lang-btn">.*?expand_more.*?</span>\s*</button>', re.DOTALL)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace button
    content = btn_pattern.sub(translate_button, content)
    
    # 2. Add CSS
    if '/* Google Translate specific styling */' not in content:
        content = content.replace('</head>', translate_css)
        
    # 3. Add JS
    if 'googleTranslateElementInit' not in content:
        content = content.replace('</body>', translate_script)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected into all HTML files successfully.")
