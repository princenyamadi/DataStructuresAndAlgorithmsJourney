# constant time operation O(1)
# linear time operation O(n)

from collections import OrderedDict
# * HASH TABLES AND HASH SETS
# * hash tables are a data structure that allows you to store key-value pairs
# * hash sets are a data structure that allows you to store unique values

data = {"Caleb": "email@gmail.com",
        "elisha": "e@gamil.com", "john": "j@gmail.com", },


colors = {"red", "blue", "green", "yellow"}
# ? to create and empty set
# colors = set()
print(type(data))
print(type(colors))

print(hash("Prince"))


# how to create unhashable types
class Test:
    __hash__ = None
