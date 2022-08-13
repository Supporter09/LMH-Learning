# Liệt kê tất cả các tập con của tập S gồm n số nguyên {S[1], S[2], ..., S[n]} nhập vào từ bàn phím 

def printResult(k, x, arr):
    for i in range(1, k+1):
        print(arr[x[i]-1], end=" ")
    print()


def Try(i, n, k, x, arr):
    # Voi moi x_i thi x_i co the nhan cac gia tri tu [x_i-1] + 1 => n-k+i (+1 trong code do python se chi chay den end-1)
    for j in range(x[i-1]+1, n-k+i+1):
        x[i] = j
        if i == k:  # Diem dung (breakpoint)
            printResult(k, x, arr)
        else:
            Try(i+1, n, k, x, arr)  # (Backtrack)


def main():
    n = int(input())
    arr = (list(map(int, input().split())))
    for j in range(1, n+1):
        x = [0 for _ in range(n+1)]
        Try(1, n, j, x, arr)


main()
