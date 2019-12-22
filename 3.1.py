from random import *

infile = open("input3.1.txt")
paths = infile.readlines()

path1str = paths[0]#"R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"#"R8,U5,L5,D3" #paths[0]
path2str = paths[1]#"U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"#"U7,R6,D4,L4" #paths[1]

print path1str
print path2str

path1 = path1str.split(',')
path2 = path2str.split(',')

wire1 = [(0, 0)]
wire2 = [(0, 0)]

def getSubpath1(dest, wire):
	dirxn = dest[0]
	dist = int(dest[1:])
	origin = wire[-1]
	if dirxn == 'R':
		for i in range(1, dist + 1):
			wire.append((origin[0] + i, origin[1]))
	elif dirxn == 'L':
		for i in range(1, dist + 1):
			wire.append((origin[0] - i, origin[1]))
	elif dirxn == 'U':
		for i in range(1, dist + 1):
			wire.append((origin[0], origin[1] + i))
	elif dirxn == 'D':
		for i in range(1, dist + 1):
			wire.append((origin[0], origin[1] - i))
	else:
		print "Unrecognizable direction", dirxn
	# print wire

def appendPoint(wire1, wire2, point):
	if point in wire1:
		wire2.append(point)
	if randint(0, 1000) == 1:
		print wire2, point

def getSubpath2(dest, wire, origin):
	dirxn = dest[0]
	dist = int(dest[1:])
	if dirxn == 'R':
		for i in range(1, dist + 1):
			point = (origin[0] + i, origin[1])
			appendPoint(wire1, wire2, point)
		return (origin[0] + dist, origin[1])
	elif dirxn == 'L':
		for i in range(1, dist + 1):
			point = (origin[0] - i, origin[1])
			appendPoint(wire1, wire2, point)
		return (origin[0] - dist, origin[1])
	elif dirxn == 'U':
		for i in range(1, dist + 1):
			point = (origin[0], origin[1] + i)
			appendPoint(wire1, wire2, point)
		return (origin[0], origin[1] + dist)
	elif dirxn == 'D':
		for i in range(1, dist + 1):
			point = (origin[0], origin[1] - i)
			appendPoint(wire1, wire2, point)
		return (origin[0], origin[1] - dist)
	else:
		print "Unrecognizable direction", dirxn
	# print wire
'''
def getSubpath2(dest, wire, origin):
	dirxn = dest[0]
	dist = int(dest[1:])
	if dirxn == 'R':
		for i in range(1, dist + 1):
			point = (origin[0] + i, origin[1])
			appendPoint(wire1, wire2, point)
		return (origin[0] + dist, origin[1])
	elif dirxn == 'L':
		for i in range(1, dist + 1):
			wire.append((origin[0] - i, origin[1]))
		return (origin[0] - dist, origin[1])
	elif dirxn == 'U':
		for i in range(1, dist + 1):
			wire.append((origin[0], origin[1] + i))
		return (origin[0], origin[1] + dist)
	elif dirxn == 'D':
		for i in range(1, dist + 1):
			wire.append((origin[0], origin[1] - i))
		return (origin[0], origin[1] - dist)
	else:
		print "Unrecognizable direction", dirxn
	# print wire
'''
for i in path1:
	getSubpath1(i, wire1)
origin = (0, 0)
for i in path2:
	origin = getSubpath2(i, wire2, origin)
print wire1
print wire2

crossovers = []
crossover_dists = []

for locus in wire2:
	crossover_dists.append(abs(locus[0]) + abs(locus[1]))
'''
for locus in wire1:
	if locus in wire2:
		crossovers.append(locus)
		crossover_dists.append(abs(locus[0]) + abs(locus[1]))

print crossovers
print crossover_dists
'''
print min(crossover_dists[1:])
