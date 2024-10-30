import feedparser
import time
from datetime import datetime

URL = "https://def-init.tistory.com/rss"  # URL = "내블로그 주소/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break

    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

print(markdown_text)


# 현재 날짜를 '월 이름 일, 년' 형식으로 포맷
today_date = datetime.now().strftime("%B %d, %Y")

# 메시지 출력
print(f"# Hello, {today_date}! Let's give it our best today!")