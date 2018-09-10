def is_substring(s, sub):
    if len(s) < len(sub):
        return False

    target = hash_code(sub)
    next_sub = [0] * len(sub)
    index = 0
    while index < len(sub):
        po = len(sub) - 1 - index
        next_sub[index] = get_code(s[index]) * pow(128, po)
        index += 1

    next_hash_code = sum(next_sub)

    for i in range(len(sub), len(s)):
        if next_hash_code == target:
            return True
        next_sub = next_sub[1:]
        next_sub = list(map(lambda a: 128 * a, next_sub))
        next_sub.append(get_code(s[i]))
        next_hash_code = sum(next_sub)

    return False


def hash_code(sub):
    code, po = 0, len(sub) - 1
    for c in sub:
        code += get_code(c) * pow(128, po)
        po -= 1
    return code


def get_code(c):
    if c == ' ':
        return 0
    return ord(c) - ord('a') + 1


print(is_substring('the hare is here', 'here'))