import os

class BinarySearchTree(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if not self.data:
            self.data = data
            return
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = BinarySearchTree(data)
            return
        if self.right:
            self.right.insert(data)
            return
        self.right = BinarySearchTree(data)

    def PreOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreOrderTraversal(root.left)
            res = res + self.PreOrderTraversal(root.right)
        return res
    
tree = BinarySearchTree()
tree.insert(11)
tree.insert(7)
tree.insert(15)
tree.insert(3)
tree.insert(9)

print(tree.PreOrderTraversal(tree))
