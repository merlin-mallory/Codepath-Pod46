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
        1. Create s1_counts. Keys: Chars in s1, Values: Count of keys.
        2. Create s2_window. Initialized empty, but will contain Keys: Chars in current window, and Values: Count of
        keys.
        3. l = 0
        4. Loop r until end of s2[r].
            5. Add s2[r] to s2_window.
            6. If r >= len(s1_counts)
                7. Subtract s2[l] from s2_window, and iterate l
            8. Check if s1_counts == s2_window. This means we found a match, so return true
        9. Otherwise, if r reaches the end and we haven't found a match, then return false.
        """
        import collections
        s1_counts = collections.Counter(s1)
        s2_window = collections.Counter()

        for i in range(len(s2)):
            s2_window[s2[i]] += 1

            if i >= len(s1):
                if s2_window[s2[i - len(s1)]] == 1:
                    del(s2_window[i - len(s1)])
                else:
                    s2_window[s2[i - len(s1)]] -= 1

            if s1_counts == s2_window:
                return True

        return False


result = Solution()
print(result.checkInclusion("ab", "eidbaooo"))  # True
print(result.checkInclusion("ab", "eidboaoo"))  # False
