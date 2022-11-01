"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1
 
"""

def firstUniqChar(s):
    for index in range(len(s)):
        # the below if condition also works
        #if s.count(s[index]) == 1:
        if s[index] not in s[index+1:] and s[index] not in s[:index]:
            return index
    return -1


print(firstUniqChar("loveleetcode"))
    