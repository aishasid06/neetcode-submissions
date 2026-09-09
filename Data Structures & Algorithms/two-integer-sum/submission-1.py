class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        differences = {}
        for index, num in enumerate(nums):
            differences[num] = index

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in differences and differences[difference]!= i:
                return [i, differences[difference]]


        The above works for [5, 5] b/c the first past updates the index of 5 to 1 from 0.
        Since we iterate from the start in the second pass, the first 5 is encoutered.
        Hence the indices of the two 5s appear to be different.
        We can also do one-pass as shown below. But both have a space and time complexity of O(n)
        """

        prevMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i

