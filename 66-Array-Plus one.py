# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:34:29 2020

@author: bobeep
"""


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    注意：python传入列表的时候，应该是传入了指针的形式，实参也会发生变化
    """
    if len(digits) == 1:
        if digits[0] != 9:
            return [digits[0]+1]
        else:
            return [1,0]
    else:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            temp = plusOne(digits[:-1])  # 这一行运行结束后，digits前几位为啥不变
            temp.append(0)
            return temp



digits = [9,9]
result = plusOne(digits)



#%% 哈哈哈 我的解法比别人都快

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1:
            if digits[0] != 9:
                return [digits[0]+1]
            else:
                return [1,0]
        else:
            if digits[-1] != 9:
                digits[-1] += 1
                return digits
            else:
                temp = self.plusOne(digits[:-1])  # 这一行运行结束后，digits前几位为啥不变
                # 注意放到class里面，需要改成self的形式
                temp.append(0)
                return temp


#%%
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])  # 别人的解法，这里起到了我的temp的功能
            return digits  
#%%
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[~i] < 9:
                # it's ones complement. ~i gives i-th element from the back.
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)

#%%
        
