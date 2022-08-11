# 220810
# 델타검색

# 정답 코드

# 절댓값 구하는 함수 선언
def absV(a):
    if a >= 0:
        return a
    else: 
        return -a

T = int(input())

di = [0, 0, -1, 1] # 상하좌우
dj = [-1, 1, 0, 0]

for t in range(1, T + 1):
    
    # input을 받아준다.
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 정답을 담을 변수
    result = 0

    # 모든 원소에 대해서 델타 탐색 시행
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 유효한 인덱스일 경우 판별
                if 0 <= ni < N and 0 <= nj < N:
                    # 이웃과의 차의 절댓값을 result에 더해준다.
                    diff = arr[i][j] - arr[ni][nj]
                    result += absV(diff)
  
    # 정답을 양식에 맞게 출력한다.
    print('#{} {}'.format(t, result))
