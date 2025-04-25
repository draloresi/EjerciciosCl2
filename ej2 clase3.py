def buscar_palabra(palabra, *args):
    
    mensaje = f"La palabra '{palabra}' está en la lista." if palabra in args else f"La palabra '{palabra}' NO está en la lista."
    print(mensaje)


entrada = input("Ingresá una lista de palabras separadas por coma: ")
lista_palabras = entrada.split(",")

lista_palabras = [palabra.strip() for palabra in lista_palabras]

palabra_buscar = input("Ingresá la palabra que querés buscar: ")


buscar_palabra(palabra_buscar, *lista_palabras) 

