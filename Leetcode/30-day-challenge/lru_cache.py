# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3309/

"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        val = self.hashmap.pop(key) 
        self.hashmap[key] = val   # rewrite value at the "top"
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1  
            else:  # self.dic is full
                self.hashmap.popitem(last=False) 
        self.hashmap[key] = value

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
cache.get(1)       # returns -1 (not found)
cache.get(3)       # returns 3
cache.get(4)       # returns 4