from .binary_search_tree import BinarySearchTree


def test_from_collection():
    assert BinarySearchTree.from_collection([33, 35, 54, 37, 41]) == BinarySearchTree(
        value=33,
        right=BinarySearchTree(
            value=35,
            right=BinarySearchTree(
                left=BinarySearchTree(value=37, right=BinarySearchTree(value=41)),
                value=54,
            ),
        ),
    )


def test_insert_simple_inserts():
    tree = BinarySearchTree(value=2)
    tree.insert(1)
    tree.insert(3)

    assert tree == BinarySearchTree(
        left=BinarySearchTree(value=1),
        value=2,
        right=BinarySearchTree(value=3),
    )
