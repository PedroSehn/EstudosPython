from codigo import numer_odd, divide
import pytest

def test_number_odd_returns_true():
  'Deve retornar true'
  assert numer_odd(3) is True


def test_number_odd_returns_false():
  'Deve retornar false'
  assert numer_odd(2) is False

def test_divide_when_other_number_is_zero_raises_an_exception():
  with pytest.raises(ZeroDivisionError, match='division by zero'):
    divide(2, 0)