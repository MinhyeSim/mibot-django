from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re
import pandas as pd
from context.domains import File,Reader


class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'

    def crawling(self):
        file = self.file
        file.fname = 'origin_validation.xlsx'
        report = self.new_file(file)
        f = open(report, 'w', encoding='UTF-8')

if __name__ == '__main__':
    pass