from bs4 import BeautifulSoup
from urllib.request import urlopen

from context.domains import File

'''
구조를 파악하도록 객체지향으로 분리하는 훈련을 해주세요. 
템플릿 메소드 패턴은 반드시 걸어야 합니다.
1.Preprocessing
2.Tokenization
3.Token Embedding
4.Document Embedding
'''

class Solution:
    def __init__(self):
        self.file = File()
        self.url_base = 'http://www.chicagomag.com'
        self.url_sub = '/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
        self.url = self.url_base + self.url_sub

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. chicago sandwich restaurants map')

            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.preprocessing()

    def preprocessing(self):
        #file = self.file
        #file.context = './data/'
        html = urlopen(self.url)
        soup = BeautifulSoup(html, "html.parser")

        print(soup)



if __name__ == '__main__':
    Solution().preprocessing()
