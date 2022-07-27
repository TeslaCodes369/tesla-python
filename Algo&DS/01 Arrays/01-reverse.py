# Reversing an array in-place solution

def reverse(nums):
    print('Input Array')
    print(nums[:])

    for index in range(0, len(nums)//2):
        nums[index], nums[len(nums)-index -
                          1] = nums[len(nums)-index-1], nums[index]

    print('Reversed Array')
    print(nums[:])


def reverseWh(nums):
    print('Input Array')
    print(nums[:])

    start = 0
    end = len(nums)-1

    while end > start:
        nums[start], nums[end] = nums[end], nums[start]
        end -= 1
        start += 1

    print('Reversed Array')
    print(nums[:])


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9, 10]
    reverse(arr)
    reverseWh(arr)
