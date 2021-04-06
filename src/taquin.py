from utils import *
from math import *
from copy import deepcopy
import argparse

class Taquin(object):
	def __init__(self, board, heuristic='manhatan'):
		self.size = len(board)
		self.board = deepcopy(board)
		self.heuristic = heuristic
		if not self.isSolvable(board):
			error('unsolvable')
		if self.isSolved():
			error('Already solved')
		self.closed_list = [self.hash(self.board)]
		self.timeComplexity = 1
		self.spaceComplexity = 1
		self.solution = []
		self.bestScore = 99999
		self.tmpSolution = []


	# Apply "function" to each tuile of the taquin in the right order
	def map(self,  function, board=None, begin=0):
		directions = [
			{'begin': 0, 'end': self.size -1, 'step': 1},	# right
			{'begin': 1, 'end': self.size -1, 'step': 1},	# down
			{'begin': self.size -2, 'end': 0, 'step': -1},	# left
			{'begin': self.size -2, 'end': 1, 'step': -1}	# up
		]
		board = self.board if board is None else board
		data = {'x': 0, 'y': 0, 'i': 0}
		ret = []
		d = 0
		while data['i'] <= self.size*self.size - 1:
			if data['i'] >= begin:
				r = function(data, board)
				if r is not None:
					ret.append(r)
			data['i'] += 1
			if d % 2 == 0:
				if data['y'] == directions[d]['end']:
					directions[d]['begin'] += directions[d]['step']
					directions[d]['end'] -= directions[d]['step']
					d = 0 if d >= len(directions) -1 else d + 1
					data['x'] = directions[d]['begin']
				else:
					data['y'] += directions[d]['step']
			else:
				if data['x'] == directions[d]['end']:
					directions[d]['begin'] += directions[d]['step']
					directions[d]['end'] -= directions[d]['step']
					d = 0 if d >= len(directions) -1 else d + 1
					data['y'] = directions[d]['begin']
				else:
					data['x'] += directions[d]['step']
		return ret

	# check if the taquin is currently solved or not
	def isSolved_map(self, data, board=None):
		board = self.board if board is None else board
		if board[data['x']][data['y']] == data['i'] + 1 or (data['i'] == self.size*self.size-1 and board[data['x']][data['y']] == 0):
			return True
		return False

	def isSolved(self, board=None):
		board = self.board if board is None else board
		return all(self.map(self.isSolved_map, board))

	def inversionCount__map(self, data, board=None):
		board = self.board if board is None else board
		return 1 if self.toCmp > board[data['x']][data['y']] and board[data['x']][data['y']] != 0 else 0

	def inversionCount_map(self, data, board=None):
		self.toCmp = board[data['x']][data['y']]
		board = self.board if board is None else board
		return sum(self.map(self.inversionCount__map, board, data['i']))

	def inversionCount(self, board=None):
		board = self.board if board is None else board
		return sum(self.map(self.inversionCount_map, board))

	def isSolvable(self, board=None):
		board = self.board if board is None else board
		return True if not self.inversionCount(board) % 2 else False

	def getCoor(self, value, board=None):
		return {
			'x': [board.index(line) for line in board if value in line][0],
			'y': [line.index(value) for line in board if value in line][0]
		}

	def getDestCoor_map(self, data, board=None):
		board = self.board if board is None else board
		if data['i'] + 1 == self.toCmp or (self.toCmp == 0 and data['i'] == self.size*self.size-1):
			return {'x': data['x'], 'y': data['y']}

	def getDestCoor(self, value, board=None):
		board = self.board if board is None else board
		self.toCmp = value;
		ret = self.map(self.getDestCoor_map, board)
		return ret[0] if len(ret) == 1 else None;


	def hash(self, board=None):
		board = self.board if board is None else board
		tmp = []
		for line in board:
			tmp.append(hash(tuple(line)));
		return hash(tuple(tmp))

	def manhatan(self, board=None):
		board = self.board if board is None else board
		score = 0
		for line in board:
			for tuile in line:
				p =  self.getCoor(tuile, board);
				d = self.getDestCoor(tuile)
				score += abs(p['x'] - d['x']) + abs(p['y'] - d['y'])
		return score

	def euclide(self, board=None):
		board = self.board if board is None else board
		score = 0
		for line in board:
			for tuile in line:
				p =  self.getCoor(tuile, board);
				d = self.getDestCoor(tuile)
				d1 = abs(p['x'] - d['x'])
				d2 = abs(p['y'] - d['y'])
				score +=  sqrt(d1*d1+d2*d2)
		return score

	def all(self, board=None):
		board = self.board if board is None else board
		return self.manhatan(board) + self.euclide(board) / 5 + self.inversionCount(board) / 2



	def score(self, board=None):
		board = self.board if board is None else board
		if self.heuristic == 'all':
			return self.all(board)
		if self.heuristic == 'inversions':
			return self.inversionCount(board) / 2
		if self.heuristic == 'euclide':
			return self.euclide(board)
		return self.manhatan(board)

	def getLegalMove(self, board=None):
		board = self.board if board is None else board
		emptyCaseCoor = self.getCoor(0, board);
		ret = []
		if emptyCaseCoor['x'] > 0:
			ret.append('down')
		if emptyCaseCoor['x'] < self.size - 1: 
			ret.append('up')
		if emptyCaseCoor['y'] > 0: 
			ret.append('right')
		if emptyCaseCoor['y'] < self.size - 1: 
			ret.append('left')
		return ret

	def backMove(self, direction):
		if direction == 'up':
			return 'down';
		if direction == 'down':
			return 'up';
		if direction == 'left':
			return 'right';
		if direction == 'right':
			return 'left';

	def move(self, direction, board=None):
		board = self.board if board is None else board
		if direction in self.getLegalMove(board):
			p =  self.getCoor(0, board);
			if direction == "right":
				board[p['x']][p['y']] = board[p['x']][p['y'] - 1];
				board[p['x']][p['y'] - 1] = 0;
			elif direction == "left":
				board[p['x']][p['y']] = board[p['x']][p['y'] + 1];
				board[p['x']][p['y'] + 1] = 0;
			elif direction == "down":
				board[p['x']][p['y']] = board[p['x'] - 1][p['y']];
				board[p['x'] - 1][p['y']] = 0;
			elif direction == "up":
				board[p['x']][p['y']] = board[p['x'] + 1][p['y']];
				board[p['x'] + 1][p['y']] = 0;

	def test_move(self, direction, board=None):
		board = self.board if board is None else board
		self.move(direction, board)
		score = -1 if self.hash(board) in self.closed_list else self.score(board);
		self.move(self.backMove(direction), board)
		return score

	def getMoves(self, board=None):
		board = self.board if board is None else board
		moves = []
		scores = []
		for move in self.getLegalMove(board):
			score = self.test_move(move, board)
			if score > 0:
				scores.append(score)
				moves.append(move)
		return moves, scores

	def resolv(self):
		while not self.isSolved():
			moves, scores = self.getMoves();		
			if any([True if score >= 0 else False for score in scores]):
				deep += 1
				move = moves[scores.index(min([score for score in scores if score >= 0]))]
				solution.append(move)
				self.move(move);
				self.closed_list.append(self.hash())     
				self.timeComplexity += 1
				self.spaceComplexity += 1
			elif len(solution) >= 1:
				deep -= 1
				self.move(self.backMove(solution[-1]));
				solution.pop()
				self.timeComplexity += 1
		return self.showSolution()

	
	def board(self, board=None):
		board = self.board if board is None else board
		for line in board:
			print(line)
			
	def showSolution(self):
		print('Time complexity :', self.timeComplexity)
		print('Space complexity : ', self.spaceComplexity)
		print('Move count  : ', len(self.solution))
		print('Moves : ', self.solution)
		return (self.solution)