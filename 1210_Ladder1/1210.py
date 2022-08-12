# 220811
# 1210 Ladder1

# 정답 코드 

import sys

sys.stdin = open('input.txt', 'r')

# 델타 탐색 이동 방향(상, 우, 좌)
di = [-1, 0, 0] 
dj = [0, 1, -1]


for _ in range(10):
    # 테스트 케이스 번호와 사다리 정보
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 시작 인덱스(사다리의 도착점)을 찾아준다.
    startidx = 0
    for k in range(100):
        if ladder[99][k] == 2:
            startidx = k
            break

    # d: 이동 방향, i: 행, j: 열
    d = 0
    i = 99
    j = startidx

    # i가 0(사다리의 출발점)에 도달할 때까지
    while i > 0:

        # 오른쪽에 사다리가 있을 경우
        if j + 1 < 100 and ladder[i][j + 1]:
            # 탐색 방향 설정(오른쪽)
            d = 1
            # 오른쪽에 더이상 사다리가 없을 때까지 오른쪽으로 이동한다.
            while True:
                i += di[d]
                j += dj[d]
                if not(j + 1 < 100 and ladder[i][j + 1]):
                    break
        
        # 왼쪽에 사다리가 있을 경우
        elif j - 1 >= 0 and ladder[i][j - 1]:
            # 탐색 방향 설정(왼쪽)
            d = 2
            # 왼쪽에 더이상 사다리가 없을 때까지 왼쪽으로 이동한다.
            while True:
                i += di[d]
                j += dj[d]
                if not(j - 1 >= 0 and ladder[i][j - 1]):
                    break
        
        # 탐색 방향 초기화(위)
        d = 0
        i += di[d]
        j += dj[d]

        # 사다리 이동 확인하기
        # print(i, j) 

    # 정답을 양식에 맞게 출력해준다.
    print('#{} {}'.format(T, j))

