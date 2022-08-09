# 1208 flatten
# 220808  

# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

# 상자의 높이가 100보다 작으므로 count sort를 이용한다.
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


for t in range(1, 11):
    n = int(input())
    box = list(map(int, input().split()))
    # 상자의 높이를 정렬해준다.
    sorted_box = count_sort(box)

    # 덤프 횟수만큼 덤프를 시행하고 다시 정렬하는 루프를 만든다.
    for _ in range(n):
        sorted_box[-1] -= 1
        sorted_box[0] += 1
        sorted_box = count_sort(sorted_box)
    
    # 최고점과 최저점의 높이 차를 양식에 맞게 출력한다.
    print('#{} {}'.format(t, sorted_box[-1] - sorted_box[0]))
