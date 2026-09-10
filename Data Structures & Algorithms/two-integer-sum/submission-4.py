class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        difference = target - nums[i]

        while difference not in nums[i+1:]: 
            i+= 1
            difference = target - nums[i]

        return [i, nums.index(difference, i+1)] 
        