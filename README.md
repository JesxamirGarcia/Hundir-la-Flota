# Hundir-la-Flota
Hundir la Flota entregable #1

Autor: Jesxamir Garcia Berrios


PRIMER PASO: Definicion de funciones 

Se realizo una funcion para crear 3 tableros: 
    a. El tablero del Jugador 1.
    b. Tablero Jugador 2.
    c. tablero vacio jugador 1.
Se relizo "def colocar_barcos" para ubicar los barcos en el tablero 1 y tablero 2. 
Se relizo una funcion "def accion_disparo1" y "accion_disparo2" para ejecutar el comentado de atacar para cada jugador.
En las funciones antes descritas se ocuparon bulques "for" y las condiciones if, elif y else.

SEGUNDO PASO: Tableros

Se crearon los tableros 1, tablero 2 y tablero_vacio. 
Se ubicaron los barcos con coordenadas fijas: 
  
    a. fijos_1 = [
        [(4, 3)], [(7,0)], [(6, 2)], [(7, 5)],
        [(1, 8), (1, 7)], [(1, 2), (1, 1)], [(5, 1), (5, 2)],
        [(6, 0), (5, 0), (4, 0)],  [(4, 6), (5, 6), (6, 6)],
        [(0, 5), (0, 6), (0, 7), (0, 8)]
        ]
   
    
    b. fijos_2 = [
        [(9, 8)], [(8, 3)], [(8, 1)], [(5, 1)],
        [(4, 6), (4, 7)], [(4, 5), (3, 5)], [(1, 7), (1, 6)],
        [(5, 8), (4, 8), (3, 8)], [(4, 4), (5, 4), (6, 4)],
        [(4, 0), (5, 0), (6, 0), (7, 0)]
        ].

TERCER PASO: desarollo del juego

Se inserto con un print letras especiales de ASCII. 
Se ingreso un input para dar incio al juego mediante un "enter"
En el desarollo del juego programe un bucle "while True" para colocar los barcos e impirmir los barcos para la visualizacion del jugador 1. 
Cree un bucle "while True" con las condiciones if, elif, else donde se llamaron las funciones de "Def accion_disparo1" y "accion_disparo2" para ejecutar el juego. 

