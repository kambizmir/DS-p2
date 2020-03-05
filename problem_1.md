To implement LRU, we need to maintain a queue which keeps track of the keys that have been used most recently.
We call this queue as HitQ.
For each key we store the value along with a reference to its location in HitQ.
The HitQ is implemented as a doubly linked list in which we can add an item to the head, remove an item from the tail 
and  move an item in HitQ to the head in order to increase its priority. All the operations of the HitQ are of time complexity of O(1).
"get" operation retrieves the value if exists and also moves its reference to the head of the HitQ. "set" operation 
moves the reference to head if it already exists, otherwise creates a new reference and adds it to the head of HitQ.
Also if the number of the items exceeds the capacity, the item at the end of the HitQ will be removed. All the operations 
are using hash and linked list and are of time comlexity of O(1).
The space complexity is of O(n) in which n is max capacity of LRU because the queue and cache both take space proportional to n
