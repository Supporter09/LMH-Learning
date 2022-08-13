m(arr, n, sum_):
	
# 	# Initialize curr_sum as
# 	# value of first element
# 	# and starting point as 0
# 	curr_sum = arr[0]
# 	start = 0

# 	# Add elements one by
# 	# one to curr_sum and
# 	# if the curr_sum exceeds
# 	# the sum, then remove
# 	# starting element
# 	i = 1
# 	while i <= n:
		
# 		# If curr_sum exceeds
# 		# the sum, then remove
# 		# the starting elements
# 		while curr_sum > sum_ and start < i-1:
		
# 			curr_sum = curr_sum - arr[start]
# 			start += 1
			
# 		# If curr_sum becomes
# 		# equal to sum, then
# 		# return true
# 		if curr_sum == sum_:
# 			print ("Sum found between indexes")
# 			print ("% d and % d"%(start+1, i))
			

# 		# Add this element
# 		# to curr_sum
# 		if i < n:
# 			curr_sum = curr_sum + arr[i]
# 		i += 1

# 	# If we reach here,
# 	# then no subarray
# 	# print ("No subarray found")
# 	return 0