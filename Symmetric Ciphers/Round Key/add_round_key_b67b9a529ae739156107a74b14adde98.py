state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    return [[s[i][j] ^ k[i][j] for j in range(len(s[0]))] for i in range(len(s))]


def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return b''.join(bytes(row) for row in matrix)

# Using the add_round_key function to XOR the state and round_key
result = add_round_key(state, round_key)

# Converting the resulting matrix to bytes and decoding to get the flag
flag = matrix2bytes(result).decode()
print(flag)

