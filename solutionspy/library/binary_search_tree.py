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
        if value == self.value:
            return value
        elif value > self.value:
            return None if self.right is None else self.right.search(value)
        elif value < self.value:
            return None if self.left is None else self.left.search(value)

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
        return self._delete(None, value)

    def _delete(self, parent, value):
        if value == self.value:
            self._delete_node(parent)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                self.right._delete(self, value)
        elif value < self.value:
            if self.left is None:
                return None
            else:
                self.left._delete(self, value)
        else:
            raise RuntimeError("Logic error")

    def _delete_node(self, parent):
        if self._leaf:
            parent._replace_with(self, None)
        elif self._only_right_child:
            parent._replace_with(self, self.right)
        elif self._only_left_child:
            parent._replace_with(self, self.left)
        else:
            successor_node = self._find_successor_node()
            self.value = successor_node.value

    def _replace_with(self, old, new):
        if self.left == old:
            self.left = new
        elif self.right == old:
            self.right = new
        else:
            RuntimeError("Logic error")

    def _find_successor_node(self):
        return self.right._leftmost_leaf(self)

    def _leftmost_leaf(self, parent):
        if self.left is None:
            parent._replace_with(self, None)
            return self
        else:
            return self.left._leftmost_leaf(self)

    @property
    def _leaf(self):
        return self.left is None and self.right is None

    @property
    def _only_right_child(self):
        return self.right is not None and self.left is None

    @property
    def _only_left_child(self):
        return self.left is not None and self.right is None

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
