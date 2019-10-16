from requests_html import HTMLSession

session = HTMLSession()

# Yahoo!ニュースの主要ニュースの見出しを出力
r = session.get("https://news.yahoo.co.jp/")

print(r.html.url)
items = r.html.find(".topicsListItem", first=False)
for item in items:
    print(item.text)
