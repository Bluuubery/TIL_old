# 220812
# 9367 점점커지는당근의개수

# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    # N과 당근의 개수 정보를 입력 받는다.
    N = int(input())
    C = list(map(int, input().split()))

    # 연속으로 커지는 당근의 개수랑 그것들의 최댓값을 담을 변수 선언
    max_cnt = 1
    cnt = 1

    for idx in range(1, len(C)):
        # 당근의 갯수를 담은 리스트를 돌면서 당근이 이전 것보다 크면 카운트를 더해준다. 
        if C[idx] > C[idx - 1]:
            cnt += 1
            # 최댓값과 비교하면서 계속 갱신해준다.
            max_cnt = cnt
        # 이전 것보다 크지 않으면 최댓값과 비교 후 카운트를 초기화해준다.
        elif max_cnt > cnt:
            max_cnt = cnt
            cnt = 1
        else:
            cnt = 1

    # 정답을 양식에 맞게 출력해준다.
    print('#{} {}'.format(t, max_cnt))