class BinarySearchTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @classmethod
    def from_collection(cls, collection):
        first, *rest = collection

        tree = cls(value=first)

        for i in rest:
            tree.insert(i)

        return tree

    def search(self, value):
        pass

    def insert(self, value):
        if value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value=value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value=value)
            else:
                self.left.insert(value)
        else:
            return self

    def delete(self, value):
        pass

    def __eq__(self, other):
        if other is None:
            return False

        return (
            self.left == other.left
            and self.value == other.value
            and self.right == other.right
        )

    def __repr__(self):
        return f"({self.left}, {self.value}, {self.right})"
