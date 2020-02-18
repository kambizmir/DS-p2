import sys
from queue import PriorityQueue

class TreeNode:
     def __init__(self):
        self.data = None
        self.frequency = 0
        self.left = None
        self.right = None

     def __lt__(self,other):
        return self.frequency < other.frequency

def preorder(node):
    print(node.data,node.frequency)
    if node.left:
    	preorder(node.left)
    if node.right:
    	preorder(node.right)


def huffman_encoding(data):
    frequency_hash = {}
    pq = PriorityQueue()

    for c in data:
        if c not in frequency_hash:
            frequency_hash[c] = 1
        frequency_hash[c] += 1

    frequency_tuples = [(k, v) for k, v in frequency_hash.items()] 
    #sorted_tuples = sorted(frequency_tuples , key=lambda x: x[1])

    for t in frequency_tuples:
        node = TreeNode()
        node.data = t[0]
        node.frequency = t[1]
        pq.put( node )

    root = None
    while not pq.empty():
        if pq.qsize() == 1:
            root = pq.get()
            break
        x1 = pq.get()
        x2 = pq.get()
        t = TreeNode()
        t.frequency = x1.frequency + x2.frequency
        t.left = x1
        t.right = x2
        pq.put(t)



    preorder(root)

    #print("AAA",root.frequency, root.left.frequency, root.right.frequency)

    #print (pq.qsize())


    # while not pq.empty():
    #     next_item = pq.get()
    #     print(next_item.frequency,next_item.data)



    #print (sorted_tuples)



def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))