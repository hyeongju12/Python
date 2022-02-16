'''
문제 설명
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때 같은 경우 YES 출력 아니면 NO
출력 단, 회문을 검사할 떄 대소문자를 구분하지 않은다.

입력 설명
첫 줄에 정수 N이 주어지고, 그 다음 줄 부터 N개의 단어가 입력된다ㅕ.
단어는 길이 100을 넘지 않는다.

출력 설명
각 줄에 해당 문자열의 결과를 Yes 또는 No로 출력한다.
'''
import sys
sys.stdin = open('input7.txt', 'r')
n = int(input())

for i in range(n):
    word = input()
    word = word.upper()
    s = len(word)
    for j in range(s//2):
        if word[j] != word[-1-j]:
            print("#{0} NO".format(i+1))
            break
    else:
        print("#{0} YES".format(i+1))