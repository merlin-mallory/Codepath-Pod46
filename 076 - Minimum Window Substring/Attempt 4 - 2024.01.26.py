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
        1. Create t_counts, fill it with t. Keys: Chars in t, Values: Count of keys.
        2. Create s_window, initially empty. But will contain Keys: Chars in s's window, Values: Count of keys.
        3. Initialize minimum_substring = [-1,-1]. This will hold the l and r values for the minimum valid substring.
        4. Initialize len_of_minimum_substring = inf. Also set l = 0. Set have = 0, and need = len(t_counts
        5. Loop r to len(s).
            6. Add s[r] to s_window.
            7. if t_counts[s[r]] == s_window[s[r]], then have++
            8. Check if we have a valid substring (need == have). If we do, then calculate the current_len,
            and update minimum_substring, and then iterate l (removing from s_window) until need != have.
        9. Deconstruct minimum_substring and return the slice.
        Time Complexity: Time: O(n), Space: O(n)
        Edge Case: If len is still inf at the end, then return empty string. Otherwise, return minimum_substring.
        '''

        import collections
        t_counts = collections.Counter(t)
        s_window = collections.Counter()
        minimum_substring = [-1, -1]
        len_of_minimum_substring = float('inf')
        have, need = 0, len(t_counts)
        l, r = 0, 0

        for r in range(len(s)):
            s_window[s[r]] += 1
            if (s[r] in t_counts) and (s_window[s[r]] == t_counts[s[r]]):
                have += 1
            while need == have:
                current_len = r - l + 1
                if current_len < len_of_minimum_substring:
                    len_of_minimum_substring = current_len
                    minimum_substring = [l, r]
                s_window[s[l]] -= 1
                if (s[l] in t_counts) and (s_window[s[l]] < t_counts[s[l]]):
                    have -= 1
                l += 1

        l, r = minimum_substring
        if len_of_minimum_substring == float('inf'):
            return ""
        else:
            return s[l:r+1]


result = Solution()

print(result.minWindow("ADOBECODEBANC", "ABC")) # "ABC"
print(result.minWindow("a", "a"))               # "a"
print(result.minWindow("a", "aa"))              # ""