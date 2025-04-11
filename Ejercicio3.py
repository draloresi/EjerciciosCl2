try:
    datos = {"nombre": "Ana", "edad": 30}
    print(datos["apellido"])
except KeyError:
    print("¡Error! La clave no existe en el diccionario.")
