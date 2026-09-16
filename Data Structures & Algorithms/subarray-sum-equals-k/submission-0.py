class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        The following slising window solution works for
        an array that just has non-negative values

        i, j = 0, 0
        count = 0
        sum = nums[i]

        while i <= j and j < len(nums):
            if sum == k:
                count += 1
                j += 1
                if j < len(nums):
                    sum += nums[j]

            elif sum < k:
                j += 1
                if j < len(nums):
                    sum += nums[j]

            else:
                sum -= nums[i]
                i += 1

        return count
        """

        res = 0
        currSum = 0
        prefixSums = {0:1}

        for num in nums:
            currSum += num
            diff = currSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)

        return res

            