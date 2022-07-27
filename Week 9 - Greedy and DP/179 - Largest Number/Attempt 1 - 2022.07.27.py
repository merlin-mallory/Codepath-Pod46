class Solution:
    def largestNumber(self, nums) -> str:
        '''
        Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

        Since the result may be very large, so you need to return a string instead of an integer.

        Input: nums = [10,2]
        Output: "210"

        Input: nums = [3,30,34,5,9]
        Output: "9534330"

        Constraints:
        1 <= nums.length <= 100
        0 <= nums[i] <= 109

        Plan:
        1. Convert each element in the array to arrays of digits.
        2. Create a final return array, an array to keep track of each index in the element, as well as a string that
        will keep track of the added indexes.
        3. While the length of the final return array != length of nums:
            4. Loop through unvisited nums, and select the index that has the highest [0] index. Turn that array into a
            string, add it to the final return string, and mark that index as visited. Increment through indexes.
        '''
        import collections
        final_str = str()
        element_to_arr_dict = {}
        num_of_digits_in_nums = 0
        unvisited_nums = [0] * len(nums)

        for i in range(len(nums)):
            element_to_arr_dict[i] = [int(x) for x in str(nums[i])]
            num_of_digits_in_nums += len(element_to_arr_dict.get(i))
        print(element_to_arr_dict)

        current_i_arr = [0] * len(nums)

        current_index = 0
        while len(final_str) != num_of_digits_in_nums:
            current_optimal_element = None
            if unvisited_nums[current_index] == 0:
                if current_optimal_element is None:
                    current_optimal_element = current_index
                elif current_optimal_element


        return final_str

result = Solution()
final_result = result.largestNumber([3,30,34,5,9])
print(final_result)
