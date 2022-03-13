from search_while import seq_search

print("실수를 검색합니다.")
print("주의 : 'END'를 입력하면 종료")

number = 0
x = []

while True:
    s = input(f'x[{number}]')
    if s == 'End':
        break
    x.append(s)
    # x.append(float(s))
    number += 1


ky = input('검색할 값 입력 : ')

idx = seq_search(x, ky)
if idx == -1:
    print("검색값 없음")
else:
    print(f'검색값은 x[{idx}]')