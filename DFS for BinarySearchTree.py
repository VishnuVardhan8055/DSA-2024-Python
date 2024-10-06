class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def Insert(self, data):
        NewNode = Node(data)

        if self.root is None:
            self.root = NewNode
            return

        current = self.root
        while current:
            if data < current.data:
                if current.left is None:
                    current.left = NewNode
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = NewNode
                    break
                current = current.right

    def Height(self, node):
        if node is None:
            return -1
        else:
            left_height = self.Height(node.left)
            right_height = self.Height(node.right)
            return max(left_height, right_height) + 1

    def Level(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.data, end=" ")
        elif level > 1:
            self.Level(node.left, level - 1)
            self.Level(node.right, level - 1)

    def BreadthFirstSearch(self):
        height = self.Height(self.root)
        for level in range(1, height + 2):
            self.Level(self.root, level)
            print()

    def PreorderTraversal(self, node):
        if node:
            print(node.data, end=" ")
            self.PreorderTraversal(node.left)
            self.PreorderTraversal(node.right)

    def InorderTraversal(self, node):
        if node:
            self.InorderTraversal(node.left)
            print(node.data, end=" ")
            self.InorderTraversal(node.right)

    def PostorderTraversal(self, node):
        if node:
            self.PostorderTraversal(node.left)
            self.PostorderTraversal(node.right)
            print(node.data, end=" ")


bst = BinarySearchTree()
values = [6, 4, 5, 3, 8, 7, 9]
for value in values:
    bst.Insert(value)

print("Breadth-First Search (Level Order):")
bst.BreadthFirstSearch()

print( )
print("Depth First Search to perform ||| ways like PreOder , Inorder , Postorder ")

print("\nPreorder Traversal:")
bst.PreorderTraversal(bst.root)

print("\nInorder Traversal:")
bst.InorderTraversal(bst.root)

print("\nPostorder Traversal:")
bst.PostorderTraversal(bst.root)


