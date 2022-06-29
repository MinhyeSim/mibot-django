import math
import urllib.request
from collections import Counter, defaultdict

import pandas as pd
from bs4 import BeautifulSoup

from matplotlib import pyplot as plt
from matplotlib import rc, font_manager

from context.domains import Reader, File

rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
import numpy as np
import re
import jpype
from konlpy.tag import Okt
from wordcloud import WordCloud



class Solution(Reader):
    def __init__(self, k=0.5):
        self.movie_comments = pd.DataFrame()
        self.file = File()
        self.file.context = './data/'
        self.k = k
        self.work_probs = []

    def hook(self):
        self.preprocess()
        self.abc()
        self.review()

    def carwling(self):
        file = self.file
        file.fname = 'movie_review.txt'
        path = self.new_file(file)
        f = open(path, 'w', encoding='UTF-8')

        # -- 500페이지까지 크롤링
        for no in range(1, 501):
            url = 'https://movie.naver.com/movie/point/af/list.naver?&page=%d' % no
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')

            reviews = soup.select('tbody > tr > td.title')
            for rev in reviews:
                rev_lst = []
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
    def preprocess(self):
        file = self.file
        file.fname = 'movie_review.txt'
        path = self.new_file(file)
        self.movie_comments = pd.read_csv(path, delimiter='\t',
                                          names=['title', 'score', 'comment', 'label'])  # -- 본인 환경에 맞게 설치 경로 변경할 것

        self.movie_comments.to_csv('./save/movie_comments.csv', index=False)


    def abc(self):
        self.movie_comments.info()
        # 코멘트가 없는 리뷰 데이터(NaN) 제거
        df_reviews = self.movie_comments.dropna()
        # 중복 리뷰 제거
        df_reviews = df_reviews.drop_duplicates(['comment'])

        df_reviews.info()
        df_reviews.head(10)
        # 영화 리스트 확인
        movie_lst = df_reviews.title.unique()
        #print('전체 영화 편수 =', len(movie_lst))
        #print(movie_lst[:10])
        # 각 영화 리뷰 수 계산
        cnt_movie = df_reviews.title.value_counts()
        #print(cnt_movie[:20])
        # 각 영화 평점 분석
        info_movie = df_reviews.groupby('title')['score'].describe()
        print(info_movie.sort_values(by=['count'], axis=0, ascending=False))
        # 긍정, 부정 리뷰 수
        df_reviews.label.value_counts()

        top10 = df_reviews.title.value_counts().sort_values(ascending=False)[:10]
        top10_title = top10.index.tolist()
        top10_reviews = df_reviews[df_reviews['title'].isin(top10_title)]

        print(top10_title)
        print(top10_reviews.info())
        movie_title = top10_reviews.title.unique().tolist()  # -- 영화 제목 추출
        avg_score = {}  # -- {제목 : 평균} 저장
        for t in movie_title:
            avg = top10_reviews[top10_reviews['title'] == t]['score'].mean()
            avg_score[t] = avg

        plt.figure(figsize=(10, 5))
        plt.title('영화 평균 평점 (top 10: 리뷰 수)\n', fontsize=17)
        plt.xlabel('영화 제목')
        plt.ylabel('평균 평점')
        plt.xticks(rotation=20)

        for x, y in avg_score.items():
            color = np.array_str(np.where(y == max(avg_score.values()), 'orange', 'lightgrey'))
            plt.bar(x, y, color=color)
            plt.text(x, y, '%.2f' % y,
                     horizontalalignment='center',
                     verticalalignment='bottom')

        plt.show()
        fig, axs = plt.subplots(5, 2, figsize=(15, 25))
        axs = axs.flatten()

        for title, avg, ax in zip(avg_score.keys(), avg_score.values(), axs):
            num_reviews = len(top10_reviews[top10_reviews['title'] == title])
            x = np.arange(num_reviews)
            y = top10_reviews[top10_reviews['title'] == title]['score']
            ax.set_title('\n%s (%d명)' % (title, num_reviews), fontsize=15)
            ax.set_ylim(0, 10.5, 2)
            ax.plot(x, y, 'o')
            ax.axhline(avg, color='red', linestyle='--')  # -- 평균 점선 나타내기

        plt.show()
        fig, axs = plt.subplots(5, 2, figsize=(15, 25))
        axs = axs.flatten()
        colors = ['pink', 'gold', 'whitesmoke']
        labels = ['1 (8~10점)', '0 (1~4점)', '2 (5~7점)']

        for title, ax in zip(avg_score.keys(), axs):
            num_reviews = len(top10_reviews[top10_reviews['title'] == title])
            values = top10_reviews[top10_reviews['title'] == title]['label'].value_counts()
            ax.set_title('\n%s (%d명)' % (title, num_reviews), fontsize=15)
            ax.pie(values,
                   autopct='%1.1f%%',
                   colors=colors,
                   shadow=True,
                   startangle=90)
            ax.axis('equal')
        plt.show()
    def review(self):
        self.movie_comments.info()
        # 코멘트가 없는 리뷰 데이터(NaN) 제거
        df_reviews = self.movie_comments.dropna()
        # 중복 리뷰 제거
        df_reviews = df_reviews.drop_duplicates(['comment'])

        pos_reviews = df_reviews[df_reviews['label'] == 1]
        neg_reviews = df_reviews[df_reviews['label'] == 0]
        # -- 긍정 리뷰
        pos_reviews['comment'] = pos_reviews['comment'].apply(lambda x: re.sub(r'[^ㄱ-ㅣ가-힝+]', ' ', x))
        # -- 부정 리뷰
        neg_reviews['comment'] = neg_reviews['comment'].apply(lambda x: re.sub(r'[^ㄱ-ㅣ가-힝+]', ' ', x))

        okt = Okt()
        pos_comment_nouns = []
        for cmt in pos_reviews['comment']:
            pos_comment_nouns.extend(okt.nouns(cmt))  # -- 명사만 추출
        # -- 추출된 명사 중에서 길이가 1보다 큰 단어만 추출
        pos_comment_nouns2 = []
        word = [w for w in pos_comment_nouns if len(w) > 1]
        pos_comment_nouns2.extend(word)
        #print(pos_comment_nouns2)
        pos_word_count = Counter(pos_comment_nouns2)

        #print(pos_word_count)
        max = 20
        pos_top_20 = {}
        for word, counts in pos_word_count.most_common(max):
            pos_top_20[word] = counts
            print(f'{word} : {counts}')
        font_path = './data/D2Coding.ttf'
        wc = WordCloud(font_path, background_color='ivory', width=800, height=600)
        cloud = wc.generate_from_frequencies(pos_word_count)
        plt.figure(figsize=(8, 8))
        plt.imshow(cloud)
        plt.axis('off')
        plt.show()



    def naiveBayesClassifier(self):

       self.load_corpus()

    def load_corpus(self):

        file = self.file
        file.context = './save/'
        file.fname = 'movie_reviews.txt'
        corpus = pd.read_table(self.new_file(file), names=['title', 'point', 'doc', 'label'])
        corpus.drop(columns=['title','label'], inplace=True)
        corpus.to_csv('./save/movie.csv', index=False)
        corpus = corpus[['doc', 'point']] #타입이 데이터 프레임
        corpus = np.array(corpus) #데이터프레임은 수정을 못하니까 array로 변경
        return corpus

    def count_word(self):
        counts = defaultdict(lambda : [0, 0])
        for doc, point in self.load_corpus():
            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 8 else 1] += 1

    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    # Solution().hook()
    Solution().naiveBayesClassifier()
    #hook을 안쓰기위한 방법. s가 오버라이딩이 되었음.
