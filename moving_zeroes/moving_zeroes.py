'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    non_zero = []
    zero = []

    for item in arr:
        if item == 0:
            zero.append(item)
        else:
            non_zero.append(item)
    for item in zero:
        non_zero.append(item)
        
    return non_zero
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")