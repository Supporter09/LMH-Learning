#  Với n = 5, k = 3, vẽ cây tìm kiếm quay lui của chương trình liệt kê tổ hợp chập k của tập { 1, 2, ..., n } nhập vào từ bàn phím

def printResult(i, k, arr):
    for i in range(1,k+1):
        print(arr[i], end=" ") 
    print()

def Try(i, n, k, arr):
    for j in range(arr[i-1]+1,n-k+i+1): # Voi moi x_i thi x_i co the nhan cac gia tri tu x_i-1 + 1 => n-k+i (+1 trong code do python se chi chay den end-1)
        arr[i] = j
        if i == k: #Diem dung (breakpoint)
            printResult(i, k, arr)
        else:
            Try(i+1, n, k, arr) #(Backtrack)

def main():
    n, k = 5, 3
    arr = [0 for i in range(n+1)]
    Try(1, n, k, arr)

main()