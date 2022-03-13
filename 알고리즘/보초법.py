from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)
    print(a)

    i = 0
    while True:
        if a[i] == key:
            break

        i += 1
    return -1 if i == len(a) else i


if __name__ == '__main__':
    num = int(input("원소 수를 입력하세요 : "))
    lst = [None] * num

    for i in range(num):
        lst[i] = int(input("원소를 입력하세요."))

    key = int(input("찾으려는 키값을 입력하시오 : "))
    res = seq_search(lst, key)
    print(lst)

    if res == -1:
        print("키값이 없습니다.")
    else:
        print(f'idx 는 lst[{res}] 입니다.')
    