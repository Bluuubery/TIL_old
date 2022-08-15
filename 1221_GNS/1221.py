# 220812
# 1221 GNS

# 정답코드
import sys

sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())

for t in range(T):
    # 테스트 케이스와 길이를 입력 받는다.
    # 길이 N은 입력만 받고 활용을 하지 않기 때문에 굳이 정수형으로 변환하지 않아도 된다.
    tc, N = input().split()

    # 숫자 정보를 입력 받는다.
    numbers = list(map(str, input().split()))

    # 키: 숫자 이름, 값: 빈 리스트(이후 숫자를 담아준다)인 딕셔너리를 만든다.
    num_dict = {
        'ZRO': [],
        'ONE': [],
        'TWO': [],
        'THR': [],
        'FOR': [],
        'FIV': [],
        'SIX': [],
        'SVN': [],
        'EGT': [],
        'NIN': []
    }

    # 숫자를 딕셔너리에 담아준다.
    for number in numbers:
        num_dict[number].append(number)

    # 딕셔너리에서 값만 추출해낸다.
    sorted_num = num_dict.values()

    # 정답을 양식에 맞게 출력한다.
    print(tc)
    for num_list in sorted_num:
        print(*num_list, end=' ')
    print()