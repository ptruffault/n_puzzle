import argparse
from parserTools import getBoard
from game import TaquinGame
from taquin import Taquin
from utils import *

def findSolution(board):
	TAQUIN = Taquin(board)
	solution = TAQUIN.resolv()
	TAQUIN.showResult()
	return solution


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
		if args.view:
			TaquinGame(board, solution)

if __name__ == "__main__":
	main()
	
