def laceStrings1(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    if len( s1 ) > len( s2 ):
        temp = s1
    else:
        temp = s2

    result = ''
    n = 0

    while n < len( temp ):
        if n < len( s1 ):
            result += s1[n]

        if n < len( s2 ):
            result += s2[n]

        n += 1

    return result