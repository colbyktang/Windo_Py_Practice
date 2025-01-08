# This is a solution to a LeetCode's Interview Crash Course: Data Structures and Algorithms problem
# Problem: Running Sum of 1d Array

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(nums[i] + ans[i-1])
        return ans
    
if __name__ == "__main__":
    input = [1,2,3,4]
    expected_output = [1,3,6,10]
    sol = Solution()
    output = sol.runningSum(input)
    print (f"Input: {input}")
    print (f"Expected: {expected_output}")
    print (f"Output: {output}")