# 4831 전기버스
# 220809

# 정답 코드 (in 활용)
import sys

sys.stdin = open('sample_input.txt', 'r')

# 범위 내에 해당 값의 존재 여부를 반환하는 in 함수를 만들어준다.
def is_in (i, a):
    for j in a:
        if i == j:
            return True
    else:
        return False



T = int(input())

for t in range(1, T+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))
    # bus: 버스의 현재 위치, count: 충전횟수
    bus = 0
    count = 0

    # bus가 종점에 도달하기 전까지 범위를 설정
    while bus + k < n:
        # 이동 가능 범위(k)내에서 가장 먼 충전소를 탐색해서 충전소가 있다면 해당 충전소로 이동하고 충전 횟수를 세준다.
        for move in range(k, 0, -1):
            if is_in((bus+move), charge):
                bus += move
                count += 1
                break
        # 충전소가 없으면 0을 반환한다.
        else:
            count = 0
            break

    print('#{} {}'.format(t, count))

# 평균 0.14s
