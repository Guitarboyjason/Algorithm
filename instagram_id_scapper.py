import requests
from bs4 import BeautifulSoup

# 인스타그램 게시물 URL
url = 'https://www.instagram.com/p/Co3vWZ-P02D/'

# 요청 헤더 (User-Agent) 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
headers = {
    'User-Agent':'58.0.3029.110'}

# URL 요청
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.content, 'html.parser')

# 댓글 추출
comments = soup.find_all('div', {'class': 'C4VMK'})

# 댓글 작성자 아이디 추출
for comment in comments:
    username = comment.find('a', {'class': 'FPmhX'}).text
    print(username)
