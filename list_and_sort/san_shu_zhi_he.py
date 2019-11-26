class Solution():
    def method(self, nums):
        if nums == []:
            return []
        elif len(nums)<3:
            return []
        results = []
        for i in range(0,len(nums)):
            a = nums[i]
            for j in range(i+1,len(nums)):
                b = nums[j]
                c = 0-a-b
                sorted_comb = sorted([a,b,c])
                if c in nums[j+1:] and sorted_comb not in results:
                    results.append(sorted_comb)
        return results

if __name__=="__main__":
    sol = Solution()
    print(sol.method([1,-1,-1,0]))
