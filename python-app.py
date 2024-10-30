import feedparser
import time
from datetime import datetime

URL = "https://def-init.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

# 현재 날짜를 '월 이름 일, 년' 형식으로 포맷
today_date = datetime.now().strftime("%B %d, %Y")

hello_there = f"## Hello, {today_date}! Let's give it our best today💪"
recently_posts = ""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break

    else:
        feed_date = feed['published_parsed']
        recently_posts += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"



markdown_text = f"""{hello_there}

### 🚀About Me

- Studying to become an **NLP AI researcher**; interested in open-source contributions.
- On a break from senior year in Electronics Engineering at The Catholic University of Korea (GPA 4.3/4.5).
- Enrolled in **Naver Boostcamp AI Tech** program.

### ✏️ Log
{recently_posts}

<div align="center">

#### 💡 More posts here

[![Velog Badge](http://img.shields.io/badge/Tistory-F76A1C?style=flat-square&logo=Tistory&logoColor=white&link=https://def-init.tistory.com)](https://def-init.tistory.com/)
&nbsp;&nbsp;
[![Velog Badge](http://img.shields.io/badge/Velog-20C997?style=flat-square&logo=Velog&logoColor=white&link=https://velog.io/@kms39273/posts)](https://velog.io/@kms39273/posts)
&nbsp;&nbsp;
[![Naver Badge](https://img.shields.io/badge/Naver-03C75A?style=flat-square&logo=Naver&logoColor=white&link=https://blog.naver.com/def__init__)](https://blog.naver.com/def__init__)

</div>

<div align="center">

<img src="https://github.com/user-attachments/assets/8fa48fc4-0b28-4ea3-9f77-241896097d70" style="width: 50%;">

### See you👋

</div>

"""

# 추후 다듬고 추가할 예정
temp = """
### 🎓 Education

### [네이버 부스트 캠프 AI Tech 7기](https://boostcamp.connect.or.kr/program_ai.html)

#### NLP트랙
- 2024.08. ~ 2025.02.

### [네트워크과학 연구실](https://nslab-cuk.github.io/)
#### 학부연구생
- 2023.07. ~ 2024.05.

### [가톨릭대학교](https://www.catholic.ac.kr/ko/index.do)
#### 정보통신전자공학부 1전공
#### 컴퓨터정보공학부 2전공
#### 인공지능학과 부전공

- 2019.03. ~ 2025.08.


### 🪧 My Stats

<div align="center">
    <picture>
        <img width="40%" src="http://mazassumnida.wtf/api/generate_badge?boj=kms39273">
    </picture>
    &nbsp;&nbsp;&nbsp;
    <picture>
        <img width="47%" src="https://github-readme-stats.vercel.app/api?username=luckyvickyricky&show_icons=true&theme=dark">
    </picture>
</div>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fcukminseo&count_bg=%23A9AFA5&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
"""


f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()