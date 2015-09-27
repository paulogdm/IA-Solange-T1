#External imports
import sys

#Project internal imports
import utils


def DFS(map, covered, idx):
	
	stack = []

	covered[idx[0]][idx[1]] = 1

	if(map[idx[0]][idx[1]] == utils.getEndAlias()):
		stack.append(idx)
		return stack
	
	options = utils.getOptions(map, idx, covered)

	for fork in options:
		stack = DFS(map, covered, fork)
		if stack:
			stack.append(idx)
			return stack

	return stack

def createEmptyMatrix(x, y):

	new_matrix = [[0 for i in range(x)] for j in range(y)] 

	return new_matrix

def printPath(list):
	print("Mask = [LINE, COLUMN]")
	print("Start!", end=" ")
	for point in list:
		print(point, end ="->")
	print(" End!")

def main():
	map = utils.readBitmap("map1.bmp")

	covered = createEmptyMatrix(len(map[0]), len(map))

	stack = DFS(map, covered, utils.findStart(map))

	printPath(reversed(stack))

if __name__ == "__main__":
    main()

