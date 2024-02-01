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
        1. Create t_counts. Init with t. Keys: Unique chars in t. Values: Count of keys.
        2. Create s_window. Init empty. Keys: Unique chars in s. Values: Count of keys.
        3. have = 0, need = len(t_counts)
        4. l = 0, r = 0.
        5. min_substring = [-1, -1]
        6. len_min_substring = float('inf')
        5. Loop while r < len(s).
            6. Add s[r] to s_window.
            7. Update have.
            8. Check if r > len(t), and if so, calculate the cur_len. If cur_len < len_min_substring, then update
            len_min_substring and min_substring. Then remove s[l], update have, l++
            10. r++
        11. Deconstruct min_substring and return the sliced string.
        Edge Cases: None
        Time: O(n)
        Space: O(1)
        '''
        import collections
        t_counts = collections.Counter(t)
        s_window = collections.Counter()
        have, need = 0, len(t_counts)
        min_substring = [-1, -1]
        len_of_min_substring = float('inf')
        l, r = 0, 0

        while r < len(s):
            s_window[s[r]] += 1
            if s_window[s[r]] == t_counts[s[r]]:
                have += 1
            while have == need:
                cur_len = r - l + 1
                if cur_len < len_of_min_substring:
                    min_substring = [l, r]
                    len_of_min_substring = cur_len
                if s_window[s[l]] == t_counts[s[l]]:
                    have -= 1
                s_window[s[l]] -= 1
                l += 1
            r += 1

        l, r = min_substring

        if len_of_min_substring == float('inf'):
            return ''
        else:
            return s[l:r+1]


result = Solution()

print(result.minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(result.minWindow("a", "a"))               # "a"
print(result.minWindow("a", "aa"))              # ""