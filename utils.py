import sys

from PIL import Image

FREE = 0
BLOCK = 1
START = 8
END = 9

def readMatrix(file_name):
	
	file = open(file_name, "r")

	buffer = file.readline()
	
	x = int(buffer.split(" ")[0])
	y = int(buffer.split(" ")[1])

	matrix = []

	for i in range(0, y):
		temp = []
		for j in range(0, x):
			temp.append(int (file.read(1)))
		file.read(1)
		
		matrix.append(temp)

	file.close()

	return matrix

'''
BITMAP DEFINITIONS
'''
RED 	= (255,0,0)
GREEN 	= (0,255,0)
BLACK 	= (0,0,0)
WHITE 	= (255,255,255)

def readBitmap(file_name):
	img = Image.open(file_name)
	rgb_img = img.convert('RGB')

	x = rgb_img.size[0]
	y = rgb_img.size[1]

	matrix = []

	for i in range(y):
		temp = []
		for j in range(x):
			
			pixel = rgb_img.getpixel((j, i))
			
			if(pixel == RED):
				block = END
			elif(pixel == GREEN):
				block = START
			elif(pixel == BLACK):
				block = BLOCK
			elif(pixel == WHITE):
				block = FREE
			else: block = FREE

			temp.append(block)

		matrix.append(temp)

	return matrix

'''
PRINT MAP DEFINITIONS START
'''
BLOCK_CHAR	= "X"
FREE_CHAR	= " "
END_CHAR	= "E" 
START_CHAR 	= "S" 

def printMap(matrix):

	for line in matrix:
		for char in line:
			if(char == BLOCK): print_char = BLOCK_CHAR
			elif(char == FREE): print_char = FREE_CHAR
			elif(char == START): print_char = START_CHAR
			elif(char == END): print_char = END_CHAR
			else : print_char = "?"

			print(print_char, end="")

		print()
	return


def getStartAlias():
	return START

def getEndAlias():
	return END

def isValidOption(map, idx, covered):
	if(idx[0] >= 0 and idx[0] < len(map)):
		if(idx[1] >= 0 and idx[1] < len(map[0])):
			if(map[idx[0]][idx[1]] != BLOCK):
				if(covered[idx[0]][idx[1]] == 0):
					return True
	return False

def getOptions(map, idx, covered):
	
	idx_list = []

	if(isValidOption(map, [idx[0], idx[1]+1], covered)):
		idx_list.append([idx[0], idx[1]+1])
	if(isValidOption(map, [idx[0]+1, idx[1]], covered)):
		idx_list.append([idx[0]+1, idx[1]])
	if(isValidOption(map, [idx[0], idx[1]-1], covered)):
		idx_list.append([idx[0], idx[1]-1])
	if(isValidOption(map, [idx[0]-1, idx[1]], covered)):
		idx_list.append([idx[0]-1, idx[1]])
	
	return idx_list


def findStart(matrix):
	lines_idx = 0
	for lines in matrix:
		if START in lines:
			return [lines_idx, lines.index(START)]
		lines_idx+=1

	return [len(matrix), len(matrix)]
