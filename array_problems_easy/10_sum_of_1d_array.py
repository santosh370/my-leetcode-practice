'''
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

'''

nums = [1,2,3,4]
nums_org = nums
print("Original Array = ", nums)

'''
count=i=0
for num in nums:
    count = count + num
    nums[i] = count
    i+=1

print("After sum of 1d array = ", nums)
'''

'''
print("========================================")
print("Method 2 ::")

for i in range(1, len(nums)):
    print("Val of i = ", i)
    nums[i] += nums[i-1]

print("After sum of 1d array = ", nums)
'''
l = [ sum(nums[:i+1]) for i in range(len(nums)) ]

print("One line solution - ",l)
