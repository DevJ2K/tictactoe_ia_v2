import time
import threading
import random
import copy
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
		state_msg = None
		while self.terminal_state(self.board) == False:
			state_msg = f"TICTACTOE TURN : {self.get_player_turn(self.board)}" if state_msg is None else state_msg
			self.display_board(state=state_msg)
			if self.get_player_turn(self.board) == 'X':
				player_choice = None
				while (player_choice == None):
					player_choice = convert_input_to_board(input("Choice a number between 1 and 9 : "))
					try:
						self.board = self.simulate_action(self.board, player_choice)
					except Exception as e:
						self.display_board(state=f"TICTACTOE TURN : {self.get_player_turn(self.board)}")
						if player_choice == None:
							print("Please insert a valid value.")
						else:
							player_choice = None
							print("Slot already use.")
						print(e)
						print(e.__cause__)

				pass
			else:
				if self.IA == True:
					start_classic = time.perf_counter_ns()
					value, action = self.minimax_algorithm(self.board)
					duration_classic = time.perf_counter_ns() - start_classic
					state_msg = f"IA take {duration_classic // 1000000}ms. Value : {value} , TURN TO : {self.get_player_turn(self.board)}"
					# print(f"Algorithm without Multithreading : {duration_classic // 1000000}ms.")
					# print(f"Minimax answer : [{value}, {action}]")

					self.board = self.simulate_action(self.board, action)
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
		if  self.terminal_state(board) == False:
			raise MinimaxError("The game is not terminate yet to get the state")
			# return 0
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
			new_board = [["", "", ""],["", "", ""],["", "", ""]]
			for i in range(len(board)):
				for j in range(len(board[i])):
					new_board[i][j] = board[i][j]
			new_board[action[0]][action[1]] = self.get_player_turn(new_board)
			# print(new_board)
			return new_board
		else:
			# print(BHRED)
			# print(board)
			# print(action)
			# print(RESET)
			raise TicTacToeError(f"Slot [{action[0]}][{action[1]}] already use")

	def get_actions(self, board: list[list[str]]) -> list[tuple[int, int]]:
		# return [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == ' ']
		actions = []
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == ' ':
					actions.append((i, j))
		return actions

	def multi_threading_minimax(self, board: list[list[str]]):
		DEPTH = 0
		thread_list: list[threading.Thread] = []
		for action in self.get_actions(board):
			thread_item = threading.Thread(target=self.minimax_algorithm, args=(self.simulate_action(board, action), DEPTH + 1))
			thread_list.append(thread_item)
		for thread in thread_list:
			thread.start()
			thread.join()



	def minimax_algorithm(
		self,
		board: list[list[str]],
		alpha: float = float("-inf"),
		beta: float = float("+inf"),
		DEPTH: int = 0
	):
		# print(DEPTH)
		# print(board)
		if self.terminal_state(board):
			return self.state_board(board), None

		if self.get_player_turn(board) == self.maximizing_player:
			# print("HERE MAX")
			# exit(1)
			value = float('-inf')
			best_action = None

			for action in self.get_actions(board):
				state, return_action = self.minimax_algorithm(self.simulate_action(board, action), alpha, beta, DEPTH + 1)
				# if (state != 1):
				# 	print(f"MAXIMIZE PLAYER : {state}")
				if state > value:
					value = state
					best_action = action

				alpha = max(alpha, state)
				if beta <= alpha or state == 1:
					break
			return value, best_action

		elif self.get_player_turn(board) == self.minimizing_player:
			# print("HERE MINI")
			# exit(1)
			value = float('+inf')
			best_action = None

			for action in self.get_actions(board):
				# state, return_action = self.minimax_algorithm(self.simulate_action(board, action), DEPTH + 1)
				state, return_action = self.minimax_algorithm(self.simulate_action(board, action), alpha, beta, DEPTH + 1)
				# if (state != 1):
				# 	print(f"MINIMIZE PLAYER : {state}")
				if state < value:
					value = state
					best_action = action
				beta = min(beta, state)
				if beta <= alpha or state == -1:
					break
			return value, best_action

		else:
			raise TicTacToeError("Player turn error.")

if __name__ == "__main__":
	# print(max(float('+inf'), 12))
	# PLAYER IS 'X'
	# OPPONENT IS 'O'
	tictactoe = TicTacToe(who_start='O', IA=True, board=[
		[" ", " ", " "],
		[" ", " ", " "],
		[" ", " ", " "]
	])
	tictactoe.play()
	# tictactoe.display_board()
