#External imports
import sys
import math

#Project internal imports
import utils


'''
Heuristic function. Change the order of options to value reasonable choices.
# idx 	= actual position
# map	= map with a start for the robot
# end 	= index
'''
def evaluateBestOptions(map, options, const_end):

	for i in range(0, len(options)-1):
		for j in range(i+1, len(options)):
			if(distanceToEnd(options[i], const_end) > distanceToEnd(options[j], const_end)):
				options[i], options[j] = options[j], options[i]

	return options


def distanceToEnd(position, const_end):

	xd = const_end[0] - position[0]
	yd = const_end[1] - position[1]

	return math.sqrt(xd**2 + yd**2)


'''
DFS function. Pure backtracking
# map 		= map with a start for the robot
# covered 	= paths already covered by robot
# idx 		= actual position
# end 		= index  
'''
def DFS(map, covered, idx, const_end):

	stack = []
	#clean index stack for recursion

	covered[idx[0]][idx[1]] = 1
	#covering position

	#if is the END. Celebrate and stop the recursion
	if(map[idx[0]][idx[1]] == utils.getEndAlias()):
		#append the final position and return the stack so far
		covered[idx[0]][idx[1]] = 150
		stack.append(idx)
		return stack
	
	#"where can i go?" Said the little robot
	options = utils.getOptions(map, idx, covered)

	options = evaluateBestOptions(map, options, const_end)

	#if we have options go ahead and try
	for fork in options:
		
		#trying each option recursively
		stack = DFS(map, covered, fork, const_end)

		#If success, append the position and return the stack so far
		if stack:
			stack.append(idx)
			covered[idx[0]][idx[1]] = 150
			return stack

	#return the empty stack
	return stack


'''
Print the list of coordinates
# list = list of coordinates
'''
def printPath(list):
	if list:
		print("Mask = [X, Y]")
		print("Start!", end=" ")
		for point in list:
			print(point, end ="->")
		print(" End!")

	#se a lista eh vazia
	else:
		print("No path available. The map is correct?")

'''
Main function
require sys args
'''
def main():

	#checking arguments
	if(len(sys.argv)!= 2 ):
		print("Usage: %s <BMP_FILE_NAME>" % str(sys.argv[0]))

	else :
		#file name from first arg
		file_name = str(sys.argv[1])

		#map from bitmap
		map = utils.readBitmap(file_name)

		#creating the aux matrix
		covered = utils.createEmptyMatrix(len(map[0]), len(map))

		#starting Heuristic Search

		stack = DFS(map, covered, utils.findStart(map), utils.findEnd(map))

		utils.writeBitmap(file_name, "out_heuris_", map, stack, covered)

if __name__ == "__main__":
    main()

