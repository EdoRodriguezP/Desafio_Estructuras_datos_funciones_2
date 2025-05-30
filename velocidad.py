
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,    # Velocidades entregadas
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]


def calculo_media (velocidad):                  # Funcion calculo media
    media = sum(velocidad)/len(velocidad)       # Se calcula suma total dividida por cantidad de datos
    sobre_media = []                            # Lista vacia para guardar datos
    for posicion, valor in enumerate(velocidad):  # Recorre la lista opteniendo posicion y valor
        if valor > media:                        # si valor sobre la media guarda posicion
            sobre_media.append(posicion)
    print(f"\nLas posiciones que superan la media son: {sobre_media}\n") # Muestra las posiciones donde los valores superan la media
    return media       

calculo_media(velocidad)