# 4831 전기버스
# 220809

# 정답 코드 (slicing 활용)
import sys

sys.stdin = open('sample_input.txt', 'r')


T = int(input())

for t in range(1, T+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))

    # 충전소의 정보를 담은 버스 정류장의 배열을 만들어준다.
    bus_stop = [0] * (n+1)
    for i in charge:
        bus_stop[i] += 1
    
    # bus: 버스의 현재 위치, count: 충전횟수
    bus = 0
    count = 0
    
    while bus + k < n:
        # 이동 가능 범위 내에서 가장 멀리 있는 충전소를 탐색한다
        for move in range(bus+k, bus, -1):
            # 충전소가 있으면 헤딩 층전소로 이동하고 충전 횟수를 세준다.
            if bus_stop[move]:
                bus = move
                count += 1
                print(bus)
                break
        # 충전소가 없으면 0을 반환한다.
        else:
            count = 0
            break

    print('#{} {}'.format(t, count))
# 평균 0.13s
