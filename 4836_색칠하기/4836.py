# 220811
# 4836 색칠하기

# 정답 코드 

import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    # 색을 칠할 빈 격자를 만들어준다.
    blank = [[0] * 10 for _ in range(10)]
    # 보라색(겹치는 영역)을 셀 변수
    purple = 0

    for i in range(N):
        color = list(map(int, input().split()))
        
        # 빨강
        if color[-1] == 1:
            for i in range(color[0], color[2] + 1):
                for j in range(color[1], color[3] + 1):
                    # 색을 칠하려는 곳에 이미 파란색으로 칠해져 있으면 보라색을 세준다.
                    if blank[i][j] == 2:
                        purple += 1
                    # 비어있거나 같은색(빨강)으로 칠해져있으면 해당 좌표를 빨강으로 칠해준다.
                    else: 
                        blank[i][j] = 1
        # 파랑
        elif color[-1] == 2:
            for i in range(color[0], color[2] + 1):
                for j in range(color[1], color[3] + 1):
                    # 색을 칠하련느 곳에 이미 빨간색으로 칠해져 있으면 보라색을 세준다.
                    if blank[i][j] == 1:
                        purple += 1
                    # 비어있거나 같은색(파랑)으로 칠해져있으면 해당 좌표를 파랑으로 칠해준다.
                    else: 
                        blank[i][j] = 2
    
    # 양식에 맞게 정답을 출력해준다.
    print('#{} {}'.format(t, purple))
