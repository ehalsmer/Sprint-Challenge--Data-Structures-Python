import time
import sys
sys.path.append('./binary_search_tree')
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

bst = BinarySearchTree('l')
for name in names_2:
    bst.insert(name)

duplicates = []

# this nested loop has complexity O(m(n^2)), where m is the number of duplicates, n is the length of the lists (assuming they have the same length)
# for name_1 in names_1:
    # for name_2 in names_2:
        # if name_1 == name_2:
            # duplicates.append(name_1)
for name in names_1:
    # use a binary search tree to search names_2 for name
    if bst.contains(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
