# 220816
# 5432 쇠막대기 자르기

# 정답 코드

import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T+1):

    # 쇠막대기(자르기 전)과 잘린 쇠막대기를 담을 변수
    # 처음에 쇠막대기 한 개로 시작한다.
    stick = 1
    result = 1

    string = input()

    for i in range(1, len(string) - 1):
        # 열린 괄호의 경우
        if string[i] == '(':
            # 다음 괄호도 열린 괄호면 쇠막대기이므로 쇠막대기 갯수와 결괏값을 더해준다.
            if string[i + 1] == '(':
                stick += 1
                result += 1
            # 다음 괄호가 닫힌 괄호면 레이저이므로 현재 쇠막대기 개수만큼 결괏값을 더해준다.
            else:
                result += stick

        # 닫힌 괄호의 경우
        else:
            # 두 번째 괄호가 닫힌 괄호였을 때 레이저이므로(첫 괄호는 무조건 열린 괄호) 쇠막대기와 결괏값을 빼준다.
            if i == 1:
                stick -= 1
                result -= 1
            else:
                # 이전 괄호가 열린 괄호였을 때(레이저)는 위에서 계산했으므로 패스한다.
                if string[i - 1] == '(':
                    pass
                # 그 외의 경우에는 쇠막대기를 한 개 빼준다.
                else:
                    stick -= 1

    # 정답을 양식에 맞게 출력해준다.
    print('#{} {}'.format(t, result))