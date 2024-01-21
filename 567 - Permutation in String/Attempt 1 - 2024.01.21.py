class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        567 - Permutation in String

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
        Hashmap
        1. Create a counts dict. Keys: letters in s1, Values: count of key in s1.
        2. Get the counts_len.
        3. Loop through s2. If a char is found in counts, start the counter. Loop counts_len time, each time checking
        if the next value is in counts. If it reaches the end, return true. Otherwise, restart the counter and the
        new value.
        4. If the s2 loop finishes, then we know that there isn't a permutation in s2, so return False.
        Time: O(n), Space: O(26)
        """
        # ChatGPT Slow
        import collections

        if len(s1) > len(s2):
            return False

        s1_counts = collections.Counter(s1)
        window_count = collections.Counter()

        for i in range(len(s2)):
            window_count[s2[i]] += 1

            if i >= len(s1):
                if window_count[s2[i - len(s1)]] == 1:
                    del window_count[s2[i - len(s1)]]
                else:
                    window_count[s2[i - len(s1)]] -= 1

            if window_count == s1_counts:
                return True

        return False

        # Leetcode Comments Little Faster
        # import collections
        # cntr, w, match = collections.Counter(s1), len(s1), 0
        #
        # for i in range(len(s2)):
        #     if s2[i] in cntr:
        #         if cntr[s2[i]] == 0:
        #             match -= 1
        #         cntr[s2[i]] -= 1
        #         if cntr[s2[i]] == 0:
        #             match += 1
        #
        #     if i >= w and s2[i - w] in cntr:
        #         if cntr[s2[i - w]] == 0:
        #             match -= 1
        #         cntr[s2[i - w]] += 1
        #         if cntr[s2[i - w]] == 0:
        #             match += 1
        #
        #     if match == len(cntr):
        #         return True
        #
        # return False

        # Neetcode Fast
        # if len(s1) > len(s2):
        #     return False
        #
        # s1Count, s2Count = [0] * 26, [0] * 26
        #
        # for i in range(len(s1)):
        #     s1Count[ord(s1[i]) - ord('a')] += 1
        #     s2Count[ord(s2[i]) - ord('a')] += 1
        #
        # matches = 0
        # for i in range(26):
        #     matches += (1 if s1Count[i] == s2Count[i] else 0)
        #
        # l = 0
        # for r in range(len(s1), len(s2)):
        #     if matches == 26:
        #         return True
        #
        #     index = ord(s2[r]) - ord('a')
        #     s2Count[index] += 1
        #     if s1Count[index] == s2Count[index]:
        #         matches += 1
        #     elif s1Count[index] + 1 == s2Count[index]:
        #         matches -= 1
        #
        #     index = ord(s2[l]) - ord('a')
        #     s2Count[index] -= 1
        #     if s1Count[index] == s2Count[index]:
        #         matches += 1
        #     elif s1Count[index] - 1 == s2Count[index]:
        #         matches -= 1
        #     l += 1
        # return matches == 26


result = Solution()
print(result.checkInclusion("ab", "eidbaooo"))  # True
print(result.checkInclusion("ab", "eidboaoo"))  # False
