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
        1. Create s1dict. Keys: chars in s1, Values: Counts of keys.
        2. Create s2window. Keys: chars in the current window for s2, Values: Counts of keys.
        3. l = 0, r Loops through s2.
            4. Add s2[r] to s2window
            4. If r >= len(s1), then check if s1window[s2[r - len(s1)] >= s2window[s2[r - len(s1)]]
        """
        import collections
        s1_dict = collections.Counter(s1)
        s2_window = collections.Counter()

        for i in range(len(s2)):
            s2_window[s2[i]] += 1

            if i >= len(s1):
                # Delete the left term
                if s2_window[s2[i - len(s1)]] == 1:
                    del s2_window[s2[i - len(s1)]]
                else:
                    s2_window[s2[i - len(s1)]] -= 1

            if s1_dict == s2_window:
                return True

        return False

result = Solution()
print(result.checkInclusion("ab", "eidbaooo"))  # True
print(result.checkInclusion("ab", "eidboaoo"))  # False
