class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            self._from_iterable(iterable)


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def _from_iterable(self, iterable):
        previous_node = None
        for item in iterable:
            current_node = Node(item)
            if previous_node is not None:
                previous_node.next = current_node
            if self.head is None:
                self.head = current_node
            previous_node = current_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return f'{list(self)}'

    def __repr__(self):
        return f'{list(self)}'


def union(llist_1, llist_2):
    s1 = set(llist_1)
    s2 = set(llist_2)

    uniques = s1.union(s2)
    ll_union = LinkedList(uniques)

    del uniques, s1, s2
    return ll_union


def intersection(llist_1, llist_2):
    s1 = set(llist_1)
    s2 = set(llist_2)

    set_intersection = s1.intersection(s2)
    ll_intersection = LinkedList(set_intersection)

    del s1, s2, set_intersection
    return ll_intersection


if __name__ == "__main__":
    def test_case(test_data):
        l1, l2 = test_data

        ll1 = LinkedList(l1)
        ll2 = LinkedList(l2)

        assert list(union(ll1, ll2)) == list(set(l1 + l2))
        assert list(intersection(ll1, ll2)) == list(set(l1).intersection(l2))

    t1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21], [6, 32, 4, 9, 6, 1, 11, 21, 1]
    t2 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23], [1, 7, 8, 9, 11, 21, 1]
    t3 = [], [1, 2, 3]
    t4 = [], []

    t = [t1, t2, t3, t4]

    # run tests
    for test_data in t:
        test_case(test_data)