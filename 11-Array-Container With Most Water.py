# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:00:04 2020

@author: bobeep
"""





#def maxArea(height):
#    """
#    :type height: List[int]
#    :rtype: int
#    这道题我理解错了，中间的边比两端的短也没有关系。。。
#    不是那个木桶原理。。。。如果是的话，用这种解法
#    """
#    n = len(height) 
#    max_size = 0
#    
#    if n == 1:
#        return 0
#    if n == 2:
#        max_size = min(height) * 1
#        return max_size
#    else:
#        loc_min = height.index(min(height))
#        width = max(loc_min, n-1-loc_min)           # 不要忘记减去1
#        max_size = min(height)*width if min(height)*width>max_size else max_size
#        height[loc_min] = 999999
#        if height.index(min(height)) < loc_min:
#            temp = maxArea(height[:loc_min]) 
#        else:
#            temp = maxArea(height[loc_min+1:n])
#       
#    return max(max_size, temp)

#import numpy as np
#def maxArea(height):
#    """
#    :type height: List[int]
#    :rtype: int
#
#    """
#    n = len(height) 
#    max_size = 0
#    
#    for i in range(n-1):            
#        loc_min = height.index(min(height))
#        loc_other = [i for i in range(n) if ((height[i]>=min(height)) & (height[i]<999999))]
#        if len(loc_other) < 2:
#            break
#        width = np.abs(np.array(loc_other) - loc_min).max()
#        max_size = min(height)*width if min(height)*width>max_size else max_size
#        height[loc_min] = 999999
#    return max_size
#
#
#        
#
#import numpy as np
#class Solution(object):
#    def maxArea(self, height):
#        """
#        :type height: List[int]
#        :rtype: int
#        """
#        n = len(height) 
#        max_size = 0
#        
#        for i in range(n-1):            
#            loc_min = height.index(min(height))
#            loc_other = [i for i in range(n) if ((height[i]>=min(height)) & (height[i]<999999))]
#            if len(loc_other) < 2:
#                break
#            width = np.abs(np.array(loc_other) - loc_min).max()
#            max_size = min(height)*width if min(height)*width>max_size else max_size
#            height[loc_min] = 999999
#        return max_size

#%% 答案
'''
The intuition behind this approach is that the area formed between the lines 
will always be limited by the height of the shorter line. Further, 
the farther the lines, the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array 
constituting the length of the lines. Futher, we maintain a 
variable \text{maxarea}maxarea to store the maximum area obtained till now. 
At every step, we find out the area formed between them, 
update \text{maxarea}maxarea and move the pointer pointing to the shorter line 
towards the other end by one step.

The algorithm can be better understood by looking at the example below:
    
Initially we consider the area constituting the exterior most lines. 
Now, to maximize the area, we need to consider the area between the 
lines of larger lengths. If we try to move the pointer at the longer 
line inwards, we won't gain any increase in area, since it is limited 
by the shorter line. But moving the shorter line's pointer could turn 
out to be beneficial, as per the same argument, despite the reduction 
in the width. This is done since a relatively longer line obtained by 
moving the shorter line's pointer might overcome the reduction in area 
caused by the width reduction.

'''

# 自己写的
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int

    """
    low = 0
    high = len(height)-1
    max_size = 0
    while low <= high:
        max_size = max(max_size, min(height[low], height[high]) * (high-low))
        if height[low] < height[high]:
            low += 1
        else:
            high -= 1
    
    return max_size

height = [1,8,6,2,5,4,8,3,7]
max_size = maxArea(height)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        high = len(height)-1
        max_size = 0
        while low <= high:
            max_size = max(max_size, min(height[low], height[high]) * (high-low))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        
        return max_size