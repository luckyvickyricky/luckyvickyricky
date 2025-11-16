from datetime import datetime, timedelta

import feedparser
import pytz

# 한국 시간대 설정
seoul_tz = pytz.timezone("Asia/Seoul")

# 한국 시간(KST)로 현재 날짜 가져오기
today_date = datetime.now(seoul_tz).strftime("%B %d, %Y")

RSS_MAX_POST = 5

# tistory RSS parser
TISTORY_RSS_URL = "https://def-init.tistory.com/rss"
TISTORY_RSS_FEED = feedparser.parse(TISTORY_RSS_URL)

recently_tistory_posts = ""

for idx, feed in enumerate(TISTORY_RSS_FEED["entries"]):
    if idx >= RSS_MAX_POST:
        break

    else:
        # 받아온 RSS시간에 9시간을 더하여 한국 시간대로 변환(RSS설정을 KST로 설정했으나 UTC로 받아오는 문제 발생)
        feed_date_utc = datetime(*feed["published_parsed"][:6])
        feed_date_kst = feed_date_utc + timedelta(hours=9)
        escaped_title = feed["title"].replace("]", "\\]").replace("[", "\\[")
        recently_tistory_posts += f"[{feed_date_kst.strftime('%Y/%m/%d')} - {escaped_title}]({feed['link']}) <br/>\n"


# velog RSS parser
VELOG_RSS_URL = "https://api.velog.io/rss/@kms39273"
VELOG_RSS_FEED = feedparser.parse(VELOG_RSS_URL)
recently_velog_posts = ""

for idx, feed in enumerate(VELOG_RSS_FEED["entries"]):
    if idx >= RSS_MAX_POST:
        break
    feed_date_utc = datetime(*feed["published_parsed"][:6])
    feed_date_kst = feed_date_utc + timedelta(hours=9)

    recently_velog_posts += f"[{feed_date_kst.strftime('%Y/%m/%d')} - {feed['title']}]({feed['link']}) <br/>\n"


markdown_text = f"""## Hello, {today_date}:D Let's give it our best shot.

### 🚀About Me

- Studying to become an **AI researcher**; interested in LLM alignment tuning, quantization, etc.
- B.S. in EE & CS (GPA 4.3/4.5, **Ranked 1st**).
- Interested in open-source contributions.

### ✏️ Study Logs
{recently_tistory_posts}
[See all...](https://def-init.tistory.com)

### ✍🏻 Retrospective Logs, News
{recently_velog_posts}
[See all...](https://velog.io/@kms39273/posts)

### 📍 Milestones

| Period | Experience |
| ------ | ---------- |
| Oct 2025 - Present | **AI Engineer** @ [Nota AI](https://nota.ai/) |
| Aug 2025 - Oct 2025 | **Hugging Face Open Source Contributor** @ [OSSCA](https://www.contribution.ac/) |
| May 2025 - Aug 2025 | **AI Research Engineer** @ [Upstage](https://www.upstage.ai/) |
| Aug 2024 - Feb 2025 | **NLP Track** @ [Naver Boostcamp AI Tech 7th](https://boostcamp.connect.or.kr/program_ai.html) |
| Aug 2023 - Jul 2024 | **Undergraduate Researcher** @ [Network Science Lab, CUK](https://nslab-cuk.github.io/) |

<div align="center">

<table border="0">
<tr>
<td width="50%">

### 🏆 Awards

| Date | Award |
| ---- | ----- |
| Sep 2025 | **3rd Place** - AWS Hackathon |

</td>
<td width="50%">

### 🎓 Certifications

| Date | Certification |
| ---- | ------------- |
| Apr 2025 | [AWS Certified ML - Specialty](https://www.credly.com/badges/54edcc42-016b-4e57-8138-54e3e25c4cec/linked_in_profile) |
| Apr 2025 | [AWS Certified ML Engineer - Associate](https://www.credly.com/badges/6e181d13-c2f5-4374-aa2a-374d8f07b93a/linked_in_profile) |

</td>
</tr>
</table>


### See you👋

</div>

"""

# 추후 다듬고 추가할 예정
temp = """


<img src="https://github.com/user-attachments/assets/8fa48fc4-0b28-4ea3-9f77-241896097d70" style="width: 50%;">

<div align="center">

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

- 2019.03. ~ 2025.08.


### 🪧 My Stats

<div align="center">
    <picture>
        <img width="40%" src="http://mazassumnida.wtf/api/generate_badge?boj=kms39273">
    </picture>
    &nbsp;&nbsp;&nbsp;
    <picture>
        <img width="47%" src="https://github-readme-stats.vercel.app/api?username=nevertmr&show_icons=true&theme=dark">
    </picture>
</div>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fcukminseo&count_bg=%23A9AFA5&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
"""


f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
