import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

# 스크래핑할 웹 페이지의 URL로 HTTP 요청을 보냅니다.
url = "https://hkebi.tistory.com/2486"
response = requests.get(url)

# BeautifulSoup으로 웹 페이지의 HTML 내용을 파싱합니다.
soup = BeautifulSoup(response.content, "html.parser")

# 웹 페이지 내 모든 이미지(<img> 태그)를 찾아서 다운로드합니다.
for idx, img in enumerate(soup.find_all('img')):
    img_url = img.get('src')

    # 이미지 URL을 기반으로 파일 이름을 생성합니다.
    filename = f'image_{idx}.{img_url.split(".")[-1]}'

    # 이미지를 다운로드하고 저장합니다.
    img_data = requests.get(img_url).content
    with open(filename, 'wb') as f:
        f.write(img_data)

    # 다운로드한 이미지를 Pillow로 열어 크기를 확인합니다.
    with Image.open(filename) as img:
        width, height = img.size

    print(f'Downloaded image with URL: {img_url} and size: {width}x{height}')

    # 이미지를 100x100 크기로 리사이즈합니다.
    resized_img = Image.open(filename).resize((100, 100))

    # 리사이즈한 이미지를 저장합니다.
    resized_filename = f'resized_image_{idx}.png'
    resized_img.save(resized_filename)

    print(f'Resized image saved with filename: {resized_filename}')

# 다운로드한 이미지를 저장할 폴더를 생성합니다.
if not os.path.exists('/Users/jason/study/chatGPT/results'):
    os.makedirs('/Users/jason/study/chatGPT/results')

# 이미지를 다운로드한 폴더와 리사이즈한 이미지를 저장할 폴더를 생성합니다.
if not os.path.exists('resized_images'):
    os.makedirs('resized_images')

# 현재 디렉토리에 있는 이미지 파일을 다운로드한 폴더로 이동합니다.
for filename in os.listdir('.'):
    if filename.startswith('image_'):
        os.rename(filename, os.path.join('/Users/jason/study/chatGPT/results', filename))

# 현재 디렉토리에 있는 리사이즈한 이미지 파일을 리사이즈한 이미지를 저장할 폴더로 이동합니다.
for filename in os.listdir('.'):
    if filename.startswith('resized_image_'):
        os.rename(filename, os.path.join('resized_images', filename))
