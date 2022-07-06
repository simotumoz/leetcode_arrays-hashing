# Design an algorithm to encode a list of strings to a string. The encoded string is then
# sent over the network and is decoded back to the original list of strings.

# Input: ["lint","code","love","you"] -> any possible char
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"


def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(str):
    res, i = [], 0

    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1  # incrementing the second until I find the delimeter
        length = int(str[i:j])  # finding word's lenght
        res.append(str[j + 1: j + 1 + length])
        i = j + 1 + length
    return res


if __name__ == '__main__':
    strs = ["lint", "code", "love", "you", "cacca", "pupu", "supercalifragilistichespiralidoso"]

    single_string = encode(strs)
    print(single_string)

    original_string = decode(single_string)
    print(original_string)
