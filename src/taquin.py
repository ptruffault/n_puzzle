from utils import *
from math import *
from copy import deepcopy

class Taquin(object):
	def __init__(self, board):
		self.board = deepcopy(board)
		self.size = len(board)
		if not self.isSolvable():
			error('unsolvable')
		if self.isSolved():
			error('Already solved')
		self.closed_list = [self.hash(self.board)]
		self.timeComplexity = 1
		self.spaceComplexity = 1
		self.solution = []


	# Apply "function" to each tuile of the taquin in the right order
	def map(self, function, begin=0):
		directions = [
			{'begin': 0, 'end': self.size -1, 'step': 1},	# right
			{'begin': 1, 'end': self.size -1, 'step': 1},	# down
			{'begin': self.size -2, 'end': 0, 'step': -1},	# left
			{'begin': self.size -2, 'end': 1, 'step': -1}	# up
		]
		data = {'x': 0, 'y': 0, 'i': 0}
		ret = []
		d = 0
		while data['i'] <= self.size*self.size - 1:
			if data['i'] >= begin:
				r = function(data)
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
	def isSolved_map(self, data):
		if self.board[data['x']][data['y']] == data['i'] + 1 or (data['i'] == self.size*self.size-1 and self.board[data['x']][data['y']] == 0):
			return True
		return False

	def isSolved(self):
		return all(self.map(self.isSolved_map))

	def isSolvable__map(self, data):
		return 1 if self.toCmp > self.board[data['x']][data['y']] and self.board[data['x']][data['y']] != 0 else 0

	def isSolvable_map(self, data):
		self.toCmp = self.board[data['x']][data['y']]
		return sum(self.map(self.isSolvable__map, data['i']))

	def inversionCount(self):
		return sum(self.map(self.isSolvable_map))

	def isSolvable(self):
		return True if not self.inversionCount() % 2 else False

	def getCoor(self, board, value):
		return {
			'x': [board.index(line) for line in board if value in line][0],
			'y': [line.index(value) for line in board if value in line][0]
		}

	def getDestCoor_map(self, data):
		if data['i'] + 1 == self.toCmp or (self.toCmp == 0 and data['i'] == self.size*self.size-1):
			return {'x': data['x'], 'y': data['y']}

	def getDestCoor(self, value):
		self.toCmp = value;
		ret = self.map(self.getDestCoor_map)
		return ret[0] if len(ret) == 1 else None;


	def hash(self, board):
		tmp = []
		for line in board:
			tmp.append(hash(tuple(line)));
		return hash(tuple(tmp))

	def manhatan(self, board):
		score = 0
		for line in board:
			for tuile in line:
				p =  self.getCoor(board, tuile);
				d = self.getDestCoor(tuile)
				score += abs(p['x'] - d['x']) + abs(p['y'] - d['y'])
		return score

	def score(self, board):
		#return self.inversionCount() / 2
		return self.manhatan(board)


	def getLegalMove(self):
		emptyCaseCoor = self.getCoor(self.board, 0);
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

	def move(self, board, direction):
		p =  self.getCoor(board, 0);
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

	def test_move(self, direction, test):
		board = deepcopy(self.board)
		self.move(board, direction)
		return -2 if self.hash(board) in self.closed_list else self.score(board);

	def resolv(self):
		while not self.isSolved():
			scores = []
			moves = self.getLegalMove();
			for move in moves:
				scores.append(self.test_move(move, True))
			if any([True if score >= 0 else False for score in scores]):
				self.timeComplexity += 1
				self.spaceComplexity += 1
				move = moves[scores.index(min([score for score in scores if score >= 0]))]
				self.solution.append(move)
				self.move(self.board, move);
				self.closed_list.append(self.hash(self.board))
			elif len(self.solution) >= 1:
				self.timeComplexity += 1
				self.move(self.board, self.backMove(self.solution[-1]));
				self.solution.pop()
		return self.show()
			
	def show(self):
		print('Time complexity :', self.timeComplexity)
		print('Space complexity : ', self.spaceComplexity)
		print('Move count  : ', len(self.solution))
		print('Moves : ', self.solution)
		return (self.solution)