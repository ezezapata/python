def reverse_string(s):
    split_ls = s.split(' ')
    new_str = ' '.join(split_ls[::-1])
    return new_str

print reverse_string("Hello how are you")
