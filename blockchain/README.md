# Blockchain

This is a basic blockchain implementation using a Block class and a Chain class.

## Time Complexity

* Adding a block to the chain is constant time `O(1)`.
* Finding a block by height / index is constant `O(1)`.
* Finding a block by hash takes linear time `O(n)` where n is the number of blocks in the chain.
* Validating the chain takes linear time `O(n)` where n is the number of blocks in the chain.

## Space Complexity

The space complexity of the chain is linear `O(n)` as the size of the chain grows in proportion to the number of blocks added to the chain.
