import pytest

from helloworld import helloworld

def test_print_me():
	if helloworld.return_me('hi') != 'hi':
		raise AssertionError()

def test_plus_me():
	if helloworld.plus_me(99) != 100:
		raise AssertionError()

def test_minus_me():
	if helloworld.minus_me(1) != 0:
		raise AssertionError()
