import pytest
from app.calculadora import calcular

## Casos exitosos
def test_suma_correcta():
    assert calcular(5, 6, "suma") == 11

def test_resta_correcta():
    assert calcular(5, 6, "resta") == -1

def test_multiplicacion_correcta():
    assert calcular(5, 6, "multiplicacion") == 30

def test_division_correcta():
    assert calcular(5, 5, "division") == 1


## Casos error
def test_division_por_cero():
    with pytest.raises(ValueError):
        calcular(10, 0, "division")

def test_operacion_invalida():
    with pytest.raises(ValueError):
        calcular(2, 2, "raíz cuadrada")


## Casos border
def test_input_decimal_invalido():
    with pytest.raises(TypeError):
        calcular(2.3, 3, "suma")

def test_division_decimal():
    assert calcular(5, 2, "division") == 2.5
