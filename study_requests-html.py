from requests_html import HTMLSession

session = HTMLSession()

# Yahoo!ニュースの主要ニュースの見出しを出力
r = session.get("https://news.yahoo.co.jp/")

print(r.html.url)
items = r.html.find(".topicsListItem", first=False)
for item in items:
    print(item.text)
    # 重複を除くためset型で返されるのでlistに変換しておく
    link = list(item.absolute_links)
    
    # 詳細ページのサマリ表示する
    r_detail = session.get(link[0])
    item_detail = r_detail.html.find(".tpcNews_summary", first=True)
    print(item_detail.text)
