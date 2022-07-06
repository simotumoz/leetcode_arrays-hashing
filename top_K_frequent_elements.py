# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


def topKFrequentElements(nums, k):
    # initializing hashmap and array

    count = {}  # the hashmap will count the occurrences

    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c, in count.items():
        freq[c].append(n)  # n occurs c times

    res = []  # initializing the result array

    for i in range(len(freq) - 1, 0, -1):  # descending order
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequentElements(nums, k))
