from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def is_available(table, pos):

   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

#prime: Número primo usado para calcular el hash. Inicializado con el valor de prime y en caso de no ser dado, con el valor por defecto de 109345121.

#capacity: Tamaño de la tabla. Inicializado con el siguiente primo mayor a num_elements/ load_factor.

#scale: Número entero aleatorio entre 1 y prime- 1.

#shift: Número entero aleatorio entre 0 y prime- 1.

#table: Lista de tamaño capacity con las entradas de la tabla de tipo array_list. Inicializado con una lista donde cada elemento es una map_entry con llave y valor None.

#current_factor: Factor de carga actual de la tabla. Inicializado en 0.

#limit_factor: Factor de carga límite de la tabla antes de hacer un rehash. Inicializado con el valor de load_factor.

#size: Número de elementos en la tabla. Inicializado en 0.


def new_map(num_elements, load_factor, prime=109345121):
   my_map = {
      "shift": 0,
      "size":0,
      "current_factor":0,
      "limit_factor":load_factor,
      "capacity": mf.next_prime(num_elements/load_factor),      
      "scale": 1,
      "prime": prime,
      "table":lt.new_list()
   }
   for i in range(my_map["capacity"]):
      entry = me.new_map_entry(None,None)
      lt.add_last(my_map["table"],entry)
   return my_map



def put(my_map, key, value):
   if my_map["current_factor"] >= my_map["limit_factor"]:
      rehash(my_map)
   hash_value = mf.hash_value(my_map, key)
   ocupied, slot = find_slot(my_map, key, hash_value)
   if ocupied:
      lt.get_element(my_map["table"], slot)["value"] = value
   else:
      lt.get_element(my_map["table"], slot)["key"] = key
      lt.get_element(my_map["table"], slot)["value"] = value
      my_map["size"] += 1
      my_map["current_factor"] = my_map["size"] / my_map["capacity"]
   return my_map

def contains(my_map,key):
   hash_value = mf.hash_value(my_map,key)
   found = False
   empty = False
   while not found and not empty:
      if is_available(my_map["table"],hash_value):
         empty = True
      elif default_compare(key, lt.get_element(my_map["table"],hash_value)) == 0:
         found = True
      hash_value = (hash_value +1)%  my_map["capacity"]
      
   return found

def get(my_map,key):
   hash_value = mf.hash_value(my_map,key)
   found = False
   empty = False
   value = None
   while not found and not empty:
      if is_available(my_map["table"],hash_value):
         empty = True
      elif default_compare(key, lt.get_element(my_map["table"],hash_value)) == 0:
         found = True
         value = lt.get_element(my_map["table"],hash_value)["value"]
      hash_value = (hash_value +1)%  my_map["capacity"]
      
   return value

def remove(my_map,key):
   hash_value = mf.hash_value(my_map,key)
   found = False
   empty = False
   value = None
   while not found and not empty:
      if is_available(my_map["table"],hash_value):
         empty = True
      elif default_compare(key, lt.get_element(my_map["table"],hash_value)) == 0:
         found = True
         value = lt.get_element(my_map["table"], hash_value)["value"]
         lt.get_element(my_map["table"], hash_value)["key"] = "__EMPTY__"
         lt.get_element(my_map["table"],hash_value)["value"] = None
         my_map["size"] -= 1
         my_map["current_factor"] = my_map["size"] / my_map["capacity"]
      hash_value = (hash_value+1) % my_map["capacity"]
   return my_map

def size(my_map):
   return my_map["size"]

def is_empty(my_map):
   for i in range(1,lt.size(my_map["table"])):
      entry = lt.get_element(my_map["table"],i)
      if me.get_key(entry) != None and me.get_value(entry) != "__EMPTY__":
         return False
   return True


def key_set(my_map):
   keys = lt.new_list()
   for i in range(1,lt.size(my_map["table"])):
      entry = lt.get_element(my_map["table"],i)
      if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":

         lt.add_last(keys,me.get_key(entry))
      
   return keys

def value_set(my_map):
   values = lt.new_list()
   for i in range(1,lt.size(my_map["table"])):
      entry = lt.get_element(my_map["table"],i)
      if me.get_key(entry) != None and me.get_key(entry) != "__EMPTY__":
         lt.add_last(values,me.get_value(entry))
      
   return values


def rehash(my_map):
    old_table = my_map["table"]
    old_capacity = my_map["capacity"]
    my_map["capacity"] = mf.next_prime(2 * old_capacity)
    my_map["table"] = lt.new_list()
    my_map["size"] = 0
    my_map["current_factor"] = 0
    for i in range(my_map["capacity"]):
        entry = me.new_map_entry(None, None)
        lt.add_last(my_map["table"], entry)
    for i in range(lt.size(old_table)):
        entry = lt.get_element(old_table, i)
        if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
            put(my_map, me.get_key(entry), me.get_value(entry))

    return my_map