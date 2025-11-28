

from DataStructures.Graph import dijsktra_structure as dijk_st
from DataStructures.Graph import digraph as g
from DataStructures.Graph import edge as e
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Stack import stack as st
from DataStructures.List import array_list as lt
import math


def dijkstra(my_graph, source):
    """
    Implementa el algoritmo de Dijkstra
    """
    aux_structure = dijk_st.new_dijsktra_structure(source, g.order(my_graph))
    
    mp.put(aux_structure['visited'], source, {
        'marked': False,
        'edge_from': None,
        'dist_to': 0
    })
    
    pq.insert(aux_structure['pq'], 0, source)
    
    while not pq.is_empty(aux_structure['pq']):
        min_vertex = pq.remove(aux_structure['pq'])
        
        if min_vertex is None:
            continue
        
        if not mp.contains(aux_structure['visited'], min_vertex):
            continue
            
        current_info = mp.get(aux_structure['visited'], min_vertex)
        
        if current_info['marked']:
            continue
        
        current_info['marked'] = True
        
        edges_list = g.edges_vertex(my_graph, min_vertex)
        
        for i in range(lt.size(edges_list)):
            edge_item = lt.get_element(edges_list, i)
            key_v = e.to(edge_item)
            weight = e.weight(edge_item)
            
            dist_u = current_info['dist_to']
            
            if not mp.contains(aux_structure['visited'], key_v):
                mp.put(aux_structure['visited'], key_v, {
                    'marked': False,
                    'edge_from': None,
                    'dist_to': math.inf
                })
            
            info_v = mp.get(aux_structure['visited'], key_v)
            dist_v = info_v['dist_to']
            
            if dist_u + weight < dist_v:
                info_v['dist_to'] = dist_u + weight
                info_v['edge_from'] = min_vertex
                
                if pq.contains(aux_structure['pq'], key_v):
                    pq.improve_priority(aux_structure['pq'], dist_u + weight, key_v)
                else:
                    pq.insert(aux_structure['pq'], dist_u + weight, key_v)
    
    return aux_structure


def dist_to(key_v, aux_structure):
    """
    Retorna el costo para llegar del vertice source al vertice key_v
    """
    if mp.contains(aux_structure['visited'], key_v):
        info = mp.get(aux_structure['visited'], key_v)
        return info['dist_to']
    return math.inf


def has_path_to(key_v, aux_structure):
    """
    Indica si hay camino entre source y key_v
    """
    if not mp.contains(aux_structure['visited'], key_v):
        return False
    
    info = mp.get(aux_structure['visited'], key_v)
    return info['dist_to'] < math.inf


def path_to(key_v, aux_structure):
    """
    Retorna el camino entre source y key_v en una pila
    """
    if not has_path_to(key_v, aux_structure):
        return None
    
    path = st.new_stack()
    
    current = key_v
    while current is not None:
        st.push(path, current)
        vertex_info = mp.get(aux_structure['visited'], current)
        if vertex_info is None:
            break
        current = vertex_info.get('edge_from')
    
    return path