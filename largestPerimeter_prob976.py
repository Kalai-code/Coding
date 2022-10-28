"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:

Input: nums = [2,1,2]
Output: 5

Example 2:

Input: nums = [1,2,1]
Output: 0
 
"""

def largestPerimeter(nums):
    nums.sort(reverse = True)
    for index in range(len(nums) - 2):
        if nums[index] < nums[index + 1] + nums[index + 2]:
            return nums[index] + nums[index + 1] + nums[index + 2]
    return 0

print(largestPerimeter([2,1,2]))
    