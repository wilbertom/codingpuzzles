def tree_by_levels(node):
    node = _create_new_tree(0, node)
    levels = _max_level(node)
    values = []
    level = 0

    while level <= levels:
        _add_values_of_level(level, values, node)
        level += 1

    return values


def _add_values_of_level(level, values, node):
    if node is None:
        return

    if node.level == level:
        values.append(node.value)

    _add_values_of_level(level, values, node.left)
    _add_values_of_level(level, values, node.right)


def _tree_by_levels(level, values, node):
    if node is None:
        return

    if node.level == level:
        values.append(node.value)

    _tree_by_levels(level, values, node.left)
    _tree_by_levels(level, values, node.right)


def _max_level(node):
    if node is None:
        return 0

    return max([_max_level(node.left), _max_level(node.right), node.level])


def _create_new_tree(level, node):
    if node is None:
        return None

    return _NodeWithLevel(
        level,
        _create_new_tree(level + 1, node.left),
        _create_new_tree(level + 1, node.right),
        node.value,
    )


class _NodeWithLevel:
    def __init__(self, level, left, right, value):
        self.level = level
        self.left = left
        self.right = right
        self.value = value
