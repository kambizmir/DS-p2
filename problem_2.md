The find_files is implemented recursively. The base case is when it sees a file and it will be apended to the result.
If there is a folder, then the function calls itself for that folder. 

The folder structure is a general tree structure and the time and space complexity of this recursive code is O(n) in which
n is the number of tree nodes.