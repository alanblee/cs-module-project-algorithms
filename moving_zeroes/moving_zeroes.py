"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    # Your code here
    zeros = []
    non_zero = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros.append(arr[i])
    for j in range(len(arr)):
        if arr[j] != 0:
            non_zero.append(arr[j])
    new_list = non_zero + zeros
    return new_list


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    moving_zeroes(arr)

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
