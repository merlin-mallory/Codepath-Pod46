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
        1. Create s1_counts dict, and populate with s1. Keys: Chars in s1, Values: Count of keys.
        2. Create s2_window dict. Starts empty, but will contain Keys: Chars in s2's window, Values: Count of key.s
        3. l = 0, loop r to len(s2).
            4. Add s2[r] to s2_window
            5. If r > len(s1), then decrement the [r - len(s1] value from s2_window.
            6. Check if s1_counts == s2_window. This means we have a perfect match, so return true.
        7. Otherwise, if the loop has completed and we haven't found a perfect match, then return False.
        Time Complexity: O(n), Space Complexity: O(n)
        Edge Cases: None
        """
        import collections

        s1_counts = collections.Counter(s1)
        s2_window = collections.Counter()

        l = 0

        for r in range(len(s2)):
            s2_window[s2[r]] += 1

            if r >= len(s1):
                if s2_window[s2[r - len(s1)]] == 1:
                    del s2_window[s2[r - len(s1)]]
                else:
                    s2_window[s2[r - len(s1)]] -= 1
                l += 1

            if s1_counts == s2_window:
                return True

        return False

result = Solution()
print(result.checkInclusion("ab", "eidbaooo"))  # True
print(result.checkInclusion("ab", "eidboaoo"))  # False
