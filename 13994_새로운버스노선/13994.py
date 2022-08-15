# 220812
# 13994 새로운 버스 노선

# 정답코드
import sys

sys.stdin = open('sample_in.txt', 'r')

T = int(input())

# max 함수 선언
def max_v(a):
    result = a[0]
    for i in a:
        if i > result:
            result = i
    return result


for t in range(1, T + 1):
    N = int(input())
    # 버스 정류장 리스트 만들기
    station = [0] * 1001

    for _ in range(N):
        bus, start, end = map(int, input().split())

        # 출발과 도착 정류장을 세준다.
        station[start] += 1
        station[end] += 1

        # 일반버스
        if bus == 1:
            for i in range(start + 1, end):
                station[i] += 1

        # 급행버스
        elif bus == 2:
            if start % 2:
                for i in range(start + 1, end):
                    if i % 2:
                        station[i] += 1
            else:
                for i in range(start + 1, end):
                    if i % 2 == 0:
                        station[i] += 1

        # 광역 급행 버스
        else:
            if start % 2:
                for i in range(start + 1, end):
                    if i % 3 == 0 and i % 10:
                        station[i] += 1
            else:
                for i in range(start + 1, end):
                    if i % 4 == 0:
                        station[i] += 1

    # 정답을 양식에 맞게 출력해준다.
    print('#{} {}'.format(t, max_v(station)))
