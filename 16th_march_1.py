"""
Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers. 
Go to the editor
Input:
[1, 2, 3, 4, 5, 6]
Output:
Increasing.
Input:
[6, 5, 4, 3, 2, 1]
Output:
Decreasing.
"""
#License: https://bit.ly/3oLErEI
def test(nums):
    return "Increasing" if all(nums[i] < nums[i+1] for i in range(len(nums)-1) ) else \
            "Decreasing" if all(nums[i+1] < nums[i] for i in range(len(nums)-1) ) else \
                "Not a monolithic sequence"

nums = [1,2,3,4,5,6]
print("Original list:")
print(nums)

print("Check the direction ('increasing' or 'decreasing') of the said list:")
print(test(nums))

nums = [6,5,4,3,2,1]
print("\nOriginal list:")
print(nums)
print("Check the direction ('increasing' or 'decreasing') of the said list:")
print(test(nums))