#!/usr/bin/env python
import re
from utils import *

def checkBoard(board):
	size = len(board)
	met = []
	if size < 3:
		error("invalid board size")
	for i in range(0, len(board)):
		if len(board[i]) != size:
			error("invalid line size")
		for j in range(0, len(board[i])):
			if board[i][j] < 0 or board[i][j] > size*size:
				error("invalid value : "+ board[i][j])
			if board[i][j] in met:
				error("invalid value")
			met.append(board[i][j])
	return True

def getBoard(filepath):
	board = []
	size = 0;
	try:
		file = open(filepath, 'r')
	except OSError:
		error("invalid file " + filepath)
	with file:
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