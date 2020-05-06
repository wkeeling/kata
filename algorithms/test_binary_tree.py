class Node:

    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    def reverse(self):
        self.left, self.right = self.right, self.left
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()

    def __repr__(self):
        return self.name


def test_reverse():
    n = Node('n')
    n1 = Node('n1')
    n2 = Node('n2')
    n.left = n1
    n.right = n2
    n3 = Node('n3')
    n4 = Node('n4')
    n1.left = n3
    n1.right = n4
    n5 = Node('n5')
    n6 = Node('n6')
    n2.left = n5
    n2.right = n6

    n.reverse()

    print('hello')
