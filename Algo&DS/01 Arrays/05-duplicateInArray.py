# find if duplicate in array of numbers
# if elem is smaller than length of array
def findDuplicates(nums):
    print(nums, end=' -> ')
    for num in nums:
        if nums[abs(num)-1] <= 0:
            return 'Duplicate Found'
        else:
            nums[abs(num)-1] = -nums[abs(num)-1]

    return 'No Duplicate found'


if __name__ == '__main__':
    print(findDuplicates([1, 3, 4, 2]))
    print(findDuplicates([1, 3, 4, 4]))
