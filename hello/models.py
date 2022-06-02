import random


class Quiz01Calc:
    def __init__(self, num1, opcode, num2):
        self.num1 = num1
        self.opcode = opcode
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def mod(self):
        return self.num1 % self.num2

    def calculator(self):
        if self.opcode == '+':
            return self.add()
        elif self.opcode == '-':
            return self.sub()
        elif self.opcode == '*':
            return self.mul()
        elif self.opcode == '/':
            return self.div()
        elif self.opcode == '%':
            return self.mod()
        else:
            return f'error (opcode is not valid)'


class Quiz02Bmi:

    @staticmethod
    def get_bmi(member):
        this = member
        bmi_res = this.weight * 10000 / this.height / this.height
        if bmi_res > 25.0:
            return '비만'
        elif bmi_res > 23.0:
            return '과체중'
        elif bmi_res > 18.5:
            return '정상'
        else:
            return '저체중'


class Quiz03Grade:
    def __init__(self, name, kr, en, math):
        self.name = name
        self.kr = kr
        self.en = en
        self.math = math

    def sum(self):
        return self.kr + self.en + self.math

    def avg(self):
        return self.sum() / 3

    def chk_pass(self):
        if self.avg() >= 60:
            return '합격'
        else:
            return '불합격'


class Quiz04GradeAuto:
    def __init__(self, name, kr, en, math):
        self.name = name
        self.kr = kr
        self.en = en
        self.math = math

    def sum(self):
        return self.kr + self.en + self.math

    def avg(self):
        return self.sum() / 3

    def get_grade(self):
        pass

    def chk_pass(self):
        if self.avg() >= 180:
            return '합격'
        else:
            return '불합격'


def my_random(start, end):
    return random.randint(start, end)


class Quiz05Dice:
    @staticmethod
    def cast():
        return my_random(1, 6)


class Quiz06RandomGenerator:
    def __init__(self, start, end):  # 원하는 범위의 정수에서 랜덤값 1개 추출
        self.start = start
        self.end = end

    def cast(self):
        return my_random(self.start, self.end)


class Quiz07RandomChoice:
    def __init__(self):  # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def extract(self):
        return self.members[my_random(0, len(self.members) - 1)]


class Quiz08Rps:
    def __init__(self, user):
        self.user = user
        self.rsp = ['가위', '바위', '보']
        self.com = random.randint(1, 3)

    def battle(self):
        if self.user == self.com:
            return f'Draw'
        elif (self.user - 1) == self.com % 3:
            return f'Win'
        else:
            return f'Lose'


class Quiz09GetPrime:
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def get_prime(self):
        res = ''
        for i in range(self.no1, self.no2 + 1):
            for j in range(2, i + 1):
                if i == j:
                    res += f'{i} '
                elif i % j == 0:
                    break
        return res


class Quiz10LeapYear:
    def __init__(self, year):
        self.year = year

    def get_leapyear(self):
        if self.year % 4 == 0 & self.year % 100 != 0 | self.year % 400 == 0:
            return '윤년'
        else:
            return '평년'


class Quiz11NumberGolf:
    def __init__(self):
        self.r_num = random.randint(1, 10000)

    def goal(self, num):
        if num == self.r_num:
            return 0
        elif num > self.r_num:
            print(f'{num}보다 작은 숫자 입니다.')
            return 1
        else:
            print(f'{num}보다 큰 숫자 입니다.')
            return 1


class Quiz12Lotto:
    @staticmethod
    def creat_lotto():
        lotto = random.sample(range(1, 46), 6)
        lotto.sort()
        return lotto

    def print_lotto(self):
        for i in self.creat_lotto():
            print(f'{i}\t', end='')


class Quiz13Bank:  # 이름, 입금, 출금만 구현
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def deposit(self, deposit):
        self.account = self.account + deposit
        print(f'{deposit}원을 입금하였습니다. 잔고는 {self.account} 입니다')

    def withdraw(self, withdraw):
        self.account = self.account - withdraw
        print(f'{withdraw}원을 출금하였습니다. 잔고는 {self.account} 입니다')

    def get_account(self):
        return self.account


class Quiz14Gugudan:  # 책받침구구단
    @staticmethod
    def googoo():
        for i in (2, 6):
            for j in range(1, 10):
                for k in range(0, 4):
                    print(f'{i + k} * {j} = {(i + k) * j}\t', end=' ')
                print()
            print()



