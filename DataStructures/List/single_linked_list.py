def new_list():
    newlist={
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos +=1
    return node["info"]


def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"])==0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    return count


def add_first(my_list, element):
    size = my_list["size"]
    N_node = {"info": element, "next": None}
    if size == 0:
        my_list["first"] = N_node
        my_list["last"] = N_node
        my_list["size"] += 1
    else:
        N_node["next"] = my_list["first"]
        my_list["first"] = N_node 
        my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    N_node = {"info": element, "next": None}
    size = my_list["size"]
    if size == 0:
        my_list["first"] = N_node
        my_list["last"] = N_node
        my_list["size"] += 1
    else:
       my_list["last"]["next"] = N_node
       my_list["last"] = N_node
       my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]


def is_empty(my_list):
    list = my_list
    if my_list["size"] == 0:
        return True
    else:
        return False
    
def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        first = my_list["first"]["info"]
    return first

def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        first = my_list["last"]["info"]
    return first

def delete_element(my_list,pos):
    searchpos = 0
    node = my_list["first"]
    if not(0 <= pos < size(my_list)):
        raise Exception('IndexError: list index out of range')
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        my_list["last"] = None
    else:
        while searchpos < pos - 1:
            node = node["next"]
            searchpos +=1  
        del_node = node["next"]
        node["next"] = del_node["next"]
        
    my_list["size"] -=1
    return my_list

def remove_first(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        deleted_element = my_list["first"]
        info_element_d = deleted_element["info"]
        my_list["first"] = my_list["first"]["next"]
        
    
        
    my_list["size"] -=1
    return info_element_d


def remove_last(my_list):
    
    current = my_list["first"]    
    
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    if my_list["size"] == 1:
        info_element_d = current["info"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = 0
        return info_element_d
    while current["next"] is not my_list["last"]:
        current = current["next"]

    info_element_d = my_list["last"]["info"]

    current["next"] = None
    my_list["last"] = current
    my_list["size"] -= 1    
    
    return info_element_d       

def insert_element(my_list, element, pos):
    N_node = {"info": element, "next":None}
    spos = 0
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    if my_list["size"] ==  0:
        my_list["element"] = element
    if pos == 0:
        N_node["next"] = my_list["first"]
        my_list["first"] = N_node
        my_list["size"] += 1
        return my_list
    current = my_list["first"]
    while spos < pos -1:
        current = current["next"]
        i+= 1
    N_node["next"] = current["next"]
    current["next"] = N_node
    my_list["size"] += 1
    return my_list
    
    
    
def change_info(my_list, pos, new_info):
    size = my_list["size"]
    current = my_list["first"]
    spos = 0
    if pos < 0 or pos > my_list["size"]:
        raise Exception('IndexError: list index out of range')
    
    else:
        while spos < pos:
            current = current["next"] 
            spos += 1
            
            
    current["info"] = new_info
    
    return my_list


def exchange(my_list, pos_1, pos_2):
    
    if pos_1 < 0 or pos_1 > size(my_list):
        raise Exception('IndexError: list index out of range')
    if pos_2 < 0 or pos_2 > size(my_list):
        raise Exception('IndexError: list index out of range')
    if pos_1 == pos_2:
       return my_list
    spos = 0
    current1 = my_list["first"]
    current2 = my_list["first"]
    for spos in range(pos_1):
          current1 = current1["next"]
          
    for spos in range(pos_2):
        current2 = current2["next"]
        
    temp = current1["info"]
    current1["info"]= current2["info"]
    current2["info"] = temp

    return my_list
    
    
    
def sub_list(my_list, pos, num_elements):
    
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    if num_elements < 0:
        raise Exception('IndexError: list index out of range')

    
    lista = new_list()

    
    current = my_list["first"]
    for _ in range(pos):
        current = current["next"]

    count = 0
    while current is not None and count < num_elements:
        add_last(lista, current["info"])
        current = current["next"]
        count += 1

    return lista

def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def selection_sort(my_list, sort_crit):
    
    if size(my_list)<=1:
        return my_list    
    else:
        head = my_list["first"] 
        while head:
            minimo = head 
            sig = head["next"] 
            
            while sig:
                if sort_crit(sig["info"], minimo["info"]):
                    minimo = sig 
                sig = sig["next"] 
            
            head["info"], minimo["info"] = minimo["info"], head["info"] 
            head = head["next"]   
        return my_list
    
def insertion_sort(my_list, sort_crit):
    
    if size(my_list) <= 1:
        return my_list
    else:
        for i in range(1, size(my_list)):
            j = i
            while j > 0 and sort_crit(get_element(my_list, j), get_element(my_list, j - 1)):
                exchange(my_list, j, j - 1)
                j -= 1
        return my_list
        
    
def shell_sort(my_list, sort_crit):
    n = size(my_list)
    if n <= 1:
        return my_list

    gap = n // 2
    while gap > 0:
        
        i = gap
        while i < n:
            temp = get_element(my_list, i)
            j = i
           
            while j >= gap and sort_crit(temp, get_element(my_list, j-gap)):
                change_info(my_list, j, get_element(my_list, j-gap))
                j -= gap
            change_info(my_list, j, temp)
            i += 1
        gap //= 2

    return my_list


def merge_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list

    mid = size(my_list) // 2
    left_half = sub_list(my_list, 0, mid)
    right_half = sub_list(my_list, mid, size(my_list) - mid)

    left_sorted = merge_sort(left_half, sort_crit)
    right_sorted = merge_sort(right_half, sort_crit)

    return merge(left_sorted, right_sorted, sort_crit)  
def merge(left, right, sort_crit):  
    n_lista = new_list()
    left_index = 0
    right_index = 0

    while left_index < size(left) and right_index < size(right):
        if sort_crit(get_element(left, left_index), get_element(right, right_index)):
            add_last(n_lista, get_element(left, left_index))
            left_index += 1
        else:
            add_last(n_lista, get_element(right, right_index))
            right_index += 1

    while left_index < size(left):
        add_last(n_lista, get_element(left, left_index))
        left_index += 1

    while right_index < size(right):
        add_last(n_lista, get_element(right, right_index))
        right_index += 1

    return n_lista

def quick_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list

    pivot = get_element(my_list, 0)
    less = new_list()
    equal = new_list()
    greater = new_list()

    for i in range(size(my_list)):
        element = get_element(my_list, i)
        if element == pivot:
            add_last(equal, element)
        elif sort_crit(element, pivot):
            add_last(less, element)
        else:
            add_last(greater, element)

    sorted_less = quick_sort(less, sort_crit)
    sorted_greater = quick_sort(greater, sort_crit)

    result = new_list()
    
    for i in range(size(sorted_less)):
        add_last(result, get_element(sorted_less, i))
    
    for i in range(size(equal)):
        add_last(result, get_element(equal, i))
    
    for i in range(size(sorted_greater)):
        add_last(result, get_element(sorted_greater, i))
    
    return result
