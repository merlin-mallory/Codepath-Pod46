class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        567 - Minimum Window Substring

        https://leetcode.com/problems/minimum-window-substring/

        Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
        every character in t (including duplicates) is included in the window. If there is no such substring, return
        the empty string "".

        The testcases will be generated such that the answer is unique.

        Example 1:
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

        Example 2:
        Input: s = "a", t = "a"
        Output: "a"
        Explanation: The entire string s is the minimum window.

        Example 3:
        Input: s = "a", t = "aa"
        Output: ""
        Explanation: Both 'a's from t must be included in the window.
        Since the largest window of s only has one 'a', return empty string.

        Constraints:
        m == s.length
        n == t.length
        1 <= m, n <= 105
        s and t consist of uppercase and lowercase English letters.

        Plan:
        Sliding Window
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        import collections
        t_counts = collections.Counter(t)
        s_counts = collections.Counter()
        min_sub = [-1, -1]
        min_sub_len = float('inf')
        l, r = 0, 0
        have, need = 0, len(t_counts)
        while r < len(s):
            s_counts[s[r]] += 1
            if t_counts[s[r]] == s_counts[s[r]]:
                have += 1
            while have == need:
                cur_len = r - l + 1
                if cur_len < min_sub_len:
                    min_sub_len = cur_len
                    min_sub = [l, r]

                if t_counts[s[l]] == s_counts[s[l]]:
                    have -= 1
                s_counts[s[l]] -= 1
                l += 1
            r += 1

        l, r = min_sub[0], min_sub[1]
        if min_sub_len == float('inf'):
            return ""
        else:
            return s[l:r+1]


result = Solution()

print(result.minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(result.minWindow("a", "a"))               # "a"
print(result.minWindow("a", "aa"))              # ""