def operacion(*args):
    
    if len(args) < 2:
        print("Error: se necesitan al menos 2 argumentos.")
    else:
        print(f"Se pasaron {len(args)} argumentos: {args}")

operacion(5)  # Va a dar error
operacion(5, 10)  # No da error
