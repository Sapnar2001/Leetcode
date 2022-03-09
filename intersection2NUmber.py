class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l=len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                if nums[j]<nums[i]:
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
        return nums[l-k]