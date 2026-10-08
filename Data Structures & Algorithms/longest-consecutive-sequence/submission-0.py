class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_length = 0
        for x in s: 
            if x - 1 not in s:
                length = 1
                while x + 1 in s: 
                    length += 1
                    x += 1
                if length > max_length: 
                    max_length = length 
                            
                

        return max_length 



            
        