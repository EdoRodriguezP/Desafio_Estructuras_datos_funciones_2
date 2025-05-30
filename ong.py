def factorial(numero):                               # Funcion para calcular factorial
    if numero < 0:                                   # Si numero menor a 0 imprime
        return "El factorial no está definido para números negativos"
    if numero == 0 or numero == 1:                   # Si numero es igual a 0 o 1 imprime 1
        return 1
    
    resultado = 1                                  # Variable para almacenar resultado
    for i in range(1, numero + 1):                 # bucle para multiplicar numeros
        resultado *= i
    return resultado                       # Devuelve el factorial calculado

def productoria(lista):                   # Funcion que calcula la productoria
    if not lista:                         # Validacion para lista vacia
        return 0
    
    resultado = 1                        # Variable para almacenar resultado
    for numero in lista:                 # bucle para multiplicar numeros
        resultado *= numero
    return resultado                     # Devuelve la productoria calculada

def calcular(**datos):                  # Funcion principal que procesa los datos
    resultados = {}                     # Diccionario para almacenar los diccionarios.
    
    for clave, valor in datos.items():                 # Recorre los argumentos recibidos
        if clave.startswith('fact'):                   # Calcula factorial si clave empieza con fact
            resultados[clave] = factorial(valor)
        elif clave.startswith('prod'):                 # calcula productoria si clave empieza con prod
            resultados[clave] = productoria(valor)
    
    print("\nResultados:")                              # Recorre y muestra los resultados
    for clave, valor in resultados.items():
        if clave.startswith('fact'):                  # Muestra factorial si clave empieza con fact
            print(f"El factorial de {datos[clave]}: {valor}")
        else:                                         # de lo contrario muestra productoria 
            print(f"La productoria de {datos[clave]}: {valor}")
    print()
    
    return resultados

if __name__ == "__main__":

    calcular(fact_1 = -5, prod_1 = [4,6,7,4,3], fact_2 = 6)