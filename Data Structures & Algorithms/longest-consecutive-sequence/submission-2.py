class Solution:
    """
    The main idea is that if the current element - 1 has been seen earlier,
    then the current element must have already been considered to be a
    part of a substring. So we don't start a new substring with the current
    element. In other words if (num - 1) is in nums then we don't need to 
    consider this as the start of the sequence. Have a hashset for for O(1) lookup
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1

                maxLength = max(length, maxLength)
            
        return maxLength


            
