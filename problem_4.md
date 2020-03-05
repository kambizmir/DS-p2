Because it's not stated in the problem definition, I assumed 2 requirements for the problem:
1- A user can be in multiple groups
2- If a user is in a child group it will be in parent group too by definition

I used a hash for storing groups to which a user belongs to. The hashing is lazy, meaning the first time the function is_user_in_group is called, the user data is not in the hash and the function search_groups_for_user is called for the user. The subsequent calls to is_user_in_group will get the user groups from the hash and therefore will be more efficient than first time. So if the number of calls to is_user_in_group is relatively high, the amortized time complexity is of O(1).

The hash maintains a set of groups which a user belongs to. The search_groups_for_user searches from the root recursively to populate the hash for particular user.

The time complexity for the first time search of a user is of O(n) in which n is the number of groups. The space is of O(m * n) in which m is the number of users and n is the number of groups which a user belongs to.

If new groups are added or deleted, the hash should be updated to reflect the changes.