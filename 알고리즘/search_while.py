from re import I
from typing import Sequence, Any

def seq_search(x : Sequence, key : Any) -> int:
    for i in range(len(x)):
        if x[i] == key:
            return i
    else:
        return -1

if __name__ == '__main__':
    num = int(input("원소 수를 입력하세요 : "))
    x = [None] * num

    for i in range(num):
        x[i] = int((input(f'x[{i}]')))

    ky = int(input("검색할 값을 입력 : "))

    res = seq_search(x, ky)

    if res == -1:
        print("값을 못찾음")
    else:
        print(f'값은 : x[{res}] 에 있다.')
        