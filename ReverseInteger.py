class Solution:
    def reverse(self, x: int) -> int:
        negative=False
        if x<0:
            negative=True
            x=-x
        sum=0
        while x:
            sum=sum*10+x%10
            x//=10
        if sum>= 2 ** 31 -1 or sum<=-2 ** 31:
            return 0
        if negative:
            return -sum
        else:
            return sum