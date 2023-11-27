nums = [3,5,2,9,6,3,7]
nums1=nums
print("Original Array :: ",nums)
for i,num in enumerate(nums):
    for j in range(i+1, len(nums)):
        tmp=0
        if nums[i]>nums[j]:
            tmp=nums[i]
            nums[i]=nums[j]
            nums[j]=tmp

print("Sorted Array   :: ",nums)


for i,num in enumerate(nums1):
    for j in range(i+1, len(nums1)):
        if nums1[i]>nums1[j]:
            nums1[i]=nums1[i]+nums1[j]
            nums1[j]=nums1[i]-nums1[j]
            nums1[i]=nums1[i]-nums1[j]
print("Sorted Array   :: ",nums1)
