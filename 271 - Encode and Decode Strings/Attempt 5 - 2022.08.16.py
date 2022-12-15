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
        1. Loop through strs. Calculate the length of each str. Construct a substring of length + # + str. Append the
        substring to the final_arr. Turn the final_arr into a str, and return.
        """
        encoded_str = []
        for my_str in strs:
            length_int = len(my_str)
            substring = str(length_int) + "#" + my_str
            encoded_str.append(substring)
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        Plan:
        1. Collect all the alphas, convert them to int to get the length.
        2. Iterate +2 to get the first character of the str.
        3. Slice from current position to current position + length+1
        4. Append that slice to the decoded_arr.
        5. Iterate +1 to get the next number
        6. Loop until we reach the end of s.
        """
        current = 0
        decoded_str = []
        while current < len(s):
            length_substring = []
            while s[current].isnumeric():
                length_substring.append(s[current])
                current += 1
            length_str = "".join(length_substring)
            length_int = int(length_str)
            current = current + 1
            slice = s[current:current+length_int]
            decoded_str.append(slice)
            current += length_int
        return decoded_str

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
