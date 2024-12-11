class Nodetree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def insert(self,value):
        if value < self.value:
            if (self.left==None):
                self.left = Nodetree(value)
            else:
                self.left.insert(value)
        else:
            if (self.right == None):
                self.right = Nodetree(value)
            else:
                self.right.insert(value)
    def inordertraversal(self):
        if self.left:
            self.left.inordertraversal()
        print(self.value)
        if self.right:
            self.right.inordertraversal()

        
tree = Nodetree(5)
tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(7)
tree.insert(12)
tree.inordertraversal()# print(tree.left.left.right.value)