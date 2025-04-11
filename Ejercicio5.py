try:
    num1 = float(input("Ingresá el primer número: "))
    num2 = float(input("Ingresá el segundo número: "))
    resultado = num1 / num2
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero.")
except ValueError:
    print("¡Error! Ingresaste un valor no válido.")
