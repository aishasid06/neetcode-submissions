class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        count[nums[0]] = 1
        maj_element = nums[0]

        for i in range(1, len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
            if maj_element != nums[i] and count[nums[i]] > count[maj_element]:
                maj_element = nums[i]

        return maj_element