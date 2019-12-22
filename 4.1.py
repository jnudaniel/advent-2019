'''
6 digit number
at each step, can choose to increase or no
if increase, can increase by 1 to 9-n
	all following numbers must also be floored up
	avoid dupes
if no dupes in whole number, number doesn't count
only count numbers within range


5 digit number

at each step, can choose to increase or no
	if increase, can increase by 1 to 9-n
	all following numbers must also be floored up

then each index duped one by one, without double-counting (if adjacent numbers same)

12345
112345
122345
123345
123445
123455
12234
112234
122234
122234

'''
valid_digits = [111]
start_digits = [1, 1, 1]
start_increases = 0
MAX_DIGIT = 2
#start with all numbers between 111 and 344, max digit is 4

def count_options(digits, i):
	print digits, i
	if i >= len(digits):
		print 1
		return 0
	if digits[i] >= MAX_DIGIT:
		print 0
		return 0
	total = 1
	for j in range(1, MAX_DIGIT - digits[i] + 1):
		print j
		flipped = digits
		flipped[i] += j
		total += count_options(flipped, i + 1)
	return total + count_options(digits, i + 1)

print count_options([0, 0], 0)

'''
def count_options(digits, i):
	print digits, i
	if i >= len(digits):
		print 1
		return 0
	if digits[i] >= MAX_DIGIT:
		print 0
		return 0
	total = 1
	for j in range(MAX_DIGIT - digits[i] + 1):
		print j
	flipped = digits
	flipped[i] += 1
	return total count_options(digits, i + 1) + count_options(flipped, i + 1) + 1
'''



