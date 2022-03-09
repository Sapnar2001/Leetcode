class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        length =0
        for i in s:
            if i == " ":
                length=0
            else:
                length+=1
        return length