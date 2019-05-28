import requests
from bs4 import BeautifulSoup
import re

def trans(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }
    chapter_html2 = requests.get(url, headers=headers)
    chapter_html2.encoding = 'utf-8'
    soup22 = BeautifulSoup(chapter_html2.text, 'html.parser')
    num = int(re.findall('\d+', soup22.get_text())[-1])
    first_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(num)
    return first_url

def ans(times):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }
    first_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
    for i in range(times):
        first_url = trans(first_url)
        print(first_url)
    return first_url

print(ans(400))
