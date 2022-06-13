from context.domains import Reader, File
import folium

class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. crime_in_seoul.csv, 구글맵 API 를 이용해서 서울시내 경찰서 주소목록파일을 작성하시오.')
            print('2. us-states.json, us_unemployment.csv 를 이용해서 미국 실업률 지도를 작성하시오.')
            print('3. 삭제')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.save_police_pos()
            if menu == '2':
                self.folium_test()
            if menu == '3':
                pass
            elif menu == '0':
                break

    def save_police_pos(self):
        file = self.file
        file.fname = 'crime_in_seoul'
        crime = self.csv(file)
        station_names = []
        for name in crime['관서명']:
            station_names.append(f'서울{str(name[:-1])}경찰서')
        # print(f'station_names range: {len(station_names)}')
        ''' 서울시내 경찰서는 31개이다. '''
        # print([{i:name} for i, name in enumerate(station_names) ])
        '''
        [{0: '서울중부경찰서'}, {1: '서울종로경찰서'}, {2: '서울남대문경찰서'}, ... , {21: '서울종암경찰서'}
        '''
        gmaps = self.gmaps()

        '''
        a = gmaps.geocode('서울중부경찰서', language='ko')
        print(a)
        [{'address_components': 
            [{'long_name': '２７', 'short_name': '２７', 'types': ['premise']}, 
            {'long_name': '수표로', 'short_name': '수표로', 'types': ['political', 'sublocality', 'sublocality_level_4']}, 
            {'long_name': '중구', 'short_name': '중구', 'types': ['political', 'sublocality', 'sublocality_level_1']}, 
            {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']}, 
            {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']}, 
            {'long_name': '100-032', 'short_name': '100-032', 'types': ['postal_code']}], 
            'formatted_address': '대한민국 서울특별시 중구 수표로 27', 
            'geometry': {'location': 
                {'lat': 37.56361709999999, 'lng': 126.9896517}, 
                'location_type': 'ROOFTOP', 
                'viewport': {'northeast': {'lat': 37.5649660802915, 'lng': 126.9910006802915}, 
                'southwest': {'lat': 37.5622681197085, 'lng': 126.9883027197085}}}, 
                'partial_match': True, 'place_id': 'ChIJc-9q5uSifDURLhQmr5wkXmc', 
                'plus_code': {'compound_code': 'HX7Q+CV 대한민국 서울특별시', 'global_code': '8Q98HX7Q+CV'}, 
                'types': ['establishment', 'point_of_interest', 'police']}]
        서울종암경찰서는 2021.12.20부터 이전함
        '''

        station_addrs = []
        station_lats = []
        station_lngs = []

        for i, name in enumerate(station_names) :
            if name != '서울종암경찰서':
                temp = gmaps.geocode(name, language='ko')
            else:
                temp = [{'address_components':
            [{'long_name': '32', 'short_name': '32', 'types': ['premise']},
            {'long_name': '화랑로7길', 'short_name': '화랑로7길', 'types': ['political', 'sublocality', 'sublocality_level_4']},
            {'long_name': '성북구', 'short_name': '성북구', 'types': ['political', 'sublocality', 'sublocality_level_1']},
            {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']},
            {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']},
            {'long_name': '100-032', 'short_name': '100-032', 'types': ['postal_code']}],
            'formatted_address': '대한민국 서울특별시 성북구 화랑로7길 32',
            'geometry': {'location':
                {'lat': 37.60388169879458, 'lng': 127.04001571848704},
                'location_type': 'ROOFTOP',
                'viewport': {'northeast': {'lat': 37.60388169879458, 'lng': 127.04001571848704},
                'southwest': {'lat': 37.60388169879458, 'lng': 127.04001571848704}}},
                'partial_match': True, 'place_id': 'ChIJc-9q5uSifDURLhQmr5wkXmc',
                'plus_code': {'compound_code': 'HX7Q+CV 대한민국 서울특별시', 'global_code': '8Q98HX7Q+CV'},
                'types': ['establishment', 'point_of_interest', 'police']}]

            #print(f'name {i} = {temp[0].get("formatted_address")}')
            '''
            0번 중부서인 경우는 "대한민국 서울특별시 중구 수표로 27"이 담긴다.
            1번 종로서인 경우는 "대한민국 서울특별시 종로구 율곡로 46"이 담긴다.
            '''
            station_addrs.append(temp[0].get('formatted_address'))
            t_loc = temp[0].get('geometry')
            station_lats.append(t_loc['location']['lat'])
            station_lats.append(t_loc['location']['lng'])

            gu_names = []
            for name in station_addrs:
                temp = name.split()
                gu_name = [gu for gu in temp if gu[-1] == '구'][0]
                gu_names.append(gu_name)
            print(gu_name)



    def save_cctv_pos(self):
        file = self.file
        file.fname = 'cctv_in_seoul'
        cctv = self.csv(file)
        pop = None # 헤더는 2행, 사용하는 컬럼은 B, D, G, J, N 을 사용한다.
        file.fname = 'pop_in_seoul'
        cols = "B,D,G,J,N"
        header = [1]
        pop = self.xls(file,header,cols)
        print(pop)
        '''
             자치구        합계      한국인   등록외국인  65세이상고령자
        0    자치구         계        계       계  65세이상고령자
        1     합계  10197604  9926968  270636   1321458
        2    종로구    162820   153589    9231     25425
        3     중구    133240   124312    8928     20764
        4    용산구    244203   229456   14747     36231
        '''



    def save_police_norm(self):
        pass

    def folium_test(self):
        file = self.file
        file.fname = 'us-states.json'
        states = self.new_file(file)
        file.fname = 'us_unemployment'
        unemployment = self.csv(file)
        print(unemployment)
        bins = list(unemployment["Unemployment"].quantile([0, 0.25, 0.5, 0.75, 1]))
        m = folium.Map(location=[48, -102], zoom_start=5)
        folium.Choropleth(
            geo_data=states,  # dataframe 아님
            name="choropleth",
            data=unemployment,
            columns=["State", "Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name="Unemployment Rate (%)",
            bins=bins,
            reset=True
        ).add_to(m)
        m.save("./save/folium_test.html")

    def draw_crime_map(self):
        file = self.file
        file.fname = 'geo_simple'
        a = self.csv(file)
        print(a)

if __name__ == '__main__':
    Solution().hook()

