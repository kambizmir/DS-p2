class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name




user_cache = {}
root_group = None


def search_groups_for_user(user, group, parent_name_set):

    if user not in user_cache:
            user_cache[user] = set() 
   
    set_copy = parent_name_set.copy()
    set_copy.add(group.name)

    if user in group.get_users(): 
        user_cache[user] = user_cache[user].union(set_copy)

    for g in group.get_groups():
        search_groups_for_user(user, g, set_copy)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user is None or user is "":
        print("No user to look for!")
        return False
    if not isinstance(group,Group):
        print("The group is not valid!")
        return False

    if user not in user_cache:
        search_groups_for_user(user, root_group, set())

    if group.name in user_cache[user]:            
        return True
    else:
        return False
    
    return False


# Test case 1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


# Test case 2
g1 = Group("g1")
g2 = Group("g2")
g3 = Group("g3")
g4 = Group("g4")
g5 = Group("g5")
g6 = Group("g6")
g7 = Group("g7")
g8 = Group("g8")

u1 = "u1"
u2 = "u2"
u3 = "u3"
u4 = "u4"

g1.add_group(g2)
g1.add_group(g3)
g1.add_group(g4)

g2.add_group(g5)
g2.add_group(g6)

g3.add_group(g7)

g6.add_group(g8)

g1.add_user(u1)

g2.add_user(u2)
g2.add_user(u3)

g3.add_user(u2)

g4.add_user(u2)

g7.add_user(u2)
g7.add_user(u3)

g8.add_user(u4)


##########    
print("Test 1")
user_cache = {}
root_group = parent


print(is_user_in_group(sub_child_user, parent))
print(user_cache)

#########
user_cache = {}
root_group = g1

print("\nTest 2")
print(is_user_in_group(u1, g1)) #True
print(is_user_in_group(u1, g2)) #False
print(is_user_in_group(u1, g3)) #False
print(is_user_in_group(u1, g4)) #False
print(is_user_in_group(u1, g5)) #False
print(is_user_in_group(u1, g6)) #False
print(is_user_in_group(u1, g7)) #False
print(is_user_in_group(u1, g8)) #False

print("\nTest 3")
print(is_user_in_group(u2, g1)) #True
print(is_user_in_group(u2, g2)) #True
print(is_user_in_group(u2, g3)) #True
print(is_user_in_group(u2, g4)) #True
print(is_user_in_group(u2, g5)) #False
print(is_user_in_group(u2, g6)) #False
print(is_user_in_group(u2, g7)) #True
print(is_user_in_group(u2, g8)) #False

print("\nTest 4")
print(is_user_in_group(u3, g1)) #True
print(is_user_in_group(u3, g2)) #True
print(is_user_in_group(u3, g3)) #True
print(is_user_in_group(u3, g4)) #False
print(is_user_in_group(u3, g5)) #False
print(is_user_in_group(u3, g6)) #False
print(is_user_in_group(u3, g7)) #True
print(is_user_in_group(u3, g8)) #False

print("\nTest 5")
print(is_user_in_group(u4, g1)) #True
print(is_user_in_group(u4, g2)) #True
print(is_user_in_group(u4, g3)) #False
print(is_user_in_group(u4, g4)) #False
print(is_user_in_group(u4, g5)) #False
print(is_user_in_group(u4, g6)) #True
print(is_user_in_group(u4, g7)) #False
print(is_user_in_group(u4, g8)) #True

print("\ncache")
print(user_cache)

#########

print("\nTest 6, edge case")
print(is_user_in_group(None, g1)) # Print No user to look for!, return False

print("\nTest 7, edge case")
print(is_user_in_group("", g1)) # Print No user to look for!, return False

print("\nTest 8, edge case")
print(is_user_in_group(u1, None)) # Print The group is not valid!, return False

print("\nTest 9, edge case")
print(is_user_in_group(u1, "Group 10")) # Print The group is not valid!, return False





