# 220816
# 5356 의석이의 세로로 말해요

# 정답코드

import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T + 1):

    # 글자를 동적 변수 선언을 통해 받아준다.
    for i in range(5):
        globals()['word{}'.format(i)] = input()

    # 기본값이 '*'인 5 * 15 행렬을 만들어준다.(다른 문자여도 됨)
    words = [['*'] * 15 for _ in range(5)]

    # 행렬에 글자를 순서대로 채워준다.
    for i in range(5):
        for j in range(len(globals()['word{}'.format(i)])):
            words[i][j] = globals()['word{}'.format(i)][j]

    print('#{}'.format(t), end=' ')
    # 세로로 탐색하면서 글자가 있을 경우 글자를 출력하고 '*'일 경우 건너뒨다.
    for i in range(15):
        for j in range(5):
            if words[j][i] == '*':
                pass
            else:
                print(words[j][i], end='')
    print()
