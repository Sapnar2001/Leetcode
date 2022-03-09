class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        minl=len(strs[0])
        for i in range(len(strs)):
            minl=min(len(strs[i]),minl)
        a=""
        i=0;
        while i<minl:
            chr=strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i]!=chr:
                    return a;
            a=a+chr
            i+=1
        return a