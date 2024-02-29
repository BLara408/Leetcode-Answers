class Solution:
    def maxSum(self, nums: List[int]) -> int:
        Sum = 0
     
        for i in range(len(nums)-1):
           num1 = max(str(nums[i]))
           for n in range(i + 1, len(nums)):
               num2 = max(str(nums[n]))
               if num2 == num1:
                   Sum = max(Sum,nums[i] + nums[n])
        return -1 if Sum == 0 else Sum