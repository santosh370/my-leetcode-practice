'''

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

'''

nums = [1,2,3,1,1,3]
#nums = [1,1,1,1]
#nums = [1,2,3]
nums = [1,3,1,2,3,5,7,9,7,9,3,1,8,2]

print("Original Arr :: ",nums)

### Method 1
print("##### Method 1 ::")

nums_len = len(nums)

i=counter=0

for i in range(nums_len):
    for j in range(i+1, nums_len):
        if nums[i] == nums[j]:
            counter +=1

print("No of Good pairs  :",counter)


print()

### Method 2
print("##### Method 2 ::")

num_count = {}
count = 0
for num in nums:
    if num in num_count:
        count += num_count[num]
        num_count[num] += 1
    else:
        num_count[num] = 1

    print("Every items : ", num, count, num_count, sep="  ::  ")

print(num_count)

print("No of Good pairs  :",count)
