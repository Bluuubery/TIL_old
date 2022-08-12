# 220811
# 1979 어디에 단어가 들어갈 수 있을까

# 정답 코드 

# import sys

# sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    # 퍼즐판을 이차원 배열의 형태로 받는다.
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    # 단어가 들어갈 수 있는 자리의 수를 담을 변수 설정
    total_cnt = 0

    # 각 행과 열마다 루프를 돌면서 들어갈 수 있는 단어의 최대 길이를 찾는다. 
    for i in range(N):
        # 각 행과 열에서 들어갈 수 있는 단어의 길이를 세줄 변수 설정
        row_cnt = 0
        col_cnt = 0
        for j in range(N):

            # 행에 대해 검사
            # 글자가 들어갈 수 없을 때(0)
            if not puzzle[i][j]:
                # 들어갈 수 있는 단어와 K의 길이가 일치하면 total_cnt를 세준다.
                if row_cnt == K:
                    total_cnt += 1 
                # 들어갈 수 있는 글자 수를 초기화해준다.
                row_cnt = 0
            # 글자가 들어갈 수 있을 때 row_cnt를 세준다.
            else:
                row_cnt += 1

            # 열에 대해서도 행과 똑같이 검사한다.
            if not puzzle[j][i]:
                if col_cnt == K:
                    total_cnt += 1
                col_cnt = 0
            else:
                col_cnt += 1

        # 해당 행과 열에 들어갈 수 있는 단어의 길이가 K와 일치하면 total_cnt를 세준다.
        if row_cnt == K:
            total_cnt += 1
        if col_cnt == K:
            total_cnt += 1
    
    # 양식에 맞게 정답을 출력해준다.    
    print('#{} {}'.format(t, total_cnt))