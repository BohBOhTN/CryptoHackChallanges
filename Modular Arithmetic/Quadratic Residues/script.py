def find_quadratic_residue(p, ints):
    for x in ints:
        for a in range(p):
            if (a * a) % p == x:
                print(f"Quadratic residue: {x}, Square root: {a}")
                return a

# Given values
p = 29
ints = [14, 6, 11]

# Find the quadratic residue and its square root
flag = find_quadratic_residue(p, ints)
print(f"Flag: {flag}")