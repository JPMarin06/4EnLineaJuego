# Se importan las librerias necesarias durante el juego
import random
import pandas as pd

# Se crean las funciones necesarias durante el juego que servirán como herramientas
# no para el desarrollo del mismo, sino funciones un poco más genéricas

# Se crea la funcion verificar numero para comprobar que un valor dado sea
# efectivamente un numero
def verificar_numero(numero):

    try:
        int(numero)
        return True

    except ValueError:
        return False

# Se crea de igual forma una funcion para verificar que un valor sea un string

def verificar_string(string):

    try:
        str(string)
        return True

    except ValueError:
        return False

# Se crea una función para pasar los valores de una lista a un string

def lista_a_string(lista):

    string = ""

    for n in lista:
        string += n

    return string


# Las siguientes funciones son mas de uso especifico para el juego

# Se crea una funcion que confirma si hay espacios para valores en una lista

def hay_espacio(lista_grande, valor):

    if valor in (item for sublist in lista_grande for item in sublist):
        return True

    else:
        return False

# Se crea una lista y un dataframe con la informacion de la lista y los respectivos titulos
# con la informacion que se irá digitando para cada uno de los jugadores y sus estadisticas

jugadores_perfiles = []
df = pd.DataFrame(jugadores_perfiles, columns=['Nombre jugador', 'Puntaje', 'Partidas jugadas', 'Victorias', 'Derrotas', 'Empates'])

# Se crea una funcion para estar actualizando la informacion del dataframe

def actualizar_df():
    global df
    df = pd.DataFrame(jugadores_perfiles, columns=['Nombre jugador', 'Puntaje', 'Partidas jugadas', 'Victorias', 'Derrotas', 'Empates'])

# Se crean variables que luego servirán para romper múltiples loops durante el código

breaker1 = False
breaker2 = False
breaker3 = False
breaker4 = False

# Se crea una lista que será la responsable de devolver los valores cuando se verifique constantemente
# si hay un ganador durante las partidas

true_o_false_ganador = False
ganador = 0
breaker = 0
lista_hay_ganador = [true_o_false_ganador, ganador, breaker]

# Se define una funcion en donde se pasa por parámetro el tablero del juego

