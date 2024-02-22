def solve(path):
    valleys, level = 0, 0
    enteredValley = False
    for step in path:
        if step == 'U':
            level += 1
        else:
            level -= 1

        if level == 0 and enteredValley:
            enteredValley = False
            valleys += 1
        elif level < 0 and not enteredValley:
            enteredValley = True

    if enteredValley:
        valleys += 1

    return valleys

class BST:

    def __init__(self, x):
        self.e = x
        self.left = None
        self.right = None

    def add(self, node):
        if str(type(node)) == "<class 'int'>":
            self.add(BST(node))
            return 
        if self.e > node.e:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)
    
    def preorder(self):
        traverse = []
        traverse.append(self.e)
        if self.left is not None:
            traverse += self.left.preorder()
        if self.right is not None:
            traverse += self.right.preorder()
        return traverse
    
    def inorder(self):
        traverse = []
        if self.left is not None:
            traverse += self.left.inorder()
        traverse.append(self.e)
        if self.right is not None:
            traverse += self.right.inorder()
        return traverse
    
    def postorder(self):
        traverse = []
        if self.left is not None:
            traverse += self.left.postorder()
        if self.right is not None:
            traverse += self.right.postorder()
        traverse.append(self.e)
        return traverse
