from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import digraph as dig
from DataStructures.Graph import dfo_structure as dfo
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.List import array_list as lt


def dfs(my_graph, source):
    if my_graph is None:
        return None

    if not dig.contains_vertex(my_graph, source):
        raise Exception("El vertice no existe")

    search = dfo.new_dfo_structure(dig.order(my_graph))

    search["edge_to"] = mp.new_map(dig.order(my_graph), 0.5)
    search["source"] = source

    dfs_vertex(my_graph, source, search)
    return search


def dfs_vertex(my_graph, vertex, visited_map):
    marked = visited_map["marked"]
    pre = visited_map["pre"]
    post = visited_map["post"]
    reversepost = visited_map["reversepost"]

    if mp.contains(marked, vertex):
        return visited_map

    mp.put(marked, vertex, True)
    q.enqueue(pre, vertex)

    adj = dig.adjacents(my_graph, vertex)
    for i in range(lt.size(adj)):
        w = lt.get_element(adj, i)

        if not mp.contains(marked, w):
            mp.put(visited_map["edge_to"], w, vertex)
            dfs_vertex(my_graph, w, visited_map)

    q.enqueue(post, vertex)
    st.push(reversepost, vertex)

    return visited_map


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
