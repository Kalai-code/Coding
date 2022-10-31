"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 
Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
"""

def areAlmostEqual(s1, s2):
    count = 0
    if s1 == s2:
        return True
    if sorted(s1) == sorted(s2):
        for ch1, ch2 in zip(s1,s2):
            if ch1 != ch2:
                count += 1
            if count > 2:
                return False
        if count == 2:
            return True
    else:
        return False


print(areAlmostEqual(s1 = "kelb", s2 = "kelb"))