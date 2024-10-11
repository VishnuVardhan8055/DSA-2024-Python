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

    # Modify Display to accept a node and recursively display the tree
    def Display(self, node):
        if node is not None:
            self.Display(node.left)  # Recursively display the left subtree
            print(f"|{node.data}|<--->",end="")  # Print the current node's data
            self.Display(node.right)  # Recursively display the right subtree


    def getHeight(self, node):
        if node is None:
            return -1

        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)

        return max(left_height, right_height) + 1

    def getLevel(self, node, data, level=1):
        if node is None:
            return 0

        if node.data == data:
            return level

        downlevel = self.getLevel(node.left, data, level + 1)
        if downlevel != 0:
            return downlevel

        return self.getLevel(node.right, data, level + 1)


# Example usage:
BST = BinarySearchTree()

BST.Insert(10)
BST.Insert(20)
BST.Insert(9)
BST.Insert(8)
BST.Insert(7)
BST.Insert(22)

# Call Display starting from the root node
if BST.root is not None:
    BST.Display(BST.root)
else:
    print("Tree is empty.")

height = BST.getHeight(BST.root)
print()
print(height)


node_value = 20
level = BST.getLevel(BST.root, node_value)

print(f"Node {node_value} is at level {level}.")
