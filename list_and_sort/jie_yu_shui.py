# -*- encoding: utf-8 -*-
'''
@File    :   jie_yu_shui.py    
@Author :   Chi Zhang
'''

class Solution():
    def method(self, heights):
        max_index = 0
        pre_height = 0
        for i in range(0,len(heights)):
            if heights[i] > pre_height:
                max_index = i
                pre_height = heights[i]
        left = 0
        right = len(heights) - 1
        pre = 0
        area_max = 0
        water = 0
        # from left->max
        for i in range(0,max_index):
            if heights[i] > area_max:
                area_max = heights[i]
                pre = heights[i]
            else:
                water += area_max - heights[i]
                pre = heights[i]
        pre = 0
        area_max = 0
        # from right -> max
        for i in range(len(heights)-1,max_index-1,-1):
            if heights[i] > area_max :
                area_max = heights[i]
                pre = heights[i]
            else:
                water += area_max - heights[i]
                pre = heights[i]
        return water


if __name__=="__main__":
    sol = Solution()
    print(sol.method([0,1,0,2,1,0,1,3,2,1,2,1]))
