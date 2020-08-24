#0으로 삼각형 만들기
def init_triangle(n):
    arr = []
    for r in range(n):
        row = []
        for c in range(r + 1):
            row.append(0)
        arr.append(row)
    return arr

#숫자 채워넣기
def num_in_triangle(n):
    init_triangle(n)
    for r in range(n):
        for c in range(r):
            arr [r][0] = 1
            arr [r][r] = 1
            arr [r][c] = arr [r - 1][c - 1] + arr [r - 1][c]
    print(arr)

#실행
n = int(input("몇 줄? "))

num_in_triangle(n)


