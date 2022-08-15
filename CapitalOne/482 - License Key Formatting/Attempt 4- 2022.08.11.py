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
        1. Sanitize the string. Delete all of the dashes, and uppercase all of the letters.
        2. Calculate first_group_len. It wil be len(sanitized_s) % k, but if the result = 0, then we should set it to k.
        3. Create a final_arr. Slice first_group_len characters, and append it to the final array.
        4. Loop through the remainder of sanitized_s, and append "-" + k length substring slices to the final array.
        5. Join and return the final array.
        """
        s = s.replace("-", "").upper()
        first_group_len = len(s) % k
        if first_group_len == 0:
            first_group_len = k
        final_arr = []
        first_group_slice = s[:first_group_len]
        final_arr.append(first_group_slice)

        for i in range(first_group_len, len(s), k):
            this_group_slice = s[i:i+k]
            final_arr.append("-" + this_group_slice)

        return "".join(final_arr)


result = Solution()
print(result.licenseKeyFormatting("5F3Z-2e-9-w", 4))  # "5F3Z-2E9W"
print(result.licenseKeyFormatting("2-5g-3-J", 2))  # "2-5G-3J"
