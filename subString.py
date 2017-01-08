def subs(input_string):
    """
    Generates a list of substrings
    """
    length = len(input_string)
    return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]

print subs('123454984')