"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
 
"""
def generate(numRows):
    outerList =[]
    count = 1
    while count <= numRows:
        innerList = []
        if count == 1:
            innerList.append(1)
            outerList.append(innerList)
            count += 1
        elif count == 2:
            innerList.append(1)
            innerList.append(1)
            outerList.append(innerList)
            count += 1
        else:
            index = 0
            while index <= len(outerList[-1]):
            #for index in range(len(outerList[-1]) + 1):
                if index == 0:
                    innerList.append(outerList[-1][index])
                else:
                    if index == len(outerList[-1]):
                        innerList.append(outerList[-1][index - 1])
                    else:
                        innerList.append(outerList[-1][index - 1] + outerList[-1][index])    
                index += 1
                #print(innerList)
            outerList.append(innerList)
            count += 1                            
    return outerList

print(generate(5))
    