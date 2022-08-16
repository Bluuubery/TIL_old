# 220816
# 4865 글자수

# 정답코드
import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    str1 = input()
    str2 = input()

    # 최대 글자 수를 담을 변수 선언
    max_cnt = 0
    for char1 in str1:
        # .count() 메소드를 이용해 글자 수를 세준다.
        cnt = str2.count(char1)
        # 최대 글자 수와 비교하면서 갱신해나간다.
        if cnt > max_cnt:
            max_cnt = cnt

    # 정답을 양식에 맞게 출력한다.
    print('#{} {}'.format(t, max_cnt))