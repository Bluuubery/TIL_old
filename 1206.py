# 1206_view
# 220808

# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

def minval(a):
    result = a[0]
    for i in a:
        if i < result:
            result = i
    return result

for tc in range(1, 11):
    t= int(input())
    answer = 0
    height = [0, 0] + list(map(int, input().split())) + [0, 0]

    for i in range(2, t+2):
        sight = [height[i] - height[i-1], height[i] - height[i-2], height[i] - height[i+1], height[i] - height[i+2]]
        if sight[0] >= 1 and sight[1] >= 1 and sight[2] >= 1 and sight[3] >= 1:
            answer += minval(sight)
    
    print('#{}} {}'.format(tc, answer))

