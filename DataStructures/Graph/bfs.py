from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import digraph as dig
from DataStructures.Graph import dfo_structure as dfo
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.List import array_list as lt


def bfs(my_graph, source):
    pass


def bfs_vertex(my_graph, vertex, visited_map):
    pass


def has_path_to(key_v, visited_map):
    marked = visited_map["marked"]
    return mp.contains(marked, key_v)


def path_to(key_v, visited_map):
    if not has_path_to(key_v, visited_map):
        return None

    edge_to = visited_map["edge_to"]
    source = visited_map["source"]

    path = st.new_stack()
    v = key_v

    while True:
        st.push(path, v)
        if v == source or not mp.contains(edge_to, v):
            break
        v = mp.get(edge_to, v)

    return path
