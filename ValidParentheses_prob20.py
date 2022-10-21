"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""
def isValid(s):
    parenList = []
    openParen = ['(','[','{']
    if len(s) % 2 != 0:
        return False
    else:
        for ch in s:
            if ch in openParen:
                parenList.append(ch)
            elif len(parenList) > 0:
                if ch == ')' and parenList[-1] == '(':
                    parenList.pop()
                elif ch == ']' and parenList[-1] == '[':
                    parenList.pop()
                elif ch == '}' and parenList[-1] == '{':
                    parenList.pop()                
                else:
                    return False
            else:
                return False
    if len(parenList) == 0:
        return True
    else:
        return False


print(isValid("()[]{}"))