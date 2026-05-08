class Node:
    """A single node in the tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """The tree structure management class."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Public method to insert a value."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        """Helper to find the correct leaf node position."""
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)
        # Duplicates are typically ignored in a standard BST

    def search(self, key):
        """Returns True if key exists, else False."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None:
            return False
        if current.key == key:
            return True
        if key < current.key:
            return self._search_recursive(current.left, key)
        return self._search_recursive(current.right, key)

    def inorder_traversal(self, node, result=None):
        """Prints nodes in ascending order."""
        if result is None: result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.key)
            self.inorder_traversal(node.right, result)
        return result

# Example Usage
bst = BinarySearchTree()
for val in [50, 30, 20, 40, 70, 60, 80]:
    bst.insert(val)

print("In-order Traversal:", bst.inorder_traversal(bst.root)) # [20, 30, 40, 50, 60, 70, 80]
print("Search 40:", bst.search(40))  # True
print("Search 90:", bst.search(90))  # False