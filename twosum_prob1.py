"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

def twoSum_solution1(nums, target):
    for index,num1 in enumerate(nums):
        num2 = target - num1
        if num2 in nums[index+ 1:]:
            return [index, nums.index(num2,index+1)]

print(twoSum_solution1(nums = [2,7,11,15], target = 9))

def twoSum_solution2(nums, target):
    dict = {}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in dict:
            return [dict[diff],i]
        else:
            dict[num] = i

print(twoSum_solution2(nums = [2,7,11,15], target = 9))
