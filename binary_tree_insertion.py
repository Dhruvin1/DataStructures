import random

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):
    if node.value == value:
        return
    if value > node.value and not node.right:
        node.right = BinaryTreeNode(value)
    elif value < node.value and not node.left:
        node.left = BinaryTreeNode(value)
    elif value > node.value and node.right:
        insert(node.right,value)
    else:
        insert(node.left, value)

def PreOrderTraversal(node):
    if not node:
        return
    PreOrderTraversal(node.left)
    print(node.value)
    PreOrderTraversal(node.right)

# Driver code
if __name__ == "__main__":
    tree_root = BinaryTreeNode(0)
    insert_list = []
    for i in range(20):
        element = random.randint(0,20)
        insert(tree_root,element)
        insert_list.append(element)
    print("Inserted elements: ", insert_list)
    print("Sorted binary search tree element")
    PreOrderTraversal(tree_root)
