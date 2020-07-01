# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:29:24 2020

@author: bobeep
"""

#def twoSum( nums, target):
#    """
#    :type nums: List[int]
#    :type target: int
#    :rtype: List[int]
#    """
#    h = {}
#    for i, num in enumerate(nums):      
#        n = target - num
#        if n not in h:                  
#            h[num] = i
#        else:
#            return [h[n], i]
#
#def threeSum(nums):
#    """
#    :type nums: List[int]
#    :rtype: List[List[int]]
#    """
#    nums.sort()
#    store = []
#    result = []
#    for i in range(len(nums)):
#        if nums[i] not in store:
#            i.append(nums[i])
#            if twoSum(nums[i+1:], -nums[i]):
#                temp = [nums[i]]
#                temp.append(twoSum(nums[i+1:], -nums[i]))
#    return result
        


#nums = [-1, 0, 1, 2, -1, -4]
#result = threeSum(nums)
            














class Solution(object):
    '''
    基本上就是我上面的思想
    先排序，锁定一个数字
    之后查找剩下的数字
    但是进行twosum运算的时候，是用的two pointer的方法
    '''
    def threeSum(self, nums):
    	res = []
    	nums.sort()
    	length = len(nums)
    	for i in range(length-2): #[8]
    		if nums[i]>=0: break       
            # 如果已经大于零，可以不考虑
            # 注意：上面不要多此一举加等号，可能出现[0,0,0]
    		if i>0 and nums[i]==nums[i-1]: continue # 出现重复的值，可以不考虑
    		l, r = i+1, length-1 #[2]
    		while l<r:
    			total = nums[i]+nums[l]+nums[r]
    			if total<0: #[3]
    				l+=1
    			elif total>0: #[4]
    				r-=1
    			else: #[5]
    				res.append([nums[i], nums[l], nums[r]])
    				while l<r and nums[l]==nums[l+1]: # 跳过重复值，不会得到重复的结果
    					l+=1
    				while l<r and nums[r]==nums[r-1]: 
    					r-=1
    				l+=1
    				r-=1
    	return res
