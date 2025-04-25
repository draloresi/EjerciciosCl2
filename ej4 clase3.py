def promedio(*args):
    
    mensaje = f"El promedio es: {sum(args) / len(args)}" if len(args) > 0 else "No se pasaron números para calcular el promedio."
    print(mensaje)


entrada = input("Ingresá una lista de números separados por coma: ")
lista_numeros = [float(num.strip()) for num in entrada.split(",")]

promedio(*lista_numeros)
