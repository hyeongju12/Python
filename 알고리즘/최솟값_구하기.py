'''
1. 최소값 구하기
'''

a = [3,4,9,12,3,4,2,1]
arrMin = float('inf')

#방법 1.
# for i in range(len(a)):
#     if arrMin > a[i]:
#         arrMin = a[i]

# 방법 2.
for i in a:
    if arrMin > i:
        arrMin = i

print(arrMin)