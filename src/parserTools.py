import re
from utils import *

#check if board is or not valid
def checkBoard(board):
	size = len(board)
	if size < 3:
		error('minimal board size is 3')
	met = []
	for i in range(0, len(board)):
		for j in range(0, len(board[i])):
			if len(board[i]) != size or board[i][j] < 0 or board[i][j] > size*size or board[i][j] in met:
				error('invalid board')
			met.append(board[i][j])
	return True

#return board from args
def getBoard(filepath):
	try:
		file = open(filepath, 'r')
	except OSError:
		error("Could not open/read/find " + filepath)
	with open(filepath, 'r') as file:
		board = []
		size = 0;
		lines = re.sub(r'#.*', '', file.read()).split('\n')
		for i in range(0, len(lines)):
			line_arr = []
			line = lines[i].split(' ')
			for j in range(0, len(line)):
				if not size and line[j].isnumeric():
					size = int(line[j])
				elif line[j] and line[j].isnumeric():
					line_arr.append(int(line[j]))
			if len(line_arr) > 0:
				board.append(line_arr)
		if checkBoard(board):
			return (board)