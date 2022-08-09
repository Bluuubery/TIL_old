# 1945 간단한 소인수분해
# 220809

# 정답 코드
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    n = int(input())

    # a ~ e에 0을 할당해준다.
    a = b = c = d = e = 0
    # n이 1이 될 때까지 나눠준다.
    while n != 1:
        
        # 2로 나눠 떨어지면 2로 나누고 a에 1을 더해준다.
        if not n % 2:
            n = n // 2
            a += 1
        
        # 3으로 나눠 떨어지면 3으로 나누고 b에 1을 더해준다.
        if not n % 3:
            n = n // 3
            b += 1
        
        # 5로 나눠 떨어지면 5로 나누고 c에 1을 더해준다.
        if not n % 5:
            n = n // 5
            c += 1

        # 7로 나눠 떨어지면 7로 나누고 d에 1을 더해준다.
        if not n % 7:
            n = n // 7
            d += 1

        # 11로 나눠 떨어지면 11로 나누고 e에 1을 더해준다.
        if not n % 11:
            n = n // 11
            e += 1

    # a, b, c, d, e를 양식에 맞게 출력해준다.
    print('#{} {} {} {} {} {}'.format(t, a, b, c, d, e))