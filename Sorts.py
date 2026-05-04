def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

def bubble_sort(nums):
    
    for i in range(len(nums)-1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def insertion_sort(nums):
    for i in range(1, len(nums)):          
        index_j = i
        index_i = i - 1
        while index_i >= 0:
            if nums[index_i] > nums[index_j]:
                nums[index_j], nums[index_i] = nums[index_i], nums[index_j]
                index_j -= 1
                index_i -= 1
            else:
                break 
    return nums

def merge_sort(nums):

    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    right = nums[mid:]
    left = nums[:mid]
    return merge(merge_sort(left), merge_sort(right))

def merge(left,right):
    res = []
    i,j = 0, 0

    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    if i<len(left):
        res.extend(left[i:])
    else:
        res.extend(right[j:])
    return res

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums)//2]
    left=[]
    right=[]
    mid=[]
    for x in nums:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            mid.append(x)
    return quick_sort(left) + mid + quick_sort(right)



nums = [3,1,2,5,4,6,7,8,0]
print(f"Selection sort: {selection_sort(nums)}")
nums = [1,2,0,5,4,6,7,9,5]
print(f"Bubble sort: {bubble_sort(nums)}")
nums = [3,0,4,2,1,2,7,8,4]
print(f"Insertion sort: {insertion_sort(nums)}")
nums = [3,9,8,3,2,5,7,2,0]
print(f"Merge sort: {merge_sort(nums)}")
nums = [5,2,2,7,4,3,7,1,0]
print(f"Quick sort: {quick_sort(nums)}")