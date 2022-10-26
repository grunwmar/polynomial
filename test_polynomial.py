import pytest
from polynomial import Polynomial
import random


def test_eval():
    """Test of evaluation of polynomial's value."""
    p = Polynomial(1, 2, 3, 4)
        # 0 -> 1 + 0 + 0 + 0
        # 1 -> 1 + 2 + 3 + 4 = 10
        # 2 -> 1 + 2*2 + 3*4 + 4*8 = 1 + 4 + 12 + 32 = 33 + 16 = 49
        # 10 -> 1 + 2*10 + 3*100 + 4*1000 = 4321
    assert p.evaluate(0) == 1
    assert p.evaluate(1) == 10
    assert p.evaluate(2) == 49
    assert p.evaluate(10) == 4321


def test_number_mult():
    """Test of multiplication of polynomial by number (number as first arg)."""

    p = Polynomial(1, 2, 3, 4)

    assert  (10 * p).tuple == (10, 20, 30, 40)
    assert  ((-5) * p).tuple == (-5, -10, -15, -20)


def test_number_div():
    """Test of division of polynomial by number (number as first arg)."""

    p = Polynomial(12, 6, 24, 18)

    assert  (p/2).tuple == (6, 3, 12, 9)
    assert  (p/3).tuple == (4, 2, 8, 6)


def test_poly_mult():
    """Test of multiplication of two polynomials."""

    p = Polynomial(1, 2, 3)
    q = Polynomial(-1, 0, 2)

    assert (p * q).tuple == (-1, -2, -1, 4, 6)


def test_add():
    """Test of addition of two polynomials."""

    p = Polynomial(1, 2, 3)
    q = Polynomial(-1, 0, 2)

    assert (p + q).tuple == (0, 2, 5)


def test_sub():
    """Test of subtraction of two polynomials."""

    p = Polynomial(1, 2, 3)
    q = Polynomial(-1, 0, 2)

    assert (p - q).tuple == (2, 2, 1)



...
