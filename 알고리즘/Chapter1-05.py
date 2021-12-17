print("*를 출력합니다.")
n = int(input())
w = int(input())

for i in range(n+1):
    print("*", end='')
    if i % 5 == 0:
        print()

if i % w :
    print()