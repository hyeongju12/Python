n, m, k = map(int, input().split())


if n == m == k:
    print(10000 + (1000 * n))

elif n == m and n != k:
    print(1000 + (100 * n))
    
elif n != m and n == k:
    print(1000 + (100 * n))
    
elif m != n and m == k:
    print(1000 + (100 * m))

elif n != m and n != k:
    if n > m and n > k:
        print(n*100)
    elif n > m and n < k:
        print(k*100)
    elif n < m and m < k:
        print(k*100)
    elif n < m and m > k:
        print(m*100)

    
            
        
    