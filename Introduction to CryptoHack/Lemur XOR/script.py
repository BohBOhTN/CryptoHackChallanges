from PIL import Image

# Load the two images
image1 = Image.open("c:/Users/baha9/OneDrive - North American Private University/Bureau/Baha/Projets/Me/CryptoHack.org/Introduction to CryptoHack/Lemur XOR/lemur_ed66878c338e662d3473f0d98eedbd0d.png")
image2 = Image.open("c:/Users/baha9/OneDrive - North American Private University/Bureau/Baha/Projets/Me/CryptoHack.org/Introduction to CryptoHack/Lemur XOR/flag_7ae18c704272532658c10b5faad06d74.png")

# Ensure both images have the same size
if image1.size != image2.size:
    raise ValueError("Images must have the same dimensions for XOR operation.")

# Perform XOR operation on the RGB values of the two images
result_image = Image.new("RGB", image1.size)

for x in range(image1.width):
    for y in range(image1.height):
        pixel1 = image1.getpixel((x, y))
        pixel2 = image2.getpixel((x, y))
        xor_pixel = tuple([p1 ^ p2 for p1, p2 in zip(pixel1, pixel2)])
        result_image.putpixel((x, y), xor_pixel)

# Save the resulting image
result_image.save("result.png")
print("XOR operation completed. Result saved as result.png.")