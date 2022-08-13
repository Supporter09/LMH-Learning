import time
input_file = open('D:\Code\LMH Learning\Backtrack\DEM_DOAN.INP', 'r')
output_file = open('DEM_DOAN.OUT', 'w+')

# def find(l, r, n):
# 	if r >= l:
# 		mid = l + (r-l)//2
# 		check = n % (mid*2)
# 		# if check == 1:
# 		# 	return find(l,mid-1,n)
# 		# else:
# 		for i in range(check+1):
# 			for j in range(check*2):
# 				start =  mid-i 
# 				end = mid+j
# 				total = ((start + end)*(end - start + 1))//2
# 				if total == n:
# 					print(total)
# 		if ( n//2 - mid ) > 1:
# 			return find(mid,r,n)
# 		if (mid - (n/(l + mid))) >= 0:
# 			return find(l,mid,n)
		
# 	else:
# 		return -1

# An efficient program
# to print subarray
# with sum as given sum

# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result.
def subArraySum(arr, n, sum_):
	
	# Initialize curr_sum as
	# value of first element
	# and starting point as 0
	curr_sum = arr[0]
	start = 0

	# Add elements one by
	# one to curr_sum and
	# if the curr_sum exceeds
	# the sum, then remove
	# starting element
	i = 1
	while i <= n:
		
		# If curr_sum exceeds
		# the sum, then remove
		# the starting elements
		while curr_sum > sum_ and start < i-1:
		
			curr_sum = curr_sum - arr[start]
			start += 1
			
		# If curr_sum becomes
		# equal to sum, then
		# return true
		if curr_sum == sum_:
			print ("Sum found between indexes")
			print ("% d and % d"%(start+1, i))
			

		# Add this element
		# to curr_sum
		if i < n:
			curr_sum = curr_sum + arr[i]
		i += 1

	# If we reach here,
	# then no subarray
	# print ("No subarray found")
	return 0

def subarraySum( nums, k):

	ans=0
	prefsum=0
	d={0:1}

	for num in nums:
		prefsum = prefsum + num

		if prefsum-k in d:
			ans = ans + d[prefsum-k]

		if prefsum not in d:
			d[prefsum] = 1
		else:
			d[prefsum] = d[prefsum]+1

	return ans


def main():
	N = int(input_file.readline().replace('\n',''))
	arr = [i for i in range(1,N//2+2)]
	subArraySum(arr, len(arr), N)
	# find(0,N//2, N)
	# O(N^2)
	# for i in range(1,int(N/2)+3):
	# 	for j in range(i, int(N/2) +3):
	# 		check = int(((j+i)*(j-i+1))/2)
	# 		if(check == N):
	# 			arr.append([i,j])
	# 		elif(check > N):
	# 			break
	# arr.append([N,N])
	# input_file.close()
	# output_file.write(str(arr)) 
	# print(arr)

	#Binary Search
	L = 0
	R = N
	return
start = time.time()
main()
end = time.time()
print(end-start)