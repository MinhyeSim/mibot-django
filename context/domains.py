# dname, fname, train, test, id, label
from dataclasses import dataclass
from abc import *
import pandas as pd
import pandas
import googlemaps


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
    def new_file(self):
        pass

    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def xls(self):
        pass

    @abstractmethod
    def json(self):
        pass

#Reader 클래스 생성
#Printer 클래스 생성 후 각 base를 상속 받는 구조

class Printer(PrinterBase):
    def dframe(self, this):
        pass

class Reader(ReaderBase):
    def new_file(self, file) -> str:
        return file.context + file.fname

    def csv(self, fname) -> object:
        return pd.read_csv(f'{self.new_file(fname)}'.csv, encoding='UTF-8', thousands=',')

    def xls(self, fname, header, cols) -> object:
        #header
        #usecols
        return pd.read_excel(f'{self.new_file(fname)}.xls', header= header, usecols=cols)

    def json(self, fname)-> object:
        return pd.read_json(f'{self.new_file(fname)}'.csv, encoding='UTF-8', thousands=',')

    def gmaps(self) -> object:
        return googlemaps.Client(key='')


