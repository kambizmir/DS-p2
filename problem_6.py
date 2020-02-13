class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

#######################

def union_with_hash(llist_1, llist_2):
    # Your Solution Here
    union_hash = {}
    p1 = llist_1.head
    while p1:
    	union_hash[p1.value] = p1.value
    	p1 = p1.next
    p2 = llist_2.head
    while p2:
    	union_hash[p2.value] = p2.value
    	p2 = p2.next

    result = LinkedList()
    for x in union_hash:
    	result.append(x)
    return result

def intersection_with_hash(llist_1, llist_2):
    # Your Solution Here
    list_hash_1 = {}
    list_hash_2 = {}
    p1 = llist_1.head
    while p1:
    	list_hash_1[p1.value] = p1.value
    	p1 = p1.next

    p2 = llist_2.head
    while p2:
    	list_hash_2[p2.value] = p2.value
    	p2 = p2.next

    result = LinkedList()
    for x in list_hash_1:
    	if x in list_hash_2:
    		result.append(x)
    return result

#####################    		

def union_repeat_allowed(llist_1, llist_2):
    # Your Solution Here
    result = LinkedList()
    p1 = llist_1.head
    while p1:
    	result.append(p1.value)
    	p1 = p1.next
    p2 = llist_2.head
    while p2:
    	result.append(p2.value)
    	p2 = p2.next    
    return result

def intersection_repeat_allowed(llist_1, llist_2):
    # Your Solution Here
    result = LinkedList()
    p1 = llist_1.head
    while p1:
    	p2 = llist_2.head
    	while p2:
    		if p1.value == p2.value:
    			result.append(p1.value)
    		p2 = p2.next
    	p1 = p1.next	
    return result

#####################    


def union_repeat_not_allowed(llist_1, llist_2):
    # Your Solution Here
    result = LinkedList()
    p1 = llist_1.head
    while p1:
    	result.append(p1.value)
    	p1 = p1.next

    p2 = llist_2.head
    while p2:
    	r = result.head
    	while r:
    		if p2.value == r.value:
    		    break
    		r = r.next
    	if r == None:
    		result.append(p2.value)
    	p2 = p2.next
    return result


def intersection_repeat_not_allowed(llist_1, llist_2):
    # Your Solution Here
    result = LinkedList()
    p1 = llist_1.head
    while p1:
    	p2 = llist_2.head
    	while p2:
    		if p1.value == p2.value:
    			result.append(p1.value)
    			break
    		p2 = p2.next
    	p1 = p1.next

    return result

##################    

# Test case 1
print("Test case 1:")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21] 
element_2 = [6,32,4,9,6,1,11,21,1] 

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("union/intersection using hash")
print (union_with_hash(linked_list_1,linked_list_2))
print (intersection_with_hash(linked_list_1,linked_list_2))

print("union/intersection not using hash, repeat allowed")
print (union_repeat_allowed(linked_list_1,linked_list_2))
print (intersection_repeat_allowed(linked_list_1,linked_list_2))

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [3,2,4,35,6,65,21]
element_2 = [6,32,4,9,11,21,1]
for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print("union/intersection not using hash, repeat not allowed")
print (union_repeat_not_allowed(linked_list_1,linked_list_2))
print (intersection_repeat_not_allowed(linked_list_1,linked_list_2))

# Test case 2
print("\nTest case 2:")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union/intersection using hash:")
print (union_with_hash(linked_list_3,linked_list_4))
print (intersection_with_hash(linked_list_3,linked_list_4))

print("union/intersection not using hash, repeat allowed:")
print (union_repeat_allowed(linked_list_3,linked_list_4))
print (intersection_repeat_allowed(linked_list_3,linked_list_4))

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,23]
element_2 = [1,7,8,9,11,21]
for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print("union/intersection not using hash, repeat not allowed")
print (union_repeat_not_allowed(linked_list_3,linked_list_4))
print (intersection_repeat_not_allowed(linked_list_3,linked_list_4))
