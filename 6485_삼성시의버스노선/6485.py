# 6485 삼성시의 버스 노선
# 220809

# 정답 코드
import sys

sys.stdin = open('s_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    print('#{}'.format(t), end=' ')
    # 버스 정류장 갯수 길이 + 1(인덱싱 시 편의)만큼의 list를 만들어준다.
    bus = [0] * 5001

    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        # 해당 노선이 경유하는 정류장에 대해서 1을 더해준다.
        for i in range(a, b+1):
            bus[i] += 1
    
    p = int(input())
    for _ in range(p):
        c = int(input())
        # 슬라이싱을 통해 노선의 경유 정보를 담은 list에서 해당 정류장을 경유하는 노선의 갯수를 양식에 맞게 출력해준다.
        print('{}'.format(bus[c]), end=' ')
    print()