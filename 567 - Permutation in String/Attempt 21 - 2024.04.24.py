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
        Time: O(n)
        Space: O(n)
        Edge: None
        """
        import collections
        s1_counter = collections.Counter(list(s1))
        s2_window = collections.Counter()
        # print(s1_counter)
        l, r = 0, 0
        while r < len(s2):
            # print("begin: ", s2_window)
            s2_window[s2[r]] += 1
            if r >= len(s1):
                if s2_window[s2[l]] == 1:
                    del s2_window[s2[l]]
                else:
                    s2_window[s2[l]] -= 1
                l += 1
            r += 1
            if s1_counter == s2_window: return True
            # print("end: ", s2_window)
        return False

result = Solution()
print(result.checkInclusion("ab", "eidbaooo"))  # True
print(result.checkInclusion("ab", "eidboaoo"))  # False
