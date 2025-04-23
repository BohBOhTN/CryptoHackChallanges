def modular_inverse(a, p):
    # Calculate the modular inverse using Fermat's Little Theorem
    return pow(a, p - 2, p)

# Given values
a = 3
p = 13

# Calculate the modular inverse
d = modular_inverse(a, p)
print(f"The modular inverse of {a} mod {p} is {d}")