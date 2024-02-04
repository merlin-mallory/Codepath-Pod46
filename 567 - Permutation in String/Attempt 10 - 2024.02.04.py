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
        1. Create s1_counts. Init with s1. Keys: Unique chars in s1. Values: Count of keys.
        2. Create s2_window. Init empty. Keys: Unique chars in s2's window. Values: Count of Keys.
        3. l = 0, r = 0
        4. Loop while r < len(s2).
            5. Add s2[r] to s2_window.
            6. If r+1 > len(s1), then delete s2[l] from the window and l++.
            7. Check if s1_counts == s2_window, and if so, return true.
        8. Return false, because we've confirmed that a permutation does not exist.
        Time: O(n)
        Space: O(26)
        Edge: None
        """
        import collections
        s1_counts = collections.Counter(s1)
        s2_window = collections.Counter()
        l, r = 0, 0
        while r < len(s2):
            s2_window[s2[r]] += 1
            if r+1 > len(s1):
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
