try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado. Creando el archivo...")
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Archivo creado automáticamente.")
