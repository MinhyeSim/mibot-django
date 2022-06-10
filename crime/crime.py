import pandas as pd

from context.domains import Reader, File, Printer


class Solution(Reader):
    def __init__(self):#
        self.file = File()
        # self.reader = Reader()
        # self.printer = Printer()
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.file.context = './data/' # 경로. 2번이상 사용 될 때

    def save_police_pos(self):
        file = self.file
        file.fname = 'crime_in_seoul' #파일 가져오기
        crime = self.csv(file)
        station_name = []
        for name in crime['관서명']:
            station_name.append(f'서울{str(name[:-1])}경찰서')
        station_addrs = []
        station_lats = []
        station_lngs = []
        gmaps = self.gmaps(crime)

    def save_cctv_pos(self):
        self.file.fname = 'cctv_in_seoul'
        self.print(self.csv(self.file))

    def save_police_norm(self):
        pass

    def folium_test(self):
        pass

    def draw_crime_map(self):
        self.file.fname = 'geo_simple'
        self.print(self.json(self.file))

if __name__ == '__main__':
    Solution().save_police_pos()
    Solution().save_cctv_pos()
    Solution().draw_crime_map()

