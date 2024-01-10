class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order(root):
    if root is None:
        return
    else:
        print(root.value)
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root is None:
        return
    else:
        post_order(root.left)
        post_order(root.right)
        print(root.value)
        
def in_order(root):
    if root is None:
        return
    else:
        in_order(root.left)
        print(root.value)
        in_order(root.right)
        
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Pre-order traversal of binary tree is")
pre_order(root)

print("Post-order traversal of binary tree is")
post_order(root)

print("In-order traversal of binary tree is")
in_order(root)

