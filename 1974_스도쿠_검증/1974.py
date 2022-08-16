# 220816
# 1974 스도쿠 검증

# 정답 코드

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

# in 연산자를 통해서 스도쿠를 검증한다.(합은 예외가 있을 수 있음!)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for t in range(1, T+1):
    # 스도쿠 숫자의 정보를 받는다.
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # 스도쿠 여부
    flag = True

    # 행에 대해 검증
    for row in sudoku:
        for number in numbers:
            # 1 ~ 9 중 행에서 빠진 숫자가 있으면 스도쿠가 아니다.
            if number not in row:
                flag = False

    # 열에 대해 검증
    for i in range(9):
        col = []
        for j in range(9):
            col.append(sudoku[j][i])
        for number in numbers:
            if number not in col:
                flag = False

    # 사각형에 대해 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for k in range(3):
                square.append(sudoku[i][j + k])
                square.append(sudoku[i + 1][j + k])
                square.append(sudoku[i + 2][j + k])
            for number in numbers:
                if number not in square:
                    flag = False

    # 스도쿠 여부를 양식에 맞게 출력한다.
    if flag:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))
