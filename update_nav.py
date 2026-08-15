import os
import re

nav_template = """    <!-- Bottom Mobile Nav Bar -->
    <nav class="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-outline-variant/30 flex justify-between items-center px-6 py-2.5 pb-[calc(10px+env(safe-area-inset-bottom))] z-[100] shadow-[0_-4px_16px_rgba(0,0,0,0.03)]">
        <a href="home.html" class="flex flex-col items-center gap-1 {home_color} transition-colors" style="text-decoration: none;">
            <span class="material-symbols-outlined text-[24px]"{home_fill}>home</span>
            <span class="text-[10px] font-bold">Home</span>
        </a>
        <a href="service.html" class="flex flex-col items-center gap-1 {service_color} transition-colors" style="text-decoration: none;">
            <span class="material-symbols-outlined text-[24px]"{service_fill}>build</span>
            <span class="text-[10px] font-bold">Services</span>
        </a>
        <a href="product.html" class="flex flex-col items-center gap-1 {product_color} transition-colors" style="text-decoration: none;">
            <span class="material-symbols-outlined text-[24px]"{product_fill}>shopping_bag</span>
            <span class="text-[10px] font-bold">Products</span>
        </a>
        <a href="profile.html" class="flex flex-col items-center gap-1 {profile_color} transition-colors" style="text-decoration: none;">
            <span class="material-symbols-outlined text-[24px]"{profile_fill}>person</span>
            <span class="text-[10px] font-bold">Profile</span>
        </a>
    </nav>"""

html_files = [
    'home.html', 'service.html', 'product.html', 'profile.html', 
    'edit-profile.html', 'notifications.html', 
    'laptops.html', 'desktops.html', 'printers.html', 'accessories.html'
]

for file in html_files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine active tab
    active = 'home'
    if file == 'service.html':
        active = 'service'
    elif file in ['product.html', 'laptops.html', 'desktops.html', 'printers.html', 'accessories.html']:
        active = 'product'
    elif file in ['profile.html', 'edit-profile.html', 'notifications.html']:
        active = 'profile'

    kwargs = {
        'home_color': 'text-on-surface-variant hover:text-[#004d99]', 'home_fill': '',
        'service_color': 'text-on-surface-variant hover:text-[#004d99]', 'service_fill': '',
        'product_color': 'text-on-surface-variant hover:text-[#004d99]', 'product_fill': '',
        'profile_color': 'text-on-surface-variant hover:text-[#004d99]', 'profile_fill': '',
    }
    kwargs[f'{active}_color'] = 'text-[#004d99]'
    kwargs[f'{active}_fill'] = ' style="font-variation-settings: \'FILL\' 1;"'

    new_nav = nav_template.format(**kwargs)

    # replace anything from <!-- Bottom Mobile Nav Bar --> to </nav>
    regex = r"<!-- Bottom Mobile Nav Bar -->\s*<nav[^>]*>.*?</nav>"
    if re.search(regex, content, re.DOTALL):
        content = re.sub(regex, new_nav, content, flags=re.DOTALL)
    else:
        # Fallback if no comment
        regex = r"<nav\s+class=\"md:hidden fixed bottom-0[^>]*>.*?</nav>"
        content = re.sub(regex, new_nav, content, flags=re.DOTALL)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all mobile navs!")
