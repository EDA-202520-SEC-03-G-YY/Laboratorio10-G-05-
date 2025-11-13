from DataStructures.Tree import bst_node
from DataStructures.List import single_linked_list as sl

def new_map():
    my_bst = {"root" : None}
    return my_bst

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst['root'], key, value)
    return my_bst

def insert_node(root, key, value):
    if root is None:
        return bst_node.new_node(key, value)
    
    comp = default_compare(key, root)
    
    if comp == 0:
        root['value'] = value
    elif comp == 1:
        root['right'] = insert_node(root['right'], key, value)
    else:
        root['left'] = insert_node(root['left'], key, value)
    
    if root["left"] is None:
        size_left = 0
    else:
        size_left = root["left"]["size"]
        
    if root["right"] is None:
        size_right = 0
    else:
        size_right = root["right"]["size"]
    root["size"] = 1 + size_right + size_left
    
    return root

def get(my_bst, key):
    nodo = get_node(my_bst["root"], key)
    if nodo is None:
        return None
    return nodo["value"]

def get_node(root, key):
    if root is None:
        return None
    
    comp = default_compare(key,root)
    
    if comp == 0:
        return root
    elif comp == 1:
        return get_node(root["right"], key)
    else:
        return get_node(root["left"], key)
            
def size(my_bst):
    return size_tree(my_bst['root'])

def size_tree(root):
    if root == None:
        return 0
    return root["size"]


def default_compare(key, element):
   if key == bst_node.get_key(element):
      return 0
   elif key > bst_node.get_key(element):
      return 1
   return -1

def contains(my_bst, key):
    node = get_node(my_bst['root'], key)
    
    if node is None:
        return False
    return True

def is_empty(my_bst):
    if my_bst['root'] is None:
        return True
    return False

def key_set(my_bst):
    lista = sl.new_list()
    key_set_tree(my_bst['root'], lista)
    
    if lista is None:
        return None
    return lista

def key_set_tree(root, lista):
    if root is None:
        return None
    
    key_set_tree(root['left'], lista)
    sl.add_last(lista, root['key'])
    key_set_tree(root['right'], lista)
    return lista

def value_set(my_bst):
    lista = sl.new_list()
    value_set_tree(my_bst['root'], lista)
    
    if lista is None:
        return None
    return lista

def value_set_tree(root, lista):
    if root is None:
        return None
    
    value_set_tree(root['left'], lista)
    sl.add_last(lista, root['value'])
    value_set_tree(root['right'], lista)
    return lista

def get_min(my_bst):
    node = get_min_node(my_bst['root'])
    
    if node is None:
        return None
    return node['key']

def get_min_node(root):
    if root is None:
        return None
    
    current = root
    while current['left'] is not None:
        current = current['left']
    return current

def get_max(my_bst):
    node = get_max_node(my_bst['root'])
    
    if node is None:
        return None
    return node['key']

def get_max_node(root):
    if root is None:
        return None
    
    current = root
    while current['right'] is not None:
        current = current['right']
    return current

def delete_min(my_bst):
    my_bst['root'] = delete_min_tree(my_bst['root'])
    
    if my_bst['root'] is None:
        return None
    return my_bst

def delete_min_tree(root):
    if root is None:
        return None
    
    if root['left'] is None:
        return root['right']
    
    root['left'] = delete_min_tree(root['left'])
    
    if root['left'] is None:
        left_size = 0
    else:
        left_size = root['left']['size']
        
    if root['right'] is None:
        right_size = 0
    else:
        right_size = root['right']['size']
        
    root['size'] = 1 + left_size + right_size
    return root

def delete_max(my_bst):
    my_bst['root'] = delete_max_tree(my_bst['root'])
    
    if my_bst['root'] is None:
        return None
    return my_bst

def delete_max_tree(root):
    if root is None:
        return None
    
    if root['right'] is None:
        return root['left']
    
    root['right'] = delete_max_tree(root['right'])
    
    if root['left'] is None:
        left_size = 0
    else:
        left_size = root['left']['size']
        
    if root['right'] is None:
        right_size = 0
    else:
        right_size = root['right']['size']
        
    root['size'] = 1 + left_size + right_size
    return root

def height(my_bst):
    h = height_tree(my_bst['root'])
    return h

def height_tree(root):
    if root is None:
        return 0
    hl = height_tree(root['left'])
    hr = height_tree(root['right'])
    
    if hl > hr:
        return 1 + hl
    else:
        return 1 + hr

def keys(my_bst, key_initial, key_final):
    lista = sl.new_list()
    keys_range(my_bst['root'], key_initial, key_final, lista)
    
    if lista is None:
        return None
    return lista

def keys_range(root, key_initial, key_final, lista):
    if root is None:
        return None
    
    comp_min = default_compare(key_initial, root)
    comp_max = default_compare(key_final, root)
    
    if comp_min == -1:
        keys_range(root['left'], key_initial, key_final, lista)
    if (comp_min == 0 or comp_min == -1) and (comp_max == 0 or comp_max == 1):
        sl.add_last(lista, root['key'])
    if comp_max == 1:
        keys_range(root['right'], key_initial, key_final, lista)
    
    return lista

def values(my_bst, key_initial, key_final):
    lista = sl.new_list()
    values_range(my_bst['root'], key_initial, key_final, lista)
    
    if lista is None:
        return None
    return lista

def values_range(root, key_initial, key_final, lista):
    if root is None:
        return None
    
    comp_min = default_compare(key_initial, root)
    comp_max = default_compare(key_final, root)
    
    if comp_min == -1:
        values_range(root['left'], key_initial, key_final, lista)
    if (comp_min == 0 or comp_min == -1) and (comp_max == 0 or comp_max == 1):
        sl.add_last(lista, root['value'])
    if comp_max == 1:
        values_range(root['right'], key_initial, key_final, lista)
        
    return lista