class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two arrays (one to store sum of prefix, the other to store suffix)
        n = len(nums)

        p = [0] * (n)
        p[0] = 1
        #prefix 
        for i in range(1, n): 
            p[i] = p[i-1] * nums[i-1]


        s = [0] * (n)
        s[n-1] = 1
        for i in range(n-2, -1, -1):
            s[i] = s[i+1] * nums[i+1]

        res = [1] * (n)
        for i in range(0, n): 
            res[i] = s[i] * p[i]

        return res
        
        