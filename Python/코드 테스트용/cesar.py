def solution(n):
    x = []
    min_x = n
    for i in range(1, n+1):
        if n % i == 1:
            x.append(i)
    for i in range(len(x)):
        if x[i] < min_x:
            min_x = x[i]

    answer = min_x
    return answer


print(solution(10))