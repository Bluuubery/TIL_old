# 220810
# 부분집합

# 정답 코드 

# 합을 구하는 함수 선언
def sumV(a):
    result = 0
    for i in a:
        result += i
    return result


T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    
    # 비트 연산자를 활용해 부분집합을 구한다.
    for i in range(1<<10):
        # 부분집합을 담을 빈 리스트
        subset = []
        for j in range(10):
            if i & (1<<j):
                # 부분집합에 원소들을 넣어서 부분 집합을 만들어 준다.
                subset.append(numbers[j])

        # 부분집합 내 원소들의 합이 0인 경우(공집합 제외) 정답을 출력하고 루프를 break한다.
        if subset and not sumV(subset):
            print('#{} 1'.format(t))
            break

    # 모든 부분집합 탐색 결과 정답이 없을 경우 0을 출력한다.
    else:
        print('#{} 0'.format(t))