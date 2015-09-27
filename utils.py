#required libs
import sys
from PIL import Image


'''
Main definitions
'''
FREE 	= 0
BLOCK 	= 1
START 	= 8
END 	= 9


def getStartAlias():
	return START

def getEndAlias():
	return END

def getFreeAlias():
	return FREE

def getBlockAlias():
	return BLOCK

'''
readMatrix is a function to read from a txt
Check the "Main definitions"

Format:
<X> <Y>
<X elements>
...Y times

Example:
4 3
8001
1100
1119
'''
def readMatrix(file_name):
	
	#open txt file
	file = open(file_name, "r")

	#read the first line to get X and Y
	buffer = file.readline()
	
	#x and y reading
	x = int(buffer.split(" ")[0])
	y = int(buffer.split(" ")[1])

	#empty list
	matrix = []

	#main loop
	for i in range(0, y):
		#new line
		temp = []

		#read the line
		for j in range(0, x):
			#append the integer
			temp.append(int (file.read(1)))

		#absorb the new line character
		file.read(1)
		
		#append the line
		matrix.append(temp)

	#never forget
	file.close()

	#return the matrix
	return matrix

'''
Bitmap reading
'''

def readBitmap(file_name):

	#open the image
	img = Image.open(file_name)
	#converting to RGB
	rgb_img = img.convert('RGB')

	#evaluating size
	x = rgb_img.size[0]
	y = rgb_img.size[1]

	#empty matrix map
	matrix = []

	#converting bmp into int matrix
	#check main definitions
	for i in range(y):
		#new line
		temp = []

		for j in range(x):
			
			#receiving the right pixel
			pixel = rgb_img.getpixel((j, i))
			
			#converting pixel
			block = pixelSwitch(pixel)

			#append code to the list
			temp.append(block)

		#append line of integers to matrix
		matrix.append(temp)

	return matrix

'''
BITMAP PIXELS DEFINITIONS
'''
RED 	= (255,0,0)
GREEN 	= (0,255,0)
BLACK 	= (0,0,0)
WHITE 	= (255,255,255)

def pixelSwitch(pixel):

	if(pixel == RED):
		block = END
	elif(pixel == GREEN):
		block = START
	elif(pixel == BLACK):
		block = BLOCK
	elif(pixel == WHITE):
		block = FREE
	else: block = FREE
	
	return block


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

'''
if the index given is a valid option or not
basically we check:
	index ranges (X and Y)
	is not a block
	was not processed yet
'''
def isValidOption(map, idx, covered):
	if(idx[0] >= 0 and idx[0] < len(map)):
		if(idx[1] >= 0 and idx[1] < len(map[0])):
			if(map[idx[0]][idx[1]] != BLOCK):
				if(covered[idx[0]][idx[1]] == 0):
					return True
	return False


'''
evaluate options up, down, left and right
is faster to check it with 4 ifs
'''
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


'''
find the start position
O(n*m)
'''
def findStart(matrix):
	lines_idx = 0
	for lines in matrix:
		if START in lines:
			return [lines_idx, lines.index(START)]
		lines_idx+=1

	return [len(matrix), len(matrix)]
