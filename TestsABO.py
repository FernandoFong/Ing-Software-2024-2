from Script2 import BST

elems = [5, 4, 2, 1, 3, 9, 7, 8, 7]
root = BST(elems[0])
for i in range(1, len(elems)):
    root.add(elems[i])

def test_preorder():
    preorder = [5, 4, 2, 1, 3, 9, 7, 8, 7]
    assert preorder == root.preorder()

def test_inorder():
    inorder = [1, 2, 3, 4, 5, 7, 7, 8, 9]
    assert inorder == root.inorder()

def test_postorder():
    postorder = [1, 3, 2, 4, 7, 8, 7, 9, 5]
    assert postorder == root.postorder()