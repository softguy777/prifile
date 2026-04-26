with open(r'c:\work\profile\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Text Replacements
html = html.replace('치명적 결함', '일부 결함')
html = html.replace('원클릭 배포 아키텍처를 완성했습니다.', '배포 아키텍처로 수정했습니다.')

# 2. Accordion Fixes
accordions = ['tusi', 'racon', 'keyvox']

for acc in accordions:
    old_onclick = f'''onclick="document.getElementById('{acc}-details').classList.toggle('hidden'); this.querySelector('svg').classList.toggle('-rotate-180')"'''
    new_onclick = f'''onclick="document.getElementById('{acc}-details').classList.toggle('hidden'); const svg = document.getElementById('{acc}-svg'); if(svg) svg.style.transform = svg.style.transform === 'rotate(180deg)' ? '' : 'rotate(180deg)'; "'''
    html = html.replace(old_onclick, new_onclick)
    
    # We also need to add the IDs to the SVGs.
    # The SVG comes right after the span with "More Detail"
    # Find the block for this accordion
    old_svg = '''<svg class="transition-all duration-300 transform group-hover/btn:translate-y-1" style="margin-left: 0.375rem; width: 0.875rem; height: 0.875rem;" fill="none" viewBox="0 0 24 24" stroke="currentColor" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>'''
    new_svg = f'''<svg id="{acc}-svg" class="transition-all duration-300 group-hover/btn:translate-y-1" style="margin-left: 0.375rem; width: 0.875rem; height: 0.875rem;" fill="none" viewBox="0 0 24 24" stroke="currentColor" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>'''
    
    # To be safe, let's just replace the SVG only in the context of this specific button.
    # Actually, we can just replace old_svg with new_svg iteratively if we match carefully, 
    # but since they are identical strings, replacing them one by one might not match the order if we use replace(old, new, 1).
    # Since we know the order is tusi, racon, keyvox:
    if old_svg in html:
        html = html.replace(old_svg, new_svg, 1)
        
with open(r'c:\work\profile\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed!')
