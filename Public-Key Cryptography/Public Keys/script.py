def rsa_encrypt(message, e, p, q):
    # Step 1: Compute the modulus N
    N = p * q

    # Step 2: Perform modular exponentiation
    ciphertext = pow(message, e, N)

    return ciphertext

# Given values
message = 12
e = 65537
p = 17
q = 23


ciphertext = rsa_encrypt(message, e, p, q)
print(f"Ciphertext: {ciphertext}")