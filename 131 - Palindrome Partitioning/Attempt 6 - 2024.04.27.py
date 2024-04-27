from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        131 - Palindrome Partitioning

        https://leetcode.com/problems/palindrome-partitioning/

        Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible
        palindrome partitioning of s.

        Example 1:
        Input: s = "aab"
        Output: [["a","a","b"],["aa","b"]]

        Example 2:
        Input: s = "a"
        Output: [["a"]]

        Constraints:
        1 <= s.length <= 16
        s contains only lowercase English letters.

        Plan:
        Backtracking
        Time: O(n * 2^n)
        Space: O(n)
        Edge: None
        '''
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        stack = []
        final_arr = []
        def backtrack(i):
            if i == len(s):
                final_arr.append(stack[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s,i,j):
                    stack.append(s[i:j+1])
                    backtrack(j+1)
                    stack.pop()
        backtrack(0)
        return final_arr

result = Solution()
print(result.partition("aab"))  # [["a","a","b"],["aa","b"]]
print(result.partition("a"))    # [["a"]]
