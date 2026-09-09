class Solution:
    """
    Brute-force method: outer-loop keeping track of the current index at which the element is being
    checked and an inner loop to iterate through the strings. 
    Time-complexity: O(n^2)


    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
    """

    """
    Notice how you will only ever need to iterate for the number of characters in the smallest str.
    So the time complexity is O(n*m) where n is the length of the shortest substring and 
    m is the no. of strings.

    Now if you sort the array in ascending order of string lengths. Then the first and the last string 
    will be the most different. So we can just compare the two. Any common prefix will also exist for 
    any of the strings in between.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]
