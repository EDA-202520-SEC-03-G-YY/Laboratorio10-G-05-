"""
DataStructures/Graph/digraph.py
Implementación del Tipo Abstracto de Datos Grafo Dirigido
"""

from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as vx
from DataStructures.Graph import edge as ed
from DataStructures.List import array_list as lt

def new_graph(order):
    """
    Crea un grafo dirigido vacio
    
    Args:
        order (int): Numero de vertices inicial del grafo
        
    Returns:
        digraph: Grafo vacio (sin vertices ni arcos)
    """
    grafo = {
        "vertices": mp.new_map(order, 0.5),
        "num_edges": 0
    }
    return grafo


def insert_vertex(my_graph, key_u, info_u):
    """
    Agrega un nuevo vertice al grafo
    
    Args:
        my_graph (digraph): Grafo al que se le desea agregar el nuevo vertice
        key_u (any): Llave del nuevo vertice
        info_u (any): Informacion asociada al vertice
        
    Returns:
        digraph: El grafo con el nuevo vertice
    """
    # Crear el nuevo vertice
    new_vertex = vx.new_vertex(key_u, info_u)
    # Agregar el vertice al mapa de vertices
    mp.put(my_graph['vertices'], key_u, new_vertex)
    return my_graph


def add_edge(my_graph, key_u, key_v, weight=1.0):
    """
    Agrega un arco dirigido al grafo del vertice key_u al vertice key_v
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        key_u (any): Llave del vertice de inicio
        key_v (any): Llave del vertice destino
        weight (double): Peso del arco, por defecto 1
        
    Returns:
        digraph: El grafo con el nuevo arco
    """
    # Verificar que ambos vertices existen
    vertex_u = mp.get(my_graph['vertices'], key_u)
    vertex_v = mp.get(my_graph['vertices'], key_v)
    
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    if vertex_v is None:
        raise Exception("El vertice v no existe")
    
    # Verificar si el arco ya existe
    edge_exists = vx.get_edge(vertex_u, key_v)
    
    # Agregar el arco al vertice origen
    vx.add_adjacent(vertex_u, key_v, weight)
    
    # Incrementar el contador de arcos solo si no existia antes
    if edge_exists is None:
        my_graph['num_edges'] += 1
    
    return my_graph


def contains_vertex(my_graph, key_u):
    """
    Retorna si el vertice con llave key_u esta presente en el grafo
    
    Args:
        my_graph (digraph): El grafo sobre el cual consultar la existencia del vertice
        key_u (any): Vertice a buscar
        
    Returns:
        bool: True si el vertice esta presente, False en caso contrario
    """
    return mp.contains(my_graph['vertices'], key_u)


def order(my_graph):
    """
    Retorna el orden del grafo (numero de vertices)
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        
    Returns:
        int: El numero de vertices del grafo
    """
    return mp.size(my_graph['vertices'])


def size(my_graph):
    """
    Retorna el tamaño del grafo (numero de arcos)
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        
    Returns:
        int: El numero de arcos del grafo
    """
    return my_graph['num_edges']


def degree(my_graph, key_u):
    """
    Retorna el grado del vertice con llave key_u
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        key_u (any): El vertice del que se desea conocer el grado
        
    Returns:
        int: El grado del vertice
    """
    vertex = mp.get(my_graph['vertices'], key_u)
    if vertex is None:
        raise Exception("El vertice no existe")
    return vx.degree(vertex)


def adjacents(my_graph, key_u):
    """
    Retorna una lista con las llaves de los vertices adyacentes al vertice con llave key_u
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        key_u (any): El vertice del que se quiere la lista
        
    Returns:
        list: La lista de vertices adyacentes
    """
    vertex = mp.get(my_graph['vertices'], key_u)
    if vertex is None:
        raise Exception("El vertice no existe")
    
    # Obtener el mapa de adyacentes
    adjacents_map = vx.get_adjacents(vertex)
    # Obtener las llaves (vertices adyacentes)
    keys_list = mp.key_set(adjacents_map)
    
    return keys_list


