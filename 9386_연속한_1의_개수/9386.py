# 220815
# 9386 연속한 1의 개수

# 정답코드
import sys

sys.stdin = open('input1.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    # for loop 순회를 위해서 문자열 형태로 받는다.
    number = input()

    # 연속한 1과 최댓값을 담을 변수 설정
    cnt = 0
    max_count = 0

    for i in number:
        # i가 1일 경우 카운트를 세주고 최댓값과 비교하면서 갱신해나간다.
        if i == '1':
            cnt += 1
            if cnt > max_count:
                max_count = cnt
        # 0일 경우 최댓값과 비교 후 카운트를 초기화 시켜준다.
        else:
            if cnt > max_count:
                max_count = cnt
            cnt = 0

    print('#{} {}'.format(t, max_count))
