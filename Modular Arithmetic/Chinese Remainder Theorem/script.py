from functools import reduce

def chinese_remainder_theorem(congruences):
    # Calculate the product of all moduli
    N = reduce(lambda x, y: x * y, (n for _, n in congruences))

    # Calculate the solution using the Chinese Remainder Theorem
    x = 0
    for a, n in congruences:
        N_i = N // n
        # Modular inverse of N_i mod n
        inv = pow(N_i, -1, n)
        x += a * N_i * inv

    return x % N

# Given congruences
congruences = [
    (2, 5),
    (3, 11),
    (5, 17)
]

# Solve using the Chinese Remainder Theorem
result = chinese_remainder_theorem(congruences)
print(f"The solution is x ≡ {result} mod 935")