# Binary search tree algorithm
# 1) Searching
# 2) Insertion of a new key
# 3) Finding the smallest (or the largest) key

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search(root, key):
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)
    return search(root.left, key)

def insert(root, key):
    if root is None:
        return Node(key)
    if root.value == key:
        return root
    if root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def findSmallest(root):
    if root is None:
        return None
    if root.left is None:
        return root
    return findSmallest(root.left)

# Driver code
root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 10)
root = insert(root, 1)
root = insert(root, 6)


print("Smallest value in BST is", findSmallest(root).value)
print("Search for 10:", search(root, 10).value)

        
