def binary_search(arr,target):
    low=0
    high=len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = list(map(int,input("Enter space seprated integer:").split()))
target= int(input("Enter Target integer value: "))
result = binary_search(arr,target)

if result != -1:
    print(f"Target value {target} found at {result}")
else:
    print(f"Target value {target} not found in the array.")