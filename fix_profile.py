import re

with open('profile.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the floating ENG/TAM div block
broken_div = '''                    </div>
                        <div class="flex bg-[#f3f4f5] rounded-full p-1 shrink-0">
                            <button
                                class="px-3 py-1 bg-white rounded-full shadow-[0_1px_4px_rgba(0,0,0,0.1)] text-[11px] font-bold text-[#004d99]">ENG</button>
                            <button
                                class="px-3 py-1 text-[11px] font-bold text-[#44474e] hover:text-[#004d99] transition-colors rounded-full">TAM</button>
                        </div>
                    </div>'''
content = content.replace(broken_div, '')

# 2. Re-replace the inserted "Help & FAQ" inside Settings back to "Rate Our App"
faq_in_settings = '''<a href="home.html#bot"
                        class="flex items-center justify-between py-4.5 px-5 md:px-6 border-b border-[#e1e3e4] hover:bg-[#f8f9fa] transition-colors cursor-pointer"
                        style="text-decoration: none;">
                        <div class="flex items-center gap-4 text-[#1a1b1e]">
                            <span class="material-symbols-outlined text-[20px] text-[#44474e]"
                                style="font-variation-settings: 'FILL' 0;">help</span>
                            <span class="text-[15px] font-medium">Help & FAQ</span>
                        </div>
                        <span class="material-symbols-outlined text-[#74777f] text-[20px]">chevron_right</span>
                    </a>'''
                    
rate_app_anchor = '''<a href="#"
                        class="flex items-center justify-between py-4.5 px-5 md:px-6 border-b border-[#e1e3e4] hover:bg-[#f8f9fa] transition-colors cursor-pointer"
                        style="text-decoration: none;">
                        <div class="flex items-center gap-4 text-[#1a1b1e]">
                            <span class="material-symbols-outlined text-[20px] text-[#44474e]"
                                style="font-variation-settings: 'FILL' 0;">star</span>
                            <span class="text-[15px] font-medium">Rate Our App</span>
                        </div>
                        <span class="material-symbols-outlined text-[#74777f] text-[20px]">chevron_right</span>
                    </a>'''
content = content.replace(faq_in_settings, rate_app_anchor)

# 3. Update the native "Help & FAQ" inside Support & Assistance to point to the bot
support_faq_orig = '''<!-- Help & FAQ -->
                    <a href="#"
                        class="bg-white rounded-[16px] md:rounded-[20px] p-5 shadow-sm border border-[#e1e3e4] flex items-center gap-4 hover:shadow-md transition-shadow cursor-pointer">
                        <div
                            class="w-12 h-12 rounded-full bg-[#f3f4f5] text-[#44474e] border border-[#c4c6d0] flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined"
                                style="font-variation-settings: 'FILL' 1;">help</span>
                        </div>
                        <h3 class="text-[15px] font-semibold text-[#1a1b1e]">Help & FAQ</h3>
                    </a>'''
                    
support_faq_new = '''<!-- Help & FAQ -->
                    <a href="home.html#bot"
                        class="bg-white rounded-[16px] md:rounded-[20px] p-5 shadow-sm border border-[#e1e3e4] flex items-center gap-4 hover:shadow-md transition-shadow cursor-pointer">
                        <div
                            class="w-12 h-12 rounded-full bg-[#f3f4f5] text-[#44474e] border border-[#c4c6d0] flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined"
                                style="font-variation-settings: 'FILL' 1;">help</span>
                        </div>
                        <h3 class="text-[15px] font-semibold text-[#1a1b1e]">Help & FAQ</h3>
                    </a>'''
content = content.replace(support_faq_orig, support_faq_new)


with open('profile.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Changes successfully applied to profile.html!")
