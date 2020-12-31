def xo(s):
    s = s.lower()
    if 'x' not in s and 'o' not in s:
        return True
    
    elif s.count('x') > s.count('o') or s.count('o') > s.count('x'):
        return False
    
    elif s.count('x') == s.count('o'):
        return True
    
    else:
        return False


print(xo('xxoo'))
