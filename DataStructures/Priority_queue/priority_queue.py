from DataStructures.List import array_list as al
from DataStructures.Priority_queue import pq_entry as pqe

def new_heap(is_min_pq = True):
    pq = {
        "elements": al.new_list(),
        "size":0,
        "cmp_function":None
    }
    inicial = pqe.new_pq_entry(None, None)
    
    al.add_first(pq["elements"], inicial)
    
    if is_min_pq:
        pq["cmp_function"] = default_compare_lower_value
    else:   
        pq["cmp_function"] = default_compare_higher_value
    return pq   

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False

def priority(my_heap, parent, child):
    return my_heap["cmp_function"](parent, child)

def exchange(my_heap, pos_i, pos_j):
    list = my_heap["elements"]
    al.exchange(list, pos_i, pos_j)

def size(my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    return (size(my_heap) == 0)

def swim(my_heap, pos):
    pos_1 = pos
    while pos_1 > 1:
        parent = al.get_element(my_heap["elements"], pos_1//2)
        child = al.get_element(my_heap["elements"], pos_1)
        if not priority(my_heap, parent, child):
            exchange(my_heap, pos, pos//2)
            pos_1 = pos_1//2
        else:
            pos_1 = 0

def sink(my_heap, pos):
    while (pos*2 +1) < size(my_heap):
        pos_child = pos*2
        parent = al.get_element(my_heap["elements"], pos)
        l_child = al.get_element(my_heap["elements"], pos_child)
        r_child = al.get_element(my_heap["elements"], pos_child+1)
        if priority(my_heap, l_child, r_child):
            mejor = l_child
        else:
            mejor = r_child
            pos_child += 1
        
        if not priority(my_heap, parent, mejor):
            exchange(my_heap, pos, pos_child)
            pos = pos_child
        else:
            pos = size(my_heap)
    

def insert(my_heap, priority, value):
    entry = pqe.new_pq_entry(priority, value)
    al.add_last(my_heap["elements"], entry)
    my_heap["size"] += 1
    swim(my_heap, size(my_heap))

def remove(my_heap):
    if is_empty(my_heap):
        return None
    raiz = al.get_element(my_heap["elements"], 1)
    exchange(my_heap, 1, size(my_heap))
    al.remove_last(my_heap["elements"])
    my_heap["size"] -= 1
    if size(my_heap) > 0:
        sink(my_heap, 1)
    return raiz["value"]

def get_first_priority(my_heap):
    if size(my_heap) == 0:
        return None
    else:
        return al.get_element(my_heap["elements"],1)["value"]

def is_present_value(my_heap, value):
    tam = size(my_heap) +1
    #tam = al.size(my_heap["elements"])
    for i in range(1, tam):
        entry = al.get_element(my_heap["elements"], i)
        if pqe.get_value(entry) == value:
            return i
    return -1

def contains(my_heap, value):
    present = is_present_value(my_heap, value)
    return present != -1 
    

def improve_priority(my_heap, priority, value):
    
    pos = is_present_value(my_heap, value)
    if pos != -1:
        entry = al.get_element(my_heap["elements"], pos)
        pqe.set_priority(entry, priority)
        swim(my_heap, pos)
    return my_heap
    