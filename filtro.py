import sys                                # Modulo SYS para manejar argumentos por linea de comandos

productos = {'Notebook': 700000,          # Diccionario entregado
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}


def validar_argumentos():                                  # Funcion para validar argumentos
    if len(sys.argv) == 1:                                 # Si no hay argumentos se muestra error
        print("\nError: Debe ingresar al menos un argumento")
        print("Uso: python filtro.py [umbral en clp] [menor (opcional)]\n")
        sys.exit(1)                                       # Cierra el programa
    elif len(sys.argv) == 2:                              # si hay un argumento se filtra productos mayores
        umbral = int(sys.argv[1])                          # Se asigna valor de sys 1 a variable umbral
        filtro_mayor(productos, umbral)
    elif len(sys.argv) == 3 and sys.argv[2] == "menor":   # Si hay 2 argumentos y el segundo es [menor] se filtran productos menores
        umbral = int(sys.argv[1])                         # Se asigna valor de sys 1 a variable umbral
        filtro_menor(productos, umbral)
    else:                                                 # Si argumentos no son validos imprime error 
        print("\nLo sentimos, no es una operación válida")
        print("Uso: python filtro.py [umbral en clp] [menor (opcional)]\n")
        sys.exit(1)
        

def filtro_mayor(productos:dict[str,int],umbral:int):  # Funcion filtro mayor al umbral
        lista = []                                      # Lista para almacenar productos filtrados
        for prod, precio in productos.items():            # Recorremos el diccionario
            if precio > umbral:                           # Si el precio es mayor a umbral
                lista.append(prod)                         # Se agrega el producto a lista
        print(f"\nLos productos mayores al umbral son:",", ".join(lista))    # Mostramos los resultados unidos por comas
        print()
    
def filtro_menor(productos:dict[str,int],umbral:int):     # Funcion filtro menor al umbral
        lista = []                                        # Lista para almacenar productos filtrados
        for prod, precio in productos.items():
            if precio < umbral:
                lista.append(prod)
        print(f"\nLos productos menores al umbral son:",", ".join(lista))
        print()
        

if __name__ == "__main__":
    validar_argumentos()    
