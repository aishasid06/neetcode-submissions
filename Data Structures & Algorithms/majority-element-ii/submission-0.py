class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        res = set()
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 3 and num not in res:
                res.add(num)

        return list(res)