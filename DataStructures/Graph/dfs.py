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

    dfs_vertex(my_graph, source, search)

    return search


def dfs_vertex(my_graph, vertex, search):
    marked = search["marked"]
    pre = search["pre"]
    post = search["post"]
    reversepost = search["reversepost"]

    if mp.contains(marked, vertex):
        return search

    mp.put(marked, vertex, True)
    q.enqueue(pre, vertex)

    adj = dig.adjacents(my_graph, vertex)
    for i in range(lt.size(adj)):
        w = lt.get_element(adj, i)
        if not mp.contains(marked, w):
            dfs_vertex(my_graph, w, search)

    q.enqueue(post, vertex)
    st.push(reversepost, vertex)

    return search


def has_path_to(key_v, visited_map):
    marked = visited_map["marked"]
    return mp.contains(marked, key_v)


def path_to(key_v, visited_map):
    if not has_path_to(key_v, visited_map):
        return None

    path = st.new_stack()
    st.push(path, key_v)
    return path