input_file = open('D:/Code/LMH Learning/Thuật toán quay lui(Backtrack(/BSTR.INP','r')
output_file = open('D:/Code/LMH Learning/Thuật toán quay lui(Backtrack(/BSTR.OUT', 'w+')

def printResult(arr):
    arr = [str(i) for i in arr]
    result = ''.join(arr)
    print(result)
    output_file.write('%s'%result)

def Try(i, n, arr):
    for j in range(2):
        arr[i] = j
        if i == n-1: 
            printResult(arr)
        else:
            Try(i+1, n, arr)

def main():
    n = int(input_file.readline().replace('/n',''))
    input_file.close()
    arr = [0 for i in range(n)]
    print(arr)
    Try(0,n,arr)

main()
