# babygin
# 유튜브 라이브
# 220808

# 해당 문제는 유튜브 라이브에서 교수님이 풀어주셔서 해당 내용을 토대로 풀이 코드를 작성했습니다.

#정답코드

T = int(input())

for t in range(1, T+1):
    num = int(input()) # Baby Gin 확인할 6자리 수
    c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

    # 리스트에 입력받은 num에서 6개 숫자의 등장 횟수를 넣어준다.
    for n in range(6):
        c[num % 10] += 1
        num //= 10

    i = 0
    tri = run = 0
    while i < 10:
        if c[i] >= 3: # triplete 조사 후 데이터 삭제
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:  #run 조사 후 데이터 삭제
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1

    # baby-gin이면 1, 아니면 0을 출력해준다.
    if run + tri == 2:
        print('#{} 1'.format(t))
    else: 
        print('#{} 0'.format(t))