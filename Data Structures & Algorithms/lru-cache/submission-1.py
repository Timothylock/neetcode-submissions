class LRUCache:

    def __init__(self, capacity: int):
        # oldest...newest
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            self.cache.popitem(False)

        self.cache[key] = value
        self.cache.move_to_end(key)


        
