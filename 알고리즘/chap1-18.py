import random

# 실습 1-18

# n = int(input('난수의 갯수를 입력하세요'))

# for _ in range(n):
#     r = random.randint(10, 99)
#     print(r, end=' ')
#     if r == 13:
#         print('\n 프로그램 종료')
#         break
# else:
#     print('\n 난수생성 종료')

# 실습 1-19
# 문제 : 1 ~ 12를 출력할 때 8을 제외하고 출력
# 풀이

# for i in range(1, 13):
#     if i == 8:
#         continue
#     print(i, end=' ')

# 위 풀이는 좋은 방법이 아니다.
# 우선 건너뛰는 값을 모를때(값이 변화 할때)에는 위 풀이 방법이 맞다.
# 하지만 건너뛰는 방법을 아는데 비용소모가 크게(판단횟수) 하는 방법은 좋지 않다. 

# 아래 방법은 리스트를 생성하여 하나씩 꺼내 출력하는 방법이다. 
# for i in list(range(1, 8)) + list(range(9, 13)):
#     print(i, end=' ')


# 실습 1-19
# 문제 : 10 ~ 99 사이의 두 자리 양수 입력받아서 출력
# 풀이

# while True:
#     num = int(input('10 ~ 99사이의 값을 입력해주세요 :'))
#     if 10 <= num <= 99:
#         break

# print(f'입력값은 {num}입니다.')


# 실습 1-20
# 문제 : 구구단 곱셈표 출력!

# print('-' * 9)
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}', end=' ')
#     print()
# print('-' * 9)

# 실습 1-21
# 문제 : 직각 이등변 삼각형 출력

# print('왼쪽 아래가 직각인 이등변 삼각형 출력')
# n = int(input('짧은 변의 길이를 입력하세요 :'))

# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     print()

# print('오른쪽 아래가 직각인 이등변 삼각형 출력')
# n = int(input('짧은 변의 길이를 입력하세요 :'))

# for i in range(n):
#     for _ in range(n-i-1):
#         print(' ', end='')
#     for j in range(i+1):
#         print('*', end='')
#     for k in range(j):
#         print('*', end='')
#     print()

# 보충 : 파이썬 변수 알아보기

'''
    파이썬에서는 데이터, 함수, 클래스, 모듈, 패키지를 모두 객체(object) 취급한다.
    객체는 데이터 타입을 가지며 메모리를 차지한다.

    x = 17 ?
    파이썬에선 x가 17이라는 값을 가지고 있다라고 생각하면 안됀다!
    변수는 객체를 참조하는 객체에 연결된 이름일 뿐이다.
    모든 객체는 메모리를 차지하고 자료형과 식별번호를 가지고 있다.
'''

x = 17
print(id(x))
print(id(17))

print('-' * 20)

n = 1
def put_id():
    x = 1
    print(f'x의 id값은 {id(x)}입니다.')

put_id()
print(f'n의 id값은 {id(n)}입니다.')
print(f'1의 id값은 {id(1)}입니다.')

'''
     위 코드를 봤을때  int형 1이라는 객체를 전역변수 n과  지역변수 x가 참조하고 있다 또한,
     함수가 종료 되더라도 객체가 생성되거나 소멸하지 않는다.
'''