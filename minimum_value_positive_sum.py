# This is a solution to a LeetCode's Interview Crash Course: Data Structures and Algorithms problem
# Problem: Minimum Value to Get Positive Step by Step Sum

from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        min_sum = 0
        for num in nums:
            total += num
            min_sum = min(min_sum, total)
        return -min_sum + 1
    
if __name__ == "__main__":
    input = [-3,2,-3,4,2]
    expected_output = 5
    sol = Solution()
    output = sol.minStartValue(input)
    print (f"Input: {input}")
    print (f"Expected: {expected_output}")
    print (f"Output: {output}")