from collections import defaultdict


def group_anagrams(strs):
    res = defaultdict(list)  # mapping char counter to the list of anagrams

    for string in strs:
        count = [0] * 26  # initialize for a...z
        # going through every character in each string and count every char occur
        for character in string:
            count[ord(character) - ord('a')] += 1  # taking ascii values and mapping from 0 to 26

        res[tuple(count)].append(string)

    return res.values()


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))
