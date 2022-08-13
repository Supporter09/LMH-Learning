input_file = open('D:\Code\LMH Learning\Thuật toán quay lui(Backtrack(\ARRANGE.INP','r')
output_file = open('D:\Code\LMH Learning\Thuật toán quay lui(Backtrack(\ARRANGE.OUT','w+')

def printResult(k, arr):
    for i in range(1,k+1):
        print(arr[i], end=" ")
        output_file.write('%s '%str(arr[i]))
    print()
    output_file.write('\n')

def Try(i, n, k, arr, check):
    for j in range(1,n+1):
        if check[j]:
            arr[i] = j
            if i == k:
                printResult(k, arr)
            else:
                check[j] = False
                Try(i+1, n, k, arr, check)
                check[j] = True

def main():
    n, k = list(map(int, input_file.readline().replace('\n','').split()))
    arr = [0 for i in range(n+1)]
    check = [True for i in range(n+1)] # Kỹ thuật mảng đánh dấu để check các phần từ đã sử dụng
    Try(1, n, k, arr, check)
    
main()