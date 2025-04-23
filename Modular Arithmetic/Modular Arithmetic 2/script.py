def modular_arithmetic_2():
    # Given values
    p = 65537
    base = 273246787654
    exponent = 65536

    # Calculate base^exponent mod p using Python's built-in pow function
    result = pow(base, exponent, p)

    print(f"Result: {result}")

# Run the function
modular_arithmetic_2()