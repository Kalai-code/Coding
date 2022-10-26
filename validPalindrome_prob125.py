"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""

def isPalindrome(s):
    startIndex = 0
    endIndex = len(s) - 1
    while startIndex < endIndex:
        if s[startIndex].isalnum() and s[endIndex].isalnum():
            if s[startIndex].lower() == s[endIndex].lower():
                startIndex += 1
                endIndex -= 1
            else:
                return False
        else:
            if not s[startIndex].isalnum():
                startIndex += 1
                continue
            if not s[endIndex].isalnum():
                endIndex -= 1
                continue
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))