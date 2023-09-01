def findLargest(arr):
	secondLargest = 0
	largest = min(arr)

	for i in range(len(arr)):
		if arr[i] > largest:
			secondLargest = largest
			largest = arr[i]
		else:
			secondLargest = max(secondLargest, arr[i])
	return secondLargest
print(findLargest([10, 20, 4, 45, 99]))

def find_second_largest(nums):
    if len(nums) < 2:
        return "List has less than two elements"
    
    largest = second_largest = float('-inf')
    
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return "No second largest element found"
    else:
        return second_largest

# Example usage
numbers = [5, 2, 8, 1, 9, 3]
result = find_second_largest(numbers)
print("The second largest element is:", result)
