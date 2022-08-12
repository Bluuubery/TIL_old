# 220811
# 4843 특별한 정렬

# 정답 코드 

import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

# 1 <= aj <= 100 이므로 카운팅 소트를 활용한다.
def count_sort(a):
    # count sort를 하기 위해 최댓값을 구하는 함수 선언
    def maxv(b):
        max = b[0]
        for i in b:
            if i > max:
                max = i
        return max
    
    # count를 담을 빈 list
    temp = [0] * (maxv(a) + 1)
    # 정렬된 list를 담을 빈 list 
    temp2 = [0] * len(a)

    # 등장 횟수 count
    for i in range(0, len(a)):
        temp[a[i]] += 1
    
    # count list 누적합으로 list로 만들기
    for i in range(1, len(temp)):
        temp[i] += temp[i-1]
    
    # 요소들을 정렬해서 반환한다.
    for i in range(len(temp2)-1, -1, -1):
        temp[a[i]] -= 1
        temp2[temp[a[i]]] = a[i]
    return temp2


for t in range(1, T + 1):
    # 테스트 케이스 번호 먼저 출력
    print('#{}'.format(t), end=' ')

    # N은 입력만 받고 활용은 안 한다.
    N = int(input())

    # 숫자들을 받아서 정렬해준다.
    numbers = list(map(int, input().split()))
    numbers = count_sort(numbers)

    # 홀수일 때 맨 뒤에 있는 숫자를 출력과 함께 빼내고, 짝수일 때는 맨 앞에 있는 숫자를 출력과 함께 빼낸다. 
    for i in range(10):
        if not i%2:
            print(numbers.pop(), end=' ')
        else:
            print(numbers.pop(0), end=' ')

    # 테스트 케이스 종료 시 개행
    print()