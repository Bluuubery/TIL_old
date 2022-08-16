# 220816
# 4864 문자열비교

# 정답코드
import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    # 찾고자 하는 문자열이 포함되어있는지 확인한다.
    for i in range(M - N + 1):
        # 포함되어 있으면 결괏값을 출력하고 탐색을 중단한다.
        if str2[i:i+N] == str1:
            print('#{} 1'.format(t))
            break
    # 탐색 결과 포함되어있지 않으면 0을 출력한다.
    else:
        print('#{} 0'.format(t))



