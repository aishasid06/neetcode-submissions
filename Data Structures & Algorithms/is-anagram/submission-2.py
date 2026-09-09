class Solution:
    """
    We can have single array of length 26 b/c
    there are 26 possible lowercase letters
    Increment count[index] where index is ord(c) - ord('a')
    Loop through the count array and if any value is not 0, return False
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for c in t:
            count[ord(c) - ord('a')] -= 1

        for i in count:
            if i != 0:
                return False

        return True