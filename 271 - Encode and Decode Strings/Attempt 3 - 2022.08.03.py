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
    # My only mistake was joining the decoded string's final input. Only the encoded function needs to join the arrays.

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        Plan:
        1. We will encode the length of the string + # + the actual string. We'll append them to an array to start,
        and then join them into a single string later.
        """
        encoded_str = []
        for my_str in strs:
            substring = str(len(my_str)) + "#" + my_str
            encoded_str.append(substring)
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        final_arr = []
        while i <= len(s)-1:
            substring = []
            substring.append(s[i])
            while s[i+1] != "#":
                i += 1
                substring.append(s[i])
            my_length = int("".join(substring))
            desired_str_slice = s[(i+2):(i+2+my_length)]
            final_arr.append(desired_str_slice)
            i += 2 + my_length
        return final_arr


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
