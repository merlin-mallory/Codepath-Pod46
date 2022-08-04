class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        You are given a license key represented as a string s that consists of only alphanumeric characters and
        dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

        We want to reformat the string s such that each group contains exactly k characters, except for the first
        group, which could be shorter than k but still must contain at least one character. Furthermore, there must
        be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

        Return the reformatted license key.

        Input: s = "5F3Z-2e-9-w", k = 4
        Output: "5F3Z-2E9W"
        Explanation: The string s has been split into two parts, each part has 4 characters.
        Note that the two extra dashes are not needed and can be removed.

        Input: s = "2-5g-3-J", k = 2
        Output: "2-5G-3J"
        Explanation: The string s has been split into three parts,
        each part has 2 characters except the first part as it could be shorter as mentioned above.

        Constraints:

        1 <= s.length <= 10^5
        s consists of English letters, digits, and dashes '-'.
        1 <= k <= 10^4

        Plan:
        1. We're going to loop through s until we encounter the first dash. Then we'll create a substring arr
        containing["-"], and continue iterating through s until we've collected k alphanumeric characters (sanitizing
        the alphas to be uppercase) in the substring. I guess we'll need the substring to grab the first chunk as well.
        2. Join and return the final_arr
        """
        # Failed attempt. If the input "2-4A0r7-4k", 4, then the output should be "24A0-R74K". Basically I need to
        # sanitize the string of dashes (and upper), and then use the modular operator to figure out the length of the
        # first group. Then grab that many characters for the first group. I think the plan for the remaining groups
        # worked fine, my result passed the more normal test cases. I didn't really understand the syntax

        # Eliminate all dashes
        S = S.replace('-', '')

        head = len(S) % K

        grouping = []

        # Special handle for first group
        if head:
            grouping.append(S[:head])

        # General case:
        for index in range(head, len(S), K):
            grouping.append(S[index: index + K])

        # Link each group togetger and separated by dash '-'
        return '-'.join(grouping).upper()

        # My failed attempt:
        # final_arr = []
        # substring_arr = []
        # i = 0
        #
        # while i < len(s):
        #     # Find the first chunk.
        #     if len(final_arr) == 0:
        #         if s[i] != "-":
        #             substring_arr.append(s[i].upper())
        #             i += 1
        #         else:
        #             final_arr.append("".join(substring_arr))
        #             i += 1
        #             substring_arr = []
        #
        #     # Find all remaining chunks
        #     else:
        #         if s[i] == "-":
        #             i += 1
        #         elif len(substring_arr) == 0:
        #             substring_arr.append("-")
        #             while i < len(s) and len(substring_arr)-1 < k:
        #                 if s[i] == "-":
        #                     i += 1
        #                 else:
        #                     substring_arr.append(s[i].upper())
        #                     i += 1
        #             final_arr.append("".join(substring_arr))
        #             i += 1
        #             substring_arr = []
        #
        # return "".join(final_arr)






result = Solution()
print(result.licenseKeyFormatting("5F3Z-2e-9-w", 4))  # "5F3Z-2E9W"
print(result.licenseKeyFormatting("2-5g-3-J", 2))  # "2-5G-3J"
