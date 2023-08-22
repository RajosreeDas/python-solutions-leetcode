class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i in range(len(nums)):
            k=target-nums[i]
            if k in res:
                return [res[k] , i]
            else:
                res[nums[i]]=i
# ob1=Solution()
# n = input(" ")
# nums = [int(num) for num in n.split()]
# target=int(input())
# print(ob1.twoSums(nums , target))
