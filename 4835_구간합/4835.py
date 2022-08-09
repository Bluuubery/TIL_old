# 4825 구간합
# 220809

# 정답 코드
import sys

sys.stdin = open('sample_input.txt', 'r')

# 합 구해주는 함수
def sumsum(a):
    result = 0
    for i in a:
        result += i
    return result

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
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    sum_list = []
    # 구간합을 리스트에 담아준다.
    for i in range(0, n-m+1):
        num_sum  = sumsum(numbers[i:i+m])
        sum_list.append(num_sum)
    
    # 최댓값과 최솟값의 차를 출력한다.
    print('#{} {}'.format(t, maxval(sum_list) - minval(sum_list)))

