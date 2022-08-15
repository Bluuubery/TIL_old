# 220812
# 1213 String

# 정답코드
import sys

sys.stdin = open('test_input.txt', 'r')

# 주어진 테스트 케이스는 10개이다.
for _ in range(10):
    # 테스트 케이스, 찾을 문자열, 문자열을 입력 받는다.
    T = int(input())
    target = input()
    string = input()
    # 인덱스 설정을 위한 변수 설정
    N = len(string)
    M = len(target)
    # 일치하는 문자열의 개수를 담을 변수 설정
    cnt = 0
    # 탐색 범위 설정
    for i in range(N-M+1):
        # 문자열 내에서 m길이의 문자열이 찾을 문자열과 동일하면 세준다.
        if string[i:i+M] == target:
            cnt += 1

    # 정답을 양식에 맞게 출력한다.
    print('#{} {}'.format(T, cnt))