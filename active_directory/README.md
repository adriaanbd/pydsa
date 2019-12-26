# Active Directory

The script's purpose is to provide an efficient lookup of whether a user is in a group. A group could consist of both user(s) and group(s).

## Time Complexity Analysis

The time complexity for the function is linear, `O(n)`.

Searching for membership in a set takes O(1) and additional searches for each recursive call take O(n) time, where n represents the number of groups.

## Space Complexity Analysis

The space complexity is multinear, `O(nm)` where n represents the number of groups at one level and m represents the depth of the call stack.
