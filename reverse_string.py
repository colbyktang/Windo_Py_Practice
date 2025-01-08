# This is a solution to a LeetCode's Interview Crash Course: Data Structures and Algorithms problem
# Problem: Reverse String

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = 0
        m = len(s) - 1
        while (n < m):
            print (f"N: {n}, M: {m}")
            s[n], s[m] = s[m], s[n]
            n += 1
            m -= 1

if __name__ == "__main__":
    input = ["h","e","l","l","o"]
    expected_output = ["o","l","l","e","h"]
    sol = Solution()
    print (f"Input: {input}")
    sol.reverseString(input)
    print (f"Expected: {expected_output}")
    print (f"Output: {input}") # Printing input since output is modified in-place