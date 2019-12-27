def find_missing_letter(chars):
    return [chr(ord(chars[i])-1) for i in range(len(chars)) if ord(chars[i]) - ord(chars[i-1]) > 1][0]

# ["a","b","c","d","f"] -> "e"
# ["O","Q","R","S"] -> "P"

