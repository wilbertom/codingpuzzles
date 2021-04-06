from collections import defaultdict


def tree_by_levels(node):
    values_by_level = _values_by_level(node)
    values = []

    for values_in_level in values_by_level.values():
        values.extend(values_in_level)

    return values


def _values_by_level(node):
    values = defaultdict(list)
    _values_by_level_agg(values, 0, node)

    return values


def _values_by_level_agg(values, level, node):
    if node is None:
        return

    values[level].append(node.value)

    _values_by_level_agg(values, level + 1, node.left)
    _values_by_level_agg(values, level + 1, node.right)
