'''import random

def generate_random_string(n, multiple_of_3_1s):
    # Calculamos cuántos unos necesitamos para que sea múltiplo de 3
    ones_needed = (n + 2) // 3 * 3 if multiple_of_3_1s else 0
    
    # Generamos una lista con unos y ceros
    random_list = ['1' if i < ones_needed else '0' for i in range(n)]

    # Mezclamos la lista para que sea aleatoria
    random.shuffle(random_list)

    # Convertimos la lista en una cadena y la devolvemos
    return ''.join(random_list)

# Ejemplo de uso:
n = 10  # Longitud de la cadena
multiple_of_3_1s = True  # La cadena debe tener un número de unos múltiplo de 3

random_string = generate_random_string(n, multiple_of_3_1s)
print("Cadena aleatoria generada:", random_string)'''


import random

def generar_cadena_random():
    # Generamos un tamaño aleatorio para la cadena
    tamano = random.randint(3, 100)  # Puedes ajustar el rango según tus necesidades
    
    # Calculamos la cantidad de 1s que necesitamos para que sea un múltiplo de 3
    cantidad_unos = tamano // 3 * 3
    
    # Generamos una lista con la cantidad necesaria de 1s y el resto de 0s
    cadena = [1] * cantidad_unos + [0] * (tamano - cantidad_unos)
    
    # Barajamos la lista para obtener una cadena aleatoria
    random.shuffle(cadena)
    
    # Convertimos la lista en una cadena de texto
    cadena_str = ''.join(map(str, cadena))
    
    # Mostramos la cantidad de 1s en la cadena generada
    print("Cantidad de 1s en la cadena generada:", cantidad_unos)
    
    return cadena_str

# Ejemplo de uso
cadena = generar_cadena_random()
print("Cadena aleatoria con cantidad de 1s múltiplos de 3:", cadena)

