import argparse
from parserTools import getBoard
from game import TaquinGame
from taquin import Taquin
from utils import *

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="Must be a valid file")
	parser.add_argument("-v", "--view", action="store_true", default=False, help="enable visualizer")
	args = parser.parse_args()
	if not getattr(args, 'file'):
		error('file expected')
	board = getBoard(args.file)
	if board:
		TAQUIN = Taquin(board)
		solution = TAQUIN.resolv()
		if args.view:
			TaquinGame(board, solution)