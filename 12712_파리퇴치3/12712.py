# 220812
# 12712 파리퇴치3

# 정답코드
import sys


sys.stdin = open('in1.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    # N과 M을 입력 받는다.
    N, M = map(int, input().split())

    # 파리의 위치 정보를 담을 빈 리스트
    fly = []
    # 파리의 위치 정보를 입력 받는다.
    # 인덱스 에러 방지를 위해 상하좌우로 M의 길이만큼 빈 리스트를 추가 해주낟.
    for _ in range(N):
        fly.append([0]*M + list(map(int, input().split())) + [0]*M)
    fly = [[0] * (N + 2*M)] * M + fly + [[0] * (N + 2*M)] * M

    # 최대 파리 퇴치 수를 담을 변수 선언
    max_kill = 0

    # +자 탐색
    # 파리가 있는 범위에 대해서 루프를 돈다
    for i in range(M, M + N):
        for j in range(M, M + N):
            kill = 0
            # 탐색하는 위치에 대해서 M길이의 세로열과 가로행을 더해준다.
            for k in range(-M + 1, M):
                kill += fly[i + k][j]
                kill += fly[i][j + k]
            # 자기 자신이 두 번 더해지므로 한번 빼준다.
            kill -= fly[i][j]
            # 기존 최댓값과 비교하면서 계속 갱신해준다.
            if kill >= max_kill: 
                max_kill = kill
      
    # X자 탐색
    # 전반적인 로직은 위의 +자 탐색과 동일하다.
    for i in range(M , M + N ):
        for j in range(M, M + N):
            kill = 0
            # 탐색하는 위치에 대해서 M길이의 대각선을 더해준다.
            for k in range(-M + 1, M):
                kill += fly[i + k][j + k]
                kill += fly[i - k][j + k]
            kill -= fly[i][j]

            if kill >= max_kill: 
                max_kill = kill

    # 양식에 맞게 정답을 출력해준다.
    print('#{} {}'.format(t, max_kill))
