# 220816
# 3143 가장 빠른 문자열 타이핑

# 정답코드
import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    A, B = map(str, input().split())
    N = len(A)
    M = len(B)

    # 타이핑 횟수와 인덱스를 담을 변수 선언
    cnt = 0
    idx = 0
    while idx < N:
        # B가 포함되어 있을 경우
        if A[idx:idx+M] == B:
            # 타이핑을 한 번 해주고 B의 길이만큼 인덱스를 건너뛴다(중복방지)
            cnt += 1
            idx += M
        # 포함되어 있지 않을 경우 한 글자씩 타이핑해준다.
        else:
            cnt += 1
            idx += 1

    # 정답을 양식에 맞게 출력한다.
    print('#{} {}'.format(t, cnt))
