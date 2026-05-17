def binarysearch(a, value):
    if not a:
        print("not found")
        return
    
    mid = len(a) // 2
    
    if a[mid] == value:
        print("found", a[mid])
        return
    if a[mid] > value:
        binarysearch(a[:mid],value)
    elif a[mid] < value:
        binarysearch(a[mid+1:], value)
#===========================
nums = [1,3,5,2]
nums.sort()
binarysearch(nums, 4)

#===========================
print("-----------------")
n=5
nums = []
for i in range(1, n + 1):
    nums.append(i)
    print(nums)