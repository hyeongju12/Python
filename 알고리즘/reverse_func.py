from typing import MutableSequence, Any

def reverse_arr(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-1-i] = a[n-1-i], a[i]
    return a

if __name__ == '__main__':
    print('배열의 원소를 역순으로 정렬')
    nx = int(input("원소 수를 입력 : "))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}] 값을 입력하세요:'))

    re_x = reverse_arr(x)
    print(re_x)