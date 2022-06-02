from hello.domains import member_choice, my_random


class Bit803:
    light = 0
    temp = 0

    def __init__(self):
        self.attendance = 0
        self.name = member_choice()
        self.age = my_random(20, 30)
        self.phone_num = '010-' + "".join(['-' if i == 4 else str(my_random(0, 9)) for i in range(9)])

    @staticmethod
    def ctrl_light():
        Bit803.light ^= 1
        print(f'전등 스위치를 눌렀습니다. 현재 상태 : {Bit803.light}')

    @staticmethod
    def ctrl_temp():
        Bit803.temp ^= 1
        print(f'냉난방기 스위치를 눌렀습니다. 현재 상태 : {Bit803.temp}')

    @staticmethod
    def print_803():
        return f'강의실 현황\t전등 : {Bit803.light}\t 냉난방기 : {Bit803.temp}'

    def atttend(self):
        self.attendance ^= 1

    def print_student(self):
        return f'이름 : {self.name}\t나이 : {self.age}\t전화번호 : {self.phone_num}\t출석 상태 : {self.attendance}'

    @staticmethod
    def main():
        # while 1:
        #     menu = input('0. Exit 1. 학생 조종하기 2. 학생 상태 출력 3. 강의실 상태 출력')
        #     if menu == '0':
        #         break

        bit_list = [Bit803() for i in range(5)]  # 5명 생성

        bit_list[0].atttend()                    # 첫번째 학생 출석
        bit_list[0].ctrl_light()                 # 첫번째 학생이 스위치 누름
        bit_list[0].ctrl_temp()                  # 첫번째 학생이 스위치 누름
        bit_list[1].atttend()                    # 두번째 학생 출석
        bit_list[2].atttend()                    # 세번째 학생 출석
        bit_list[3].atttend()                    # 네번째 학생 출석
        bit_list[1].atttend()                    # 두번째 학생 조퇴
        print('\n'.join([i.print_student() for i in bit_list]))    # 1~5번 학생 정보 출력
        print(Bit803.print_803())                # 강의실 정보 확인
        bit_list[3].ctrl_temp()                  # 세번째 학생이 스위치 누름
        print(Bit803.print_803())                # 강의실 정보 확인


if __name__ == '__main__':
    Bit803.main()

