import re

with open(r'c:\work\profile\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 3. Nav Menu
html = html.replace(
    '<span data-en="Recent Projects" data-ko="최근 프로젝트">Recent Projects</span>',
    '<span data-en="Projects" data-ko="프로젝트">Projects</span>'
)

nav_exp = '<li><a class="group flex items-center py-3" href="#experience"><span class="nav-indicator"></span><span class="nav-text"><span data-en="Experience" data-ko="주요 경력">Experience</span></span></a></li>'
nav_edu = '<li><a class="group flex items-center py-3" href="#education"><span class="nav-indicator"></span><span class="nav-text"><span data-en="Education" data-ko="학력">Education</span></span></a></li>'
if nav_edu not in html:
    html = html.replace(nav_exp, nav_exp + '\n              ' + nav_edu)

html = html.replace(
    '<div class="mt-12 mb-8">\n              <h3 class="text-sm font-bold uppercase tracking-widest text-slate-200 mb-6"><span data-en="Education"',
    '<div id="education" class="mt-12 mb-8 scroll-mt-16 lg:scroll-mt-24">\n              <h3 class="text-sm font-bold uppercase tracking-widest text-slate-200 mb-6"><span data-en="Education"'
)

# 2. Accordions
def modify_onclick(match):
    target = match.group(1)
    return f'''onclick="document.getElementById('{target}').classList.toggle('hidden'); this.querySelector('svg').classList.toggle('-rotate-180')" '''

html = re.sub(r'''onclick="document\.getElementById\('([^']+)'\)\.classList\.toggle\('hidden'\)"\s*''', modify_onclick, html)

# Add duration-300 to SVG
html = html.replace('class="transition-transform group-hover/btn:translate-y-1"', 'class="transition-all duration-300 transform group-hover/btn:translate-y-1"')

# Image rounding and shadow
html = html.replace('rounded border transition-colors', 'rounded-lg border shadow-lg transition-all')

# 4. Past Projects visual separation
past_proj_target = '''<!-- Project 5: Past Major Projects -->
              <li class="mb-12">
                <div class="group relative grid pb-1 transition-all sm:grid-cols-8 sm:gap-8 md:gap-4 lg:hover:!opacity-100 lg:group-hover/list:opacity-50">
                  <div class="absolute -inset-x-4 -inset-y-4 z-0 hidden rounded-md transition motion-reduce:transition-none lg:-inset-x-6 lg:block lg:group-hover:bg-slate-800/20 lg:group-hover:shadow-[inset_0_1px_0_0_rgba(148,163,184,0.1)] lg:group-hover:drop-shadow-lg"></div>'''

past_proj_replace = '''<!-- Project 5: Past Major Projects -->
              <li class="mb-12 mt-20 border-t border-slate-800/50 pt-12">
                <div class="relative grid pb-1 transition-all sm:grid-cols-8 sm:gap-8 md:gap-4">
                  <!-- Background hover effect removed for legacy section -->'''

if past_proj_target in html:
    html = html.replace(past_proj_target, past_proj_replace)
else:
    print("WARNING: past_proj_target not found!")

with open(r'c:\work\profile\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
