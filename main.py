from app.calculadora import calcular

def main():
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ")

        resultado = calcular(a, b, operacion)
        print(f"Resultado: {resultado}")

    except ValueError as ve:
        print(f"Error: {ve}")

    except TypeError as te:
        print(f"Error: {te}")


if __name__ == "__main__":
    main()