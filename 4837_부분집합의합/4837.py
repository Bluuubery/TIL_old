# 220811
# 4837 부분집합의 합

# 정답 코드 

import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

arr =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for t in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    # 비트 연산자를 활용해 부분집합을 구한다.
    for i in range(1<<12):
        # 부분집합의 원소의 수, 부분집합의 합
        lenset = 0
        sumV = 0
        for j in range(12):
            if i & (1<<j):
                # 부분집합의 합과 원소의 수를 계산해준다.
                sumV += arr[j]
                lenset += 1
                # 부분집합의 원소의 수가 N보다 많아지면 루프를 중단한다.
                if lenset > N:
                    break
        # 부분집합의 원소의 수와 합이 조건을 만족하면 cnt를 더해준다.
        if lenset == N and sumV == K:
            cnt += 1

    # 정답을 양식에 맞게 출력해준다.    
    print('#{} {}'.format(t, cnt))