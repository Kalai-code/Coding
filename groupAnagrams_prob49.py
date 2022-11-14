"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

def groupAnagrams(strs):
    outerList =[]
    while len(strs) > 0:
        innerList = []
        compareItem = strs.pop(-1)
        compareItemLength = len(compareItem)
        innerList.append(compareItem)
        sortedItem = sorted(compareItem)
        AnagramList = [x for x in strs if len(x) == compareItemLength]
        for item in AnagramList:
            if  sortedItem == sorted(item):
                innerList.append(item)
                strs.remove(item)
        outerList.append(innerList)
    return outerList

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))