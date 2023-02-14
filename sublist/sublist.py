"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
#SUBLIST = None
#SUPERLIST = None
#EQUAL = None
#UNEQUAL = None


#def sublist(list_one, list_two):
    #pass
#The values of the sublists are given below
#If the length of the lists are equal and the lists are identical, then they are equal. If the length of list_one is smaller than the length of list_two and list_one is present as such in list_two, then list_one is a subset of list_two. If the length of list_two is smaller than the length of list_one and list_two is present as such in list_one, then list_one is superset of list_two. If none of the above conditions is satisified, then lists are unequal
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0

def sublist(list_one, list_two):
    l_one=len(list_one)
    l_two=len(list_two)
    if l_one==l_two and list_one==list_two:
        return 3
    elif l_one<l_two and list_one in [list_two[i:l_one+i] for i in range(l_two)]:
        return 1
    elif l_one>l_two and list_two in [list_one[i:l_two+i] for i in range(l_one)]:
        return 2
    else:
        return 0 