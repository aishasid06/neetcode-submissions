class Solution:
    """
    Instead of creating a frequency list where the index represents the element
    and the value represents the frequency, we will instead have a list of length
    len(nums) b/c that's the maximum frequency that an element can have. With the
    first approach, the frequency array might then be unbounded if the values in the
    array are too large.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for _ in range(len(nums) + 1)]

        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)

        for key, val in hashMap.items():
            frequency[val].append(key)

        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result

            


