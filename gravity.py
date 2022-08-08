# gravity
# 유튜브 라이브
# 220808

# 정답코드

# 테스트 케이스 횟수
T = int(input())

# 테스트 케이스마다 루프
for t in range(1, T+1):

    n = int(input())
    arr = list(map(int, input().split()))
    # n*100 크기의 방을 만들어준다.
    box = [[0] * 100 for _ in range(n)]

    # 방에 상자를 채워준다.
    for i in range(n):
        for j in range(arr[i]):
            box[i][j] = 1
    # 최대낙폭(결괏값)을 담을 변수 maxfall을 지정해준다.
    maxfall = 0

    # 각 열마다 루프를 돈다.
    for c in range(n):
        fall = 0
        # 최대 낙폭을 가지는 상자는 가장 위에 있는 상자이다.
        # 가장 위에 있는 상자 밑에 있는 빈 공간(0)의 갯수를 구한다.
        for k in range(c+1, n):
            if box[k][arr[c]-1] == 0:
                fall += 1
            # maxfall에 최댓값을 넣어준다.
            if fall > maxfall:
                maxfall = fall

    # 정답을 출력 양식에 맞게 출력해준다.
    print('#{} {}'.format(t, maxfall))