def hay_ganador(lista):

    # Se crean variables que serán utilizadas para ir verificando de forma horizontal, vertical y en las diagonales si hay 4 
    # de las mismas fichas seguidas

    global lista_hay_ganador
    ciclo_fila = 0
    ciclo_columna = 0
    ciclo1 = True

    while ciclo1 == True:

        while True: # Verificar horizontalmente si hay fichas seguidas recorriendo todo el tablero y verificando si hay 4 fichas seguidas horizonalmente

            if ciclo_fila == 6:
                ciclo_columna = 0
                ciclo_fila = 0
                break

            elif ciclo_columna == 4:
                ciclo_fila +=1
                ciclo_columna = 0 

            elif str(lista[ciclo_fila][ciclo_columna]) == str(lista[ciclo_fila][ciclo_columna+1]) and str(lista[ciclo_fila][ciclo_columna+1]) == str(lista[ciclo_fila][ciclo_columna+2]) and str(lista[ciclo_fila][ciclo_columna+2]) == str(lista[ciclo_fila][ciclo_columna+3]):
                
                if str(lista[ciclo_fila][ciclo_columna]) == "X" or str(lista[ciclo_fila][ciclo_columna]) == "O":
                    lista_hay_ganador[0] = True
                    lista_hay_ganador[1] = str(lista[ciclo_fila][ciclo_columna])
                    lista_hay_ganador[2] = 1
                    ciclo_columna = 0
                    ciclo_fila = 0
                    ciclo1 = False
                    break
                
                else:
                    ciclo_columna +=1
            
            else:
                ciclo_columna +=1
        
        
        if ciclo1 == False:
            break
        
        
        while True: # Verificar verticalmente si hay fichas seguidas recorriendo todo el tablero y verificando si hay 4 fichas seguidas 

            if ciclo_columna == 7:
                ciclo_columna = 0
                ciclo_fila = 0
                break

            elif ciclo_fila == 3:
                ciclo_columna +=1
                ciclo_fila = 0

            elif lista[ciclo_fila][ciclo_columna] == lista[ciclo_fila+1][ciclo_columna] and lista[ciclo_fila+1][ciclo_columna] == lista[ciclo_fila+2][ciclo_columna] and lista[ciclo_fila+2][ciclo_columna] == lista[ciclo_fila+3][ciclo_columna]:
                
                if lista[ciclo_fila][ciclo_columna] == "X" or lista[ciclo_fila][ciclo_columna] == "O":
                    lista_hay_ganador[0] = True
                    lista_hay_ganador[1] = str(lista[ciclo_fila][ciclo_columna])
                    lista_hay_ganador[2] = 1
                    ciclo_columna = 0
                    ciclo_fila = 0 
                    ciclo1 = False
                    break
                
                else:
                    ciclo_fila +=1
            
            else:
                ciclo_fila +=1


        if ciclo1 == False:
            break
        
        
        while True: # Verificar diagonalmente si hay fichas seguidas recorriendo todo el tablero y verificando si hay 4 fichas seguidas 

            if ciclo_columna == 4:
                ciclo_columna = 0
                ciclo_fila = 5
                break
            
            elif ciclo_fila == 3:
                ciclo_columna +=1
                ciclo_fila = 0

            elif lista[ciclo_fila][ciclo_columna] == lista[ciclo_fila+1][ciclo_columna+1] and lista[ciclo_fila+1][ciclo_columna+1] == lista[ciclo_fila+2][ciclo_columna+2] and lista[ciclo_fila+2][ciclo_columna+2] == lista[ciclo_fila+3][ciclo_columna+3]:
                
                if lista[ciclo_fila][ciclo_columna] == "X" or lista[ciclo_fila][ciclo_columna] == "O":
                    lista_hay_ganador[0] = True
                    lista_hay_ganador[1] = str(lista[ciclo_fila][ciclo_columna])
                    lista_hay_ganador[2] = 1
                    ciclo_columna = 0
                    ciclo_fila = 5
                    ciclo1 = False
                    break
                
                else:
                    ciclo_fila +=1
           
            else:
                ciclo_fila +=1


        if ciclo1 == False:
            break
        
        
        while True: # Verificar diagonalmente en el otro sentido si hay fichas seguidas recorriendo todo el tablero y verificando si hay 4 fichas seguidas 

            if ciclo_fila == 2:
                ciclo_columna +=1
                ciclo_fila = 5
            
            elif ciclo_columna == 4:
                ciclo_columna = 0
                ciclo_fila = 0
                ciclo1 = False
                break
            
            elif lista[ciclo_fila][ciclo_columna] == lista[ciclo_fila-1][ciclo_columna+1] and lista[ciclo_fila-1][ciclo_columna+1] == lista[ciclo_fila-2][ciclo_columna+2] and lista[ciclo_fila-2][ciclo_columna+2] == lista[ciclo_fila-3][ciclo_columna+3]:
                
                if lista[ciclo_fila][ciclo_columna] == "X" or lista[ciclo_fila][ciclo_columna] == "O":
                    print("Hay ganador diag2 "+str(lista[ciclo_fila][ciclo_columna]))
                    lista_hay_ganador[0] = True
                    lista_hay_ganador[1] = str(lista[ciclo_fila][ciclo_columna])
                    lista_hay_ganador[2] = 1
                    ciclo_columna = 0
                    ciclo_fila = 0
                    ciclo1 = False
                    break
                
                else:
                    ciclo_fila -=1
            
            else:
                ciclo_fila -=1


        if ciclo1 == False:
            break

# Se comienzan a definir las funciones correspondientes a las opciones que se quieren tomar en el menú

# La opcion 1 aparece desde el principio y muestra la informacion sobre el juego

