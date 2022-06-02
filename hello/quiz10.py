import random

from quiz00 import Quiz00
from domains import my100, my_random, ten_nums


class Quiz10:
    # 인접한 두 숫자를 비교하여 차례로 정렬하는 방식.
    # 오름차순이라면 가장 후위에 있는 숫자부터 정렬된다.
    def quiz10bubble(self) -> str:
        # arr = ten_nums()
        # print(arr)
        # for i in range(0, len(arr) - 1):
        #     for j in range(0, len(arr) - 1 - i):
        #         if arr[j] > arr[j + 1]:
        #             tmp = arr[j]
        #             arr[j] = arr[j + 1]
        #             arr[j + 1] = tmp
        #     print(f'{i}회차 배열 : {arr}')

        ls = [my100() for i in range(10)]
        print(f'최초 배열 : {ls}')
        '''
        [([Quiz10.swap(ls, j) if ls[j] > ls[j + 1] else None for j in range(0, len(ls) - 1 - i)], print(f'{i}회차 배열 : {ls}')) for i in range(0, len(ls) - 1)]
        '''
        [[Quiz10.swap(ls, j) if ls[j] > ls[j + 1] else None for j in range(0, len(ls) - 1 - i)] for i in range(0, len(ls) - 1)]
        print(f'정렬된 배열 : {ls}')
        return None

    @staticmethod
    def swap(ls, j):
        ls[j], ls[j + 1] = ls[j + 1], ls[j]

    '''
    기정렬된 배열 내로 선택된 요소를 삽입하는 정렬 방식.
    앞의 요소들 부터 정렬된다.
    '''
    def quiz11insertion(self) -> str:
        # arr = ten_nums()
        # print(f'0회차 배열 : {arr}')
        # for i in range(1, len(arr)):
        #     for j in range(0, i):
        #         if arr[i] < arr[j]:
        #             arr.insert(j, arr[i])
        #             del arr[i + 1]
        #             break
        #     print(f'{i}회차 배열 : {arr}')
        # print(f'삽입 정렬 결과 : {arr}')
        
        ls = [my100() for i in range(10)]
        print(f'0회차 배열 : {ls}')
        for i in range(1, len(ls)):
            for j in range(0, i):
                if ls[i] < ls[j]:
                    Quiz10.insert(ls, i, j)
                    break
            print(f'{i}회차 배열 : {ls}')
        print(f'삽입 정렬 결과 : {ls}')
        return None

    @staticmethod
    def insert(ls, i, j):
        pass

    def quiz12selection(self) -> str:
        arr = ten_nums()
        print(f'0회차 배열 : {arr}')
        for i in range(0, len(arr)):
            tmp = min(arr[i:])
            arr.remove(tmp)
            arr.insert(i, tmp)
            print(f'{i}회차 배열 : {arr}')
        print(f'선택 정렬 결과 : {arr}')
        return None

    def quiz13quick(self) -> str:
        return None

    def quiz14merge(self) -> str:
        return None

    '''* 홀수 마방진
     * 1. 정사각형의 맨 아랫줄 가운데에 숫자 1 을 둔다.
     * 2. 이전 숫자 위치에서 오른쪽 아래칸이 비어 있으면 다음 숫자를 채운다.
     * 3. 이전 숫자 위치에서 오른쪽 아래칸이 채워져 있으면 이전 숫자의 위칸에 다음 숫자를 채운다.
     * 4. 오른쪽 아래칸이 사각형의 영역 밖이면 다음의 규칙을 따른다.
     * 4-1. 수평 및 수직으로 이동해서 마지막 칸이 비어 있으면 해당 칸에 숫자를 채운다.
     * 4-2. 수평 및 수직으로 이동해도 칸이 없는 경우 이전의 숫자 위치 위쪽 칸에 다음 숫자를 채운다.'''

    def quiz15magic(self) -> str:
        num = my_random(2, 5) * 2 - 1
        arr = [[0 for col in range(num)] for row in range(num)]
        row_index = num - 1
        col_index = len(arr) - int(num / 2) - 1
        arr[row_index][col_index] = 1
        for i in range(2, len(arr) * len(arr[0]) + 1):
            next_row_index = row_index + 1
            next_col_index = col_index + 1
            if next_row_index >= len(arr):
                next_row_index = 0
            if next_col_index >= len(arr[0]):
                next_col_index = 0
            if arr[next_row_index][next_col_index] == 0:
                arr[next_row_index][next_col_index] = i
            else:
                next_row_index = row_index - 1
                next_col_index = col_index
                arr[next_row_index][next_col_index] = i
            row_index = next_row_index
            col_index = next_col_index
        for j in range(0, len(arr[0])):
            print(arr[j])
        return None

    def quiz16zigzag(self) -> str:
        num = my_random(5, 10)
        res = ''
        for i in range(0, num):
            for j in range(0, num):
                if i % 2 != 0:
                    res += f'{i * num + num - j - 1}\t'
                else:
                    res += f'{i * num + j}\t'
            res += '\n'
        print(res)
        return None

    def quiz17prime(self) -> str:
        num = random.sample(range(1, 101), 2)
        num.sort()
        print(f'{num[0]}~{num[1]} 사이의 소수 출력')
        res = ''
        for i in range(num[0], num[1] + 1):
            for j in range(2, i + 1):
                if i == j:
                    res += f'{i} '
                elif i % j == 0:
                    break
        print(f'{res}')
        return None

    def quiz18golf(self) -> str:
        max_num = 10000
        r_num = my_random.randint(1, max_num)
        sel_num = max_num / 2
        left_num = 0
        right_num = max_num
        cnt = 1
        while 1:
            origin_sel_num = sel_num
            print(sel_num)
            if sel_num == r_num:
                print('정답입니다.')
                break
            elif sel_num < r_num:
                print(f'{sel_num}은 {r_num}보다 작은 숫자 입니다.')
                sel_num = int((right_num + sel_num) / 2)
                left_num = origin_sel_num
            else:
                print(f'{sel_num}은 {r_num}보다 큰 숫자 입니다.')
                sel_num = int((left_num + sel_num) / 2)
                right_num = origin_sel_num
            print(f'시도 횟수는 {cnt}번 입니다.')
            cnt += 1
        return None

    def quiz19booking(self) -> str:
        q00 = Quiz00()
        name = q00.quiz06member_choice()


        return None
