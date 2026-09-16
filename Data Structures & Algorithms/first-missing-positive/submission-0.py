class Solution:
    """
    all possible options are between 1 and len(nums) + 1
    we don't care about negative numbers so do some cleaning
    iterate through all nums
    make value at index = num - 1 negative (marking) if index exists
    iterate through all vals in range 1 - (len(nums) + 1)
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 10        # cleaning

        for num in nums:
            index = abs(num) - 1
            if index >= n:
                continue
            else:
                nums[index] = -abs(nums[index])       # marking

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


            
        