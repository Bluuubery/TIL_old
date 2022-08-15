# 220812
# 9489 고대 유적

# 정답코드
import sys

sys.stdin = open('input1.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    ruin = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0

    # 유적의 가로길이 측정
    for i in range(N):
        length = 0
        for j in range(M):
            if ruin[i][j]:
                length += 1
                if length > max_length:
                    max_length = length
            else:
                length = 0

    # 유적의 세로길이 측정
    for i in range(M):
        length = 0
        for j in range(N):
            if ruin[j][i]:
                length += 1
                if length > max_length:
                    max_length = length
            else:
                length = 0
    
    # 정답을 양식에 맞게 출력해준다.
    print('#{} {}'.format(t, max_length))