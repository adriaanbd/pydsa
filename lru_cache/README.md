# LRU Cache

A doubly linked list was used to keep track of the cache's order of insertion, in addition to providing constant time access to the oldest and most recent item in the cache. Furthermore, a dictionary was used as the cache because it provides constant time access to all nodes, including the ones in the middle of the doubly linked list. These data structures allow all operations to be done in constant time.

## Time Complexity

The time complexity of all operations take constant time `O(1)`. 

## Space Complexity 

The space complexity is `O(n)`, where `n` represents the number of keys added to the `cache`.