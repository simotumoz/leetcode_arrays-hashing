def two_sum(nums, target):
    previous_map = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in previous_map:
            return [previous_map[diff], i]
        else:
            previous_map[n] = i

    return


if __name__ == '__main__':
    nums = [1, 4, 5, 6, 2, 4, 5, 9]
    trgt = 10
    print(two_sum(nums, trgt))
