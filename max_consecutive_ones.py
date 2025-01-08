# This is a solution to a LeetCode's Interview Crash Course: Data Structures and Algorithms problem
# Problem: Maximum Consecutive Ones III

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr = ans = left = 0
        for right in range (len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
    
if __name__ == "__main__":
    input = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    expected_output = 6
    sol = Solution()
    output = sol.longestOnes(input, k)
    print (f"Input: {input}, k: {k}")
    print (f"Expected: {expected_output}")
    print (f"Output: {output}")