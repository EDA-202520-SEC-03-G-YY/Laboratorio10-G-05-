from DataStructures.List import array_list as lt
#from DataStructures.List import single_linked_list as lt

def new_stack():
    return lt.new_list()

def push(my_stack, elements):
    return lt.add_last(my_stack, elements)

def pop(my_stack):
    return lt.remove_last(my_stack)

def is_empty(my_stack):
    return lt.is_empty(my_stack)

def top(my_stack):
    return lt.last_element(my_stack)

def size(my_stack):
    return lt.size(my_stack)
