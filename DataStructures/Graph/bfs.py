from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import digraph as dig
from DataStructures.Graph import dfo_structure as dfo   
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.List import array_list as lt


def bfs(my_graph, source):
    if my_graph is None:
        return None

    vertex_source = mp.get(my_graph["vertices"], source)
    if vertex_source is None:
        raise Exception("El vertice source no existe")

    visited_map = {
        "marked": mp.new_map(dig.order(my_graph), 0.5),
        "edge_to": mp.new_map(dig.order(my_graph), 0.5),
        "queue": q.new_queue(),
        "source": source
    }

    bfs_vertex(my_graph, vertex_source, visited_map)
    return visited_map


def bfs_vertex(my_graph, vertex, visited_map):
    marked = visited_map["marked"]
    edge_to = visited_map["edge_to"]
    queue = visited_map["queue"]

    mp.put(marked, vertex["key"], True)
    q.enqueue(queue, vertex)

    while not q.is_empty(queue):
        current_vertex = q.dequeue(queue)
        if current_vertex is None:
            continue
        adjacents = current_vertex.get("adjacents", None)
        if adjacents is not None:
            for key_v in mp.key_set(adjacents):
                if not mp.contains(marked, key_v):
                    mp.put(marked, key_v, True)
                    mp.put(edge_to, key_v, current_vertex["key"])
                    neighbor_vertex = mp.get(my_graph["vertices"], key_v)
                    q.enqueue(queue, neighbor_vertex)


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
