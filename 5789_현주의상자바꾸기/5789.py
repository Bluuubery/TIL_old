# 5789 현주의 상자 바꾸기
# 220809

# 정답 코드
import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    n, q = map(int, input().split())
    # 0이 적힌 상자의 list를 만들어준다.
    box = [0] * n

    # q에 대해서 1부터 루프를 돈다.
    for i in range(1, q+1):
        l, r = map(int, input().split())
        # 입력 받은 범위에 해당하는 박스의 숫자를 바꿔준다.
        for j in range(l-1, r):
            box[j] = i
    
    # 상자 번호를 양식에 맞게 출력해준다.
    print ('#{}'.format(t), end= ' ')

    for k in range(n):
        print(box[k], end=' ')
    print()