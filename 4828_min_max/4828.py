# 4828 min max
# 220809

# 정답 코드
import sys

sys.stdin = open('sample_input.txt', 'r')

# 최댓값 구해주는 함수
def maxval(a):
    result = a[0]
    for i in a:
        if i > result:
            result = i
    return result

# 최솟값 구해주는 함수
def minval(a):
    result = a[0]
    for i in a:
        if i < result:
            result = i
    return result

T = int(input())

for t in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    # 위에서 선언한 함수를 이용한다.
    result = maxval(numbers) - minval(numbers)

    # 최댓값과 최솟값의 차를 출력한다.
    print('#{} {}'.format(t, result))


