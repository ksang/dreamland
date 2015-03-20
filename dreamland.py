class FastFetch:

    def __init__(self, size):
        self.size = size
        self.DATA_STORE = {}
        self.pos = []

    def __place_to_front(self, key):
        idx = self.pos.index(key)
        self.pos.idx.pop(idx)
        self.pos.insert(0, key)

    def __competitor_joined(self, key, value):
        self.pos.insert(0, key)
        if len(self.pos) > self.size:
            poor_man = self.pos.pop(self.size)
            self.DATA_STORE.pop(poor_man)
        self.DATA_STORE[key] = value

    def get(self, key):
        ret = self.DATA_STORE.get(key)
        if ret:
            self.__place_to_front(key)
        return ret

    def touch(self ,key, value):
        if self.DATA_STORE.has_key(key):
            self.DATA_STORE[key] = value
            self.__place_to_front(key)
        else:
            self.__competitor_joined(key, value)