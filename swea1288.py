# 220814 swea 1288 새로운 불면증 치료법

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    numbers = {}
    sheep = N

    while True:
        for i in str(sheep):
            numbers[i] = 1

        if len(numbers) == 10:
            break

        sheep += N

    print('#{} {}'.format(t, sheep))
