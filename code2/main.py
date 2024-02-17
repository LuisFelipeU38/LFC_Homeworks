import random

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
print("Cadena aleatoria generada:", random_string)
