import random
import string

import numpy as np
import pandas as pd
from icecream import ic
from context.models import Model
from hello.domains import membere_list


class Quiz30:
    @staticmethod
    def create_df(keys, man_num):
        return pd.DataFrame([dict(zip(keys, Quiz30.score0to100(len(keys)))) for _ in range(man_num)])

    @staticmethod
    def create_df_dict(keys, index, data=None):
        return \
            pd.DataFrame.from_dict(dict(zip(keys, Quiz30.score0to100(len(keys), len(index)))), orient='index', columns=index) \
            if data is None else \
                pd.DataFrame.from_dict(dict(zip(keys, data)), orient='index', columns=index)

    @staticmethod
    def create_df_list(keys, index):
        return pd.DataFrame([dict(zip(index, Quiz30.score0to100(len(index)))) for _ in range(len(keys))],
                            index=keys)

    def quiz30_df_4_by_3(self) -> object:
        # ls = [[j * 3 + i for i in range(1, 4)] for j in range(4)]
        # 굳이 위처럼 안해줘도 된다.
        ls = [range(i * 3 + 1, i * 3 + 4) for i in range(4)]
        df = pd.DataFrame(ls, index=range(1, 5), columns=['A', 'B', 'C'])
        ic(df)
        return df

    def quiz31_rand_2_by_3(self) -> object:
        '''
        ls = [[my_random(10, 100) for i in range(3)] for j in range(2)]
        df = pd.DataFrame(ls)
        '''
        df = pd.DataFrame(np.random.randint(10, 100, size=(2, 3)))
        ic(df)
        return df

    @staticmethod
    def score0to100(row_size, column_size=None):
        return np.random.randint(0, 100, size=row_size) if column_size is None \
            else np.random.randint(0, 100, size=(row_size, column_size))

    @staticmethod
    def create_name(name_len=5) -> str:
        return ''.join([random.choice(string.ascii_uppercase)
                        if i == 0 else random.choice(string.ascii_lowercase) for i in range(name_len)])

    def quiz32_df_grade(self) -> object:
        subjects = ['국어', '영어', '수학', '사회']
        names = [self.create_name() for i in range(10)]
        d = {names[j]: self.score0to100(4) for j in range(10)}
        d1 = self.score0to100(10, 4)
        # df = pd.DataFrame.from_dict(d, orient='index', columns=subjects)
        # ic(df)
        # print('*' * 20)
        #
        # df1 = pd.DataFrame(d1, index=names, columns=subjects)
        # ic(df1)
        # print('*' * 20)
        #
        # d2 = dict(zip(names, d1))
        # df2 = pd.DataFrame.from_dict(d2, orient='index', columns=subjects)
        # ic(df2)
        # print('*' * 20)

        d3 = {'index': names,
              'columns': subjects,
              'data': d1,
              'index_names': ['이름'],
              'column_names': ['과목']}
        df3 = pd.DataFrame.from_dict(d3, orient='tight')
        ic(df3)
        print('*' * 20)
        return None

    def quiz33_df_loc(self) -> object:
        grade_df = Model().new_model('grade.csv')
        # ic(grade_df)

        python_scores = grade_df.loc[:, '파이썬']
        ic(type(python_scores))
        ic(python_scores)

        cho_scores = grade_df.loc[['조현국', '홍정명', '김진영']]
        ic(type(cho_scores))
        ic(cho_scores)
        return None

    def quiz34_df_iloc(self) -> str:
        df = self.create_df_dict(membere_list(), ['자바', '파이썬', 'JS', 'SQL'])
        ic(df)

        # Model().save_model('grade.csv', df)
        '''
        ic| df.iloc[0]: a    41
                b    62
                c    63
                d    38
                Name: 0, dtype: int32

        ic| df.iloc[[0]]:     a   b   c   d
                          0  41  62  63  38
        
        ic| df.iloc[[0, 1]]:     a   b   c   d
                             0  41  62  63  38
                             1   9  10  74  88
        
        
        ic| df.iloc[:3]:     a   b   c   d
                         0  41  62  63  38
                         1   9  10  74  88
                         2  36  52  48   5
        
        ic| df.iloc[[True, False, True]]:     a   b   c   d
                                          0  41  62  63  38
                                          2  36  52  48   5
        
        ic| df.iloc[lambda x: x.index % 2 == 0]:     a   b   c   d
                                                 0  41  62  63  38
                                                 2  36  52  48   5
        
        ic| df.iloc[[0, 2], [1, 3]]:     b   d
                                     0  62  38
                                     2  52   5
        
        ic| df.iloc[1:3, 0:3]:     a   b   c
                               1   9  10  74
                               2  36  52  48
        
        ic| df.iloc[:, [True, False, True, False]]:     a   c
                                                    0  41  63
                                                    1   9  74
                                                    2  36  48
        
        ic| df.iloc[:, lambda df: [0, 2]]:     a   c
                                           0  41  63
                                           1   9  74
                                           2  36  48
        '''
        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
