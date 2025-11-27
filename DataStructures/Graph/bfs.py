from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import digraph as dig
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.List import array_list as lt


def bfs(my_graph, source):
    if my_graph is None:
        return None

    if not dig.contains_vertex(my_graph, source):
        raise Exception("El vertice source no existe")

    visited_map = mp.new_map(dig.order(my_graph), 0.5)
    
    mp.put(visited_map, source, {
        "edge_from": None,
        "visited": True
    })

    bfs_vertex(my_graph, source, visited_map)
    return visited_map


def bfs_vertex(my_graph, source, visited_map):
    queue = q.new_queue()
    q.enqueue(queue, source)

    while not q.is_empty(queue):
        current_key = q.dequeue(queue)
        if current_key is None:
            continue
        
        adjacents_list = dig.adjacents(my_graph, current_key)
        
        for i in range(lt.size(adjacents_list)):
            key_v = lt.get_element(adjacents_list, i)
            
            if not mp.contains(visited_map, key_v):
                mp.put(visited_map, key_v, {
                    "edge_from": current_key,
                    "visited": True
                })
                q.enqueue(queue, key_v)
    
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
        if vertex_info is None:
            break
        current = vertex_info.get("edge_from")

    return path