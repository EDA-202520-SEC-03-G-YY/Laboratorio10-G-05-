import math, random
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as ll
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def default_compare(key, element):
    
    #Copio y pego desde la documentación
    if (key == me.get_key(element)):
        return 0
    elif (key > me.get_key(element)):
        return 1
    return -1

def rehash(my_map):
    
    #Creo una copia de la tabla anterior y su capacidad
    v_tabla = my_map["table"]
    v_capacidad = my_map["capacity"]
    
    #Busco el siguiente primo para el tamaño nuevo
    my_map["capacity"] = mf.next_prime(2 * v_capacidad)
    
    #Creo la nueva tabla y los nuevos espacios
    my_map["table"] = lt.new_list()
    for i in range(my_map["capacity"]):
        lt.add_last(my_map["table"], ll.new_list())

    #Inicializo de nuevo el tamaño y el current factor
    my_map["size"] = 0
    my_map["current_factor"] = 0
    
    #Recorro la tabla anterior y añado los elementos a la nueva en su nueva posición
    for i in range(lt.size(v_tabla)):
        dic = lt.get_element(v_tabla, i)
        for j in range(ll.size(dic)):
            actual = ll.get_element(dic, j)
            llave = me.get_key(actual)
            valor = me.get_value(actual)
            put(my_map, llave, valor)
    
    return my_map

def new_map(num_elements, load_factor, prime = 109345121):
    
    #Creo el diccionario principal del mapa con los parámetros y campos iniciales
    my_map = {
        "prime": prime,
        "capacity": mf.next_prime(int(num_elements / load_factor)),
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "table": lt.new_list(),
        "size": 0,
        "limit_factor": load_factor,
        "current_factor": 0
    }
    
    #Inicializo la tabla con una single linked list en cada posición
    for i in range(my_map["capacity"]):
        lt.add_last(my_map["table"], ll.new_list())
        
    return my_map

def put(my_map, key, value):
    
    #Verifico si la tabla ya alcanzó el current factor y hago rehash si es necesario
    if my_map["current_factor"] >= my_map["limit_factor"]:
        rehash(my_map)

    #Calculo el índice con la función de hash
    indice = mf.hash_value(my_map, key)
    dic = lt.get_element(my_map["table"], indice)

    #Busco si la llave ya existe en la lista
    encontrado = False
    pos = 0
    
    while pos < ll.size(dic) and not encontrado:
        actual = ll.get_element(dic, pos)
        if me.get_key(actual) == key:
            me.set_value(actual, value)
            ll.change_info(dic, pos, actual)
            encontrado = True
        pos += 1
    
    #Si no existe la llave, creo una nueva entrada y la agrego
    if not encontrado:
        n_entrada = me.new_map_entry(key, value)
        ll.add_last(dic, n_entrada)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    #Si el current factor se pasa del límite, vuelvo a hacer rehash
    if my_map["current_factor"] > my_map["limit_factor"]:
        rehash(my_map)

    return my_map

def contains(my_map, key):
    
    #Busco si una llave existe dentro del mapa
    indice = mf.hash_value(my_map, key)
    dic = lt.get_element(my_map["table"], indice)
    
    for i in range(ll.size(dic)):
        actual = ll.get_element(dic, i)
        if me.get_key(actual) == key:
            return True
        
    return False

def get(my_map, key):
    
    #Devuelvo el valor de una llave específica si existe
    indice = mf.hash_value(my_map, key)
    dic = lt.get_element(my_map["table"], indice)  

    for i in range(ll.size(dic)):
        actual = ll.get_element(dic, i)
        if me.get_key(actual) == key:
            return me.get_value(actual)
        
    #Si la llave no se encuentra, devuelvo None
    return None

def remove(my_map, key):
    
    #Elimino una llave y su valor si existen
    indice = mf.hash_value(my_map, key)
    dic = lt.get_element(my_map["table"], indice)

    for i in range(ll.size(dic)):
        actual = ll.get_element(dic, i)
        if me.get_key(actual) == key:
            valor = me.get_value(actual)
            ll.delete_element(dic, i)
            my_map["size"] -= 1
            my_map["current_factor"] = my_map["size"] / my_map["capacity"]
            return valor
        
    #Si no se encuentra, no elimino nada
    return None

def size(my_map):
    
    #Retorno el tamaño del mapa
    return my_map["size"]

def key_set(my_map):
    
    #Creo una lista con todas las llaves del mapa
    llaves = lt.new_list()
    
    for i in range(lt.size(my_map["table"])):
        dic = lt.get_element(my_map["table"], i)
        
        for j in range(ll.size(dic)):
            actual = ll.get_element(dic, j)
            lt.add_last(llaves, me.get_key(actual))
            
    return llaves


def value_set(my_map):
    
    #Creo una lista con todos los valores en el mapa
    valores = lt.new_list()
    
    for i in range(lt.size(my_map["table"])):
        dic = lt.get_element(my_map["table"], i)
        
        for j in range(ll.size(dic)):
            actual = ll.get_element(dic, j)
            lt.add_last(valores, me.get_value(actual))
            
    return valores


def is_empty(my_map):
    
    #Retorno True si el mapa está vacio, False de lo contrario
    return my_map["size"] == 0
