# Huffman Coding

> "[...] Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression. The process of finding or using such a code proceeds by means of Huffman coding, an algorithm developed by David A. Huffman [...],published in the 1952 paper *A Method for the Construction of Minimum-Redundancy Codes*"

Read more [here](https://en.wikipedia.org/wiki/Huffman_coding).

## Time & Space Complexity Analysis

### Time Complexity

The overall time complexity for both encoding and decoding is `O(n log n)`, as described below.

#### Encoding

Overall time complexity for the encoding process is `O(n log n)`.

* Setting the frequencies take `O(n)`, where `n` represents the number of characters in the data.
* Building the tree takes takes `O(n log n)`, where n represents the number of items in que `queue`. This process involves inserting and extracting items in a priority queue at `O(n log n)`, given that `priority_queue.put(item)` takes `O(log n)` and likewise each `priority_queue.get()` takes `O(log n)`. Both methods are called for `n` amount of times where `n` represents the number of unique characters in the data.
* Setting a binary codes mapping from letter to code takes `O(n)` where n represents the number of nodes in the tree.
* Encoding the message takes `O(n)` where n represents the number of characters in the data.

#### Decoding

The overall time complexity for the decoding process is `O(n log n)`

* Reading the data takes `O(n)`, where `n` represents the number of bits in the data.
* Traversing the tree takes `O(log n)`, where `n` represents the number of nodes in the tree.

### Space Complexity

The overall space complexity of both the encoding and decoding processes is `O(n)`, as detailed below.

#### Encoding

The overall space complexity of the encoding process is `O(n)`

* The `set_frequencies` method takes `O(n)` space, where `n` represents the number of characters in the data. The size of the dictionary, queue and number of nodes grow in proportion to the amount of unique letters in the data.
* Building the tree takes `O(log n)` space, where `n` represents the number of nodes in que queue, because for every two nodes in the queue, one (1) additional node is created as parent, i.e. if we had 2 nodes we end up with 3 nodes and if we had 100 nodes we end up with 150.
* Since recursion is used to traverse the tree and collect the binary codes from each node, it takes `O(nm)` space due to the call stack, where `n` represents the number of nodes in one level and `m` represents the depth of the tree.
* Creating a dictionary to store the binary codes mapping obtained from the tree traversal takes `O(n)` space since the number of keys in the dictionary grows in proportion to the number of unique letters in the data.
* Creating a string of binary numbers takes `O(n)` space where `n` represents the number of letters in the data.

#### Decoding

Traversing the tree through iteration and building the message takes `O(n)` space, where `n` represents the number of characters decoded.
