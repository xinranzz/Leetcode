# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 00:01:14 2020

@author: bobeep
"""



def maxSubArray(nums):
    # queue
    largest = -9999999999999
    current_sum = 0
    n = len(nums)
    start = 0
    negative = 0
    for i in range(n):
        if current_sum+nums[i] > current_sum:
            current_sum += nums[i]
            temp = current_sum
            for j in range(start, negative+1):
                temp -= nums[j]
            if temp > current_sum:
                current_sum = temp
                start = negative + 1
                negative = negative + 1
            if current_sum > largest:
                largest = current_sum
        else:
            negative = i
            temp = current_sum
            flag = False
            for j in range(i, n):
                temp += nums[j]
                if temp > current_sum:
                    flag = True
                    break
            if flag:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
                if current_sum > largest:         
                    largest = current_sum     
                start = i

    return largest

#nums = [-2,1,-3,4,-1,2,1,-5,4]
#a = maxSubArray(nums)


#%%
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # queue
        largest = -9999999999999
        current_sum = 0
        n = len(nums)
        start = 0
        negative = 0
        for i in range(n):
            if current_sum+nums[i] > current_sum:
                current_sum += nums[i]
                temp = current_sum
                for j in range(start, negative+1):
                    temp -= nums[j]
                if temp > current_sum:
                    current_sum = temp
                    start = negative + 1
                    negative = negative + 1
                if current_sum > largest:
                    largest = current_sum
            else:
                negative = i
                temp = current_sum
                flag = False
                for j in range(i, n):
                    temp += nums[j]
                    if temp > current_sum:
                        flag = True
                        break
                if flag:
                    current_sum += nums[i]
                else:
                    current_sum = nums[i]
                    if current_sum > largest:         
                        largest = current_sum     
                    start = i
    
        return largest

#%%
def maxSubArray_Solu1(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)
nums = [2,-1,2]
b = maxSubArray_Solu1(nums)       