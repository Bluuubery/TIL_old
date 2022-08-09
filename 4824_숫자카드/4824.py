# 4824 숫자 카드
# 220809

# 정답 코드
import sys

sys.stdin = open('sample_input.txt', 'r')\

# enumarate된 리스트의 max_value와 해당 value의 idx 구하는 함수
def max_idx_val(a):
    max_val = a[0][1]
    max_idx = a[0][0]
    for i in a:
        if i[1] >= max_val:
            max_idx = i[0]
            max_val = i[1]
    return max_idx, max_val


T = int(input())

for t in range(1, T+1):
    n = int(input())
    # 숫자가 한덩이로 뭉쳐서 나온다.
    num_str = input()
    
    # for문을 활용해 숫자를 분리해서 list에 담아준다.
    numbers = []
    for i in num_str:
        numbers.append(int(i))

    # 숫자의 범위가 0~10으로 제한되어있으므로 counting 기법을 활용한다.
    count = [0] * 10
    for i in numbers:
        count[i] += 1

    # count된 list에 enumerate를 활용해 idx(원래 숫자)를 배정해준다.
    idx_num = list(enumerate(count))

    # 최빈값과 등장횟수를 양식에 맞게 출력해준다.    
    print('#{} {} {}'.format(t, max_idx_val(idx_num)[0], max_idx_val(idx_num)[1]))




    

    