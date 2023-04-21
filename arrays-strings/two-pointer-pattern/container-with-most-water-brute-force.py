def max_area(height):
    max_area = 0
    for left in range(len(height)):  # O(n^2)
        for rigth in range(left + 1, len(height)):
            # base: restar el apuntador de la derecha al de la izquierda para obtenerla
            # altura: minima altura de las dos barreras
            current_area = (rigth - left) * min(height[left], height[rigth])
            max_area = max(max_area, current_area)
    return max_area


if __name__ == '__main__':
    input1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    output1 = 49

    input2 = [8, 1, 6, 2, 5, 4, 1, 3, 7]
    output2 = 56

    print(max_area(input1))
    print(max_area(input2))