import random
from dataclasses import dataclass


def ten_nums():
    return random.sample(range(1, 101), 10)


def my_random(start, end):  # start 이상 end 이하의 값
    return random.randint(start, end)


def my100():
    return my_random(1, 100)

def membere_list() -> []:
    return ['홍정명', '노홍주', '전종현', '정경준', '양정오',
               "권혜민", "서성민", "조현국", "김한슬", "김진영",
               '심민혜', '권솔이', '김지혜', '하진희', '최은아',
               '최민서', '한성수', '김윤섭', '김승현',
               "강 민", "최건일", "유재혁", "김아름", "장원종"]

def member_choice():
    members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
               "권혜민", "서성민", "조현국", "김한슬", "김진영",
               '심민혜', '권솔이', '김지혜', '하진희', '최은아',
               '최민서', '한성수', '김윤섭', '김승현',
               "강 민", "최건일", "유재혁", "김아름", "장원종"]
    return members[my_random(0, len(members) - 1)]


def member_choice2(num):
    members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
               "권혜민", "서성민", "조현국", "김한슬", "김진영",
               '심민혜', '권솔이', '김지혜', '하진희', '최은아',
               '최민서', '한성수', '김윤섭', '김승현',
               "강 민", "최건일", "유재혁", "김아름", "장원종"]
    return members[num]


@dataclass
class Member:
    name: str
    height: float
    weight: float

    @property
    def name(self) -> str: return self._name

    @name.setter
    def name(self, name): self._name = name

    @property
    def height(self) -> float: return self._height

    @height.setter
    def height(self, height): self._height = height

    @property
    def weight(self) -> float: return self._weight

    @weight.setter
    def weight(self, weight): self._weight = weight
