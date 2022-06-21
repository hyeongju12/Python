def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == "__main__":
    x = int(input("x값 : "))
    y = int(input("y값 : "))
    result = gcd(x, y)
    print(result)