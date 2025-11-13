from DataStructures.Tree import rbt_node
from DataStructures.List import single_linked_list as sl

def new_map():
    return {"root": None}

def is_red(nodo):
    if nodo is None:
        return False
    return rbt_node.is_red(nodo)

def size_tree(root):
    if root is None:
        return 0
    return root["size"]

def put(my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    
    if my_rbt["root"] is not None:
        my_rbt["root"]["color"] = rbt_node.BLACK
    return my_rbt

def insert_node(h, key, value):
    if h is None:
        return rbt_node.new_node(key, value, rbt_node.RED)
    
    comp = default_compare(key, h)
    
    if comp == 0:
        h["value"] = value
    elif comp == 1:
        h["right"] = insert_node(h["right"], key, value)
    else:
        h["left"] = insert_node(h["left"], key, value)
        
    if is_red(h.get("right")) and not is_red(h.get("left")):
        h = rotate_left(h)
    if is_red(h.get("left")) and is_red(h["left"].get("left")):
        h = rotate_right(h)
    if is_red(h.get("left")) and is_red(h.get("right")):
        flip_colors(h)
        
    h["size"] = 1 + size_tree(h.get("left")) + size_tree(h.get("right"))
    return h

def get(my_rbt, key):
    node = my_rbt.get("root", None)
    
    while node is not None:
        comp = default_compare(key, node)
        if comp == 0:
            return node["value"]
        elif comp == 1:
            node = node["right"]
        else:
            node = node["left"]
    return None

def contains(my_rbt, key):
    node = my_rbt.get("root", None)
    
    while node is not None:
        comp = default_compare(key, node)
        if comp == 0:
            return True
        elif comp == 1:
            node = node["right"]
        else:
            node = node["left"]
    return False

def size(my_rbt):
    return size_tree(my_rbt.get("root", None))

def is_empty(my_rbt):
    return my_rbt.get("root", None) is None

def key_set(my_rbt):
    lista = sl.new_list()
    key_set_tree(my_rbt.get("root", None), lista)
    return lista

def key_set_tree(root, key_list):
    if root is None:
        return key_list
    
    key_set_tree(root["left"], key_list)
    sl.add_last(key_list, root["key"])
    key_set_tree(root["right"], key_list)
    return key_list

def value_set(my_rbt):
    lista = sl.new_list()
    value_set_tree(my_rbt.get("root", None), lista)
    return lista

def value_set_tree(root, value_list):
    if root is None:
        return value_list
    
    value_set_tree(root["left"], value_list)
    sl.add_last(value_list, root["value"])
    value_set_tree(root["right"], value_list)
    return value_list

def get_min(my_rbt):
    node = get_min_node(my_rbt.get("root", None))
    
    if node is None:
        return None
    return node["key"]

def get_min_node(root):
    if root is None:
        return None
    
    cur = root
    while cur["left"] is not None:
        cur = cur["left"]
    return cur

def get_max(my_rbt):
    node = get_max_node(my_rbt.get("root", None))
    
    if node is None:
        return None
    return node["key"]

def get_max_node(root):
    if root is None:
        return None
    
    cur = root
    while cur["right"] is not None:
        cur = cur["right"]
    return cur

def height(my_rbt):
    return height_tree(my_rbt.get("root", None))

def height_tree(root):
    if root is None:
        return 0
    
    hl = height_tree(root["left"])
    hr = height_tree(root["right"])
    
    if hl > hr:
        return 1 + hl
    else:
        return 1 + hr

def keys(my_rbt, key_initial, key_final):
    lista = sl.new_list()
    keys_range(my_rbt.get("root", None), key_initial, key_final, lista)
    return lista

def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return list_key
    
    comp_min = default_compare(key_initial, root)
    comp_max = default_compare(key_final, root)
    
    if comp_min == -1:
        keys_range(root["left"], key_initial, key_final, list_key)
    if (comp_min == 0 or comp_min == -1) and (comp_max == 0 or comp_max == 1):
        sl.add_last(list_key, root["key"])
    if comp_max == 1:
        keys_range(root["right"], key_initial, key_final, list_key)
        
    return list_key

def values(my_rbt, key_initial, key_final):
    lista = sl.new_list()
    values_range(my_rbt.get("root", None), key_initial, key_final, lista)
    return lista

def values_range(root, key_initial, key_final, value_list):
    if root is None:
        return value_list
    
    comp_min = default_compare(key_initial, root)
    comp_max = default_compare(key_final, root)
    
    if comp_min == -1:
        values_range(root["left"], key_initial, key_final, value_list)
    if (comp_min == 0 or comp_min == -1) and (comp_max == 0 or comp_max == 1):
        sl.add_last(value_list, root["value"])
    if comp_max == 1:
        values_range(root["right"], key_initial, key_final, value_list)
    return value_list

def rotate_left(h):
    x = h["right"]
    h["right"] = x["left"]
    x["left"] = h
    x["color"] = h["color"]
    h["color"] = rbt_node.RED
    h["size"] = 1 + size_tree(h.get("left")) + size_tree(h.get("right"))
    x["size"] = 1 + size_tree(x.get("left")) + size_tree(x.get("right"))
    return x

def rotate_right(h):
    x = h["left"]
    h["left"] = x["right"]
    x["right"] = h
    x["color"] = h["color"]
    h["color"] = rbt_node.RED
    h["size"] = 1 + size_tree(h.get("left")) + size_tree(h.get("right"))
    x["size"] = 1 + size_tree(x.get("left")) + size_tree(x.get("right"))
    return x

def flip_node_color(node_rbt):
    if rbt_node.is_red(node_rbt):
        node_rbt["color"] = rbt_node.BLACK
    else:
        node_rbt["color"] = rbt_node.RED
    return node_rbt

def flip_colors(node_rbt):
    if node_rbt is None or node_rbt.get("left") is None or node_rbt.get("right") is None:
        return None
    
    flip_node_color(node_rbt)
    flip_node_color(node_rbt["left"])
    flip_node_color(node_rbt["right"])
    return node_rbt

def default_compare(key, element):
    if key == rbt_node.get_key(element):
        return 0
    elif key > rbt_node.get_key(element):
        return 1
    return -1
