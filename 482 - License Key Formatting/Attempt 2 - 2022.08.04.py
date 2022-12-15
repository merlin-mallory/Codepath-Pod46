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

        1. Sanitize the string by removing all of the dashes, and uppercasing all of the alpha chars.
        2. Calculate the first_chunk_len, which will be len(sanitized_str) % k
        3. Create a new_str_arr. Splice sanitized_s[0:first_chunk_len]. Append the result to new_str_arr. Iterate i
        to the first_chunk_len position in sanitized_s.
        4. Until we reach the end of the sanitized_str, loop through sanitized_s with k steps. At each step, add a "-"
        character plus k characters from sanitized_str.
        5. Convert the resultant array to a str and return it.
        """

        # Sanitize the string
        sanitized_s = s.replace("-","").upper()
        first_chunk_len = len(sanitized_s) % k

        # Handle the first chunk
        if first_chunk_len == 0:
            first_chunk_len = k
        i = 0
        new_str_arr = []
        new_str_arr.append(sanitized_s[0:first_chunk_len])
        i += first_chunk_len

        print(new_str_arr, i)

        # Handling additional chunks

        while i < len(sanitized_s):
            new_str_arr.append("-" + sanitized_s[i:i+k])
            i += k

        print("After this loop:", new_str_arr, i)

        # Sanitize the result
        return "".join(new_str_arr)




result = Solution()
print(result.licenseKeyFormatting("5F3Z-2e-9-w", 4))  # "5F3Z-2E9W"
print(result.licenseKeyFormatting("2-5g-3-J", 2))  # "2-5G-3J"
