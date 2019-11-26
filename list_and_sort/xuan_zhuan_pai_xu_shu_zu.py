class Solution():
    def search(self, nums, target):
        if nums == []:
            return -1
        elif len(nums) == 1 and target == nums[0]:
            return 0
        elif len(nums) == 1 and target != nums[0]:
            return -1
        start = 0
        end = len(nums) - 1
        return self.method(nums,start,end,target)

    def method(self, nums, start, end, target):
        mid = (end - start) // 2 + start
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        elif nums[mid] == target:
            return mid
        elif nums[mid + 1] == target:
            return mid + 1
        # fen jie xian
        if nums[mid] > nums[mid + 1]:
            if target < nums[end]:
                return self.method(nums,mid+1,end,target)
            else:
                return self.method(nums,start,mid,target)
        elif nums[mid] <= nums[mid + 1]:
            if nums[mid + 1] > nums[end] and target >= nums[mid + 1]:
                return self.method(nums,mid+1,end,target)
            elif nums[mid+1] > nums[end] and target < nums[mid+1]:
                return self.method(nums,start,mid,target)
            elif nums[mid + 1] < nums[end] and target < nums[mid]:
                return self.method(nums,start,mid,target)
            elif nums[mid+1] < nums[end] and target > nums[mid]:
                return self.method(nums,mid+1,end,target)
            elif nums[mid+1] == nums[end]:
                return -1

if __name__=="__main__":
    sol = Solution()
    print(sol.search([5,6,7,8,9,10,0,1,2,3,4],11))

