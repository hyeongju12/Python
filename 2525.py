H, M = map(int, input().split())
ctime = int(input())

if M+ctime > 59:
    H = (M + ctime) // 60 + H
    M = (M + ctime) % 60
    if H > 24:
        H = abs(24 - H)
    elif H == 24:
        H = 0
    print(str(H)+ ' ' +str(M))
else:
    M = M + ctime
    print(str(H)+ ' ' +str(M))
    
