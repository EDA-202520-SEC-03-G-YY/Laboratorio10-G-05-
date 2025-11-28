"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import threading
from App import logic
from DataStructures.List import array_list as al

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


servicefile = 'bus_routes_14000.csv'
stopsfile = 'bus_stops.csv'
initialStation = None

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def print_menu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar información de buses de singapur") # Clase 1: Implementar digraph básico
    print("2- Encontrar las paradas más concurridas") # Casa 1: Implementar digraph completo
    print("3- Encontrar una ruta entre dos paradas (DFS)") # Casa 1: Implementar funcionalidad dfs
    print("4- Encontrar una ruta entre dos paradas (BFS)") # Clase 2: Implementar funcionalidad bfs
    print("5- Encontrar la ruta mínima entre dos paradas") # Casa 2: Implementar dijkstra
    print("6- Mostrar en un mapa la ruta mínima entre dos paradas") # Trabajo Complementario: Mostrar ruta con folium
    print("0- Salir")
    print("*******************************************")


def option_one(cont):
    print("\nCargando información de transporte de singapur ....")
    logic.load_services(cont, servicefile, stopsfile)
    numedges = logic.total_connections(cont)
    numvertex = logic.total_stops(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))

def option_two(cont):
    """
    Opción 2: Encontrar las paradas más concurridas
    """
    print("\n------ OPCIÓN 2 ------")
    print("Las paradas más concurridas son:")
    
    resp = logic.get_most_concurrent_stops(cont)
    for i in range(al.size(resp)):
        stop = al.get_element(resp, i)
        print(f"{i+1}. '{stop['BusStopCode']}': {stop['out_degree']} conexiones")




def option_three(cont):
    """
    Opción 3: Encontrar una ruta entre dos paradas usando DFS
    """
    print("\n----- OPCIÓN 3 (DFS) -----")
    stop1 = input("Parada inicial: ")
    stop2 = input("Parada destino: ")
    
    print(f"\n--- Tomar bus '{stop1.split('-')[1]}' desde '{stop1.split('-')[0]}' ---")
    
    path = logic.get_route_between_stops_dfs(cont, stop1, stop2)
    
    if path is None:
        print("\nNo existe ruta entre las paradas especificadas.")
        return
    previous_bus = None
    previous_stop = None
    
    for i in range(al.size(path)):
        vertex = al.get_element(path, i)
        parts = vertex.split('-')
        stop_code = parts[0]
        bus_number = parts[1]
        
        if i == 0:
            print(f"{stop_code}", end="")
            previous_bus = bus_number
            previous_stop = stop_code
        else:
            
            if bus_number != previous_bus:
                print(f"\n--- Cambiar a la parada '{previous_stop}' ---")
                print(f"--- Tomar bus '{bus_number}' desde la parada '{stop_code}' ---")
                print(f"{stop_code}", end="")
                previous_bus = bus_number
            else:
                print(f" -> {stop_code}", end="")
            
            previous_stop = stop_code
    
    print()


def option_four(cont):
    """
    Opción 4: Encontrar una ruta entre dos paradas usando BFS
    """
    print("\n----- OPCIÓN 4 (BFS) -----")
    stop1 = input("Parada inicial: ")
    stop2 = input("Parada destino: ")
    
    print(f"\n--- Tomar bus '{stop1.split('-')[1]}' desde '{stop1.split('-')[0]}' ---")
    
    path = logic.get_route_between_stops_bfs(cont, stop1, stop2)
    
    if path is None:
        print("\nNo existe ruta entre las paradas especificadas.")
        return
    
    previous_bus = None
    previous_stop = None
    
    for i in range(al.size(path)):
        vertex = al.get_element(path, i)
        parts = vertex.split('-')
        stop_code = parts[0]
        bus_number = parts[1]
        
        if i == 0:
            # Primera parada
            print(f"{stop_code}", end="")
            previous_bus = bus_number
            previous_stop = stop_code
        else:
            # Verificar si hay cambio de bus
            if bus_number != previous_bus:
                print(f"\n--- Cambiar a la parada '{previous_stop}' ---")
                print(f"--- Tomar bus '{bus_number}' desde la parada '{stop_code}' ---")
                print(f"{stop_code}", end="")
                previous_bus = bus_number
            else:
                print(f" -> {stop_code}", end="")
            
            previous_stop = stop_code
    
    print()  
        

def option_five(cont):
    """
    Opción 5: Encontrar la ruta de distancia mínima usando Dijkstra
    """
    print("\n----- OPCIÓN 5 (Dijkstra) -----")
    origin = input("Origen: ")
    destination = input("Destino: ")
    
    origin_bus = origin.split('-')[1]
    origin_stop = origin.split('-')[0]
    
    print(f"\n--- Tomar bus '{origin_bus}' desde '{origin_stop}-{origin_bus}' ---")
    
    path = logic.get_shortest_route_between_stops(cont, origin, destination)
    
    if path is None:
        print("\nNo existe ruta entre las paradas especificadas.")
        return
    
    from DataStructures.List import array_list as al
    
    previous_bus = None
    previous_stop = None
    
    for i in range(al.size(path)):
        vertex = al.get_element(path, i)
        parts = vertex.split('-')
        stop_code = parts[0]
        bus_number = parts[1]
        
        if i == 0:
            print(f"{stop_code}", end="")
            previous_bus = bus_number
            previous_stop = stop_code
        else:
            if bus_number != previous_bus:
                print(f"\n--- Cambiar a bus '{bus_number}' en la parada '{previous_stop}' ---")
                print(f"{stop_code}", end="")
                previous_bus = bus_number
            else:
                print(f" -> {stop_code}", end="")
            
            previous_stop = stop_code
    
    print()

def option_six(cont):
    # (Opcional) TODO: Imprimir los resultados de la opción 6
    ...


"""
Menu principal
"""


def main():
    working = True
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n>')

        if int(inputs[0]) == 1:
            print("\nInicializando....")
            cont = logic.new_analyzer()
            option_one(cont)
        elif int(inputs[0]) == 2:
            option_two(cont)
        elif int(inputs[0]) == 3:
            option_three(cont)
        elif int(inputs[0]) == 4:
            option_four(cont)
        elif int(inputs[0]) == 5:
            option_five(cont)
        elif int(inputs[0]) == 6:
            option_six(cont)
        else:
            working = False
            print("Saliendo...")
    sys.exit(0)


if __name__ == "__main__":
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()
