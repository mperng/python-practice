class Node:
    def __init__(self, value):
    	self.value = value
    	self.left = None
        self.right = None

def preOrderTraversal(n):
    if n is not None:
        print n.value
        preOrderTraversal(n.left)
        preOrderTraversal(n.right)

def postOrderTraversal(n):
    if n is not None:
        postOrderTraversal(n.left)
        postOrderTraversal(n.right)
        print n.value

def inOrderTraversal(n):
    if n is not None:
        inOrderTraversal(n.left)
        print n.value
        inOrderTraversal(n.right)

def validBST(node):
    if not node:
        return True
    elif not validBST(node.left) or not validBST(node.right):
        return False
    else:
        return (node.left.value <= node.value if node.left else True) and (node.value < node.right.value if node.right else True)

tree = [Node(20), Node(10), Node(30), Node(25)]

tree[0].left = tree[1]
tree[0].right = tree[2]
tree[1].right = tree[3]

"""
print inOrderTraversal(tree[0])
print postOrderTraversal(tree[0])
print preOrderTraversal(tree[0])
"""

print validBST(tree[0])
