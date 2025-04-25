

# Solicitamos dos números al usuario
a = int(input("Ingresá el primer número: "))
b = int(input("Ingresá el segundo número: "))

# Operador ternario para encontrar el mayor
mayor = a if a > b else b

print(f"El número mayor es: {mayor}")
