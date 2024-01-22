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
        1. Create s1Counts dict. Keys: Chars in s1, Values: Count of key in s1.
        2. Create s2WindowCounts dict. Keys: Chars in s2's window, Values: Count of keys in s2's window
        3. Handle edge case where len(s1) > len(s2)
        4. Calculate len_of_s1.
        5. l = 0, r = len_of_s1-1
        6. Loop while r < len(s2)
            7. Add s2[r] to s2WindowCounts.
            8. Check if s2[r]
        """
        import collections
        if len(s1) > len(s2):
            return False

        s1Counts = collections.Counter(s1)
        s2Window = collections.Counter()

        for i in range(len(s2)):
            s2Window[s2[i]] += 1

            if i >= len(s1):
                if s2Window[s2[i - len(s1)]] == 1:
                    del s2Window[s2[i - len(s1)]]
                else:
                    s2Window[s2[i - len(s1)]] -= 1

            if s1Counts == s2Window:
                return True

        return False

result = Solution()
print(result.checkInclusion("ab", "eidbaooo"))  # True
print(result.checkInclusion("ab", "eidboaoo"))  # False
