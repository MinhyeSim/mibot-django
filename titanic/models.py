import numpy as np
from icecream import ic
import pandas as pd

from context.domains import Dataset
from context.models import Model
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        '''
        1. entity 를 object로 전환.
        2. train, test, validation(id, label) => object
        3. garbage drop
        4. signal과 noise가 섞인(name) 컬럼의 값 분리 후 noise drop
        5. 자연어로 되어있는 데이터 들을 CPU가 처리 할 수 있게 int 값으로 변경
        '''
        this = self.dataset
        that = self.model
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train.drop('Survived', axis=1, inplace=True)
        this = self.drop_feature(this, 'Cabin', 'Parch', 'Ticket', 'SibSp')
        self.df_info(this)

        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.name_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.fare_ratio(this)
        this = self.drop_feature(this, 'Fare')

        k_fold = self.create_k_fold()
        acc = self.get_accuracy(this, k_fold)
        ic(acc)

        # self.print_this(this)
        # ic(this.train.head(20))
        # ic(this.test.head(20))

        '''
        this = self.pclass_ordinal(this)
        '''
        return this

    @staticmethod
    def df_info(this):
        [print(f'{i.info()}') for i in [this.train, this.test]]

    @staticmethod
    def print_this(this):
        print('*' * 100)
        ic(f'1. Train 의 타입 : {type(this.train)}\n')
        ic(f'2. Train 의 컬럼 : {type(this.train.columns)}\n')
        print(f'3. Train 의 상위 3개 : {this.train.head(3)}\n')
        ic(f'4. Train 의 null의 개수 : {this.train.isnull().sum()}\n')
        ic(f'5. Test 의 타입 : {type(this.test)}\n')
        ic(f'6. Test 의 컬럼 : {this.test.columns}\n')
        ic(f'7. Test 의 상위 3개 : {this.test.head(3)}\n')
        ic(f'8. Test 의 null의 개수 : {this.test.isnull().sum()}\n')
        ic(f'9. id 의 타입 : {type(this.id)}\n')
        ic(f'10. id 의 상위 10개 : {this.id[:10]}\n')
        print('*' * 100)

    @staticmethod
    def create_train(this) -> object:
        return this

    @staticmethod
    def drop_feature(this, *feature):
        [i.drop(list(feature), axis=1, inplace=True) for i in [this.train, this.test]]
        # https://www.geeksforgeeks.org/how-to-drop-one-or-multiple-columns-in-pandas-dataframe/
        # multiple drop
        return this

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        [print(f'{key} is {value}') for key, value in kwargs.items()]

    '''
    Categorical vs. Quantitative
    Cate -> nominal (이름) vs. ordinal (순서)
    Quan -> interval (상대) vs. ratio (절대)
    '''

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def extract_title_from_name(this):
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        return this

    @staticmethod
    def remove_duplicate(this) -> {}:
        a = set()
        [a.update(set(dataset['Title'])) for dataset in [this.train, this.test]]
        # print(a)
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        '''
        Royal (왕족) : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme']
        Mr : ['Mr', 'Mlle']
        Ms : ['Miss', 'Ms']
        Master : ['Master']
        Mrs : ['Mrs']
        '''
        return title_mapping

    @staticmethod
    def name_nominal(this, title_mapping):
        for these in [this.train, this.test]:
            these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal', inplace=True)
            these['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare', inplace=True)
            these['Title'].replace(['Mlle'], 'Mr', inplace=True)
            these['Title'].replace(['Miss'], 'Ms', inplace=True)
            # Mr, Ms, Master, Mrs는 변화 없음.
            these['Title'].fillna(0, inplace=True)
            these['Title'] = these['Title'].map(title_mapping)
        return this

    @staticmethod
    def age_ratio(this) -> object:
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        [these['Age'].fillna(-0.5, inplace=True) for these in [this.train, this.test]]
        # Q 왜 Nan 값에 -0.5 를 할당 할까?
        # A bins 의 Unknown 값의 범위는 -1 ~ 0 ( -1 초과 0 이하 right = true(default)) 이라서 -1을 주게 된다면 NaN 값이 되어버린다.
        # etc.. Unknown 값을 0을 주게 되면 포함이 되는데 그냥 0 줘도 되는게 아닌지?
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # 이것을 이해해 봐라.
        # bins[i] ~ bins[i+1] 구간의 label이므로 bins가 하나 많게 된다.
        # labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        # for these in [this.train, this.test]:
        #     these['AgeGroup'] = pd.cut(these['Age'], bins=bins, labels=labels)  # pd.cut()을 사용
        #     these['AgeGroup'] = these['AgeGroup'].map(age_mapping)  # map()을 사용

        labels = [0, 1, 2, 3, 4, 5, 6, 7]
        # labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        for these in [this.train, this.test]:
            these['AgeGroup'] = pd.cut(these['Age'], bins=bins, right=False, labels=labels)  # pd.cut()을 사용
        ic(type(this.train['AgeGroup'][0]))
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        gender_mapping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        '''test 는 null 없으니까 train 만 처리한다.
        
        null 값은 정규분포를 따라서 정해준다.
        고로 탑승 항구 3개중 가장 많은 곳으로 보내버리면 되나...?
        Title을 보고 해당 Title을 가진 집단에서의 가장 많은곳으로 보내면 될것같다.
        가 아니라 정규분포를 가장 맞춰 줄 수 있는 값으로 정해준다.
        print(these['Embarked'].value_counts())
        S    644, C    168, Q     77
        S    270, C    102, Q     46'''
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train = this.train.fillna({'Embarked': 'S'})
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        this.test['Fare'] = this.test['Fare'].fillna(1)
        for these in [this.train, this.test]:
            these['FareBand'] = pd.qcut(these['Fare'], 4, labels={1, 2, 3, 4})
        # print(f'qcut 으로 bins 값 설정 {this.train["FareBand"].head()}')
        bins = [-1, 8, 15, 31, np.inf]
        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def get_accuracy(this, k_fold):
        score = cross_val_score(RandomForestClassifier(), this.train, this.label,
                                cv=k_fold, n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def learning(self, train_fname, test_fname):
        this = self.preprocess(train_fname, test_fname)
        k_fold = self.create_k_fold()
        ic(f'사이킷런 알고리즘 정확도: {self.get_accuracy(this, k_fold)}')
        self.submit(this)

    @staticmethod
    def submit(this):
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./save/submission.csv', index=False)
