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
    assert path_obj.is_dir(), 'Path must be an existing directory'

    path_iter = path_obj.rglob(f'*{suffix}')

    if dirs:
        file_list = [str(f) for f in path_iter]
    else:
        file_list = [str(f) for f in path_iter if f.is_file()]

    return file_list


print(find_files('.gitkeep', './testdir'))

if __name__ == '__main__':
    # Tests
    def test_return_files(suffix, path, expected_count):
        print(f'\nFinding all files in path: "{path}" with suffix: "{suffix}"')
        print(len(find_files(suffix, path)) == expected_count)


    def test_assertion(suffix, path, message):
        print(f'\n{message}')
        try:
            find_files(suffix, path)
        except AssertionError as error:
            assert isinstance(error, AssertionError)
            print(True)
        else:
            print(False)

    # Run tests
    test_return_files('.c', './testdir', 4)
    test_return_files('.gitkeep', './testdir', 2)
    test_return_files('.h', './testdir', 4)
    test_return_files('', './testdir', 10)
    test_return_files('.py', './testdir', 0)
    test_return_files('.py', './testdir', 0)
    test_assertion(None, './testdir', '"None" as suffix raises AssertionError')
    test_assertion(1, './testdir', 'An "int" as suffix raises AssertionError')
    test_assertion('', None, '"None" as path raises AssertionError')
    test_assertion('', 1, 'An "int" as path raises AssertionError')
    test_assertion('.c', './inexistent', 'A path that is not a directory raises AssertionError')
