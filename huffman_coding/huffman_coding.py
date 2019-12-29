from queue import PriorityQueue


class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __add__(self, other):
        return self.freq + other.freq

    def __radd__(self, other):
        if other == 0 or other.freq is None:
            return self
        return self.__add__(other)

    def __repr__(self):
        return f"NODE[Char:{self.char}, Left: {self.left}, Right:{self.right}]"


class HuffmanCoding:
    def __init__(self, data: str):
        self.root = None
        self.queue = PriorityQueue()
        self.codes = dict()
        self.data = data

    def compress(self):
        self.set_frequencies()
        self.build_tree()
        encoded_mssg = self.encode()
        return encoded_mssg

    def set_frequencies(self):
        frequencies = dict()
        for char in self.data:
            node = frequencies.get(char)
            if node is not None:
                node.freq += 1
            else:
                node = Node(char, 1)
                frequencies[char] = node
                self.queue.put(node)

    def build_tree(self):
        if self.queue.qsize() == 1:
            fake_node = Node(freq=0, char='')
            self.queue.put(fake_node)
        while self.queue.qsize() > 1:
            nodes = self.queue.get(), self.queue.get()
            parent = Node(freq=sum(nodes))
            parent.left, parent.right = nodes
            self.queue.put(parent)
        self.root = self.queue.queue[0]

    def encode(self):
        self.set_binary_codes(self.root)
        message = ''
        for char in self.data:
            message += self.codes[char]
        return message

    def set_binary_codes(self, root, bit: str = None):
        if bit is None:
            bit = ''

        if root.char is not None:
            self.codes[root.char] = bit
            return

        self.set_binary_codes(root.left, bit + '0')
        self.set_binary_codes(root.right, bit + '1')


def run_assertions(data: str, operation: str, tree: Node = None):
    if 'encode' == operation:
        assert isinstance(data, str), 'Data must be a string'
        assert len(data) > 0, 'There is nothing to encode'
    elif 'decode' == operation:
        assert isinstance(tree, Node), 'Tree must be an instance of Node'
        assert isinstance(data, str), 'Data to decode must be a string'
        uniques = set(data)
        assert len(uniques) <= 2, 'Only binary data allowed'
        assert '0' in uniques or '1' in uniques, 'Only 0s and 1s allowed'


def huffman_encoding(data: str):
    run_assertions(data, 'encode')
    tree = HuffmanCoding(data)
    message = tree.compress()
    return message, tree.root


def huffman_decoding(data: str, tree: Node):
    run_assertions(data, 'decode', tree)
    current = tree
    message = ''

    for bit in data:
        if not current.left and not current.right:
            message += current.char
            current = tree

        if bit == '0':
            current = current.left
        else:
            current = current.right

    message += current.char
    return message


if __name__ == "__main__":
    import sys

    def print_log(data, size):
        content_mssg = f'\nThe content of the data is: {data}'
        size_mssg = f'\nThe size of the data is {size}\n'
        print(content_mssg)
        print(size_mssg)

    def print_encode_log(data, size):
        encoded_content_mssg = f'\nThe encoded data content is: {data}'
        encoded_size_mssg = f'\nThe size of the encoded data is: {size}\n'
        print(encoded_content_mssg)
        print(encoded_size_mssg)

    def print_decode_log(data, size):
        decoded_content_mssg = f'\nThe decoded data content is: {data}'
        decoded_size_mssg = f'\nThe size of the decoded data is: {size}\n'
        print(decoded_content_mssg)
        print(decoded_size_mssg)

    def test_encoded_and_decoded_data_size(data):
        print('\nTesting that encoded data size is smaller than the original')
        size = sys.getsizeof(data)
        print_log(data, size)
        encoded_data, tree = huffman_encoding(data)
        encoded_size = sys.getsizeof(int(encoded_data, base=2))
        print_encode_log(encoded_data, encoded_size)
        assert encoded_size < size, 'Encoded data is not smaller than original'
        print('TEST PASSED!\n')
        print('\nTesting that decoded data size is same as original')
        decoded_data = huffman_decoding(encoded_data, tree)
        decoded_size = sys.getsizeof(decoded_data)
        print_decode_log(decoded_data, decoded_size)
        assert decoded_size == size, 'Decoded data size != size of original'
        print('TEST PASSED!\n')

    def test_decoded_data_matches_the_original(data):
        print('Testing that the decoded data matches the original\n')
        encoded_data, tree = huffman_encoding(data)
        decoded_data = huffman_decoding(encoded_data, tree)
        assert decoded_data == data, 'Decoded data does not match original'
        print('TEST PASSED!\n')

    def test_invalid_data_to_encode(data):
        print('Testing that AssertionError is raised '
              'with invalid input to ENCODE')
        print(f'Input provided: {data}')
        try:
            huffman_encoding(data)
        except AssertionError as error:
            assert isinstance(error, AssertionError)
            print('TEST PASSED!\n')
        else:
            print('FAILED!')

    def test_invalid_data_to_decode(data):
        print('Testing that AssertionError is raised '
              'with invalid input to DECODE')
        print(f'Input provided: {data}')
        try:
            huffman_encoding(data)
        except AssertionError as error:
            assert isinstance(error, AssertionError)
            print('TEST PASSED!\n')
        else:
            print('FAILED!')

    valid_data = [
        'The bird is the word',
        'AAAAAAAAAAAAAAAAAAAA',
        'A'
    ]

    for item in valid_data:
        test_encoded_and_decoded_data_size(item)
        test_decoded_data_matches_the_original(item)

    invalid_data = [0, None, '']
    for item in invalid_data:
        test_invalid_data_to_encode(item)

    not_a_node_obj = object()
    test_invalid_data_to_decode(not_a_node_obj)
