def modular_arithmetic():
    # Calculate x for 11 ≡ x mod 6
    x = 11 % 6

    # Calculate y for 8146798528947 ≡ y mod 17
    y = 8146798528947 % 17

    # Find the smaller of x and y
    flag = min(x, y)

    print(f"x: {x}, y: {y}, Flag: {flag}")

# Run the function
modular_arithmetic()