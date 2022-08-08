# 220808 swea 1208 flatten

def count_sort(a):
    def maxv(b):
        max = 0
        for i in b:
            if i > max:
                max = i
        return max
    
    temp = [0] * (maxv(a) + 1)
    temp2 = [0] * len(a)
    for i in range(0, len(a)):
        temp[a[i]] += 1
    
    for i in range(1, len(temp)):
        temp[i] += temp[i-1]
    
    for i in range(len(temp2)-1, -1, -1):
        temp[a[i]] -= 1
        temp2[temp[a[i]]] = a[i]
    return temp2

for t in range(1, 11):
    n = int(input())
    box = list(map(int, input().split()))
    sorted_box = count_sort(box)
    for _ in range(n):
        sorted_box[-1] -= 1
        sorted_box[0] += 1
        sorted_box = count_sort(sorted_box)
    print('#{} {}'.format(t, sorted_box[-1] - sorted_box[0]))
    # 소트 한번 소트 두 번
