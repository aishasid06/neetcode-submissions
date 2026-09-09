class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for index, num in enumerate(nums):
            differences[num] = index

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in differences and differences[difference]!= i:
                return [i, differences[difference]]
