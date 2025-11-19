from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as vx
from DataStructures.Graph import edge as ed

def new_graph(order):
    grafo = {
        "vertices": mp.new_map(order, 0.5),
        "num_edges": 0
    }
    return grafo

def insert_vertex(my_graph, key_u, info_u):
    mp.put(my_graph["vertices"], key_u, (info_u, mp.new_map(5, 0.5)))
    return my_graph

def add_edge(my_graph, key_u, key_v, weight=1.0):
    if my_graph is None:
        return None
    vertex_u = mp.get(my_graph["vertices"], key_u)
    vertex_v = mp.get(my_graph["vertices"], key_v)

    if vertex_u is None or vertex_v is None:
        raise Exception("El vertice u no existe")
    else:
        if vx.get_edge(vertex_u, key_v) is not None:
            ed.set_weight(vx.get_edge(vertex_u, key_v), weight)
        else:
            edge_v = ed.new_edge(key_v, weight)
            vx.add_edge(vertex_u, edge_v)
            my_graph["num_edges"] += 1
        
    return my_graph

def contains_vertex(my_graph, key_u):
    return mp.contains(my_graph["vertices"], key_u)

def order(my_graph):
    return mp.size(my_graph["vertices"])

def size(my_graph):
    return my_graph["num_edges"]

def degree(my_graph, key_u):
    pass

def adjacents(my_graph, key_u):
    pass

def vertices(my_graph):
    pass

def edges_vertex(my_graph, key_u):
    pass

def get_vertex(my_graph, key_u):
    pass

def update_vertex_info(my_graph, key_u, new_info_u):
    pass

def get_vertex_information(my_graph, key_u):
    pass

