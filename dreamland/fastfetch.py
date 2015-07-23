class FastFetch:

    def __init__(self, size, gate=0):
        self.size = size
        self.gate = gate
        self.DATA_STORE = {}
        self.pos = []

    def __shrink(self, distance):
        for i in range(0, distance):
            dust = self.pos.pop(0)
            self.DATA_STORE.pop(dust)

    def __place_to_end(self, key):
        d = len(self.pos) - 1 - self.gate
        if d < 0:
            return
        try:
            i = self.pos.index(key, 0, d)
        except ValueError:
            return
        else:
            self.pos.pop(i)
            self.pos.append(key)

    def __competitor_joined(self, key, value):
        self.pos.append(key)
        if len(self.pos) > self.size:
            poor_man = self.pos.pop(0)
            self.DATA_STORE.pop(poor_man)
        self.DATA_STORE[key] = value

    def inspect(self, idx):
        if idx < 0 or idx > len(self.pos):
            return (None, None)
        else:
            key = self.pos[len(self.pos) - idx]
            return (key, self.DATA_STORE.get(key))

    def get(self, key):
        ret = self.DATA_STORE.get(key)
        if ret is not None:
            self.__place_to_end(key)
        return ret

    def touch(self ,key, value):
        if self.DATA_STORE.has_key(key):
            self.DATA_STORE[key] = value
            self.__place_to_end(key)
        else:
            self.__competitor_joined(key, value)

    def vitalize(self, reserv_count=None):
        if reserv_count is None:
            reserv_count = self.gate
        d = len(self.pos) - reserv_count
        if d < 0:
            return
        self.__shrink(d)