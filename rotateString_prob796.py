"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 
Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:

Input: s = "abcde", goal = "abced"
Output: false

"""

def rotateString(s, goal):
    list_s = list(s)
    list_goal = list(goal)
    count = 0
    while count < len(s):
        list_s.append(list_s.pop(0))
        if list_s ==  list_goal:
            return True
        count += 1
    return False


print(rotateString(s = "abcde", goal = "cdeab"))