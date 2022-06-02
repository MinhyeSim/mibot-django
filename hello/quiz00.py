import random

import pandas as pd

from domains import my100, my_random, member_choice

from hello import Member


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def mod(num1, num2):
    return num1 % num2


def calculator(num1, opcode, num2):
    if opcode == '+':
        return add(num1, num2)
    elif opcode == '-':
        return sub(num1, num2)
    elif opcode == '*':
        return mul(num1, num2)
    elif opcode == '/':
        return div(num1, num2)
    elif opcode == '%':
        return mod(num1, num2)
    else:
        return f'error (opcode is not valid)'


def deposit(account, deposit):
    account = account + deposit
    print(f'{deposit}원을 입금하였습니다. 잔고는 {account} 입니다')
    return account


def withdraw(account, withdraw):
    account = account - withdraw
    print(f'{withdraw}원을 출금하였습니다. 잔고는 {account} 입니다')
    return account


def chkaccount(name, account):
    print(f'{name} 님의 현재 잔액은 {account}원 입니다.')


class Quiz00:
    def __init__(self):
        pass

    def quiz00calculator(self):
        num1 = my100()
        num2 = my100()
        opcode_num = my_random(0, 4)
        opcode_symbol = ['+', '-', '*', '/', '%']
        opcode = opcode_symbol[opcode_num]
        print(f'{num1} {opcode} {num2} = {calculator(num1, opcode, num2): .1f}')
        return None

    def quiz01bmi(self):
        this = Member()
        this.name = member_choice()
        this.height = my_random(160, 190)
        this.weight = my_random(50, 100)
        bmi_res = this.weight * 10000 / this.height / this.height
        if bmi_res > 25.0:
            res = '비만'
        elif bmi_res > 23.0:
            res = '과체중'
        elif bmi_res > 18.5:
            res = '정상'
        else:
            res = '저체중'
        print(f'{this.name} 님은 \n키 : {this.height}, 몸무게 : {this.weight}\n결과 : {res}입니다.')

    def quiz02dice(self):
        print(my_random(1, 6))
        return None

    def quiz03rps(self):
        user = random.randint(1, 3)
        com = random.randint(1, 3)
        rps = ['가위', '바위', '보']
        res = 'Draw' if user == com else 'Win' if (user - 1) == com % 3 else 'Lose'
        print(f'User : {rps[user - 1]}\nCom : {rps[com - 1]}\n{res}')

        return None

    def quiz04leap(self):
        '''
        In Java
        String res = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) ? '윤년': '평년'
        '''
        year = my_random(1000, 2022)
        res = '윤년' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else '평년'
        print(f'{year}년은 {res}입니다.')
        return None

    def quiz05grade(self):
        name = member_choice()
        kr = my100()
        en = my100()
        math = my100()
        avg = (kr + en + math) / 3
        res = '합격' if avg >= 60 else '불합격'
        print(f'{name}의 성적표\n국어: {kr} 영어: {en} 수학: {math}\n평균: {avg:.1f}\n결과: {res}')
        return None

    def quiz06member_choice(self):
        members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                   "권혜민", "서성민", "조현국", "김한슬", "김진영",
                   '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                   '최민서', '한성수', '김윤섭', '김승현',
                   "강 민", "최건일", "유재혁", "김아름", "장원종"]
        return members[my_random(0, len(members) - 1)]

    def quiz07lotto(self):
        sel_num = random.sample(range(1, 46), 6)
        sel_num.sort()
        prize_num = random.sample(range(1, 46), 7)
        bonus_num = prize_num[6]
        del prize_num[6]
        prize_num.sort()
        print('내가 고른 번호')
        print(sel_num)
        print('당첨 번호')
        print(f'{prize_num} + {bonus_num}')
        res = []
        [[res.append(i) if i == j else 0 for j in sel_num] for i in prize_num]
        rank = 6 - len(res)
        if rank == 1:
            if bonus_num in sel_num:
                rank = 7
                res.append(bonus_num)
        rank_string = ['1등', '3등', '4등', '5등', '꽝', '꽝', '꽝', '2등']
        print(f'맞은 번호는 {res}이며 {rank_string[rank]}입니다.')
        return None

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        Account.main()
        return None

    def quiz09gugudan(self):  # 책받침 구구단
        [([([print(f'{i + k} * {j} = {(i + k) * j}\t', end='') for k in range(0, 4)], print()) for j in range(1, 10)], print()) for i in (2, 6)]

        # 아래의 남은 for 하나를 처리 못하겠음..
        # comprehension으로 처리 하자니 원소가 아닌 리스트 채로 들어가서 매트릭스가 된다.
        res = []
        for i in (2, 6):
            res += ['   '.join(f'{i + k} * {j} = {(i + k) * j}' for k in range(0, 4)) for j in range(1, 10)]
        print(pd.DataFrame(res))


        return None


