import pytest
from day2.move import Move


def test_my_shape():
    m = Move("B Y") # Paper, draw => paper
    assert m.my_shape() == "B"

def test_desired_outcome():
    m = Move("B Y")
    assert m.desired_outcome() == Move.Outcome.DRAW

    m = Move("C X")
    assert m.desired_outcome() == Move.Outcome.LOSE

def test_opponent_shape():
    m = Move("B Y")
    assert m.opponent_shape() == "B"

def test_shape_score():
    m = Move("B Y")
    assert m.shape_score() == 2

def test_outcome():
    m = Move("B Y")
    assert m.outcome() == Move.Outcome.DRAW

    m = Move("A Y")
    assert m.outcome() == Move.Outcome.DRAW

    m = Move("C Y")
    assert m.outcome() == Move.Outcome.DRAW

def test_outcome_score():
    m = Move("C Y")
    assert m.outcome() == Move.Outcome.DRAW
    assert m.outcome_score() == 3

def test_total_score():
    m = Move("C Y") # scissors, draw => scissors (3)
    assert m.shape_score() == 3
    assert m.outcome_score() == 3
    assert m.total_score() == 6
