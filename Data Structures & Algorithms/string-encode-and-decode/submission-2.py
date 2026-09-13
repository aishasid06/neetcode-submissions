class Solution:

    def encode(self, strs: List[str]) -> str:
        cipher = ""

        for word in strs:
            cipher += str(len(word)) + "#" + word

        return cipher


    def decode(self, s: str) -> List[str]:
        plain_text = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordlength = int(s[i:j])
            plain_text.append(s[j + 1: j + 1 + wordlength])
            i = j + 1 + wordlength

        return plain_text
