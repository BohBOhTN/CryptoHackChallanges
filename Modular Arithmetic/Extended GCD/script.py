def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, u1, v1 = extended_gcd(b, a % b)
    u = v1
    v = u1 - (a // b) * v1
    return gcd, u, v

# Given primes
p = 26513
q = 32321

# Calculate gcd, u, and v
gcd, u, v = extended_gcd(p, q)
print(f"GCD: {gcd}, u: {u}, v: {v}")

# Output the lower of u and v as the flag
flag = min(u, v)
print(f"Flag: {flag}")