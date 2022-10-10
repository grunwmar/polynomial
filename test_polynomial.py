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
    #  3 * (1 -> 1 + 2 + 3 + 4) = 30
    # 10 * (2 -> 1 + 2*2 + 3*4 + 4*8) = 10*(1 + 4 + 12 + 32) = 330 + 160 = 490
    assert  3 * p.evaluate(1) == (3*p).evaluate(1)
    assert 10 * p.evaluate(2) == (10*p).evaluate(2)


def test_number_div():
    """Test of division of polynomial by number (number as first arg)."""
    p = Polynomial(12, 6, 24, 18)

    assert  (p/2).evaluate(2) == p.evaluate(2)/2
    assert  (p/2).evaluate(3) == p.evaluate(3)/2
    assert  (p/3).evaluate(2) == p.evaluate(2)/3
    assert  (p/3).evaluate(3) == p.evaluate(3)/3


def test_poly_mult():
    """Test of multiplication of two polynomials."""
    p_coefs = [[random.randint(-9, 9) for j in range(0, i+1)] for i in range(5)]
    q_coefs = [[random.randint(-9, 9) for j in range(0, i+1)] for i in range(5)]
    polynomials_p = [Polynomial(*p) for p in p_coefs]
    polynomials_q = [Polynomial(*q) for q in q_coefs]
    for p in polynomials_p:
        for q in polynomials_q:
            r = p * q
            for x in [random.randint(-9, 9) in range(5)]:
                p_val = p.evaluate(x)
                q_val = q.evaluate(x)
                r_val = (p * q).evaluate(x)
                assert p_val * q_val == r_val


def test_add():
    """Test of addition of two polynomials."""
    p_coefs = [[random.randint(-9, 9) for j in range(0, i+1)] for i in range(5)]
    q_coefs = [[random.randint(-9, 9) for j in range(0, i+1)] for i in range(5)]
    polynomials_p = [Polynomial(*p) for p in p_coefs]
    polynomials_q = [Polynomial(*q) for q in q_coefs]
    for p in polynomials_p:
        for q in polynomials_q:
            r = p * q
            for x in [random.randint(-9, 9) in range(5)]:
                p_val = p.evaluate(x)
                q_val = q.evaluate(x)
                r_val = (p + q).evaluate(x)
                assert p_val + q_val == r_val


def test_sub():
    """Test of subtraction of two polynomials."""
    p_coefs = [[random.randint(-9, 9) for j in range(0, i+1)] for i in range(5)]
    q_coefs = [[random.randint(-9, 9) for j in range(0, i+1)] for i in range(5)]
    polynomials_p = [Polynomial(*p) for p in p_coefs]
    polynomials_q = [Polynomial(*q) for q in q_coefs]
    for p in polynomials_p:
        for q in polynomials_q:
            r = p * q
            for x in [random.randint(-9, 9) in range(5)]:
                p_val = p.evaluate(x)
                q_val = q.evaluate(x)
                r_val = (p - q).evaluate(x)
                assert p_val - q_val == r_val


...
