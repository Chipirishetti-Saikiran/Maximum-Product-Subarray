class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ini_prd=1 
        max_prd=1 
        for i in nums:
            if i==0:
                max_prd=0
            else:
                ini_prd=ini_prd*int(i)
                ini_prd=max(ini_prd,0)
                max_prd=max(max_prd,ini_prd)
        return max_prd    
