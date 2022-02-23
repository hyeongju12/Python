from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    '''시퀀스형 a 원소의 최대값을 반환'''
    maximum = 0
    for i in range(len(a)):
        if maximum < a[i]:
            maximum = a[i]
    return maximum

if __name__ == "__main__":
    print("배열의 최댓값을 구합니다.")
    num = int(input("원소 수 입력 !"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요'))


    print(f'최댓값은 {max_of(x)} 입니다.')