def vertices(my_graph):
    """
    Retorna una lista con las llaves de todos los vertices del grafo
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        
    Returns:
        list: La lista con los vertices del grafo
    """
    return mp.key_set(my_graph['vertices'])


def edges_vertex(my_graph, key_u):
    """
    Retorna una lista con todos los arcos asociados a los vertices adyacentes del vertice con llave key_u
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        key_u (any): El vertice del que se quiere la lista
        
    Returns:
        list: La lista de arcos adyacentes
    """
    vertex = mp.get(my_graph['vertices'], key_u)
    if vertex is None:
        raise Exception("El vertice no existe")
    
    # Obtener el mapa de adyacentes
    adjacents_map = vx.get_adjacents(vertex)
    # Obtener los valores (arcos)
    edges_list = mp.value_set(adjacents_map)
    
    return edges_list


def get_vertex(my_graph, key_u):
    """
    Retorna la informacion completa del vertice con llave key_u
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        key_u (any): Llave del vertice del que se quiere la informacion completa
        
    Returns:
        vertex: El vertice. Retorna None en caso de que el vertice no exista
    """
    vertex = mp.get(my_graph['vertices'], key_u)
    if vertex is None:
        raise Exception("El vertice no existe")
    return vertex


def update_vertex_info(my_graph, key_u, new_info_u):
    """
    Actualiza la información del vertice con llave key_u
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        key_u (any): Llave del vertice que se desea actualizar
        new_info_u (any): La nueva informacion asociada al vertice
        
    Returns:
        digraph: El grafo con la nueva informacion asociada al vertice
    """
    vertex = mp.get(my_graph['vertices'], key_u)
    if vertex is not None:
        vx.set_value(vertex, new_info_u)
    return my_graph


def get_vertex_information(my_graph, key_u):
    """
    Retorna la informacion (value) asociada al vertice con llave key_u
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        key_u (any): Vertice del que se quiere la informacion
        
    Returns:
        any: La informacion asociada al vertice
    """
    vertex = mp.get(my_graph['vertices'], key_u)
    if vertex is None:
        raise Exception("El vertice no existe")
    return vx.get_value(vertex)


def get_edge(my_graph, key_u, key_v):
    """
    Retorna el arco que conecta al vertice key_u con el vertice key_v
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        key_u (any): Llave del vertice de inicio
        key_v (any): Llave del vertice destino
        
    Returns:
        edge: El arco que une los vertices key_u a key_v
    """
    vertex = mp.get(my_graph['vertices'], key_u)
    if vertex is None:
        raise Exception("El vertice u no existe")
    return vx.get_edge(vertex, key_v)


def remove_vertex(my_graph, key_u):
    """
    Remueve el vertice con llave key_u del grafo
    
    Args:
        my_graph (digraph): El grafo sobre el que se ejecuta la operacion
        key_u (any): Llave del vertice a eliminar
        
    Returns:
        digraph: El grafo sin el vertice
    """
    if not contains_vertex(my_graph, key_u):
        return my_graph
    
    # Contar los arcos salientes del vertice a eliminar
    vertex = mp.get(my_graph['vertices'], key_u)
    outgoing_edges = vx.degree(vertex)
    
    # Eliminar el vertice del grafo
    mp.remove(my_graph['vertices'], key_u)
    
    # Eliminar arcos entrantes desde otros vertices
    all_vertices = mp.key_set(my_graph['vertices'])
    incoming_edges = 0
    for i in range(lt.size(all_vertices)):
        other_key = lt.get_element(all_vertices, i)
        other_vertex = mp.get(my_graph['vertices'], other_key)
        edge = vx.get_edge(other_vertex, key_u)
        if edge is not None:
            # Eliminar el arco
            adjacents_map = v.get_adjacents(other_vertex)
            mp.remove(adjacents_map, key_u)
            incoming_edges += 1
    
    # Actualizar contador de arcos
    my_graph['num_edges'] -= (outgoing_edges + incoming_edges)
    
    return my_graph