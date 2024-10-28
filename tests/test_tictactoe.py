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
