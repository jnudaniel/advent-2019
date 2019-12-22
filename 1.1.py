import math

input = open("1.1.input.txt")
modules = input.readlines()
sum = 0

def getFuel(module):
	fuelForModule = math.floor(int(module) / 3) - 2
	if fuelForModule <= 0:
		return 0
	return fuelForModule + getFuel(fuelForModule)

for module in modules:
	fuel = getFuel(module)
	sum += fuel
	print fuel

print sum