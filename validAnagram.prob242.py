"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
 
"""

def isAnagram(s, t):
    #dictAnagram = defaultdict(int)
    dictAnagram = {}
    for ch in s:
        if ch in dictAnagram:
            dictAnagram[ch] += 1
        else:
            dictAnagram[ch] = 1
    for ch in t:
        if ch in dictAnagram and dictAnagram[ch] > 0:
            dictAnagram[ch] -= 1
        else:
            return False
    a = sorted(dictAnagram.items(), key = lambda x: x[1], reverse = True)
    if a[0][1] != 0:
        return False
    return True
    """
    if sorted(s) == sorted(t):
        return True
    else:
        return False
    """


print(isAnagram(s = "rat", t = "car"))
    