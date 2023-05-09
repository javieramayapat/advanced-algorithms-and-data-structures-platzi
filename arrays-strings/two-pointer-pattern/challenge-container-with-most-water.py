def max_area(height):
    """
    T = O(n)
    We only iterate once our list to calculate the area,
    that meand tha is linear.

    S = O(1)
    We only storage 3 varibales that regardless of the input
    they do not change their value so it´s linear.
    """
    max_area = 0
    left_pointer, right_pointer = 0, len(height) - 1

    while left_pointer < right_pointer:  # T = O(n)
        area = (right_pointer - left_pointer) * min(
            height[right_pointer], height[left_pointer]
        )
        max_area = max(max_area, area)
        if height[right_pointer] >= height[left_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return max_area


if __name__ == "__main__":
    input1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    output1 = 49

    input2 = [8, 1, 6, 2, 5, 4, 1, 3, 7]
    output2 = 56

    print(max_area(input1))
    print(max_area(input2))
