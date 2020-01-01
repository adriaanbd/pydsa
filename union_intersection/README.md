# Union Intersection

Union and intersection methods are implemented to be used on a `LinkedList`. The approach taken was to leverage Python's built-in `set` methods `union` and `intersection` by providing an `__iter__` method to the `LinkedList` class, which would allow calling `set(LinkedList)`.

## Complexity Analysis

Overall time and space complexity are both `O(n)`.

### Time Complexity

The overall time complexity of both operations in `O(n)`

Converting from `LinkedList` to `set` is done through iteration and takes `O(n)`.
Calling `set1.union(set2)` takes `O(n + m)` where `n` is the number of elements in `set1` and `m` is the number of elements in `set2`.

Calling `set1.intersection(set2)` takes `O(min(n, m))` on average, where `n` is the number of elements in `set1` and `m` is the number of elements in `set2`.

Converting back to a LinkedList takes `O(n)` as this is achieved through a single iteration.

## Space Complexity

The overall space complexity of both operations is `O(n)`.

In both operations two `set`s are used to store uniques of both linked lists, and at worst they'd contain an exact copy of each.

Converting the set to a `LinkedList` takes `O(n)` space.