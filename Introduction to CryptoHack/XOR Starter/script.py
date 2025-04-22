label = "label"
new_string = ''.join([chr(ord(c) ^ 13) for c in label])
flag = f"crypto{{{new_string}}}"
print(flag)