def opcion_1():

    # Se da la bienvenida al juego y se pasa a la parte donde se explica, se dan las instrucciones, reglas y formato del mismo.
    # A esta parte se podrá acceder siempre desde el menu principal del juego

    print("\n¡Bienvenido a Cuatro seguidas!\n\n"
        "A continuación se mostrarán las instrucciones y reglas del juego.\n\n"

        "Este juego para dos participantes consiste en intentar obtener cuatro fichas seguidas ubicadas de manera vertical,\n"
        "horizontal o diagonal en el tablero de juego. Cada participante intentará obtener sus cuatro fichas mientras impide\n"
        "al oponente obtener las suyas. Gana el participante que primero logre sus cuatro fichas seguidas. Cada participante\n" 
        "juega un turno a la vez y en caso de que el participante quiera tentar a la suerte, se le permitirá la opción para\n" 
        "que el computador determine de manera aleatoria la ubicación de la ficha de su turno. Un participante jugará con las\n" 
        "fichas X y otro con las O, será su decisión, pero el segundo jugará con las fichas que le toquen. Quién empiece la\n" 
        "partida será determinado aleatoriamente. El jugador que gane, se llevará 3 puntos, el que pierda no se llevará puntos\n" 
        "y en caso de empate, cada uno de los jugadores sumará de a 1 punto. El tablero del juego consta de 6 filas y 7 columnas\n" 
        "donde podrán ubicar cada una de sus fichas. Se debe tener presente que las fichas se irán apilando en orden en cada una de\n" 
        "las columnas, comenzando desde la fila inferior, de acuerdo con la elección del jugador en su respectivo turno.\n" 
        "El juego termina cuando haya algún ganador, no haya más espacio para seguir jugando o los jugadores hayan decidido\n" 
        "usar la opción de abandonar la partida. Siempre se mostrará quiénes han estado jugando en el juego con su total de puntaje\n"
        "o en el menú en la opción 3, donde si la seleccionas, tambien actualizarás la info del archivo con estadisticas.\n" 
        "Si deseas comenzar una partida, deberás ir a la opción 2 del menú principal y en caso de que quieras abandonar el juego y\n" 
        "todo el progreso acumulado del top jugadores histórico será borrado, deberás ir a la opción 4 en el menú principal.\n\n"

        "Siempre podrás volver a leer este texto en la opción 1 en el menú principal.\n\n"

        "¡Disfruta!\n\n")

# La opcion 3 muestra el historico de jugadores y sus estadisticas

def opcion_3():

    # Verifica si la lista esta vacia en caso de no haber introducido ningun jugador 

    if len(jugadores_perfiles) == 0:
        print("\nAún no hay datos de jugadores por mostrar ni por descargar")

    # Actualiza el dataframe y muestra la informacion en formato de dataframe

    else:

        actualizar_df()

        print("\nEsta es la tabla de jugadores\n")
        print(df.sort_values(by=['Puntaje'], ascending=False))

        print("\nLas estadisticas del juego han sido guardadas y actualizadas en el archivo stats_top_jugadores.txt\n")
        
        file = open("stats_top_jugadores.txt","w")
        file.write(str(df.sort_values(by=['Puntaje'], ascending=False)))
        file.close()

# La opcion 2 es en donde comienza el juego

