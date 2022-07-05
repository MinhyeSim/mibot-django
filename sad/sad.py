import pandas as pd

from context.domains import File,Reader


class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'

    def crawling(self):
        file = self.file
        file.fname = 'origin_validation.xlsx'
        report = self.xls(file)
        a = pd.read_excel(report)
        #a = report.drop(['번호', 'value', '연령', '성별', '상황키워드', '신체질환',
                    #'감정_소분류', '시스템응답1', '시스템응답2', '사람문장3', '시스템응답3'], axis=1)
        print('리뷰 개수 : '+len(a))



    def preprocessing(self):
        pass


if __name__ == '__main__':
    Solution().crawling()