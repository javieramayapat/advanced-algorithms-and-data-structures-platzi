def marge_two_sorted_list(nums1, m, nums2, n):
    p = len(nums1) - 1
    p1 = m - 1
    p2 = n - 1

    while p1 >= 0 and p2 >= 0:
        if nums2[p2] >= nums1[p1]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1

        p -= 1

    # nums1 y nums2  has diferent length
    if n != m:
        nums1[: p2 + 1] = nums2[: p2 + 1]

    return nums1


def run():
    nums1 = [1, 2, 3, 0, 0, 0, 0]
    m = 3
    nums2 = [-4, 2, 3, 9]
    n = 4
    result = marge_two_sorted_list(nums1, m, nums2, n)
    print(result)


if __name__ == "__main__":
    run()
