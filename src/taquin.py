
class Taquin(object):
	def __init__(self, board):
		self.board = board
		self.size = len(board)
		self.solution = []

	# Apply "function" to each tuile of the taquin in the right order
	def map(self, function):
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
	

	def isSolved(self):
		def isSolved_map(data):
			if self.board[data['x']][data['y']] == data['i'] + 1 or data['i'] == self.size*self.size-1 and self.board[data['x']][data['y']] == 0:
				return True
			return False
		return all(self.map(isSolved_map))

	

	def resolv(self):
		print(self.isSolved())

		self.solution = ['right', 'right','up','up','left','down']
		self.solution = []
		return self.solution

	def showResult(self):
		print('Step: ', len(self.solution))
		print('Solution: ', ' '.join(str(e) for e in self.solution))

		
	
