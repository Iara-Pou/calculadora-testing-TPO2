def calcular(a, b, operacion):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Los operandos deben ser números enteros")

    if operacion == "suma":
        return a + b

    elif operacion == "resta":
        return a - b

    elif operacion == "multiplicacion":
        return a * b

    elif operacion == "division":
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    else:
        raise ValueError("Operación no válida")