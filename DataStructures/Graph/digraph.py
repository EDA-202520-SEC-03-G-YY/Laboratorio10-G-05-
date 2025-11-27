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
    if my_graph is None:
        return None
    vertex_u = vx.new_vertex(key_u, info_u)
    mp.put(my_graph["vertices"], key_u, vertex_u)
    return my_graph


def _ensure_adj_map(vertex_u):
    if vertex_u.get("adjacents", None) is None:
        vertex_u["adjacents"] = mp.new_map(0, 0.5)
    return vertex_u["adjacents"]


def add_edge(my_graph, key_u, key_v, weight=1.0):
    if my_graph is None:
        return None

    vertex_u = mp.get(my_graph["vertices"], key_u)
    vertex_v = mp.get(my_graph["vertices"], key_v)

    if vertex_u is None or vertex_v is None:
        raise Exception("El vertice u no existe")

    adj_map = _ensure_adj_map(vertex_u)
    edge_uv = vx.get_edge(vertex_u, key_v)

    if edge_uv is None:
        new_e = ed.new_edge(key_v, weight)
        mp.put(adj_map, key_v, new_e)
        my_graph["num_edges"] += 1
    else:
        ed.set_weight(edge_uv, weight)

    return my_graph


def contains_vertex(my_graph, key_u):
    return mp.contains(my_graph["vertices"], key_u)


def order(my_graph):
    return mp.size(my_graph["vertices"])


def size(my_graph):
    return my_graph["num_edges"]


def degree(my_graph, key_u):
    vertex_u = mp.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice no existe")
    return vx.degree(vertex_u)


def adjacents(my_graph, key_u):
    vertex_u = mp.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice no existe")
    adj_map = _ensure_adj_map(vertex_u)
    return mp.key_set(adj_map)


def vertices(my_graph):
    return mp.key_set(my_graph["vertices"])


def edges_vertex(my_graph, key_u):
    vertex_u = mp.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice no existe")
    adj_map = _ensure_adj_map(vertex_u)
    return mp.value_set(adj_map)


def get_vertex(my_graph, key_u):
    return mp.get(my_graph["vertices"], key_u)


def update_vertex_info(my_graph, key_u, new_info_u):
    if my_graph is None:
        return None
    vertex_u = mp.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        return None
    vx.set_value(vertex_u, new_info_u)
    mp.put(my_graph["vertices"], key_u, vertex_u)
    return my_graph


def get_vertex_information(my_graph, key_u):
    vertex_u = mp.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice no existe")
    return vx.get_value(vertex_u)
