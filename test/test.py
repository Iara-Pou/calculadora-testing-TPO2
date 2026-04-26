import pytest
from app.calculadora import calcular

def test_suma_correcta():
    assert calcular(2, 3, "suma") == 5

def test_division_decimal():
    assert calcular(5, 2, "division") == 2.5

def test_division_por_cero():
    with pytest.raises(ValueError):
        calcular(10, 0, "division")

def test_input_decimal_invalido():
    with pytest.raises(TypeError):
        calcular(2.3, 3, "suma")

def test_operacion_invalida():
    with pytest.raises(ValueError):
        calcular(2, 2, "raíz cuadrada")