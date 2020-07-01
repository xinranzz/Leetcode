# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:16:49 2020

@author: bobeep
"""



def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    h = {}
    for i in range(n):
        if nums[i] not in h:
            h[nums[i]] = 1
        else:
            h[nums[i]] += 1

    for ele, freq in h.items():
        if freq > int(n/2):
            break
    return ele
    
#nums = [3,2,3]
#a = majorityElement(nums)









class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        h = {}
        for i in range(n):
            if nums[i] not in h:
                h[nums[i]] = 1
            else:
                h[nums[i]] += 1
    
        for ele, freq in h.items():
            if freq > int(n/2):
                break
        return ele

#%% 别人的答案
def majorityElement2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    return sorted(nums)[len(nums)//2]
nums = [3,2,3,7]
a = majorityElement2(nums)