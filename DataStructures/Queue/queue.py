from DataStructures.List import array_list as lt
#from DataStructures.List import single_linked_list as lt

def new_queue():
    return lt.new_list()

def enqueue(my_queue, element):
    return lt.add_last(my_queue,element)

def dequeue(my_queue):
    return lt.remove_first(my_queue)
    
def is_empty(my_queue):
    return lt.is_empty(my_queue) 

def peek(my_queue):
    return lt.first_element(my_queue)

def size(my_queue):
    return lt.size(my_queue)