# 220811
# 4839 이진탐색

# 정답 코드 

import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

# 이진 탐색 함수 선언
def binarySearch (a, N, key):
    # 시작, 끝, 카운터 선언
    start = 0
    end = N-1
    cnt = 0
    while start <= end:
        # 매 이진 탐색마다 카운터를 더해준다.
        cnt += 1
        middle = (start + end) // 2
        # 검색 성공 시 카운트 값을 반환한다.
        if a[middle] == key :
            return cnt
        # 검색 실패시 영역을 분할해 다시 탐색을 진행한다.
        elif a[middle] > key:
            end = middle
        else:
        	start = middle

for t in range(1, T+1):
    P, A, B = map(int, input().split())
    # 탐색할 책(페이지 수를 담은 리스트)를 만들어준다.
    book = [i for i in range(1, P+1)]

    # 탐색 횟수가 적은 사람을 출력한다.
    if binarySearch(book, P, A) < binarySearch(book, P, B):
        print('#{} A'.format(t))
    elif binarySearch(book, P, A) > binarySearch(book, P, B):
        print('#{} B'.format(t))
    # 탐색 횟수가 같을 경우에 0을 출력한다
    else:
        print('#{} 0'.format(t))