'''
08번 문제 해결을 위한 클래슨느 다음과 같다.
[요구사항(RFP)]
은행 이름은 : 비트은행
입금자 이름, 계좌번호, 금액 속성값으로 계좌를 생성한다.
계좌번호는 xxx-xx-xxxxxx 형태로 랜덤하게 생성된다.(comprehension)으로 생성
금액은 100~999 사이로 랜덤하게 입금된다.(단위는 만단위로 암묵적으로 판단한다)
'''


class Account:
    def __init__(self, name=None, account_number=None, money=None):
        self.BANK_NAME = '비트은행'
        self.name = member_choice() if name is None else name
        self.account_number = self.creat_account_number() if account_number is None else account_number
        self.money = my_random(100, 999) if money is None else money
        print(f'{self.to_string()}...개설 되었습니다.')

    def to_string(self) -> str:
        return f'은행 : {self.BANK_NAME}\t' \
               f'입금주 : {self.name}\t' \
               f'계좌번호 : {self.account_number}\t' \
               f'잔고 : {self.money}만원'

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                res = f'{j.name}님의 {j.account_number} 계좌가 삭제 되었습니다.'
                ls.remove(j)
                return res
            elif i == len(ls) - 1:
                return '존재하지 않는 계좌입니다.'

    @staticmethod
    def find_account(ls, account_number):
        '''for i, j in enumerate(ls):
            if j.account_number == account_number:
                return j.to_string()
            elif i == len(ls):
                return '존재하지 않는 계좌입니다.'''''
        return ''.join([j.to_string() if j.account_number == account_number else '' for j in ls])

    @staticmethod
    def deposit(ls, account_number, deposit_money):
        for i in ls:
            if i.account_number == account_number:
                i.money += deposit_money
                return f'{i.name}님의 계좌에 {deposit_money}만원 입금 되었습니다.\n' \
                       f'현재 잔액 : {i.money}만원'
            elif i == ls[len(ls) - 1]:
                return '존재하지 않는 계좌입니다.'

    @staticmethod
    def withdraw(ls, account_number, withdraw_money):
        if account_number in ls:
            for i in ls:
                if i.account_number == account_number:
                    if i.money >= withdraw_money:
                        i.money -= withdraw_money
                        return f'{i.name}님의 계좌에 {withdraw_money}만원 출금 되었습니다.\n' \
                               f'현재 잔액 : {i.money}만원'
                    else:
                        return '잔액이 부족합니다'
        else:
            return '존재하지 않는 계좌입니다.'

    @staticmethod
    def creat_account_number():
        '''account_number = f'{str(my_random(0, 999)).zfill(3)}-' \
                         f'{str(my_random(0, 99)).zfill(2)}-' \
                         f'{str(my_random(0, 999999)).zfill(6)}'
        account_number3 = [str(my_random(0, 9)) for i in range(11)]
        account_number4 = [str(my_random(0, 9)) for i in range(11)]
        account_number4.insert(3, '-')
        account_number4.insert(6, '-')'''
        return ''.join(['-' if i == 3 or i == 6 else str(my_random(0, 9)) for i in range(13)])

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0. 종료 1. 계좌개설 2. 계좌목록 3. 입금 4. 출금 5. 계좌해지 6. 계좌조회')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account())
            elif menu == '2':
                res = '\n'.join([i.to_string() for i in ls])
                print(res)
            elif menu == '3':
                print(Account.deposit(ls, input('입금할 계좌번호'), int(input('입금액'))))
            elif menu == '4':
                print(Account.withdraw(ls, input('출금할 계좌번호'), int(input('출금액'))))
            elif menu == '5':
                print(Account.del_account(ls, input('삭제할 계좌번호를 입력해주세요.')))
            elif menu == '6':
                print(Account.find_account(ls, input('조회할 계좌번호를 입력해주세요.')))
