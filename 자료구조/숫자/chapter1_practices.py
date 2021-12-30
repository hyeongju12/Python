# Chapter1 연습문제 5개 

# 1번 진법변환
# 내용 : 다른 진법의 숫자를 10진수로 변환하는 함수를 직접 만들어보자.

def convert_to_decimal(number, base):
    multiple, result = 1, 0
    while number > 0:
        result += number % 10 * multiple
        multiple *= base
        number = number // 10
    return result

def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print("테스트 통과")



if __name__ == "__main__":
    test_convert_to_decimal()

# 최대공약수

# random 모듈

# 피보나치 수열

# 소수 판단ㅎㅅ