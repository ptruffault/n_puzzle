import argparse
from parserTools import getBoard
from game import TaquinGame
from utils import *

def findSolution(taquin):
	return ['right', 'right','up','up','left','down']

def showSolution(solution):
	print('Step: ', len(solution))
	print('Solution: ', ' '.join(str(e) for e in solution))

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="Must be a valid file")
	parser.add_argument("-v", "--view", action="store_true", default=False, help="enable visualizer")
	args = parser.parse_args()
	if not getattr(args, 'file'):
		error('file expected')
	board = getBoard(args.file)
	if board:
		solution = findSolution(board)
		showSolution(solution)
		if args.view:
			TaquinGame(board, solution)

if __name__ == "__main__":
	main()
	
