# 220810
# 1209 sum

# 정답 코드 

import sys

sys.stdin = open('input.txt', 'r')

# 최댓값 구하는 함수 선언
def maxV(a):
    result = 0
    for i in a:
        if i > result:
            result = i
    return result

for _ in range(1, 11):

    # input을 받아온다.
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    # 결과를 담을 변수 선언
    max_sum = 0

    for i in range(100):
        sum_row = 0     # 행의 합
        sum_col = 0     # 열의 합
        sum_diag1 = 0   # 우 -> 좌 대각선의 합
        sum_diag2 = 0   # 좌 -> 우 대각선의 합
        # 두 대각선의 합을 구해준다.
        sum_diag1 += arr[i][i] 
        sum_diag2 += arr[i][99 -i]
        for j in range(100):
            # 행과 열의 합을 구해준다.
            sum_col += arr[j][i]
            sum_row += arr[i][j]

        # 행, 열, 대각선 1,2의 합 중 가장 큰 값을 max_sum과 계속 비교해가면서 최댓값을 갱신해준다.
        if maxV([sum_col, sum_row, sum_diag1, sum_diag2]) > max_sum:
            max_sum = maxV([sum_col, sum_row, sum_diag1, sum_diag2])

    # 정답을 양식에 맞게 출력해준다.
    print('#{} {}'.format(T, max_sum))

