Huffman coding algorithms is based on building a code tree containing the frequency of the characters in the string. Each leaf of a tree has one of the characters and the code of that character is calculated by assigning 0s and 1s to each branch of the tree from the root to the leaf.
To implement, I created a tree node which can hold character and frequency of the character. Also I added a "less than" operator to the tree node in order to be able to compare the nodes based on the frequency they hold.

For Huffman encoding, we create frequency hash first and then build a list of tuples of characters and their frequency. Then we create tree nodes from each character and enter the nodes to a priority queue. Then we get 2 items every time from priority queue, which gives us 2 smallest frequency characters and create a new node with sum of their frequency and put back it into priority queue. We do this until there is one node remaining which will be the root of Huffman tree. Then we preorder traverse the tree to create a map of the characters and their code which is built by alternating 0 and 1 for left and right children.

when the code map is built, encoding the string is concatinating the code for each character which creates a string of 0s and 1s. In reality, this string should be converted to the bit stream to be transferred. The output of the encoding will be encoded string and the code tree.

The decoder scans the bits and moves in the tree until it gets to a leaf which will be one character.

Time complexity for building the tree is O(n * log(n)) in which n is the number of characters of the string, because we need to scan all the characters and put it into a priority queue. Space is of order(m) in which m is the number of distinct characters.

Time complexity of encoding is O(n), n is the number of original characters.

Time complexity of decoding is O(n), n is the number of encoded string