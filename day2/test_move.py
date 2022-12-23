import pytest
from day2.move import Move


def test_my_shape():
    m = Move("B Y")
    assert m.my_shape() == "Y"

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
    assert m.outcome() == Move.Outcome.WIN

    m = Move("C Y")
    assert m.outcome() == Move.Outcome.LOSE

def test_outcome_score():
    m = Move("C Y")
    assert m.outcome() == Move.Outcome.LOSE
    assert m.outcome_score() == 0

def test_total_score():
    m = Move("C Y")
    assert m.shape_score() == 2
    assert m.outcome_score() == 0
    assert m.total_score() == 2
