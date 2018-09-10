def add(s1, s2):
    result = curry = 0
    for i in range(max(len(s1), len(s2))):
        temp = curry
        if i < len(s1):	temp += ord(s1[i]) - ord('0')
        if i < len(s2): temp += ord(s2[i]) - ord('0')

        curry = temp if temp < 10 else (temp - 10)
        result = result * 10 + temp if temp < 10 else 1

    return str(result)


print(add('1', '1'))
