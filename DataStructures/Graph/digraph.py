from DataStructures.Map import map_linear_probing as mp

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
    
    pass

def contains_vertex(my_graph, key_u):
    pass

def order(my_graph):
    return mp.size(my_graph["vertices"])

def size(my_graph):
    return my_graph["num_edges"]