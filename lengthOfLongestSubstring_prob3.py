"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
def lengthOfLongestSubstring(s):  
    if len(s) > 2:
        longStr = 0
        index = 0
        while index <= len(s) - 2:
            print(index)
            nonRepeat = s[index]
            for ch in s[index + 1:]:
                if ch not in nonRepeat:
                    nonRepeat += ch
                else:
                    index += 1
                    if longStr < len(nonRepeat):
                        longStr = len(nonRepeat)
                    break
        return longStr 
    else:
        return len(set(s))
"""
def lengthOfLongestSubstring(s):  
    if len(s) > 2:
        index = 0
        longNonRepeatStrCount = 0
        while index <= len(s) - 2:
            nonRepeatStr = []
            nonRepeatStr.append(s[index])
            if len(s[index + 1:]) >= longNonRepeatStrCount:
                for ch in s[index + 1:]:
                    if ch not in nonRepeatStr:
                        nonRepeatStr.append(ch)
                    else:
                        break
                index += 1
                if len(nonRepeatStr) > longNonRepeatStrCount:
                    longNonRepeatStrCount = len(nonRepeatStr)
            else:
                return longNonRepeatStrCount
        return longNonRepeatStrCount    
    else:
        return len(set(s))



print(lengthOfLongestSubstring("pwwkew"))