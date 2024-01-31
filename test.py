from . import decode_image
from PIL import Image


# To decode, load the encoded image
decoded_img = Image.open('encoded_image.png')

# Decode to retrieve the password
password = decode_image(decoded_img)
print(password)