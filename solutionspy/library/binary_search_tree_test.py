from .binary_search_tree import BinarySearchTree


def test_from_collection():
    tree = BinarySearchTree.from_collection([33, 35, 54, 37, 41])

    assert tree == BinarySearchTree(
        value=33,
        right=BinarySearchTree(
            value=35,
            right=BinarySearchTree(
                left=BinarySearchTree(
                    value=37,
                    right=BinarySearchTree(
                        value=41,
                    ),
                ),
                value=54,
            ),
        ),
    )


def test_simple_inserts():
    tree = BinarySearchTree(value=2)
    tree.insert(1)
    tree.insert(3)

    assert tree == BinarySearchTree(
        left=BinarySearchTree(value=1),
        value=2,
        right=BinarySearchTree(value=3),
    )


def test_simple_searches():
    tree = BinarySearchTree.from_collection([33, 35, 54, 37, 41])

    assert tree.search(33) == 33
    assert tree.search(35) == 35
    assert tree.search(54) == 54
    assert tree.search(37) == 37
    assert tree.search(41) == 41

    assert tree.search(44) is None
    assert tree.search(1) is None
    assert tree.search(0) is None
