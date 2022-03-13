from copy import deepcopy
from msilib import sequence
from typing import Sequence


# 보초법 추가!
def seq_search(a : Sequence, key: int) -> int:
    a_copy = deepcopy(a)
    a_copy.append(key)

    i = 0
    while True:
        # if i == len(a):    ---> 보초법을 사용하면 i == len(a)를 for문을 이용하여 검사할 필요없음
        #     return False
        if a_copy[i] == key:
            return False if i == len(a_copy) else f'key : {key}는 a[{i}]에 있습니다.'
        i += 1

if __name__ == '__main__':
    # int 형 검색
    # num = int(input('a 길이를 입력하세요 : '))
    # a = [None] * num

    # for i in range(len(a)):
    #     a[i] = int(input(f'a[{i}] 값 : '))

    # key = int(input('찾으려는 키값 입력 : '))

    # result = seq_search(a, key)

    # print(result)

    # float 형 검색    
    # i = 0
    # x = []

    # while True:
    #     val = input(f'x[{i}] :')
    #     if val == 'end':
    #         break
    #     x.append(float(val))
    #     i += 1

    # key = float(input('찾으려는 키값 입력 : '))

    i = 0
    x = []

    while True:
        val = input(f'x[{i}] 값 : ')
        if val == 'end':
            break
        x.append(val)
        i+=1

    key = input('찾으려는 값 : ')

    result = seq_search(x, key)

    print(result)