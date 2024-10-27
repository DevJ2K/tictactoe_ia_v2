import time

class TicTacToe:
	def __init__(self) -> None:
		self.board = [
			[" ", " ", " "],
			[" ", " ", " "],
			[" ", " ", " "]
		]
		pass

	def display_board(self) -> None:
		board = self.board
		print(" ___________ ")
		print("|           |")
		print("| {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))
		print("|-----------|")
		print("| {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))
		print("|-----------|")
		print("| {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))
		print("|___________|")


if __name__ == "__main__":
	tictactoe = TicTacToe()
	tictactoe.display_board()
