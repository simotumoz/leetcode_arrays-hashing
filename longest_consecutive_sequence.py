# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.


def longestConsecutiveSequence(nums):
    numSet = set(nums)
    longest = 0

    for number in nums:

        if (number - 1) not in numSet:  # checking if that's the start of the sequence
            lenght = 0
            while (number + lenght) in numSet:  # getting each consecutive number and checking if exist in numSet
                lenght += 1
            longest = max(lenght, longest)

    return longest


if __name__ == '__main__':
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longestConsecutiveSequence(nums))
