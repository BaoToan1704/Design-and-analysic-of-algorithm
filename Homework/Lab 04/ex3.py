class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))
    

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(height(root))

# Basic OP: addition in line 11
# Worst case: O(n)
# T(n) = T(n/2) + 1
# Time complexity: O(n)
