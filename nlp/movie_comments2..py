from bs4 import BeautifulSoup
import urllib.request
from context.domains import File, Reader
import re
import pandas as pd
from wordcloud import WordCloud
from konlpy.tag import Okt
from icecream import ic


class Solution(Reader):
    def __init__(self):
        self.movie_comments = pd.DataFrame()
        self.file = File()
        self.file.context = './data/'

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. 전처리 : 텍스트 마이닝(크롤링)')
            print('2. 전처리 :DF로 정형화')
            print('3. 토큰화')
            print('4. 임베딩')
            print('5. ')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.crawling()
            elif menu == '2':
                self.preprocess()
            elif menu == '3':
                pass

    def preprocess(self):
        self.steroetype()
        ic(self.movie_comments.head(5))
        ic(self.movie_comments)


    def crawling(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        f = open(path, 'w', encoding='UTF-8')

        # -- 500페이지까지 크롤링
        for no in range(1, 501):
            url = 'https://movie.naver.com/movie/point/af/list.naver?&page=%d' % no
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')
            reviews = soup.select('tbody > tr > td.title')
            for rev in reviews:
                title = rev.select_one('a.movie').text.strip()
                score = rev.select_one('div.list_netizen_score > em').text.strip()
                comment = rev.select_one('br').next_sibling.strip()

                # -- 긍정/부정 리뷰 레이블 설정
                if int(score) >= 8:
                    label = 1  # -- 긍정 리뷰 (8~10점)
                elif int(score) <= 4:
                    label = 0  # -- 부정 리뷰 (0~4점)
                else:
                    label = 2

                f.write(f'{title}\t{score}\t{comment}\t{label}\n')



    def steroetype(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        self.movie_comments = pd.read_csv(path, delimiter='\t',
                           names=['title', 'score', 'comment', 'label'])  # -- 본인 환경에 맞게 설치 경로 변경할 것

    def tokenization(self):
        pass

    def embedding(self):
        pass

if __name__ == '__main__':
    Solution().hook()

