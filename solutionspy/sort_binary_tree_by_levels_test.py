from .sort_binary_tree_by_levels import tree_by_levels


class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


def test_tree_by_levels_when_root_is_empty():
    assert tree_by_levels(None) == []


def test_example_1():
    tree = Node(
        Node(Node(None, None, 1), Node(None, None, 3), 8),
        Node(Node(None, None, 4), Node(None, None, 5), 9),
        2,
    )

    assert tree_by_levels(tree) == [2, 8, 9, 1, 3, 4, 5]


def test_example_2():
    tree = Node(
        Node(None, Node(None, None, 3), 8),
        Node(None, Node(None, Node(None, None, 7), 5), 4),
        1,
    )

    assert tree_by_levels(tree) == [1, 8, 4, 3, 5, 7]


def test_with_three_levels():
    tree = Node(
        Node(Node(Node(None, None, 6), None, 1), Node(None, None, 3), 8),
        Node(Node(None, None, 4), Node(None, None, 5), 9),
        2,
    )

    assert tree_by_levels(tree) == [2, 8, 9, 1, 3, 4, 5, 6]
