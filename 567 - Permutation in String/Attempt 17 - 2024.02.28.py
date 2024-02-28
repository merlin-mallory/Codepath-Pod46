class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        https://leetcode.com/problems/permutation-in-string/

        Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

        In other words, return true if one of s1's permutations is the substring of s2.

        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").

        Input: s1 = "ab", s2 = "eidboaoo"
        Output: false

        Constraints:
        1 <= s1.length, s2.length <= 104
        s1 and s2 consist of lowercase English letters.

        Plan:
        Sliding Window
        Create s1_counter and s2_window Counter dicts.
        Loop through s2
            Add s2[r] to s2_window.
            if r >= len(s1), remove s[l] from s2_window and l++
            Check if s1_counts == s2_window, if so, return True
            r++
        If the loop completes without returning true, then we've verified that a match does not exist, so return False.
        Time: O(n)
        Space: O(1)
        Edge: None (We will assume that permutations can include multiple non-unique chars)
        """
        import collections
        s1_counts = collections.Counter(s1)
        s2_window = collections.Counter()
        l, r = 0, 0
        while r < len(s2):
            s2_window[s2[r]] += 1
            if r >= len(s1):
                if s2_window[s2[l]] == 1:
                    del s2_window[s2[l]]
                else:
                    s2_window[s2[l]] -= 1
                l += 1
            if s1_counts == s2_window:
                return True
            r += 1
        return False

result = Solution()
print(result.checkInclusion("ab", "eidbaooo"))  # True
print(result.checkInclusion("ab", "eidboaoo"))  # False
