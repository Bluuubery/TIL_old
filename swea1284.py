# 220814 swea 1284 수도 요금 경쟁

T = int(input())

for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    A = P * W

    if W > R:
        B = Q + S * (W - R)
    else:
        B = Q

    if A > B:
        print('#{} {}'.format(t, B))
    else:
        print('#{} {}'.format(t, A))
