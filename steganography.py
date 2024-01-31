# IMG format PNG
# 
from PIL import Image
import stepic

def encode_image(img, msg):
    encoded = stepic.encode(img, msg.encode())
    return encoded

def decode_image(img):
    decoded = stepic.decode(img)
    return decoded

# Usage example
# Load your image (it should be a PNG for lossless encoding)
img = Image.open('sloth.png')

# Encode the image with your password
encoded_img = encode_image(img, '21126Ac8*')

# Save the encoded image
encoded_img.save('encoded_image.png')

# To decode, load the encoded image
decoded_img = Image.open('encoded_image.png')

# Decode to retrieve the password
password = decode_image(decoded_img)
print(password)

