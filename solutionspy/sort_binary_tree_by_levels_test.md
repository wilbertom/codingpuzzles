# Sort Binary Tree by Levels

https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python

## AAR

### What went well

* Brute forcing an approach even though it was hacky.
* Coming back and refactoring that hack into something better.
* Knowing the new python dictionaries keep their insert order. Without it, my
  solution would of being longer.

### What went bad

* I spend a lot of time misunderstanding the problem, implementing it with the
  wrong iteration order.
* My solution walks the entire tree and duplicates it in memory in a dictionary.
  The deque solution doesn't seem to do this.
* I don't understand the most popular solution using a dequeue

```python
from collections import deque


def tree_by_levels(node):
    if not node:
        return []
    res, queue = [], deque([node,])
    while queue:
        n = queue.popleft()
        res.append(n.value)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
    return res
```

### Lessons Learned / Action Items

* Brute force when you need to
* [ ] Learn the deque solution
* [ ] Learn more about binary trees
