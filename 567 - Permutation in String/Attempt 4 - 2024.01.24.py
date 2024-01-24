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
        1. Create s1_dict. Keys: Chars in s1, Values: Count of key in s1.
        2. Create window_dict. Starts empty, but will contain Keys: Chars in window, and Values: Count of keys in
        window.
        3. l = 0. Loop until the end of s2.
            4. Calculate current_val.
            5. Add current_val to window_dict.
            6. If r > len(s1), then remove s2[l] and l++
            7. If s1_dict == window, then return True
        8. Return False
        """
        import collections
        s1_dict = collections.Counter(s1)
        window_dict = collections.Counter()

        for i in range(len(s2)):
            window_dict[s2[i]] += 1

            if i >= len(s1):
                if window_dict[s2[i - len(s1)]] == 1:
                    del window_dict[s2[i - len(s1)]]
                else:
                    window_dict[s2[i - len(s1)]] -= 1

            if s1_dict == window_dict:
                return True

        return False

result = Solution()
print(result.checkInclusion("ab", "eidbaooo"))  # True
print(result.checkInclusion("ab", "eidboaoo"))  # False
