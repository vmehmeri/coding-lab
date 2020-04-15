from abc import ABC, abstractmethod
from collections import OrderedDict, deque, Counter
from heapq import heappush, heappop
from queue import Queue
from datetime import datetime

class DataHolder(ABC):
    _HOW_MUCH_STUFF_I_CAN_HANDLE = 10

    def __init__(self):
        self.my_set = set()
        self.my_dict = {}
        self.my_list = []
        self.my_heap = []
        self.my_queue = Queue()
        self.my_deque = deque()
        self.my_odict = OrderedDict()
    
class DataManipulator(DataHolder):

    _internal_property = "secret! but not really"
    __hidden = "a little more hidden, but still not really"

    def add_to_set(self, item):
        self.my_set.add(item)
    
    def add_to_list(self, item):
        self.my_list.append(item)

    def add_to_heap(self, item):
        heappush(self.my_heap, item)

    def enqueue(self, item):
        self.my_queue.put(item)

    def add_to_beginning_of_deque(self, item):
        self.my_deque.appendleft(item)

    def add_to_end_of_deque(self, item):
        self.my_deque.append(item)

    def add_to_dict(self, key, value):
        self.my_dict[key] = value

    def add_to_ordered_dict(self, key, value):
        self.my_odict[key] = value

    def get_random_item_from_set(self):
        return self.my_set.pop()
    
    def get_from_dict(self, key):
        return self.my_dict.get(key)
    
    def get_from_ordered_dict(self, key):
        return self.my_odict.get(key)
    
    def dequeue(self):
        return self.my_queue.get()

    def get_from_end_of_deque(self, item):
        self.my_deque.pop()

    def get_from_beginning_of_deque(self, item):
        self.my_deque.popLeft()
    
    # A generator
    def generate_stuff(self):
        word_set = {'hi', 'hello', 'world', 'john', 'fox', 'yellow', 'big'}
        number_set = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 20, 30, 40, 50}
        tuple_set = { ('why', 'not'), ('what', 'now'), ('oh', 'dear') }
        big_set_of_stuff = word_set | number_set | tuple_set

        for stuff in big_set_of_stuff:
            yield stuff

    ## A decorator 
    def make_it_elegant(func):
        def wrapper(*args, **kwargs):
            rows = 4
            for i in range (0, rows):
                for j in range(0, i + 1):
                    print("*", end=' ')
                print("\r")
            func(*args, **kwargs)
            for i in range (rows+1, 0, -1):
                for j in range(0, i -1):
                    print("*", end=' ')
                print("\r")
            
        return wrapper

    @classmethod
    def build(cls):
        dm = cls()
        print("Here you go you lazy, you")
        return dm
    
    @staticmethod
    @make_it_elegant
    def print_info():
        print ("This class contains a lot of data structures")

if __name__ == '__main__':
    # Instantiate class
    dm = DataManipulator()

    # Add various items to various data structures
    # through instance methods
    dm.add_to_set(2)
    dm.add_to_dict('akey', 'avalue')
    dm.my_dict.setdefault('anotherkey', 'anothervalue')
    value_already_there = dm.my_dict.setdefault('akey','avalueincasenotthere')
    print("[1] Dictionary content: ", dm.my_dict)
    print("[1] Dictionary setdefault('akey','avalueincasenotthere'): ", value_already_there)
    
    dm.add_to_ordered_dict('one',1)
    dm.add_to_ordered_dict('two',2)
    dm.add_to_ordered_dict('three',3)
    some_other_dict = { 'four': 4 }
    merged_dict =  {**dm.my_odict, **some_other_dict}
    print("\n[2] Merged two dictionaries: ", merged_dict)
    
    atuple = (1,2)
    another_tuple = (0,5)
    dm.add_to_list(atuple)
    dm.add_to_list(another_tuple)
    # Sort by second number in the tuple
    sorted_list = sorted(dm.my_list, key=lambda x: x[1])
    print("[2] List with custom sorting function: ", sorted_list)
      
    ## Calling in a class method
    lazy_dm = DataManipulator.build()

    ## Calling in a static method
    print ("\n[3] Here's a static method that should print something with decorator and stuff")
    DataManipulator.print_info()
    
    # A static method can also be 
    # called from the instance...
    print ("\n[3] Calling the static method from an instance...")
    dm.print_info()

    ## To include a breakpoint here:
    # breakpoint()
    
    ## Printing internal, hidden properties
    ## Using "f" strings for formatting
    print(f"\n[4] Here's an internal property, that was prefixed with _: {dm._internal_property}")
    print(f"[4] Here's a hidden property using name mangling or whatever it is called: {dm._DataManipulator__hidden}")
   
    print("\n[5] Some generator action!")
    stuff_count = 0
    for stuff in lazy_dm.generate_stuff():
        print(f"[5]\tAdding {stuff} to queue for no reason")
        lazy_dm.enqueue(stuff)
        stuff_count += 1
        if (stuff_count >= DataManipulator._HOW_MUCH_STUFF_I_CAN_HANDLE):
            break
    
        
    alist = ['a', 'a', 'b', 'c', 'c', 'c', 'e']
    print("\n[6] Using counter on this list: ", alist)
    c = Counter(alist)
    print("[6]", c) 
    print("[6] Now initializing a Counter with Counter(a=7, b=2, c=1)")
    c2 = Counter(a=7, b=2, c=1)
    print("[6]", c2)
