# 220811
# 2001 파리퇴치

# 정답 코드 

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    # 파리의 위치 정보 이차원 배열로 받는다.
    fly = [list(map(int, input().split())) for _ in range(N)]

    # 최대 파리 퇴치 수를 담을 변수 설정
    maxkill = 0

    # N - M + 1 의 범위에 대해서 루프를 돈다.
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 파리 퇴치 수
            kill = 0
            # 각 좌표마다 M*m 이차원 배열의 합 구하기
            for k in range(M):
                for l in range(M):
                    kill += fly[i + k][j + l]
            # 최대 파리 퇴치 수를 비교해가면서 갱신한다.
            if kill > maxkill:
                maxkill = kill
                
    # 정답을 양식에 맞게 출력해준다.
    print('#{} {}'.format(t, maxkill))
        
