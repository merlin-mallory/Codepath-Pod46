class Codec:
    """
    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and
    is decoded back to the original list of strings.

    Machine 1 (sender) has the function:

    string encode(vector<string> strs) {
      // ... your code
      return encoded_string;
    }
    Machine 2 (receiver) has the function:
    vector<string> decode(string s) {
      //... your code
      return strs;
    }
    So Machine 1 does:

    string encoded_string = encode(strs);
    and Machine 2 does:

    vector<string> strs2 = decode(encoded_string);
    strs2 in Machine 2 should be the same as strs in Machine 1.

    Implement the encode and decode methods.

    You are not allowed to solve the problem using any serialize methods (such as eval).

    Input: dummy_input = ["Hello","World"]
    Output: ["Hello","World"]
    Explanation:
    Machine 1:
    Codec encoder = new Codec();
    String msg = encoder.encode(strs);
    Machine 1 ---msg---> Machine 2

    Machine 2:
    Codec decoder = new Codec();
    String[] strs = decoder.decode(msg);
    Example 2:

    Input: dummy_input = [""]
    Output: [""]


    """
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        Plan:
        1. Create final_str as an array
        2. Loop through strs.
            3. Get the length of each str, and append str_len + "#" + str to the final array..
        4. Join and return the final array
        """
        final_str = []
        for cur_str in strs:
            final_str.append(str(len(cur_str)) + "#" + cur_str)
        return "".join(final_str)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        Plan:
        1. Calculate the cur_str_len by scanning right until we reach "#", converting the string into an int.
        2. i + 1 to move beyond the "#" char
        3. Append sliced_str to the final_arr.
        4. Return final_arr.
        """
        final_arr = []

        i = 0
        while i < len(s):
            target_len_arr = []
            while s[i].isdigit():
                target_len_arr.append(s[i])
                i += 1
            target_len = int(''.join(target_len_arr))

            i += 1

            sliced_str = s[i:i+target_len]
            final_arr.append(sliced_str)

            i += target_len

        return final_arr


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
