# n = int(input("구간을 입력해 주세요 : "))

# ch = (n+1)*[0]
# cnt = 0

# for i in range(2, n+1):
#     if ch[i] == 0:
#         cnt += 1
#         for j in range(i, n+1, i):
#             ch[j] = 1


# print(cnt)

n = int(input("구간을 입력해 주세요 :"))

val_list = [i for i in range(1, n+1)]
res_list = []

for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        res_list.append(i)


print(res_list)