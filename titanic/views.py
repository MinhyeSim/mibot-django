from context.models import Model
from models import TitanicModel
from context.domains import Dataset


class TitanicView:
    # titanicModel = TitanicModel('train.csv', 'test.csv')
    model = Model()
    dataset = Dataset()

    def modeling(self, train, test):
        model = self.model

    def preprocess(self, train, test):
        pass

