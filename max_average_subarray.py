from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumNums = 0
        for i in range(k):
            sumNums += nums[i]
        ans = sumNums / k
        
        left = 0
        right = k - 1
        
        while right < len(nums)-1:
            right += 1
            print (f"Right:{right} Left:{left}")
            sumNums += nums[right] 
            sumNums -= nums[left]
            left += 1
            ans = max(ans, sumNums / k)
        
        return ans
    
if __name__ == "__main__":
    input = [1,12,-5,-6,50,3]
    k = 4
    expected_output = 12.75000
    sol = Solution()
    output = sol.findMaxAverage(input, k)
    print (f"Input: {input}, k: {k}")
    print (f"Expected: {expected_output}")
    print (f"Output: {output}")