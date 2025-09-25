import pytest
from calculator import Calculator
from main import Calculate

def test_sum():
    assert Calculator.sum(2, 3) == 5
    assert Calculator.sum(-2, 3) == 1
    assert Calculator.sum(2, -3) == -1
    assert Calculator.sum(-2, -3) == -5

def test_sub():
    assert Calculator.sub(5, 3) == 2
    assert Calculator.sub(-2, 3) == -5
    assert Calculator.sub(2, -3) == 5
    assert Calculator.sub(-2, -3) == 1

def test_mul():
    assert Calculator.mul(2, 3) == 6
    assert Calculator.mul(-2, 3) == -6
    assert Calculator.mul(2, -3) == -6
    assert Calculator.mul(-2, -3) == 6

def test_div():
    assert Calculator.div(6, 3) == 2
    assert Calculator.div(-6, 3) == -2
    assert Calculator.div(6, -3) == -2
    assert Calculator.div(-6, -3) == 2
    assert Calculator.div(6, 0) == None

def test_exp():
    assert Calculator.exp(2, 3) == 8
    assert Calculator.exp(-2, 3) == -8
    assert Calculator.exp(2, -3) == 0.125
    assert Calculator.exp(-2, -3) == -0.125
    assert Calculator.exp(0, 0) == None

def test_decimal_operations():
    assert Calculator.sum(2.5, 3.5) == 6
    assert Calculator.sub(5.5, 2.1) == 3.4
    assert Calculator.mul(1.5, 2.5) == 3.75
    assert Calculator.div(7.5, 2.5) == 3
    assert Calculator.exp(2.5, 2) == 6.25

def test_Calculate():
    result = Calculate(5, 3, '+')
    assert result == 8, f"Esperado 8, mas obteve {result}"

    result = Calculate(10, 3, '-')
    assert result == 7, f"Esperado 7, mas obteve {result}"

    result = Calculate(4, 2, '*')
    assert result == 8, f"Esperado 8, mas obteve {result}"

    result = Calculate(6, 2, '/')
    assert result == 3, f"Esperado 3, mas obteve {result}"

    result = Calculate(2, 3, '^')
    assert result == 8, f"Esperado 8, mas obteve {result}"

    result = Calculate(5, 0, '/')
    assert result is None, f"Esperado None, mas obteve {result}"

    result = Calculate(5, 3, '%')  # Operação % não válida
    assert result is None, f"Esperado None, mas obteve {result}"

    result = Calculate('abc', 3, '+')
    assert result is None, f"Esperado None, mas obteve {result}"

    result = Calculate(5, 'xyz', '+')
    assert result is None, f"Esperado None, mas obteve {result}"