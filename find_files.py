# https://www.python.org/dev/peps/pep-0428/#directory-walking
# https://docs.python.org/3/library/pathlib.html
# https://pathlib.readthedocs.io/en/pep428/
# https://bitbucket.org/pitrou/pathlib/src/default/pathlib.py

# rglob https://bitbucket.org/pitrou/pathlib/src/1f9672002e3a5e54c48dd48912cc6d45f8a2137d/pathlib.py#lines-1218
# fundamental functionality here: https://bitbucket.org/pitrou/pathlib/src/1f9672002e3a5e54c48dd48912cc6d45f8a2137d/pathlib.py#lines-638

from pathlib import Path


def check_types(suffix, path):
    assert isinstance(suffix, str), 'Suffix must be a string'
    assert isinstance(path, str), 'Path must be a string'


def find_files(suffix: str, path: str, dirs=False) -> list:
    check_types(suffix, path)

    path_obj = Path(path)
    path_iter = path_obj.rglob(f'*{suffix}')

    if dirs:
        file_list = [str(f) for f in path_iter]
    else:
        file_list = [str(f) for f in path_iter if f.is_file()]

    return file_list


if __name__ == '__main__':
    path = './testdir'
    suffix = '.c'
    print(find_files(suffix, path))
