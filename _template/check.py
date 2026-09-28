"""上線前檢查：每一頁都要有 Travelpayouts Drive、AdSense、手動廣告格，sitemap 有收錄、沒有 href="#" 空連結。
用法：在 story-home 資料夾裡執行  python3 _template/check.py
"""
import glob, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKS = {
    'Travelpayouts Drive': 'emrld.ltd/NTc4NjI0.js',
    'AdSense 腳本': 'adsbygoogle.js?client=ca-pub-2022028565680247',
}
# 刻意不放進 sitemap 的頁面（寫上原因）
SITEMAP_SKIP = {
    'lighter-and-princess/index.html',  # 跟主站 /lighter-and-princess/ 長文同主題，避免搶關鍵字
}
bad = 0
pages = sorted(p for p in glob.glob(os.path.join(ROOT, '**/index.html'), recursive=True)
               if '/_' not in p.replace(ROOT, ''))
sitemap = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
for p in pages:
    rel = os.path.relpath(p, ROOT)
    s = open(p, encoding='utf-8').read()
    miss = [k for k, v in CHECKS.items() if v not in s]
    if rel != 'index.html' and '<ins class="adsbygoogle"' not in s:
        miss.append('手動廣告格')
    url = 'https://story.knittinghiyori.com/' + os.path.dirname(rel) + ('/' if os.path.dirname(rel) else '')
    if rel.count('/') == 1 and rel not in SITEMAP_SKIP and url not in sitemap:
        miss.append('sitemap 沒有這頁')
    live_lines = [l for l in s.splitlines() if not l.lstrip().startswith('//')]
    if any('href="#"' in l for l in live_lines):
        miss.append('有 href="#" 空連結')
    print(('✅ ' if not miss else '❌ ') + rel + ('' if not miss else '　缺：' + '、'.join(miss)))
    bad += bool(miss)
print(f'\n共 {len(pages)} 頁，{bad} 頁有問題')
sys.exit(1 if bad else 0)
