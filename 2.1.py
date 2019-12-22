
for i in range(25, 50):
	for j in range(25, 50):
		intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,5,19,23,2,9,23,27,1,27,5,31,2,31,13,35,1,35,9,39,1,39,10,43,2,43,9,47,1,47,5,51,2,13,51,55,1,9,55,59,1,5,59,63,2,6,63,67,1,5,67,71,1,6,71,75,2,9,75,79,1,79,13,83,1,83,13,87,1,87,5,91,1,6,91,95,2,95,13,99,2,13,99,103,1,5,103,107,1,107,10,111,1,111,13,115,1,10,115,119,1,9,119,123,2,6,123,127,1,5,127,131,2,6,131,135,1,135,2,139,1,139,9,0,99,2,14,0,0]
		intcode[1] = i
		intcode[2] = j

		currPos = 0
		currInt = intcode[currPos]

		while currInt != 99:

			input1index = intcode[currPos + 1]
			input2index = intcode[currPos + 2]
			input1 = intcode[input1index]
			input2 = intcode[input2index]
			outputIndex = intcode[currPos + 3]

			if currInt == 1:
				intcode[outputIndex] = input1 + input2
			elif currInt == 2:
				intcode[outputIndex] = input1 * input2
			else:
				print "error currInt = " + currInt

			currPos += 4
			currInt = intcode[currPos]

		print str(intcode[0]) + " " + str(i) + " " + str(j)
		#print intcode