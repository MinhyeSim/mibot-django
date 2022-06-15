# dname, fname, train, test, id, label
import json
from dataclasses import dataclass
from abc import *
import pandas as pd
import pandas
import googlemaps
from typing import TypeVar
PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')
GooglemapsClient = TypeVar('googlemaps.Client')


@dataclass()
class Dataset:
    dname: str
    sname: str
    fname: str
    train: pandas.core.frame.DataFrame
    test: pandas.core.frame.DataFrame
    id: str
    label: str

    @property
    def dname(self) -> str: return self._dname

    @dname.setter
    def dname(self, value): self._dname = value

    @property
    def sname(self) -> str: return self._sname

    @sname.setter
    def sname(self, sname): self._sname = sname

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, value): self._fname = value

    @property
    def train(self) -> pandas.core.frame.DataFrame: return self._train

    @train.setter
    def train(self, value): self._train = value

    @property
    def test(self) -> pandas.core.frame.DataFrame: return self._test

    @test.setter
    def test(self, value): self._test = value

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, value): self._id = value

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, value): self._label = value

@dataclass
class File(object):
    context: str
    fname: str
    dframe: object

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def dframe(self) -> str: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe

class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def dframe(self):
        pass
    #new_file, csv, xls, json
class ReaderBase(metaclass=ABCMeta):

    @abstractmethod
    def new_file(self, file) -> str:
        pass

    @abstractmethod
    def csv(self) -> PandasDataFrame:
        pass

    @abstractmethod
    def xls(self) -> PandasDataFrame:
        pass

    @abstractmethod
    def json(self) -> PandasDataFrame:
        pass

#Reader 클래스 생성
#Printer 클래스 생성 후 각 base를 상속 받는 구조

class Printer(PrinterBase):
    pass


class Reader(ReaderBase):
    def new_file(self, file) -> str:
        return file.context + file.fname
        # file.context = './data/'
        # file.fname = 'cctv_in_seoul'
        # file 객체에 있는 context와 fname이 필요하다.

    def csv(self, path: str) -> PandasDataFrame:
        o = pd.read_csv(f'{self.new_file(path)}.csv', encoding='UTF-8', thousands=',')
        print(f'type: {type(o)}')
        return o

    def xls(self, path: str, header: str, cols: str, skiprows) -> PandasDataFrame:
        return pd.read_excel(f'{self.new_file(path)}.xls', header=header, usecols=cols, skiprows=skiprows)

    def json(self, path: str) -> PandasDataFrame:
        return pd.read_json(f'{self.new_file(path)}.json', encoding='UTF-8')

    def map_json(self, path: str) -> object:
        return json.load(open(f'{self.new_file(path)}.json', encoding='UTF-8'))

    @staticmethod
    def gmaps() -> GooglemapsClient:
        a = googlemaps.Client(key='')
        print(type(a))
        return a

    def print(self, this):
        print('*' * 100)
        print(f'1. Target type \n {type(this)} ')
        print(f'2. Target column \n {this.columns} ')
        print(f'3. Target top 1개 행\n {this.head(1)} ')
        print(f'4. Target bottom 1개 행\n {this.tail(1)} ')
        print(f'4. Target null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)

if __name__ == '__main__':
    Reader.gmaps()