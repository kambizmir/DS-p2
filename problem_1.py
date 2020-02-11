class QNode(object):

	def __init__(self, value, next = None, prev = None):
		self.next = next
		self.prev = prev
		self.value = value

class HitQ(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def add_to_head(self, key):
		node = QNode(key)
		if self.head:
		    node.next = self.head
		    self.head.prev = node
		    self.head  = node
		else:
		    self.head = node
		    self.tail = node
		return node

	def remove_from_tail(self):
		key = self.tail.value
		if self.tail:
			if self.tail.prev:
				self.tail.prev.next = None
			temp = self.tail.prev
			self.tail.prev = None
			self.tail = temp
		return key

	def move_to_head(self, node):
		if node != self.head:
			if node != self.tail:
				node.next.prev = node.prev
				nodex.prev.next = node.next
				node.next = self.head
				node.prev = None
				self.head.prev = node
				self.head = node
			else:
				node.prev.next = None
				self.tail = node.prev
				node.next = self.head
				node.prev = None
				self.head.prev = node
				self.head = node


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.store = {}
        self.capacity = capacity
        self.size = 0
        self.hitq = HitQ()


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.store:
        	value = self.store[key][0]
        	reference = self.store[key][1]
        	self.hitq.move_to_head(reference)
        	return value
        else:
        	return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 

        if key in self.store:
        	current_value = self.store[key][0]
        	reference = self.store[key][1]
        	self.store[key] = (value,reference)
        	self.hitq.move_to_head(reference)
        else:
        	if self.size == self.capacity:
        		key_to_remove = self.hitq.remove_from_tail()
        		del self.store[key_to_remove]        		
        		new_reference = self.hitq.add_to_head(key)
        		self.store[key] = (value, new_reference)
        	else:
        		new_reference = self.hitq.add_to_head(key)
        		self.store[key] = (value, new_reference)
        		self.size += 1

    
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print( our_cache.get(1)  )     # returns 1
print( our_cache.get(2)  )    # returns 2
print( our_cache.get(9)  )    # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print( our_cache.get(3)  )    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

