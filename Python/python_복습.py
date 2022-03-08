def change_idx(x, idx, val):
    x[idx] = val
    return x

x = [11,22,33,44,55]
idx = int(input("바꾸려는 인덱스 입력 : "))
val = int(input("바꾸려는 값 입력 : "))

print(id(x))
print(id(change_idx(x, 2, 99)))
