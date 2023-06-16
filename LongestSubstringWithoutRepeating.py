def lengthOfLongestSubstring(s):
    length = len(s)
    if length < 2:
        return length

    sequence = list(s)
    maxLength = len(set(sequence))

    start = 0
    end = 1

    longest = 0

    while end < length and longest < maxLength:
        curSlice = set(sequence[start:end+1])
        if len(curSlice) < end - start + 1:
            start += 1
        else:
            longest = max(longest, len(curSlice))
            end += 1


    return longest


if __name__ == '__main__':
    myS = "bbbbbbb"
    print(lengthOfLongestSubstring(myS))


"""
Take a slinky approach when evaluating the word:
- Move the endpoint forwards until a duplicate letter is encountered
- Move the startpoint forwards until the duplicate letter is removed
- When the endpoint reaches the end of the string, return the max length

e.g., for the string "pwwkew":

p
pw
pww
ww
w
wk
wke
wkew
End has been reached, return max length
"""