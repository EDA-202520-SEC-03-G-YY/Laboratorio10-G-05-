from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import digraph as dig
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.List import array_list as lt


def dfs(my_graph, source):
    if my_graph is None:
        return None

    if not dig.contains_vertex(my_graph, source):
        raise Exception("El vertice no existe")

  
    visited_map = mp.new_map(dig.order(my_graph), 0.5)
    

    mp.put(visited_map, source, {
        'edge_from': None,
        'visited': True
    })

    dfs_vertex(my_graph, source, visited_map)

    return visited_map


def dfs_vertex(my_graph, vertex, visited_map):
    
    adj = dig.adjacents(my_graph, vertex)
    
    for i in range(lt.size(adj)):
        w = lt.get_element(adj, i)
        if not mp.contains(visited_map, w):
            
            mp.put(visited_map, w, {
                'edge_from': vertex,
                'visited': True
            })
            dfs_vertex(my_graph, w, visited_map)

    return visited_map


def has_path_to(key_v, visited_map):
    return mp.contains(visited_map, key_v)


def path_to(key_v, visited_map):
    if not has_path_to(key_v, visited_map):
        return None

    path = st.new_stack()
    
    current = key_v
    while current is not None:
        st.push(path, current)
        vertex_info = mp.get(visited_map, current)
        current = vertex_info['edge_from']
    
    return path