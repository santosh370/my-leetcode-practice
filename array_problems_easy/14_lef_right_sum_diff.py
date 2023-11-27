'''
2574. Left and Right Sum Differences

Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

 

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

'''



nums = [10,4,8,3]

#print(nums)
#print(nums[::-1])
#exit()

ls=[]
cnt = len(nums)
ls_tmp=0
rs_tmp=0
print(nums)
for i in range(0,cnt):
    ls_tmp=sum(nums[0: i])
    #print(ls_tmp)
    rs_tmp=sum(nums[:i:-1])
    print(rs_tmp)
    ls.append(abs(ls_tmp-rs_tmp))

print(ls)
    
print("===============================")

result = []
leftSum = 0
rightSum = sum(nums)
for num in nums:
    rightSum -= num
    print("Right , left = ", rightSum, leftSum)
    result.append(abs(leftSum - rightSum))
    leftSum += num
    

print("Method 2 - ", result)
