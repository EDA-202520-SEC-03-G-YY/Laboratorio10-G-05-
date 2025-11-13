#Funciones existentes

def new_list():
    newlist = {
        'elements' : [],
        'size' : 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size>0:
        keyexist = False
        for keypos in range(0, size):
            info=my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


#Funciones primer release
def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def first_element(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    else:
        return my_list["elements"][0]

#Funciones release final

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False


def size(my_list):
    return my_list["size"]


def last_element(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    else:
        return my_list["elements"][-1]
    

def delete_element(my_list, pos):
    if not (0 <= pos < my_list["size"]):
        raise IndexError("list index out of range")
    else:
        my_list["elements"].pop(pos)
        my_list["size"] -= 1
        return my_list

def remove_first(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    else:
        first = my_list["elements"][0]
        my_list["elements"].pop(0)
        my_list["size"] -= 1
        return first

def remove_last(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    else:
        last = my_list["elements"][-1]
        my_list["elements"].pop(-1)
        my_list["size"] -= 1
        return last

def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1  
    return my_list

def change_info(my_list, pos, new_info):
    if not (0 <= pos < my_list["size"]):
        raise IndexError("list index out of range")
    else:
        my_list["elements"][pos] = new_info  
        return my_list
    

def exchange(my_list, pos_1, pos_2):
    if not ((0 <= pos_1 < my_list["size"]) and (0 <= pos_2 < my_list["size"])):
        raise IndexError("list index out of range")
    else:
        temp = my_list["elements"][pos_1]
        my_list["elements"][pos_1] = my_list["elements"][pos_2]
        my_list["elements"][pos_2] = temp
        return my_list
          

def sub_list(my_list, pos_i, num_elements):
    if not (0 <= pos_i < my_list["size"]):
        raise IndexError("list index out of range")
    else:
        n_lista = new_list()
        n_lista["elements"] = my_list["elements"][pos_i:pos_i + num_elements]
        n_lista["size"] = num_elements
        return n_lista
    
def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def selection_sort(my_list, sort_crit):
    
    if size(my_list)<=1:
        return my_list    
    else:
        for i in range(0,size(my_list)-1):
            minimo = my_list["elements"][i]
            posmin = i
            for j in range(i+1,size(my_list)):
                if sort_crit(my_list["elements"][j],minimo):
                    minimo = my_list["elements"][j]
                    posmin = j
            exchange(my_list,i,posmin)
        return my_list
    
def insertion_sort(my_list, sort_crit):
    if size(my_list)<=1:
        return my_list
    else:
        for i in range(1,size(my_list)):
            j = i
            while j>0 and sort_crit(get_element(my_list, j), get_element(my_list, j - 1)):
                exchange(my_list, j, j-1)
                j -= 1
        return my_list 
    
def shell_sort(my_list, sort_crit):
    tam = size(my_list)
    if tam<=1:
        return my_list
    else:
        inc = tam // 2
        while inc > 0:
            i = inc
            while i < tam:
                temp = get_element(my_list, i)
                j = i
                while j >= inc and sort_crit(temp, get_element(my_list, j-inc)):
                    change_info(my_list, j , get_element(my_list, j-inc))
                    j -= inc
                change_info(my_list, j, temp)
                i+= 1
            inc //= 2
        return my_list
    
def merge_sort(my_list, sort_crit):
	if size(my_list) <= 1:
		return my_list

	n = size(my_list)
 
	mid = n // 2
	left = sub_list(my_list, 0, mid)
	right = sub_list(my_list, mid, n - mid)
	left = merge_sort(left, sort_crit)
	right = merge_sort(right, sort_crit)
	merged = merge_sort_aux(left, right, sort_crit)
 
	for i in range(size(merged)):
		change_info(my_list, i, get_element(merged, i))
	my_list["size"] = size(merged)
	return my_list


def merge_sort_aux(left, right, sort_crit):
	i = 0
	j = 0
	result = new_list()
	while i < size(left) and j < size(right):
		a = get_element(left, i)
		b = get_element(right, j)
		if sort_crit(a, b) or (not sort_crit(b, a)):
			add_last(result, a)
			i += 1
		else:
			add_last(result, b)
			j += 1
	while i < size(left):
		add_last(result, get_element(left, i))
		i += 1
	while j < size(right):
		add_last(result, get_element(right, j))
		j += 1
	return result
    



def merge_sort_aux(left, right, sort_crit):
	i = 0
	j = 0
	result = new_list()
	while i < size(left) and j < size(right):
		a = get_element(left, i)
		b = get_element(right, j)
		if sort_crit(a, b) or (not sort_crit(b, a)):
			add_last(result, a)
			i += 1
		else:
			add_last(result, b)
			j += 1
	while i < size(left):
		add_last(result, get_element(left, i))
		i += 1
	while j < size(right):
		add_last(result, get_element(right, j))
		j += 1
	return result

def quick_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list
    else:
        _quick_sort_helper(my_list, 0, size(my_list) - 1, sort_crit)
        return my_list
def _quick_sort_helper(my_list, low, high, sort_crit):
    if low < high:
        pivot_index = _partition(my_list, low, high, sort_crit)
        _quick_sort_helper(my_list, low, pivot_index - 1, sort_crit)
        _quick_sort_helper(my_list, pivot_index + 1, high, sort_crit)       
def _partition(my_list, low, high, sort_crit):
    pivot = get_element(my_list, high)
    i = low - 1
    for j in range(low, high):
        if sort_crit(get_element(my_list, j), pivot) or (not sort_crit(pivot, get_element(my_list, j))):
            i += 1
            exchange(my_list, i, j)
    exchange(my_list, i + 1, high)
    return i + 1    
