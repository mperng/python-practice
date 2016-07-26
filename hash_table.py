import types

class hashTable(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hashval = _hashfunction(key, len(self.slots))
        if not self.slots[hashval]:
            self.slots[hashval] = key
            self.data[hashval] = value
        else:
            if self.slots[hashval] == key:
                self.data[hashval] = value
            else:
                nextslot = self.rehash(hashval, len(self.slots))
                while self.slots[nextslot] and self.slots[nextslot] != key:
                    nextslot = self.rehash(hashval, len(self.slots))
                if not self.slots[nextslot]:
                    self.slots[nextslot] = key
                self.data[nextslot] = value

   def get(self,key):
       startslot = self.hashfunction(key,len(self.slots))
       stop = False
       found = False
       pos = startslot
       while self.slots[pos] != None and not found and not stop:
           found = (self.slots[pos] == key)
           if found:
               data = self.data[position]
           else:
               position=self.rehash(position,len(self.slots))
               stop = (position == startslot)

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def _hashfunction(self, key, size):
        if isinstance(key, types.IntType):
            return key % size
        elif isinstance(key, types.StringTypes):
            return sum(map(ord, key)) % size

    def _rehash(self, oldhash):
        return (oldhash + 1) % size

h = hashTable()
test_vals = [54, 26, 93, 17, 77, 31]
for val in test_vals:
    print h._hash_function(val)
