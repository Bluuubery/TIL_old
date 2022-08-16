# 220816
# 4861 회문

# 정답코드
import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    words = [[] for _ in range(N)]
    
    # 단어를 쪼개서 리스트에 받아준다.(생각해보니 안 쪼개도 될 것 같다.)
    for i in range(N):
        word = input()
        for char in word:
            words[i].append(char)
    
    # 회문 여부 표시 변수
    flag = False
    while flag is False:
        
        # 행 검증
        for i in range(N):
            for j in range(N - M + 1):
                new_word = words[i][j:j+M]
                # 회문일 경우 바로 정답을 출력하고 break(회문은 1개만 존재한다.)
                if new_word == new_word[::-1]:
                    ans = ''.join(new_word)
                    print('#{} {}'.format(t, ans))
                    flag = True
                    break
        
        # 열 검증
        for i in range(N - M + 1):
            for j in range(N):
                new_word = ''
                for k in range(i, i+M):
                    new_word += words[k][j]
                if new_word == new_word[::-1]:
                    ans = new_word
                    print('#{} {}'.format(t, ans))
                    flag = True
                    break
