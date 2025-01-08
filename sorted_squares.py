# This is a solution to a LeetCode's Interview Crash Course: Data Structures and Algorithms problem
# Problem: Squares of a Sorted Array

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret_nums = []
        left = 0
        right = len(nums) - 1
        while (left <= right):
            left_sq = nums[left]*nums[left]
            right_sq = nums[right]*nums[right]
            if (left_sq > right_sq):
                ret_nums.insert(0,left_sq)
                left += 1
            else:
                ret_nums.insert(0,right_sq)
                right -= 1

        return ret_nums

if __name__ == "__main__":
    input = [-4,-1,0,3,10]
    expected_output = [0,1,9,16,100]
    sol = Solution()
    output = sol.sortedSquares(input)
    print (f"Input: {input}")
    print (f"Expected: {expected_output}")
    print (f"Output: {output}")