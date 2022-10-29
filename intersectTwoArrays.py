import collections
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as 
it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
def intersect_solution1(nums1, nums2):
    num1counter = collections.Counter(nums1)
    output = []
    for num in nums2:
        if num1counter[num] > 0:
            num1counter[num] -= 1
            output.append(num)
    return output


print(intersect_solution1(nums1 = [1,2,2,1], nums2 = [2,2]))


def intersect_solution2(nums1, nums2):
    result_nums = []
    for num in nums1:
        if num in nums2:
            result_nums.append(num)
            nums2.remove(num)
    return result_nums


print(intersect_solution2(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))