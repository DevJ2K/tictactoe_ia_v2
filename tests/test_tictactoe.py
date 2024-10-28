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

def test_terminal_state_false():
	assert TicTacToe().terminal_state([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]) == False
	assert TicTacToe().terminal_state([[" ", " ", " "], [" ", "X", "X"], [" ", " ", " "]]) == False
	assert TicTacToe().terminal_state([["X", " ", " "], [" ", "X", "X"], [" ", " ", " "]]) == False
