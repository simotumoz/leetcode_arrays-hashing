def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # building hashmaps

    countS, countT = {}, {}

    for i in range(len(s)):
        # counting occurrencies of a certain character
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    # comparing keys of the two hashmaps
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True


def is_anagram_sorted_strings(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    if is_anagram_sorted_strings('pipo', 'iopp'):
        print('Is a valid anagram')
    else:
        print('Not a valid anagram')
