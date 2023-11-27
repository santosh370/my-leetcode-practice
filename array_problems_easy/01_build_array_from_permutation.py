nums = [0,2,4,5,3,1]
res = []
#### Method 1
print("###### Method 1 :: ")
res = [0,0,0,0,0,0]
i=0
print("Exisitng List: ", nums)
while i<len(nums):
    val = nums[i]
    res[i] = nums[val]
    i=i+1
print("Final List - ", res)
print()


res = []

#### Method 2
print("###### Method 2 ::")
print([nums[i] for i in nums])

print()

#### Method 3
print("#### Method 3 ::")
print([nums[nums[i]] for i in range(len(nums))])

print()
