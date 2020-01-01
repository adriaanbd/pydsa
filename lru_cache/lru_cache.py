class Node:
    def __init__(self, *values):
        self.key, self.value = values
        self.front = None
        self.back = None


class LRU_Cache:
    def __init__(self, limit=5):
        assert isinstance(limit, int), 'Limit must be an integer'
        assert limit and limit > 0, 'Must provide a limit'
        self.limit = limit
        self.cache = {}
        self.lru = None
        self.oldest = None
        self.size = 0

    def _make_node(self, *values):
        return Node(*values)

    def _remove(self, node, full=False):
        front, back = node.front, node.back
        back.next = front
        if full: del self.cache[node.key]
        if front:
            front.back = back
            self.oldest = front
        else:
            self.oldest = back
        self.size -= 1

    def _insert(self, node):
        if self.lru:
            old_lru = self.lru
            old_lru.back = node
            self.lru.next = old_lru
        elif self.oldest is None:
            self.oldest = node
        self.lru = node
        self.cache[node.key] = node
        self.size += 1

    @property
    def full(self):
        return self.limit == self.size

    def get(self, key):
        node = self.cache.get(key)
        if node:
            self._remove(node)
            self._insert(node)
            return node.value
        else:
            return -1

    def set(self, *values):
        key, _ = values
        if key not in self.cache:
            node = self._make_node(*values)
            if self.full:
                self._remove(self.oldest, full=True)
            self._insert(node)


if __name__ == "__main__":
    def test_lru_and_oldest_on_insert():
        cache = LRU_Cache(3)
        cache.set(1, 1)
        assert cache.lru.value == 1, 'LRU item was not set'
        assert cache.oldest.value == 1, 'Oldest item was not set'
        cache.set(2, 2)
        assert cache.lru.value == 2, 'LRU item did not update'
        assert cache.oldest.value == 1, 'Oldest item was incorrectly updated'

    def test_when_cache_is_full():
        cache = LRU_Cache(3)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)
        assert cache.cache.get(1) is None, 'Oldest was not removed'
        assert cache.lru.value == 4, 'LRU item was not updated'

    def test_multiple_get_and_set():
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)
        assert cache.get(1) == 1
        assert cache.get(2) == 2
        assert cache.get(9) == -1
        cache.set(5, 5)
        cache.set(6, 6)
        assert cache.get(3) == -1

    def test_assertion_limit():
        try:
            cache = LRU_Cache(0)
        except AssertionError as e:
            assert isinstance(e, AssertionError)
        else:
            msg = 'Should raise AssertionError when no limit'
            raise AssertionError(msg)

    test_lru_and_oldest_on_insert()
    test_when_cache_is_full()
    test_multiple_get_and_set()
    test_assertion_limit()
