
from tqdm import tqdm_notebook
from context.domains import File, Reader
import folium
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.parse import urljoin
import re
from tqdm import tqdm

'''
구조를 파악하도록 객체지향으로 분리하는 훈련을 해주세요. 
템플릿 메소드 패턴은 반드시 걸어야 합니다.
1.Preprocessing
2.Tokenization
3.Token Embedding
4.Document Embedding
'''

class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'
        self.url_base = 'https://www.chicagomag.com/'
        self.url_sub = '/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
        self.url = self.url_base + self.url_sub

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. 전처리')
            print('2. 필터')
            print('3. 맵')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.preprocess()
            elif menu == '2':
                self.filter()
            elif menu == '3':
                self.map()
            elif menu == '0':
                break

    def preprocess(self):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'}) #접근방지 오류 해결 코드
        html = urlopen(req)
        soup = BeautifulSoup(html, "html.parser")
        tmp_one = soup.find_all('div', 'sammy')[0]
        tmp_one.find(class_='sammyRank').get_text()
        tmp_one.find('a')['href']
        tmp_string = tmp_one.find(class_='sammyListing').get_text()

        re.split(('\n|\r\n'), tmp_string)
        rank = []
        main_menu = []
        cafe_name = []
        url_add = []

        list_soup = soup.find_all('div', 'sammy')

        for item in list_soup:
            rank.append(item.find(class_='sammyRank').get_text())
            tmp_string = item.find(class_='sammyListing').get_text()
            main_menu.append(re.split(('\n|\r\n'), tmp_string)[0])
            cafe_name.append(re.split(('\n|\r\n'), tmp_string)[1])
            url_add.append(urljoin(self.url_base, item.find('a')['href']))

        data = {'Rank': rank, 'Menu': main_menu, 'Cafe': cafe_name, 'URL': url_add}
        df = pd.DataFrame(data, columns=['Rank', 'Cafe', 'Menu', 'URL'])
        df.to_csv("./data/best_sandwiches_list_chicago.csv", sep=',', encoding='UTF-8')

    def filter(self):
        file = self.file
        file.fname = 'best_sandwiches_list_chicago'
        df = self.csv(file)
        price = []
        address = []

        for i in df['URL']:
            req = Request(i, headers={'User-Agent': 'Mozilla/5.0'})
            html = urlopen(req)
            soup_tmp = BeautifulSoup(html, 'lxml')
            gettings = soup_tmp.find('p', 'addy').get_text()
            price.append(gettings.split()[0][:-1])
            address.append(' '.join(gettings.split()[1:-2]))
        df['Price'] = price
        df['Address'] = address
        df = df.loc[:, ['Rank', 'Cafe', 'Menu', 'Price', 'Address']]
        df.set_index('Rank', inplace=True)
        df.to_csv("./data/best_sandwiches_list_chicago2.csv", sep=',', encoding='UTF-8')



    def map(self):
        file = self.file
        file.fname = 'best_sandwiches_list_chicago2'
        df = self.csv(file)
        gmaps = self.gmaps()
        lat = []
        lng = []

        for n in tqdm(df.index):
            if df['Address'][n] != 'Multiple':
                target_name = df['Address'][n] + ', ' + 'Cicago'
                gmaps_output = gmaps.geocode(target_name)
                location_output = gmaps_output[0].get('geometry')
                lat.append(location_output['location']['lat'])
                lng.append(location_output['location']['lng'])

            else:
                lat.append(np.nan)
                lng.append(np.nan)
        df['lat'] = lat
        df['lng'] = lng
        mapping = folium.Map(location=[df['lat'].mean(), df['lng'].mean()], zoom_start=11)

        for n in df.index:

            if df['Address'][n] != 'Multiple':
                folium.Marker([df['lat'][n], df['lng'][n]], popup=df['Cafe'][n]).add_to(mapping)

        mapping.save('./data/best_sandwiches_list_chicago2_map.html')




if __name__ == '__main__':
    Solution().hook()
