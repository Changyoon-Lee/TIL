import requests
from bs4 import BeautifulSoup
import os

url = 'https://github.com/Changyoon-Lee/TIL/tree/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B3%B5%EB%B6%80/programmers'
github_url = 'https://github.com/'

resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'lxml')
tag = soup.select('div span a')

title = []
link = []

with open('README.md','wt') as f:
    f.write('# 프로그래머스 알고리즘 문제 풀이\n\n')
    
    for idx, i in enumerate(tag):
        if idx%5==0:
            f.write('   ')
        try:
            f.write('[{}]({})\t\t'.format(i['title'], github_url+i['href']))
        except:
            pass

os.system('git add .')
os.system('git commit -m "readme_update"')
os.system('git push')
# os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())