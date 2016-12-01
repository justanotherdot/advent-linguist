
old_passkey = 'hxbxwxba'

def increment_char(char):
    if char == 'z':
        return 'a'
    else:
        return chr(ord(char)+1)

def increment_passkey(passkey):
    code_points = list(passkey)
    new_code_points = code_points
    first_char_ix = -len(code_points)-1
    for i in xrange(-1, first_char_ix, -1):
        if code_points[i] != 'z':
            new_code_points[i] = increment_char(code_points[i])
            break
        else:
            new_code_points[i] = increment_char(code_points[i])
    return new_code_points

def has_alpha_straight(s):
    for i in xrange(len(s)):
        actual = s[i:i+3]
        expected = s[i]+increment_char(s[i])+increment_char(increment_char(s[i]))
        if actual == expected:
            return True
    return False

def contains_invalid_chars(s):
    if s.count('o') > 0 or s.count('i') > 0 or s.count('l') > 0:
        return True
    return False


def contains_overlapping_sets(s):
    used_chars = []
    for i,c in enumerate(s):
        if i+1 < len(s):
            if (s[i+1] not in used_chars and c == s[i+1]):
                used_chars.append(c)
    if len(used_chars) > 1:
        return True
    else:
        return False



def find_new_passkey(passkey):
    """
    Keep incrementing the passkey until:
        * There's at least 3+ letters in an alphabetic sequence (e.g. 'abc')
        * Does not contain the letters 'i', 'o', or 'l'
        * Must contain two non-overlapping pairs of letters (e.g. 'aa' and 'bb', but not 'aa' and 'aa')
    """
    conds = has_alpha_straight(passkey) and \
            not contains_invalid_chars(passkey) and \
            contains_overlapping_sets(passkey)
    while not conds:
        passkey = increment_passkey(passkey)
        print(passkey)
    return passkey

print(find_new_passkey(old_passkey))
