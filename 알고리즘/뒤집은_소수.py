'''
문제 설명
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는
프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다.
단 910을 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시,
뒤집은 함수인 def reverse(x)와 확인하는 함수 isPrime(x)를 반드시 작성하여 프로그래밍한다.

입력 설명
첫 줄에 자연수의 개수 N이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 100,000을 넘지 않는다.

출력 설명
첫 줄에 뒤집은 소수를 출력합니다. 출력 순서는 입력된 순서대로 출력합니다.
'''

def reverse(val):
    res = 0
    while val > 0:
        t = val % 10
        res = res * 10 + t
        val = val // 10
    return res

def isPrime(val):
    if val == 1:
        return False
    for i in range(2, val//2+1):
        if val % i == 0:
            return False
    else:
        return True


x = [23, 91, 33]

for i in x:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp)
