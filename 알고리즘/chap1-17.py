# 직사각형 변의 길이 구하기
# 중복되지 않게 출력

area = int(input('직사각형의 넓이를 입력하세요 :'))

for i in range(1, area+1):
    if i * i > area : break
    if area % i : continue
    print(f'{i} * {area // i} = {area}')