# import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TicTacToe import TicTacToe

def test_player_turn():
	assert TicTacToe(who_start='X').get_player_turn([["X", "O", " "], [" ", " ", " "], [" ", " ", " "]]) == 'X'
	assert TicTacToe(who_start='O').get_player_turn([["X", "O", " "], [" ", " ", " "], [" ", " ", " "]]) == 'O'
	assert TicTacToe(who_start='X').get_player_turn([["X", "O", "X"], [" ", " ", " "], [" ", " ", " "]]) == 'O'
	assert TicTacToe(who_start='O').get_player_turn([["X", "O", "O"], [" ", " ", " "], [" ", " ", " "]]) == 'X'

def test_terminal_state_true():
	# Horizontal
	assert TicTacToe().terminal_state([["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]) == True
	assert TicTacToe().terminal_state([[" ", " ", " "], ["X", "X", "X"], [" ", " ", " "]]) == True
	assert TicTacToe().terminal_state([[" ", " ", " "], [" ", " ", " "], ["X", "X", "X"]]) == True

	# Vertical
	assert TicTacToe().terminal_state([["X", " ", " "], ["X", " ", " "], ["X", " ", " "]]) == True
	assert TicTacToe().terminal_state([[" ", "X", " "], [" ", "X", " "], [" ", "X", " "]]) == True
	assert TicTacToe().terminal_state([[" ", " ", "X"], [" ", " ", "X"], [" ", " ", "X"]]) == True

	# Diagonal
	assert TicTacToe().terminal_state([["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]) == True
	assert TicTacToe().terminal_state([[" ", " ", "X"], [" ", "X", " "], ["X", " ", " "]]) == True

	# Tie
	assert TicTacToe().terminal_state([["O", "O", "X"], ["X", "X", "O"], ["O", "O", "X"]]) == True
	assert TicTacToe().terminal_state([
		["O", "X", "X"],
		["X", "X", "O"],
		["O", "O", "X"]
		]) == True

def test_terminal_state_false():
	assert TicTacToe().terminal_state([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]) == False
	assert TicTacToe().terminal_state([[" ", " ", " "], [" ", "X", "X"], [" ", " ", " "]]) == False
	assert TicTacToe().terminal_state([["X", " ", " "], [" ", "X", "X"], [" ", " ", " "]]) == False

def test_state_board():
	assert TicTacToe().state_board([["O", "O", "X"], ["X", "X", "O"], ["O", "O", "X"]]) == 0
	assert TicTacToe(who_start='O').state_board([
		["O", "X", "X"],
		["O", "O", "O"],
		["O", "X", "X"]
		]) == 1
	assert TicTacToe(who_start='X').state_board([
		["X", "X", "X"],
		["O", "O", "O"],
		["O", "X", "X"]
		]) == 1
	assert TicTacToe(who_start='X').state_board([
		["O", "X", "X"],
		["X", "X", "O"],
		["O", "O", "X"]
		]) == 0

def test_simulate_action():
	assert TicTacToe(who_start='O').simulate_action([
		["O", " ", "X"],
		["X", "X", "O"],
		["O", "O", "X"]
		], action=(0, 1)) == [["O", "O", "X"],["X", "X", "O"],["O", "O", "X"]]
	assert TicTacToe(who_start='O').simulate_action([
		["O", " ", "X"],
		["X", " ", "O"],
		["O", "O", "X"]
		], action=(1, 1)) == [["O", " ", "X"],["X", "X", "O"],["O", "O", "X"]]

def test_get_actions():
	assert TicTacToe().get_actions([
		["O", " ", "X"],
		["X", " ", "O"],
		["O", "O", "X"]
		]) == [(0, 1), (1, 1)]
	assert TicTacToe().get_actions([
		[" ", " ", "X"],
		["X", " ", "O"],
		["O", "O", "X"]
		]) == [(0, 0), (0, 1), (1, 1)]
	assert TicTacToe().get_actions([
		["O", "X", "X"],
		["X", "O", "O"],
		["O", "O", "X"]
		]) == []
