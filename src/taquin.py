from utils import *

class Taquin(object):
	def __init__(self, board):
		self.board = board
		self.size = len(board)
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
				ret.append(function(data))
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
		if self.board[data['x']][data['y']] == data['i'] + 1 or data['i'] == self.size*self.size-1 and self.board[data['x']][data['y']] == 0:
			return True
		return False

	def isSolved(self):
		return all(self.map(self.isSolved_map))

	#check if the taquin is currently solvable or not

	def isSolvable__map(self, data):
		return 1 if self.toCmp > self.board[data['x']][data['y']] and self.board[data['x']][data['y']] != 0 else 0

	def isSolvable_map(self, data):
		self.toCmp = self.board[data['x']][data['y']]
		return sum(self.map(self.isSolvable__map, data['i']))

	def isSolvable(self):
		return True if not sum(self.map(self.isSolvable_map)) % 2 else False



	def resolv(self):
		if self.isSolvable():
			if self.isSolved():
				print('Already solved')
				return []
			else:
				return ['right', 'right','up','up','left','down']
		else:
			error('unsolvable')