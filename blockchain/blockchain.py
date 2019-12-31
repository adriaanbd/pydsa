from hashlib import sha256
from datetime import datetime
import json


class Block:
    def __init__(self, data):
        self.data = data
        self.height = -1
        self.timestamp = str(datetime.utcnow())
        self.prev_hash = None
        self.hash = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        bytes_str = data.encode('utf-8')
        self._data = bytes_str.hex()

    def validate_block(self) -> bool:
        aux_hash = self.hash
        self.hash = None
        is_valid = self.calc_hash() == aux_hash
        self.hash = aux_hash
        return is_valid

    def calc_hash(self) -> str:
        sha = sha256()
        enc_type = 'utf-8'
        sha.update(self.data.encode(enc_type))
        sha.update(self.timestamp.encode(enc_type))
        sha.update(str(self.height).encode(enc_type))
        if self.prev_hash:
            sha.update(self.prev_hash.encode(enc_type))
        return sha.hexdigest()

    @property
    def block_data(self) -> dict:
        block_data = {
            'data': self.data,
            'height': self.height,
            'timestamp': self.timestamp,
            'prev_hash': self.prev_hash,
            'hash': self.hash
            }
        return block_data

    def as_json(self):
        return json.dumps(self.block_data)

    def __repr__(self):
        return str(self.block_data)

    def __str__(self):
        return str(self.block_data)


class Chain:
    def __init__(self):
        self.__chain = []

    def add_block(self, data: str):
        assert isinstance(data, str), 'Data must be a string'
        assert data and len(data) > 0, 'Cannot create Block with no data'
        block = self._create_block(data)
        self.__chain.append(block)

    def _create_block(self, data) -> Block:
        block = Block(data)
        block.height = len(self.__chain)
        if len(self.__chain) > 0:
            prev_idx = len(self.__chain) - 1
            prev_block = self.get_block_by_height(prev_idx)
            block.prev_hash = prev_block.hash
        block.hash = block.calc_hash()
        return block

    def get_block_by_height(self, height: int) -> Block:
        assert isinstance(height, int), 'Height must be an integer'
        assert 0 <= height < len(self.__chain), 'Height is invalid'
        return self.__chain[height]

    def get_block_by_hash(self, hash_str: str) -> Block:
        assert isinstance(hash_str, str), 'Hash must be a string'
        for block in self.__chain:
            if block.hash == hash_str:
                return block

    def validate_chain(self) -> list:
        errors = []
        for height, block in enumerate(self.__chain):
            if not block.validate_block():
                errors.append({
                    'error': 'invalid block',
                    'block': block
                    })
            if height:
                prev_block = self.__chain[height - 1]
                prev_hash, prev_block.hash = prev_block.hash, None
                current_hash = prev_block.calc_hash()
                prev_block.hash = prev_hash
                has_invalid_hashes = current_hash != block.prev_hash
                if has_invalid_hashes:
                    errors.append({
                        'error': 'discrepancy between blocks',
                        'current': block,
                        'previous': prev_block
                        })
        return errors

    def __iter__(self):
        for block in self.__chain:
            yield block

    def __repr__(self):
        return f'{self.__chain}'

    def __str__(self):
        return f'{self.__chain}'


if __name__ == "__main__":
    def test_add_block_empty_string():
        chain = Chain()
        try:
            chain.add_block('')
        except AssertionError as error:
            assert isinstance(error, AssertionError)
        else:
            raise AssertionError('Should raise AssertionError')

    def test_add_block_with_none():
        chain = Chain()
        try:
            chain.add_block(None)
        except AssertionError as error:
            assert isinstance(error, AssertionError)
        else:
            raise AssertionError('Should raise AssertionError')

    def test_add_block_with_integer():
        chain = Chain()
        try:
            chain.add_block(1)
        except AssertionError as error:
            assert isinstance(error, AssertionError)
        else:
            raise AssertionError('Should raise AssertionError')

    def test_chain_validation_returns_errors():
        chain = Chain()
        chain.add_block('Alpha')
        chain.add_block('Bravo')
        chain.add_block('Charlie')
        bravo = chain.get_block_by_height(1)
        bravo.height = 5
        errors = chain.validate_chain()
        assert len(errors) == 2, 'Validation failed to find invalid block'

    def test_chain_validation_returns_no_errors():
        chain = Chain()
        chain.add_block('Alpha')
        chain.add_block('Bravo')
        chain.add_block('Charlie')
        errors = chain.validate_chain()
        assert len(errors) == 0, 'Validation failed with false positive'

    def test_block_hashes_are_different():
        chain = Chain()
        chain.add_block('Alpha')
        chain.add_block('Bravo')
        chain.add_block('Charlie')
        for height, block in enumerate(chain):
            if height:
                prev_block = chain.get_block_by_height(height - 1)
                assert prev_block.hash != block.hash, 'Hashes should differ'

    # run tests
    test_add_block_empty_string()
    test_add_block_with_none()
    test_add_block_with_integer()
    test_chain_validation_returns_errors()
    test_chain_validation_returns_no_errors()
    test_block_hashes_are_different()
