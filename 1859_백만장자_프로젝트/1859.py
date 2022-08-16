# 220816
# 1859 백만 장자 프로젝트

# 정답 코드

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    n = int(input())
    # 뒤에서부터 거꾸로 검증하기 위해 가격 정보의 리스트를 뒤집는다.
    # 최댓값을 찾고 완전탐색으로 앞에서부터 비교하면서 검증하면 시간초과가 발생한다.
    price = list(map(int, input().split()))[::-1]

    # 이익과 최대 가격을 담을 변수 선언
    profit = 0
    max_price = price[0]

    for j in range(1, n):
        # 현재 가격이 최대가격(역순이기 때문에 미래의 최대 가격)보다 낮으면 차익만큼 이익에 더해준다.
        if max_price > price[j]:
            profit += max_price - price[j]
        # 현재 가격이 더 높으면 최대가격을 갱신해준다.
        else:
            max_price = price[j]

    # 정답을 양식에 맞게 출력해준다.
    print('#{} {}'.format(t, profit))

