# 220810
# 1954 달팽이 숫자

# 정답 코드 

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

# 달팽이 진행 방향(우 -> 하 -> 좌 -> 상)에 맞게 델타 list 만들기
di = [0, 1, 0, -1] 
dj = [1, 0, -1, 0]

for t in range(1, T + 1):
    N = int(input())
    # 달팽이 숫자를 담을 빈 이차원 배열 반들기
    snail = [[0] * N for _ in range(N)]

    # 초기 좌표 설정
    i = 0
    j = 0

    # 이동 방향 설정
    direction = 0 

    for n in range(1, N*N + 1):
        # 위치에 맞는 달팽이 숫자를 넣어주고 좌표를 이동 시킨다.
        snail[i][j] = n
        i += di[direction]
        j += dj[direction]

        # 좌표가 범위를 벗어나거나 해당 좌표에 이미 숫자가 있을 경우
        if not (0 <= i < N and 0 <= j < N and snail[i][j]==0):
            # 좌표 이동을 취소한다.
            i -= di[direction]
            j -= dj[direction]
            # 진행 방향을 바꿔준다.
            direction = (direction + 1) % 4
            # 진행 방향에 맞는 새로운 좌표를 설정해준다.
            i += di[direction]
            j += dj[direction]
    
    # 정답을 양식에 맞게 출력해준다.
    print("#{}".format(t))

    for row in snail:
        print(*row)