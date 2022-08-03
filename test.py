from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        print("Starting Output:", output)
        # for num in nums:
            # output += [curr + [num] for curr in output]
            # print("Output this iteration:", output)
        for item in output:
            for num in nums:
                output.append(item+[num])

        return output


result = Solution()
print(result.subsets([1,2,3]))