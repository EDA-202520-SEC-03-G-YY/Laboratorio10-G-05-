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

# ___________________________________________________
#  Importaciones
# ___________________________________________________

from DataStructures.List import single_linked_list as lt
from DataStructures.Map import map_linear_probing as m
from DataStructures.Graph import digraph as G
from DataStructures.Graph import dfs as dfs
from DataStructures.List import array_list as al
from DataStructures.Graph import bfs as bfs
from DataStructures.Stack import stack as st

import csv
import time
import os

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = new_analyzer()
    return analyzer


def new_analyzer():
    """ Inicializa el analizador

   stops: Tabla de hash para guardar la información de las paradas
   connections: Grafo para representar las rutas entre estaciones
   paths: Estructura que almancena los caminos de costo minimo desde un
           vertice determinado a todos los otros vértices del grafo
    """
    try:
        analyzer = {
            'stops': None,
            'connections': None,
            'paths': None
        }

        analyzer['stops'] = m.new_map(
            num_elements=8000, load_factor=0.7, prime=109345121)

        analyzer['connections'] = G.new_graph(order=20000)
        return analyzer
    except Exception as exp:
        return exp

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def load_services(analyzer, servicesfile, stopsfile):
    """
    Carga los datos de los archivos CSV en el modelo.
    Se crea un arco entre cada par de estaciones que
    pertenecen al mismo servicio y van en el mismo sentido.

    addRouteConnection crea conexiones entre diferentes rutas
    servidas en una misma estación.
    """
    stopsfile = data_dir + stopsfile
    stops_input_file = csv.DictReader(open(stopsfile, encoding="utf-8"),
                                      delimiter=",")

    for stop in stops_input_file:
        add_stop(analyzer, stop)

    servicesfile = data_dir + servicesfile
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8"),
                                delimiter=",")
    lastservice = None
    for service in input_file:
        if not G.contains_vertex(analyzer['connections'], format_vertex(service)):
            add_stop_vertex(analyzer, format_vertex(service))
        add_route_stop(analyzer, service)

        if lastservice is not None:
            sameservice = lastservice['ServiceNo'] == service['ServiceNo']
            samedirection = lastservice['Direction'] == service['Direction']
            samebusStop = lastservice['BusStopCode'] == service['BusStopCode']
            if sameservice and samedirection and not samebusStop:
                add_stop_connection(analyzer, lastservice, service)

        add_same_stop_connections(analyzer, service)
        lastservice = service

    return analyzer

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def total_stops(analyzer):
    """
    Total de paradas de autobus en el grafo
    """
    # número de vértices del grafo
    return G.order(analyzer["connections"])

def total_connections(analyzer):
    """
    Total de enlaces entre las paradas
    """
    # número de arcos del grafo de conexiones
    return G.size(analyzer["connections"])


# Funciones para la medición de tiempos

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Funciones para agregar informacion al grafo

def add_stop_connection(analyzer, lastservice, service):
    """
    Adiciona las estaciones al grafo como vertices y arcos entre las
    estaciones adyacentes.

    Los vertices tienen por nombre el identificador de la estacion
    seguido de la ruta que sirve.  Por ejemplo:

    75009-10

    Si la estacion sirve otra ruta, se tiene: 75009-101
    """
    try:
        origin = format_vertex(lastservice)
        destination = format_vertex(service)
        clean_service_distance(lastservice, service)
        distance = float(service['Distance']) - float(lastservice['Distance'])
        distance = abs(distance)
        add_connection(analyzer, origin, destination, distance)
        return analyzer
    except Exception as exp:
        return exp


def add_stop(analyzer, stop):
    """
    Adiciona una parada (BusStopCode) en los stops del sistema de transporte
    """
    stop['services'] = lt.new_list()
    m.put(analyzer['stops'], stop['BusStopCode'], stop)
    return analyzer

def add_stop_vertex(analyzer, stopid):
    """
    Adiciona una estación como un vertice del grafo
    """

    G.insert_vertex(analyzer['connections'], stopid, stopid)
    return analyzer


def add_route_stop(analyzer, service):
    """
    Agrega a una estacion, una ruta que es servida en ese paradero
    """
    stop_info = m.get(analyzer['stops'], service['BusStopCode'])
    stop_services = stop_info['services']
    if lt.is_present(stop_services, service['ServiceNo'], lt.default_sort_criteria) == -1:
        lt.add_last(stop_services, service['ServiceNo'])

    return analyzer


def add_connection(analyzer, origin, destination, distance):
    """
    Adiciona un arco entre dos estaciones
    """

    G.add_edge(analyzer['connections'], origin, destination, distance)



def add_same_stop_connections(analyzer, service):
    stop_1 = format_vertex(service)
    stop_buses_lt = m.get(analyzer['stops'], service['BusStopCode'])['services']

    if lt.size(stop_buses_lt) > 1:
        pass

    node = stop_buses_lt['first']
    for _ in range(lt.size(stop_buses_lt)):
        stop_2 = format_vertex({'BusStopCode': service['BusStopCode'], 'ServiceNo': node['info']})
        if stop_1 != stop_2:
            add_connection(analyzer, stop_1, stop_2, 0)
        node = node['next']
    return analyzer


