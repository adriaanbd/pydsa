# Find Files

The script's main functionality is to find all files with a specific `suffix` under a target directory. It accomplishes this by using Python's pathlib's `Path.rgblob` [method](https://bitbucket.org/pitrou/pathlib/src/1f9672002e3a5e54c48dd48912cc6d45f8a2137d/pathlib.py#lines-1218), which "recursively yields all existing files [...] matching the given pattern [...]" under a subtree. Setting the `dirs` option to `True`, will also yield all directories matching the given `suffix`.

## Time and Space Complexity Analysis

Here's the complexity analysis for the `find_files` function in terms of *Big O* of its core functionality. Please note that `rglob` utilizes the `WildCardSelector` class of Pathlib, particularly its private `_select_from` [method](https://bitbucket.org/pitrou/pathlib/src/1f9672002e3a5e54c48dd48912cc6d45f8a2137d/pathlib.py#lines-644).

### Time Complexity

The complexity is `O(n * m)` where `n` represents the number of items at the first level of the tree (level 0 being the provided `path` as root) and `m` represents the number of levels or depth of all subdirectories under the root.

### Space Complexity

The complexity is `O(n * m)` where `n` represents the number of items at the first level of the tree, representing the first item on the call stack after the root directory, and `m` represents the number of levels or depth of the call stack as each subdirectory is added onto it. Similar to the following stack.

This is called `n` times and `m` represents the subdirectories.
```
dir3
dir2
dir1
root
```

## Future enhancements

* **Implementing a CLI interface like `$ find_files.py suffix path output_file -option`**

Example:

```
$ find_files.py .gitkeep ./testdir
testdir/subdir4/.gitkeep
testdir/subdir2/.gitkeep
```

* **Specifying an output file like `$ find_files.py suffix path output_file_name`**

Example:

```
$ find_files.py .c ./testdir files.txt
$ cat files.txt
Scanned on: 12-21-2019 12:00:00.000000
testdir/subdir4/.gitkeep
testdir/subdir2/.gitkeep
```

* **Isolating and adding more tests**

The tests are currently minimal and in the main script. I'd like to add more tests and have them in their own file, using either `unittest` or `pytest`.

## How to Contribute

If you'd like to add any feature to this script feel free to clone this repository and submit a PR with your suggested changes. I'd be happy to discuss.

## Sources

1. PEP 0428 [here](https://www.python.org/dev/peps/pep-0428/#directory-walking)
2. Pathlib's docs 1 [here](https://docs.python.org/3/library/pathlib.html)
3. Pathlib's docs 2 [here](https://pathlib.readthedocs.io/en/pep428/)
4. Pathlib's source code [here](https://bitbucket.org/pitrou/pathlib/src/default/pathlib.py)
5. `Path.rglob` [here](https://bitbucket.org/pitrou/pathlib/src/1f9672002e3a5e54c48dd48912cc6d45f8a2137d/pathlib.py#lines-1218)
6. Pathlib's `WildCardSelector` [here](https://bitbucket.org/pitrou/pathlib/src/1f9672002e3a5e54c48dd48912cc6d45f8a2137d/pathlib.py#lines-638)
