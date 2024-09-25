#running total 

running_sum = 0 

#Loop 1-1000 
for num in range(1000):
	if num % 3 == 0 or num % 5 ==0:
		running_sum += num


print(running_sum)
