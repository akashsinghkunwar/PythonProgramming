"""
Given a list of n-1 integers, these integers are in the range of 1 to n.
There are no duplicates in the list. One of the integers is missing in the list.
Can you write an efficient code to find the missing integer?
"""


def find_missing_number(nums):
    n = len(nums) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(nums)  # Sum of elements in the given list
    return expected_sum - actual_sum  # The missing number


# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]  # Missing number is 3
print("Missing number:", find_missing_number(nums))
