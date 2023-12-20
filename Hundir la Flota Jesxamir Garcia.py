import numpy as np
from random import randint

def tablero1(filas, columnas, espacio=" "):
    return np.full((filas, columnas), espacio, dtype=str)

def tablero2(filas, columnas, espacio=" "):
    return np.full((filas, columnas), espacio, dtype=str)


def tablero_vacio(filas, columnas, espacio=" "):
    return np.full((filas, columnas), espacio, dtype=str)

def colocar_barcos(tablero, barcos, caracter='O'):
    for barco in barcos:
        for posicion in barco:
            fila, columna = posicion
            tablero[fila][columna] = caracter

def accion_disparo1():
    fila = int(input("Jugador 1: Ingrese la fila para el disparo (0-9): "))
    columna = int(input("Jugador 1: Ingrese la columna para el disparo (0-9): "))
    
    print("Turno Jugardo 1:""\n")
    
    if 0 < fila >=10 and  0 < columna >=10:
        print("Ingresa numeros (0 al 9)")
        return accion_disparo1()
    
    elif tablero2 [fila, columna] == "O":
        print("Jugador 1:", "¡Le diste, muy bien!")
        tablero2[fila, columna] = "#"
        tablero_vacio[fila,columna] = "#"
        print(tablero_vacio)
        print("Tu turno otra vez")       
        return accion_disparo1()
    
    elif tablero2 [fila, columna] == "#":
        print("¡Ingresa otras coordenadas del (0-9)")
        return accion_disparo1()
     
    else:
        print("Jugador 1:", "¡Fallaste, Agua!")
        tablero_vacio[fila, columna] = "A"
        tablero2[fila,columna] = "A"
        print("Turno Jugador 2")  
        print(tablero_vacio) 
        return False
            
def accion_disparo2():
    fila = randint(0,9)
    columna = randint(0,9)
    if tablero1 [fila, columna] == "O":
        print("Jugador 2:", "¡Te dispare, voy otra vez!")
        tablero1[fila, columna] = "#"
        print(tablero1)
        return accion_disparo2()
    
    elif tablero1 [fila, columna] == "#":
        print("¡Ingresa otras coordenadas del (0-9)")
        return accion_disparo2()
     
    else:
        print("Jugador 2:", "¡Fallaste, Agua!")
        tablero1[fila,columna] = "A"
        print("Turno Jugador 1") 
        print(tablero1)
        return False


tablero1 = tablero1(10, 10)
tablero2 = tablero2(10,10)
tablero_vacio = tablero_vacio(10,10)

fijos_1 = [
    [(4, 3)], [(7,0)], [(6, 2)], [(7, 5)],
    [(1, 8), (1, 7)], [(1, 2), (1, 1)], [(5, 1), (5, 2)],
    [(6, 0), (5, 0), (4, 0)],  [(4, 6), (5, 6), (6, 6)],
    [(0, 5), (0, 6), (0, 7), (0, 8)]
    ]
fijos_2 = [
    [(9, 8)], [(8, 3)], [(8, 1)], [(5, 1)],
    [(4, 6), (4, 7)], [(4, 5), (3, 5)], [(1, 7), (1, 6)],
    [(5, 8), (4, 8), (3, 8)], [(4, 4), (5, 4), (6, 4)],
    [(4, 0), (5, 0), (6, 0), (7, 0)]
    ]




arte_ascii = """     
    ██   ██ ██    ██ ███    ██ ██████  ██ ██████      ██       █████      ███████ ██       ██████  ████████  █████  
    ██   ██ ██    ██ ████   ██ ██   ██ ██ ██   ██     ██      ██   ██     ██      ██      ██    ██    ██    ██   ██ 
    ███████ ██    ██ ██ ██  ██ ██   ██ ██ ██████      ██      ███████     █████   ██      ██    ██    ██    ███████ 
    ██   ██ ██    ██ ██  ██ ██ ██   ██ ██ ██   ██     ██      ██   ██     ██      ██      ██    ██    ██    ██   ██ 
    ██   ██  ██████  ██   ████ ██████  ██ ██   ██     ███████ ██   ██     ██      ███████  ██████     ██    ██   ██ 
                                                                                                                
    """
print(arte_ascii)
    
inicio = input("Bienvenidos! Presiona Enter para comenzar")

while True:
           
    colocar_barcos(tablero1, fijos_1)
    colocar_barcos(tablero2, fijos_2)

    print("Tablero vacio Jugador 1:","\n", tablero_vacio, "\n")

    print(tablero1, "\n")
    
    break

while True:
    
    if "O" in tablero1 and "O" in tablero2:
        accion_disparo1()
        accion_disparo2()
    
    elif "O" not in tablero1:
        print("Gano el Jugador 2, Felicidades!")
        break

    elif "O" not in tablero2:
        print("Gano el Jugador 1, Felicidades!")
        break
    
    else:
        break
    
      
arte_ascii2 = """     

███████╗██╗███╗   ██╗    ██████╗ ███████╗██╗              ██╗██╗   ██╗███████╗ ██████╗  ██████╗ ██╗
██╔════╝██║████╗  ██║    ██╔══██╗██╔════╝██║              ██║██║   ██║██╔════╝██╔════╝ ██╔═══██╗██║
█████╗  ██║██╔██╗ ██║    ██║  ██║█████╗  ██║              ██║██║   ██║█████╗  ██║  ███╗██║   ██║██║
██╔══╝  ██║██║╚██╗██║    ██║  ██║██╔══╝  ██║         ██   ██║██║   ██║██╔══╝  ██║   ██║██║   ██║╚═╝
██║     ██║██║ ╚████║    ██████╔╝███████╗███████╗    ╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚██████╔╝██╗
╚═╝     ╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚══════╝╚══════╝     ╚════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝
                                                                                                   
                                                                                                                                                                                            
    """
print(arte_ascii2)

input("Presiona Enter para salir...")