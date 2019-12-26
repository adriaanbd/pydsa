from hashlib import sha256
from datetime import datetime
import json


class Block:
    def __init__(self, data):
        self.data = data
        self.height = -1
        self.timestamp = datetime.utcnow().__str__()
        self.prev_hash = None
        self.hash = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        bytes_str = data.encode('utf-8')
        self._data = bytes_str.hex()

    def validate_block(self):
        aux_hash = self.hash
        self.hash = None
        is_valid = self.calc_hash() == aux_hash
        self.hash = aux_hash
        return is_valid

    def calc_hash(self):
        sha = sha256()
        enc_type = 'utf-8'
        sha.update(self.data.encode(enc_type))
        sha.update(self.timestamp.encode(enc_type))
        sha.update(str(self.height).encode(enc_type))
        if self.prev_hash:
            sha.update(self.prev_hash.encode(enc_type))
        return sha.hexdigest()

    @property
    def block_data(self):
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
        self.chain = []

    def add_block(self, data):
        assert isinstance(data, str), 'Data must be a string'
        assert len(data) > 0, 'Cannot create Block with empty data'
        block = self._create_block(data)
        self.chain.append(block)

    def _create_block(self, data):
        block = Block(data)
        block.height = len(self.chain)
        if len(self.chain) > 0:
            prev_block = self.chain[len(self.chain) - 1]
            block.prev_hash = prev_block.hash
        block.hash = block.calc_hash()
        return block

    def get_block_by_height(self, height):
        assert isinstance(height, int), 'Height must be an integer'
        assert 0 <= height < len(self.chain), 'Height is invalid'
        return self.chain[height]

    def get_block_by_hash(self, hash_str):
        assert isinstance(hash_str, str), 'Hash must be a string'
        for block in self.chain:
            if block.hash == hash_str:
                return block

    def validate_chain(self):
        errors = []
        for height, block in enumerate(self.chain):
            if not block.validate_block():
                errors.append({
                    'error': 'invalid block',
                    'block': block
                    })
            if height:
                prev_block = self.chain[height - 1]
                has_invalid_hashes = prev_block.hash != block.prev_hash
                if has_invalid_hashes:
                    errors.append({
                        'error': 'discrepancy between blocks',
                        'current': block,
                        'previous': prev_block
                        })
        return errors

    def __repr__(self):
        return f'{self.chain}'

    def __str__(self):
        return f'{self.chain}'
