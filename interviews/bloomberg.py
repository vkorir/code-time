## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

# "aaa" -> ""
# "aaaabbb" -> ""
# "aabbba" -> "aa__a" -> "aaa" -> ""
# "aaacbbb" -> "cbbb" ->  "c"

# """
# s = 'aaaabbb'
# a: 4
# b: 3
# """

# "aaaabbbaa" -> "aa"
# "aaaabbbaa" : "bbbaa", "aaaaaa"
# "bbbaa": r["aa"]
# "aaaaaa": r[""]

# "aabbbac" -> "c"

def crashElems(s):
    """
    s1 = aabbbac
    s2 = aaac
    s3 = c
    """
    if len(s) < 3: return s
    
    crashables = [] # [(0, 2)]
    
    start = end = 0
    
    while start < len(s): # n
        while end < len(s) and s[end] == s[start]: end += 1
        if end - start >= 3:
            crashables.append((start, end - 1))
        start = end
    
    min_elements = s
    
    for (start, end) in crashables: # n
        temp = crashElems(s[0:start] + s[end + 1:])
        if len(temp) < len(min_elements):
            min_elements = temp
    
    # O(n^2)
    return min_elements

strings = ['aaa', 'aaaabbb', 'aabbba', 'aaacbbb', 'aaaabbbaa', 'aabbbac']

# print([s + ' -> ' + crashElems(s) for s in strings])

    