import time
import random
import os
from Colors import *

class PlayerError(Exception):
	pass

class TicTacToeError(Exception):
	pass

class MinimaxError(Exception):
	pass

def convert_input_to_board(number: str) -> tuple[int, int]:
	if number == None:
		return None
	try:
		value = int(number)
	except:
		return None
	if value < 1 or value > 9:
		return None
	match value:
		case 1:
			return (0, 0)
		case 2:
			return (0, 1)
		case 3:
			return (0, 2)
		case 4:
			return (1, 0)
		case 5:
			return (1, 1)
		case 6:
			return (1, 2)
		case 7:
			return (2, 0)
		case 8:
			return (2, 1)
		case 9:
			return (2, 2)
	return None

class TicTacToe:
	def __init__(self, who_start: str = 'X', IA: bool = True, board: list[list[str]] = [
			[" ", " ", " "],
			[" ", " ", " "],
			[" ", " ", " "]
		]) -> None:
		if who_start not in ['X', 'O']:
			raise PlayerError("The player who start is invalid.")
		# WHO_START
		self.maximizing_player = who_start
		self.minimizing_player = 'O' if who_start == 'X' else 'X'
		self.IA = IA
		# self.player_turn = who_start
		self.who_start = who_start
		self.board = board

	def play(self):
		while self.terminal_state(self.board) == False:
			self.display_board(state=f"TICTACTOE TURN : {self.get_player_turn(self.board)}")
			if self.get_player_turn(self.board) == 'X':
				player_choice = None
				while (player_choice == None):
					player_choice = convert_input_to_board(input("Choice a number between 1 and 9 : "))
					try:
						self.board = self.simulate_action(self.board, player_choice)
					except:
						self.display_board(state=f"TICTACTOE TURN : {self.get_player_turn(self.board)}")
						if player_choice == None:
							print("Please insert a valid value.")
						else:
							player_choice = None
							print("Slot already use.")

				pass
			else:
				if self.IA == True:
					actions = self.get_actions(self.board)
					self.board = self.simulate_action(self.board, random.choice(actions))
				else:
					player_choice = None
					while (player_choice == None):
						player_choice = convert_input_to_board(input("Choice a number between 1 and 9 : "))
						try:
							self.board = self.simulate_action(self.board, player_choice)
						except:
							self.display_board(state="TICTACTOE")
							if player_choice == None:
								print("Please insert a valid value.")
							else:
								player_choice = None
								print("Slot already use.")




		game_issue = self.state_board(self.board)
		if game_issue == 0:
			message = "Tie"
		elif game_issue == 1:
			message = f"'{self.maximizing_player}' has won."
		elif game_issue == -1:
			message = f"'{self.minimizing_player}' has won."
		else:
			# message = "Game issue error ???"
			raise TicTacToeError("Game issue error")
		self.display_board(state="Game is over", end_message=message)


	def display_board(self, state: str, end_message: str = None) -> None:
		board = self.board
		os.system('clear')
		print(f"State : {state}")
		print(" ___________ ")
		print("|           |")
		print("| {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))
		print("|-----------|")
		print("| {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))
		print("|-----------|")
		print("| {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))
		print("|___________|")
		if end_message != None:
			print(end_message)

	def game_has_a_winner(self, board: list[list[str]]) -> bool:
		return True in [
			# Horizontal
			board[0][0] == board[0][1] == board[0][2] != " ",
			board[1][0] == board[1][1] == board[1][2] != " ",
			board[2][0] == board[2][1] == board[2][2] != " ",
			# Vertical
			board[0][0] == board[1][0] == board[2][0] != " ",
			board[0][1] == board[1][1] == board[2][1] != " ",
			board[0][2] == board[1][2] == board[2][2] != " ",
			# Diagonal
			board[0][0] == board[1][1] == board[2][2] != " ",
			board[0][2] == board[1][1] == board[2][0] != " ",
		]

	def terminal_state(self, board: list[list[str]]) -> bool: # Terminal()
		if self.game_has_a_winner(board) == True:
			return True
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == ' ':
					return False
		return True

	def get_player_turn(self, board: list[list[str]]) -> str: # maximizing_player | minimizing_player
		x = 0
		o = 0
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == 'X':
					x += 1
				elif board[i][j] == 'O':
					o += 1
		if x == o:
			return self.maximizing_player
		else:
			return self.minimizing_player

	def state_board(self, board: list[list[str]]) -> int: # Value()
		"""
		Evaluation Function:
		1 : Maximizing player wins
		0 : Tie
		-1: Minimizing player wins
		"""
		if self.terminal_state(board) == False:
			raise MinimaxError("The game is not terminate yet to get the state")
		print(self.game_has_a_winner(board=board))
		if self.game_has_a_winner(board) == False:
			return 0
		if self.get_player_turn(board) == self.minimizing_player:
			return 1
		else:
			return -1

	def simulate_action(self, board: list[list[str]], action: tuple[int, int]) -> list[list[str]]:
		if action is None:
			raise TicTacToeError("Please give an action to do.")
		if len(action) != 2:
			raise TicTacToeError("Cannot perform action")
		if (action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2):
			raise TicTacToeError("Index out of range")
		if board[action[0]][action[1]] == " ":
			board[action[0]][action[1]] = self.get_player_turn(board)
			return board
		else:
			raise TicTacToeError(f"Slot [{action[0]}][{action[1]}] already use")

	def get_actions(self, board: list[list[str]]) -> list[tuple[int, int]]:
		actions = []

		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == ' ':
					actions.append((i, j))
		# return [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == ' ']
		return actions

	def minimax_algorithm(self, board: list[list[str]]):
		if self.terminal_state(board):
			return self.state_board(board)

		if self.get_player_turn(board) == self.maximizing_player:
			value = float('-inf')
			for action in self.get_actions(board):
				value = max(value, self.minimax_algorithm(self.simulate_action(board, action)))
			return value

		elif self.get_player_turn(board) == self.minimizing_player:
			value = float('+inf')
			for action in self.get_actions(board):
				value = min(value, self.minimax_algorithm(self.simulate_action(board, action)))
			return value
		else:
			raise TicTacToeError("Player turn error.")

if __name__ == "__main__":
	# print(max(float('+inf'), 12))
	# PLAYER IS 'X'
	# OPPONENT IS 'O'
	tictactoe = TicTacToe(who_start='X', IA=False, board=[
		[" ", " ", " "],
		[" ", " ", " "],
		[" ", " ", " "]
		])
	tictactoe.play()
	# tictactoe.display_board()
