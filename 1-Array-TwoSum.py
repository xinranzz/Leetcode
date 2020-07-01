# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:22:47 2020

@author: bobeep
"""






def twoSum(nums, target):
    n = len(nums)
    flag = True
    for i in range(n):
        if flag:        # continue loop
            for j in range(i+1, n):
                if nums[i]+nums[j] == target:
                    flag = False
                    break
        else:
            i = i-1
            break
    return [i, j]

nums = [1, 2, 3, 7]
target = 3
a = twoSum(nums, target)


#%% 我的答案
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        flag = True
        for i in range(n):
            if flag:        # not find the solution yet, continue loop
                for j in range(i+1, n):
                    if nums[i]+nums[j] == target:
                        flag = False
                        break
            else:
                i = i-1
                break
        return [i, j]

#%% 别人的答案
'''
It turns out we can do it in one-pass.
While we iterate and inserting elements into the table, 
we also look back to check if current element's complement already exists in the table. 
If it exists, we have found a solution and return immediately.
Time complexity : O(n)
Space complexity : O(n)
感觉这种方法是往回看的，找到第二个数字后，再判断第一个数字是否已经存在
我的那种方法，更像是往前看的
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):      # 这里只遍历了一次
            n = target - num
            # 注意：h是字典。python的字典本质是哈希表，因此查找速度为O(1)
            # 问题：这里哈希表的原理是什么呢？散列函数？怎么想到用哈希表
            # key和存储的地址对应
            if n not in h:                  
                h[num] = i
            else:
                return [h[n], i]