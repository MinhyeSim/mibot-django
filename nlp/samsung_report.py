from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from icecream import ic
from context.domains import File, Reader


class Solution(Reader):
    def __init__(self):
        self.okt = Okt()
        self.file = File()
        self.file.context = './data/'

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. crime_in_seoul.csv, 구글맵 API 를 이용해서 서울시내 경찰서 주소목록파일(police_pos.csv)을 작성하시오.')
            print('2. us-states.json, us_unemployment.csv 를 이용해서 미국 실업률 지도(folium_test.html)를 작성하시오.')
            print('3. cctv_in_seoul.csv, pop_in_seoul.csv 를 이용해서 서울시내 경찰서 주소목록파일(cctv_pop.csv)을 작성하시오.')
            print('4. police_pos.csv, 를 이용해서 경찰서 범죄검거율 정규화파일(police_norm.csv)을 작성하시오.')
            print('5. .')
            return input('메뉴 선택 \n')

    def read_file(self):
        file = self.file
        file.fname = 'kr-Report_2018.txt'
        report = self.csv(file)
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        with open(report, 'r', encoding='utf-8') as f:
            texts = f.read()
            return texts
if __name__ == '__main__':
    Solution().read_file()