def opcion_2():

    # Se toman variables que ayudan a romper loops de manera consecutiva

    global breaker2
    global breaker3
    global breaker4

    # Esta es la opcion donde se comienza una nueva partida
    
    while True:

        if breaker3 == True:
            break
        
        breaker2 = False

        jugador1 = ""
        jugador2 = ""
        ficha1 = ""
        ficha2 = ""

        # Se pide el nombre del jugador 1
        jugador1 = str(input('\nPor favor indique nombre de participante #1: '))
        

        while True:

            if breaker2 == True:
                break

            # Se pide la ficha con la que el jugador 1 quiere jugar, en caso de que introduzca algun valor erroneo
            # el codigo lo detectara y volvera a pedir el valor de ficha1

            ficha1 = input("\n"+str(jugador1)+", por favor indica con qué ficha deseas jugar [X] o [O]:")
            

            if ficha1.upper() == "X" or ficha1.upper() == "O":

                ficha1 = ficha1.upper()

                while True:

                    # Pide el nombre del jugador 2 y no dejará avanzar en caso de que se indique el mismo nombre que del jugador 2

                    jugador2 = str(input('\nPor favor indique nombre de participante #2: '))

                    if str(jugador1) == str(jugador2):

                        print("El nombre del jugador 2 es igual al del jugador 1, por favor, verifica tu entrada")

                    else:
                        break


                # Se asignan las fichas con las que cada jugador estará durante la partida

                if str(ficha1) == "X":

                    ficha2 = "O"
                    print(jugador2+", te toca jugar con la siguiente ficha [O]")

                if str(ficha1) == "O":

                    ficha2 = "X"
                    print(jugador2+", te toca jugar con la siguiente ficha [X]")

                # Se añaden cada uno de los valores a un respectivo diccionario

                jugador1_diccionario = {"nombre": jugador1, "fichas": ficha1}
                jugador2_diccionario = {"nombre": jugador2, "fichas": ficha2}

                # Se crea una lista que contiene cada uno de los diccionarios con la información de los jugadores

                jugadores = []
                jugadores.append(jugador1_diccionario)
                jugadores.append(jugador2_diccionario)

                # Se selecciona aleatoriamente el jugador que comenzará la partida, se borra de la lista y se vuelve a añadir
                # con el motivo de asegurarse que el que empieza queda en la posición [1] de la lista y el otro en la posición
                # [0] de la lista

                diccionario_jugador_inicial = random.choice(jugadores)
                jugadores.remove(diccionario_jugador_inicial)
                jugadores.append(diccionario_jugador_inicial)

                # Se da un print con la información de la partida 

                print("\nLa partida comenzará..\n\n"

                    +jugador1+" juega con las fichas "+ficha1+"\n"
                    +jugador2+" juega con las fichas "+ficha2+"\n"

                    "La partida la inicia "+diccionario_jugador_inicial["nombre"]+"\n")

                actualizar_df()

                # Se crean y se llaman variables y valores que se utilizarán durante la partida
                # Las filas que serán el tablero que se estará modificando

                fila_1 = [".",".",".",".",".",".","."]
                fila_2 = [".",".",".",".",".",".","."]
                fila_3 = [".",".",".",".",".",".","."]
                fila_4 = [".",".",".",".",".",".","."]
                fila_5 = [".",".",".",".",".",".","."]
                fila_6 = [".",".",".",".",".",".","."]
                tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]

                # El turno será un valor que determinará qué jugador será el que sigue 

                breaker4 = False
                lista_hay_ganador[0] = False
                lista_hay_ganador[0] = 0
                lista_hay_ganador[0] = 0
                turno = 2

                while True:

                    if breaker4 == True:
                        break

                    # Se verifica si aun hay espacio para seguir jugando en el tablero y en caso de que esté lleno, la partida
                    # se dará como en empate

                    elif hay_espacio(tablero, "."):

                        # Se verifica constantemente si hay algun ganador 
                        
                        hay_ganador(tablero)

                        if lista_hay_ganador[0]:

                            # Se verifica si los jugadores digitados son nombres nuevos o ya habian jugado alguna partida

                            revisar_perfil = 0

                            es_nuevo = 1
                            for n in range(len(jugadores_perfiles)):
                                if str(jugadores_perfiles[revisar_perfil][0]) == str(jugador1):
                                    es_nuevo = 0
                                    break
                                else:
                                    revisar_perfil +=1
                            if es_nuevo == 1:
                                jugador_perfil1 = [jugador1, 0, 0, 0, 0, 0]
                                jugadores_perfiles.append(jugador_perfil1)


                            revisar_perfil = 0
                            es_nuevo = 1

                            for n in range(len(jugadores_perfiles)):
                                if str(jugadores_perfiles[revisar_perfil][0]) == str(jugador2):
                                    es_nuevo = 0
                                    break
                                else:
                                    revisar_perfil +=1
                            if es_nuevo == 1:
                                jugador_perfil2 = [jugador2, 0, 0, 0, 0, 0]
                                jugadores_perfiles.append(jugador_perfil2)
                                    

                            # Se actualiza de nuevo el dataframe

                            actualizar_df()

                            print(
                            "\n 1234567 \n"
                            "+-------+\n"
                            "|"+str(lista_a_string(fila_1))+"|\n"
                            "|"+str(lista_a_string(fila_2))+"|\n"
                            "|"+str(lista_a_string(fila_3))+"|\n"
                            "|"+str(lista_a_string(fila_4))+"|\n"
                            "|"+str(lista_a_string(fila_5))+"|\n"
                            "|"+str(lista_a_string(fila_6))+"|\n"
                            "+-------+\n")
                            
                            if str(lista_hay_ganador[1]) == str(ficha1): # Si el ganador es el jugador 1

                                registro_jugador = 0

                                for n in range(len(jugadores_perfiles)): # Comienza a buscar el nombre de jugador 1 como ganador y actualizar sus estadisticas

                                    if jugadores_perfiles[registro_jugador][0] == jugador1:
                                        jugadores_perfiles[registro_jugador][1] +=3
                                        jugadores_perfiles[registro_jugador][2] +=1
                                        jugadores_perfiles[registro_jugador][3] +=1
                                        break

                                    else:
                                        registro_jugador +=1

                                registro_jugador = 0

                                for n in range(len(jugadores_perfiles)): # Actualiza tambien las estadisticas del jugador 2

                                    if jugadores_perfiles[registro_jugador][0] == jugador2:
                                        jugadores_perfiles[registro_jugador][4] +=1
                                        jugadores_perfiles[registro_jugador][2] +=1
                                        break

                                    else:
                                        registro_jugador +=1

                                print("El ganador de la partida es "+jugador1+" con las fichas "+ficha1)
    

                            elif str(lista_hay_ganador[1]) == str(ficha2): # Comienza a hacer lo mismo pero en este caso si el ganador fue el jugador 2

                                print("El ganador de la partida es "+jugador2+" con las fichas "+ficha2)

                                registro_jugador = 0

                                for n in range(len(jugadores_perfiles)):
                                    
                                    if jugadores_perfiles[registro_jugador][0] == jugador2:
                                        jugadores_perfiles[registro_jugador][1] +=3
                                        jugadores_perfiles[registro_jugador][2] +=1
                                        jugadores_perfiles[registro_jugador][3] +=1
                                        break

                                    else:
                                        registro_jugador +=1


                                registro_jugador = 0

                                for n in range(len(jugadores_perfiles)):
                                    
                                    if jugadores_perfiles[registro_jugador][0] == jugador1:
                                        jugadores_perfiles[registro_jugador][4] +=1
                                        jugadores_perfiles[registro_jugador][2] +=1
                                        break

                                    else:
                                        registro_jugador +=1

                            # Mostrará de nuevo el dataframe de la tabla de los jugadores

                            opcion_3()


                            while True:

                                # Preguntará si los jugadores desean volver a tomar la partida

                                decision = input("¿Desean volver a tomar la partida Si [S] No [N]?: ")

                                if verificar_string(decision):

                                    if str(decision).upper() == "S":

                                        # Si deciden volver a retomar la partida reinicia valores que durante la partida jugada fueron modificados

                                        fila_1 = [".",".",".",".",".",".","."]
                                        fila_2 = [".",".",".",".",".",".","."]
                                        fila_3 = [".",".",".",".",".",".","."]
                                        fila_4 = [".",".",".",".",".",".","."]
                                        fila_5 = [".",".",".",".",".",".","."]
                                        fila_6 = [".",".",".",".",".",".","."]
                                        tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]

                                        lista_hay_ganador[0] = False
                                        lista_hay_ganador[0] = 0
                                        lista_hay_ganador[0] = 0
                                        break

                                    elif str(decision).upper() == "N":

                                        breaker2 = True
                                        breaker3 = True
                                        breaker4 = True
                                        break 

                                    else:
                                        print("Verifica tu entrada, introduce N o S")
                                
                                else:
                                    print("Verifica tu entrada, introduce N o S")

                    
                        # Sistema de turnos en donde se da 1 por 1

                        elif int(turno) % 2 == 0:

                            # Se muestra el tablero

                            print(
                            "\n 1234567 \n"
                            "+-------+\n"
                            "|"+str(lista_a_string(fila_1))+"|\n"
                            "|"+str(lista_a_string(fila_2))+"|\n"
                            "|"+str(lista_a_string(fila_3))+"|\n"
                            "|"+str(lista_a_string(fila_4))+"|\n"
                            "|"+str(lista_a_string(fila_5))+"|\n"
                            "|"+str(lista_a_string(fila_6))+"|\n"
                            "+-------+\n")


                            # Se muestra la información del turno

                            print("\n"+str(jugadores[1]["nombre"])+" ["+str(jugadores[1]["fichas"])+"] "+" es tu turno.\n")


                            # Se da al usuario las opciones de su turno, en caso de introducir un valor no válido
                            # perderá su turno

                            eleccion = input("\nSelecciona el # de la columna o [S] para jugar a la suerte o [0] para abandonar la partida: ")

                            if verificar_numero(eleccion):


                                if int(eleccion) in range(1,8):

                                    ciclo = 5

                                    while True:

                                        if ciclo == -1:          

                                            # En caso de que la columna seleccionada esté llena, perderá el turno

                                            print("\nEsta columna está llena, has perdido el turno") 
                                            turno += 1
                                            break 

                                        else:

                                            if tablero[ciclo][int(eleccion)-1] == ".":

                                                tablero[ciclo][int(eleccion)-1] = jugadores[1]["fichas"]
                                                turno +=1
                                                break

                                            else:
                                                ciclo -=1


                                # Si la eleccion fue 0, en ese caso se saldrá de la partida actual y no guardará ningún dato ocurrido durante la partida

                                elif int(eleccion) == 0:

                                    breaker2 = True
                                    breaker3 = True
                                    break

                                else:

                                    print("\nEl mensaje digitado es incorrecto, has perdido el turno")
                                    turno += 1


                            elif verificar_string(eleccion):


                                if str(eleccion).upper() == "S":

                                    eleccion = random.randint(1, 7)
                                    ciclo = 5

                                    while True:

                                        if ciclo == -1:         

                                            print("\nLa maquina ha seleccionado la columna "+str(eleccion)+
                                            " la cual está llena, mala suerte, pierdes el turno") 
                                            turno += 1
                                            break 

                                        else:

                                            if tablero[ciclo][int(eleccion)-1] == ".":

                                                tablero[ciclo][int(eleccion)-1] = jugadores[1]["fichas"]
                                                turno +=1
                                                break

                                            else:
                                                ciclo -=1

                                else:

                                    print("\nEl mensaje digitado es incorrecto, has perdido el turno")
                                    turno += 1
                            else:

                                turno +=1
                                print("\nEl mensaje digitado es incorrecto, has perdido el turno")


                        # Comienza el turno del otro jugador que funciona exactamente de la misma forma        

                        elif int(turno) % 2 != 0:

                            # Se muestra el tablero

                            print(
                            "\n 1234567 \n"
                            "+-------+\n"
                            "|"+str(lista_a_string(fila_1))+"|\n"
                            "|"+str(lista_a_string(fila_2))+"|\n"
                            "|"+str(lista_a_string(fila_3))+"|\n"
                            "|"+str(lista_a_string(fila_4))+"|\n"
                            "|"+str(lista_a_string(fila_5))+"|\n"
                            "|"+str(lista_a_string(fila_6))+"|\n"
                            "+-------+\n")


                            # Se muestra la información del turno

                            print("\n"+str(jugadores[0]["nombre"])+" ["+str(jugadores[0]["fichas"])+"] "+" es tu turno.\n")


                            # Se da al usuario las opciones de su turno, en caso de introducir un valor no válido
                            # perderá su turno

                            eleccion = input("\nSelecciona el # de la columna o [S] para jugar a la suerte o [0] para abandonar la partida: ")

                            if verificar_numero(eleccion):


                                if int(eleccion) in range(1,8):

                                    ciclo = 5

                                    while True:

                                        if ciclo == -1:          

                                            print("\nEsta columna está llena, has perdido el turno") 
                                            turno += 1
                                            break 

                                        else:

                                            if tablero[ciclo][int(eleccion)-1] == ".":

                                                tablero[ciclo][int(eleccion)-1] = jugadores[0]["fichas"]
                                                turno +=1
                                                break
                                            else:

                                                ciclo -=1

                                elif int(eleccion) == 0:

                                    breaker2 = True
                                    breaker3 = True
                                    break

                                else:

                                    print("\nEl mensaje digitado es incorrecto, has perdido el turno")
                                    turno += 1


                            elif verificar_string(eleccion):


                                if str(eleccion).upper() == "S":

                                    eleccion = random.randint(1, 7)
                                    ciclo = 5

                                    while True:

                                        if ciclo == -1:                   

                                            print("\nLa maquina ha seleccionado la columna "+str(eleccion)+
                                            " la cual está llena, mala suerte, pierdes el turno") 
                                            turno += 1
                                            break 

                                        else:
                                            if tablero[ciclo][int(eleccion)-1] == ".":

                                                tablero[ciclo][int(eleccion)-1] = jugadores[0]["fichas"]
                                                turno +=1
                                                break
                                            else:

                                                ciclo -=1

                                else:

                                    print("\nEl mensaje digitado es incorrecto, has perdido el turno")
                                    turno += 1
                            else:

                                turno +=1
                                print("\nEl mensaje digitado es incorrecto, has perdido el turno")


                    # Esta opcion saltará en caso de que el tablero se haya llenado

                    else:

                        print(
                            "\n 1234567 \n"
                            "+-------+\n"
                            "|"+str(lista_a_string(fila_1))+"|\n"
                            "|"+str(lista_a_string(fila_2))+"|\n"
                            "|"+str(lista_a_string(fila_3))+"|\n"
                            "|"+str(lista_a_string(fila_4))+"|\n"
                            "|"+str(lista_a_string(fila_5))+"|\n"
                            "|"+str(lista_a_string(fila_6))+"|\n"
                            "+-------+\n")

                        print("El tablero se ha llenado, la partida ha finalizado en empate.")

                        # Hará lo mismo que hizo cuando hay algun ganador pero en este caso, sólo dará puntos por empate y sumará en el item de empates

                        revisar_perfil = 0

                        es_nuevo = 1

                        for n in range(len(jugadores_perfiles)):
                            
                            if str(jugadores_perfiles[revisar_perfil][0]) == str(jugador1):

                                es_nuevo = 0
                                break

                            else:

                                revisar_perfil +=1

                        if es_nuevo == 1:

                            jugador_perfil1 = [jugador1, 0, 0, 0, 0, 0]
                            jugadores_perfiles.append(jugador_perfil1)

                        actualizar_df()
                        
                        revisar_perfil = 0
                        es_nuevo = 1

                        for n in range(len(jugadores_perfiles)):

                            if str(jugadores_perfiles[revisar_perfil][0]) == str(jugador2):

                                es_nuevo = 0
                                break

                            else:
                                revisar_perfil +=1

                        if es_nuevo == 1:

                            jugador_perfil2 = [jugador2, 0, 0, 0, 0, 0]
                            jugadores_perfiles.append(jugador_perfil2)

                        registro_jugador = 0

                        for n in range(len(jugadores_perfiles)): 

                            if jugadores_perfiles[registro_jugador][0] == jugador1:

                                jugadores_perfiles[registro_jugador][1] +=1
                                jugadores_perfiles[registro_jugador][2] +=1
                                jugadores_perfiles[registro_jugador][5] +=1
                                break

                            else:
                
                                registro_jugador +=1


                        registro_jugador = 0

                        for n in range(len(jugadores_perfiles)):

                            if jugadores_perfiles[registro_jugador][0] == jugador2:

                                jugadores_perfiles[registro_jugador][1] +=1
                                jugadores_perfiles[registro_jugador][2] +=1
                                jugadores_perfiles[registro_jugador][5] +=1
                                break

                            else:

                                registro_jugador +=1

                        actualizar_df()

                        opcion_3()

                        while True:

                            decision = input("¿Desean volver a tomar la partida Si [S] No [N]?: ")

                            if verificar_string(decision):

                                if str(decision).upper() == "S":

                                    fila_1 = [".",".",".",".",".",".","."]
                                    fila_2 = [".",".",".",".",".",".","."]
                                    fila_3 = [".",".",".",".",".",".","."]
                                    fila_4 = [".",".",".",".",".",".","."]
                                    fila_5 = [".",".",".",".",".",".","."]
                                    fila_6 = [".",".",".",".",".",".","."]
                                    tablero = [fila_1, fila_2, fila_3, fila_4, fila_5, fila_6]
                                    break

                                elif str(decision).upper() == "N":

                                    breaker2 = True
                                    breaker3 = True
                                    breaker4 = True
                                    break 

                                else:

                                    print("Verifica tu entrada, introduce N o S")
                                
                            else:

                                print("Verifica tu entrada, introduce N o S")
                            
                        
            else:

                print("La ficha que has introducido es incorrecta, sólo puedes escoger entre X y O.")

