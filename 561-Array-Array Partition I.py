# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:19:51 2020

@author: bobeep
"""



def arrayPairSum(nums):
    nums = sorted(nums)
    n = len(nums)
    sums = 0
    for i in range(n):
        if i%2 == 0:
            sums += nums[i]
    return sums

nums =  [-100,1,-39,888]
a = arrayPairSum(nums)



class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        sums = 0
        for i in range(n):
            if i%2 == 0:
                sums += nums[i]
        return sums
    
    
   

#%% 别人的解法1
def arrayPairSum(self, A):
    return sum(sorted(A)[::2])

#%% 别人的解法2
# 没看，感觉又麻烦做出来又慢
'''
We use the same idea to pair adjacent elements, but instead use a counting sort approach.
Range of numbers is -10k to 10k. This means 20001 elements.
Build the frequency map for the input.
Now iterate this map. 
When frequency is even, the contribution is the implied number times freq//2. 
When odd, it is (implied number) times (freq//2 + 1).
Implied number: (idx-10000)
The time and space complexity is order K where K is the range of the numbers.
两条斜杠代表整除
'''
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 共有20001个元素，建立一个哈希表
        # 索引和原来的数字有关
        # 索引上的元素，代表原来的数字出现了多少次
        res = [0]*20001
        # 可能有的元素重复出现
        for x in nums:
            res[x+10000] += 1
            
        s_so_far, adjust = 0, False
        for idx, freq in enumerate(res):
            if freq:
                # 如果adjust等于True，代表左相邻的小的数字已经加进去了
                # 所以当前这个数字出现的频率要减少1.例，如果原始频率是1的话，相当于当前这个数字是两个数字中比较大的一个，不要了
                freq = freq-1 if adjust else freq
                if freq&1:
                    s_so_far += ((freq//2) + 1)*(idx-10000)
                    adjust = True
                    # 出现奇数次，肯定相邻位置的数字已经出现
                else:
                    s_so_far += ((freq//2))*(idx-10000)
                    adjust = False
                    # 出现偶数次，说明正好是整的几组，相邻位置没有出现
        return s_so_far

#%%
def arrayPairSum(nums):
    nums.sort()
    return sum(nums[0::2])