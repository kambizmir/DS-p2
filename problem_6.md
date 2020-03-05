Implementation 1: using hash

Union: Iterate the lists and add them to a common hash. Hash takes care of creating the union. Time complexity is O(n+m) in which m and n are size of linked lists. Space is of O(n) in which n is the size of the union.

Intersection: Add linked list items to 2 hashes and then create the intersection by iteration. Time complexity is O(m+n) for adding to hashes and O(m) or O(n) for iteration, so overall O(m+n). Space is of O(m+n).

------
***I considered this case because the provided examples had repeating set members***

Implementation 2: not using hash, repeat is allowed in input or output linekd lists:

Union: Iterate the lists, add memebers to the result list. Time and space complexity are O(m+n)

Intersection: Use nested loops to find the intersection. Time complexity is O(m * n) and space is of O(m + n)

-------

Implementation 3: not using hash, repeat is NOT allowed in input or output linekd lists:

There are no repeating members in input sets.

Union: Add set 1 to result. Iterate over list 2 and if there is a member already added break, otherwise add it. Time complexity worst case is O(m * n). Space is of order(n) in which n is the size of the union.

Intersection: Nested loop over 2 lists. If a member is in common break because there are no repeating members and no need to go further. Time complexity worst case is O(m * n). Space is of order(n) in which n is the size of the intersection.