import sys

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
PRINT MAP DEFINITIONS
'''
BLOCK_CHAR	= "X"
FREE_CHAR	= " "
END_CHAR	= "E" 
START_CHAR 	= "S" 

FREE = 0
BLOCK = 1
START = 8
END = 9

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
