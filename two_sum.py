class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique=set(nums)
        for i,n in enumerate(nums):
            other=target-n
            if other in unique and i!=nums.index(other):
                return [i,nums.index(other)]
