# 220807 swea 2005 파스칼의 삼각형
t = int(input())

for _ in range(1, t+1):
    n = int(input())
    print(f'#{_}')

    for i in range(1, n+1):
        temp = [1] * i
        if i == 1 or i == 2:
            pass
        else:    
            for j in range(1, i-1):
                    temp[j] = temp2[j-1] + temp2[j]
        temp2 = temp

        print(*temp)