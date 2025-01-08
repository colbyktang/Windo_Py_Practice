# This is a solution to a LeetCode's Interview Crash Course: Data Structures and Algorithms problem
# Problem: K Radius Subarray Averages

# You are given a 0-indexed array nums of n integers, and an integer k.
# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
# The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.
# For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

# Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
# Output: [-1,-1,-1,5,4,4,-1,-1,-1]
# Explanation:
# - avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
# - The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
#   Using integer division, avg[3] = 37 / 7 = 5.
# - For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
# - For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
# - avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.


from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return nums
        window_size = (k*2)+1
        n = len(nums)
        averages = [-1] * n
        
        if window_size > n: return averages
        
        # first window sum
        window_sum = 0
        for i in range(window_size):
            window_sum += nums[i]
        averages[k] = window_sum // window_size

        for i in range(window_size, n):
            window_sum = window_sum + (nums[i] - nums[i - window_size])
            averages[i - k] = window_sum // window_size

        return averages
    
if __name__ == "__main__":
    input = [7,4,3,9,1,8,5,2,6]
    k = 3
    expected_output = [-1,-1,-1,5,4,4,-1,-1,-1]
    sol = Solution()
    output = sol.getAverages(input, k)
    print (f"Input: {input}, k: {k}")
    print (f"Expected: {expected_output}")
    print (f"Output: {output}")