def opcion_4():

    global breaker1

    # En esta opcion se toma la opcion de que los jugadores quieran salir del juego

    while True:

        # Se imprime lo que implica salirse del juego y la confirmacion de querer salirse

        confirmacion = input("\n¿Estás seguro que deseas salir del juego?\n"
        "Todo tu progreso de top jugadores históricos será borrado.\n"
        "(SI para salir, NO para volver al menú principal): ")

        # Si la persona decidio salirse, se daran las gracias y el codigo rompera los ciclos anteriores

        if confirmacion.upper() == "SI":

            print("\n¡Gracias por jugar!")
            breaker1 = True
            break

        elif confirmacion.upper() == "NO":

            print("\nPasarás del nuevo al menú principal")
            break

        else:

            print("\nHas introducido un valor incorrecto, verifica tu entrada")
            continue

def juego():

    global breaker1
    global breaker2
    global breaker3
    global breaker4

    # Se utiliza la funcion del juego que agrupa todas las funciones anteriores y lo que hace es 
    # manejar las decisiones que toma el usuario en el menú principal y redijirlo dependiendo 
    # de lo que quiere el usuario

    # Se imprime para empezar la bienvenida

    opcion_1()

    while True:

        if breaker1 == True:
            break

        breaker3 = False

        # Se comienza a pedir lo que el usuario desea hacer y dependiendo de eso va a una u otra
        # de las funciones que contiene el menu principal

        menu_decision = input("\nDigita el número (1,2,3 o 4) de la opción a la que quieras dirigirte\n"
                              "1. Ver las instrucciones del juego\n"
                              "2. Jugar\n"
                              "3. Top jugadores\n"
                              "4. Salir\n")

        if verificar_numero(menu_decision):

            menu_decision = int(menu_decision)

            if menu_decision == 1:

                opcion_1()

            elif menu_decision == 2:

                opcion_2()

            elif menu_decision == 3:

                opcion_3()

            elif menu_decision == 4:

                opcion_4()

            # En caso de que el usuario introduzca un valor incorrecto, se le volvera a pedir que introduzca uno correcto

            else:

                print("\nHas introducido un valor incorrecto, verifica tu entrada.")

        # En caso de que el usuario introduzca un valor incorrecto, se le volvera a pedir que introduzca uno correcto

        else:
            
            print("\nHas introducido un valor incorrecto, verifica tu entrada.")

# Se comienza el juego llamando la funcion juego

juego()