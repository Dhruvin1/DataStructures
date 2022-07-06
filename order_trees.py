class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# class BinaryTree:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.root = value

def PrintPreorder(root):
    if not root:
        return
    print(root.value)
    PrintPreorder(root.left)
    PrintPreorder(root.right)

def PrintInorder(root):
    if not root:
        return
    PrintInorder(root.left)
    print(root.value)
    PrintInorder(root.right)

def PrintPostorder(root):
    if not root:
        return
    PrintPostorder(root.left)
    PrintPostorder(root.right)
    print(root.value)

# Driver code
if __name__ == "__main__":
    mytree = Node(1)
    mytree.left = Node(2)
    mytree.right = Node(3)
    mytree.left.left = Node(4)
    mytree.left.right = Node(5)
    mytree.right.left = Node(6)
    mytree.right.right = Node(7)
    mytree.left.left.left = Node(8)
    mytree.left.left.right = Node(9)
    mytree.left.right.left = Node(10)
    mytree.left.right.right = Node(11)
    mytree.right.left.left = Node(12)
    mytree.right.left.right = Node(13)
    mytree.right.right.left = Node(14)
    mytree.right.right.right = Node(15)
    print("Printing pre-order tree: ")
    PrintPreorder(mytree)
    print("Printing in-order tree: ")
    PrintInorder(mytree)
    print("Printing post-order tree: ")
    PrintPostorder(mytree)