# ___________________________________________________
#  Funciones de resolución de requerimientos
# ___________________________________________________


def get_most_concurrent_stops(analyzer):
    """
    Obtiene las 5 paradas más concurridas, es decir, con más arcos salientes
    """
    vertices = G.vertices(analyzer["connections"])
    
    stops_dict = {}
    
    for i in range(al.size(vertices)):
        vertex = al.get_element(vertices, i)
        
        parts = vertex.split('-')
        if len(parts) != 2:
            continue
            
        bus_stop_code = parts[0]
        service_no = parts[1]
        
        if bus_stop_code not in stops_dict:
            stops_dict[bus_stop_code] = {
                'services': set(),
                'vertices': [],
                'out_degree': 0
            }
        
        stops_dict[bus_stop_code]['services'].add(service_no)
        stops_dict[bus_stop_code]['vertices'].append(vertex)
        
        adjacents_list = G.adjacents(analyzer["connections"], vertex)
        
        for j in range(al.size(adjacents_list)):
            adj = al.get_element(adjacents_list, j)
            adj_stop_code = adj.split('-')[0]
           
            if adj_stop_code != bus_stop_code:
                stops_dict[bus_stop_code]['out_degree'] += 1
    
    items = al.new_list()
    for bus_stop_code, info in stops_dict.items():
        al.add_last(items, {
            'BusStopCode': bus_stop_code,
            'num_services': len(info['services']),
            'services': sorted(list(info['services'])),
            'out_degree': info['out_degree'],
            'vertices': info['vertices']
        })
    
    def sort_crit(e1, e2):
        if e1['out_degree'] != e2['out_degree']:
            return e1['out_degree'] > e2['out_degree']
        return e1['num_services'] > e2['num_services']
    
    items = al.merge_sort(items, sort_crit)
    
    # Tomar los top 5
    result = al.new_list()
    tam = min(5, al.size(items))
    
    for i in range(tam):
        al.add_last(result, al.get_element(items, i))
    
    return result



       
def get_route_between_stops_dfs(analyzer, stop1, stop2):
    """
    Obtener la ruta entre dos paradas usando DFS
    """
    graph = analyzer["connections"]
    
    if not G.contains_vertex(graph, stop1):
        return None
    if not G.contains_vertex(graph, stop2):
        return None
    
    visited_map = dfs.dfs(graph, stop1)
    
    if not dfs.has_path_to(stop2, visited_map):
        return None
    
    path_stack = dfs.path_to(stop2, visited_map)
    
    if path_stack is None:
        return None
    
    result = al.new_list()
    temp_stack = st.new_stack()
    
    while not st.is_empty(path_stack):
        vertex = st.pop(path_stack)
        st.push(temp_stack, vertex)
    
    while not st.is_empty(temp_stack):
        vertex = st.pop(temp_stack)
        al.add_last(result, vertex)
    
    return result
            
    
def get_route_between_stops_bfs(analyzer, stop1, stop2):
    
    """
    Obtener la ruta entre dos paradas usando BFS
    """
    graph = analyzer["connections"]
    
    if not G.contains_vertex(graph, stop1):
        return None
    if not G.contains_vertex(graph, stop2):
        return None
    
    visited_map = bfs.bfs(graph, stop1)
    
    if not bfs.has_path_to(stop2, visited_map):
        return None
    
    path_stack = bfs.path_to(stop2, visited_map)
    
    if path_stack is None:
        return None
    
    result = al.new_list()
    temp_stack = st.new_stack()
    
    while not st.is_empty(path_stack):
        vertex = st.pop(path_stack)
        st.push(temp_stack, vertex)
    
    while not st.is_empty(temp_stack):
        vertex = st.pop(temp_stack)
        al.add_last(result, vertex)
    
    return result

def get_shortest_route_between_stops(analyzer, stop1, stop2):
    """
    Obtener la ruta mínima entre dos paradas
    """
    # TODO: Obtener la ruta mínima entre dos paradas
    # Nota: Tenga en cuenta que el debe guardar en la llave
    #       analyzer['paths'] el resultado del algoritmo de Dijkstra
    ...

def show_calculated_shortest_route(analyzer, destination_stop):
    # (Opcional) TODO: Mostrar en un mapa la ruta mínima entre dos paradas usando folium
    ...




# ___________________________________________________
# Funciones Helper
# ___________________________________________________

def clean_service_distance(lastservice, service):
    """
    En caso de que el archivo tenga un espacio en la
    distancia, se reemplaza con cero.
    """
    if service['Distance'] == '':
        service['Distance'] = 0
    if lastservice['Distance'] == '':
        lastservice['Distance'] = 0


def format_vertex(service):
    """
    Se formatea el nombrer del vertice con el id de la estación
    seguido de la ruta.
    """
    name = service['BusStopCode'] + '-'
    name = name + service['ServiceNo']
    return name
