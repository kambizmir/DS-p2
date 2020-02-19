import sys
from queue import PriorityQueue

codeMap = {}

class TreeNode:
     def __init__(self):
        self.data = None
        self.frequency = 0
        self.left = None
        self.right = None

     def __lt__(self, other):
        return self.frequency < other.frequency

def preorder(node, prefix):
    if node.data:    	
    	codeMap[node.data] = prefix
    	#print(node.data,node.frequency , prefix)
    if node.left:
    	preorder(node.left, prefix + '0')
    if node.right:
    	preorder(node.right, prefix + '1')


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


    preorder(root, "")
    #print(codeMap)

    encoded = ""
    for c in data:
    	encoded += codeMap[c]

    return encoded , root


    


def huffman_decoding(data,tree):
    result = ""
    node = tree
    for c in data:
        if c == '0':
            node = node.left
        else:
            node = node.right
        if node.data:
            result += node.data
            node = tree
    return result




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


    print("\nTest 2 \n")

    sentence2 = "Huffman algorithm is implemented!"

    print ("The size of the data is: {}\n".format(sys.getsizeof(sentence2)))
    print ("The content of the data is: {}\n".format(sentence2))

    encoded_data, tree = huffman_encoding(sentence2)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))