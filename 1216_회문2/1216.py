# 220816
# 1216 회문2

# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

# import time
# start = time.time()

# 주어진 테스트 케이스는 10개이다.
for t in range(10):
    # 테스트 케이스 번호
    T = int(input())

    # 단어들을 쪼개서 배열에 받아준다.(생각해보니 굳이 안 쪼개도 될듯)
    words = [[] for _ in range(100)]

    for i in range(100):
        word = input()
        for char in word:
            words[i].append(char)

    # 최대 회문 길이를 담을 변수 선언
    max_palindrome = 0

    # 100 * 100 이므로 회문의 길이 경우의 수 (1 - 100)개마다 회문 탐색을 한다.
    for length in range(1, 101):

        # 행 검증(슬라이싱)
        for i in range(100):
            for j in range(100 - length + 1):
                new_word = words[i][j:j+length]
                # 회문일 경우 기존 최대 길이와 비교하면서 갱신해준다.
                if new_word == new_word[::-1]:
                    if len(new_word) > max_palindrome:
                        max_palindrome = len(new_word)

        # 열은 슬라이싱이 안되므로 빈 스트링을 선언해서 더해준다.
        for i in range(100 - length + 1):
            for j in range(100):
                new_word = ''
                for k in range(i, i+length):
                    new_word += words[k][j]
                # 회문일 경우 기존 최대 길이와 비교하면서 갱신해준다.
                if new_word == new_word[::-1]:
                    if len(new_word) > max_palindrome:
                        max_palindrome = len(new_word)

    # 정답을 양식에 맞게 출력해준다.
    print('#{} {}'.format(T, max_palindrome))

# end = time.time()
# print(end-start)
