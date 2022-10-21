"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix_solution1(strs):
    subStr = ""
    if len(strs) > 1:
        for index, ch in enumerate(strs[0]):            
            for word in strs[1:]:
                if len(word) > index and word[index] == ch:
                    continue
                else:
                    return subStr
            subStr += ch
            #print(subStr)
        return subStr
    elif len(strs) == 1:
        return strs[0]
    else:
        return ""

print(longestCommonPrefix_solution1(["flower","flow","flight"]))

def longestCommonPrefix_solution2(strs):
    output = ""
    i = 0
    while i < len(strs[0]):
        tempStr = strs[0][:i+1]
        for j in range(1,len(strs)):
            if tempStr != strs[j][:i+1]:
                return output
        output = tempStr
        i = i+1
    return output


print(longestCommonPrefix_solution2(["flower","flow","flight"]))