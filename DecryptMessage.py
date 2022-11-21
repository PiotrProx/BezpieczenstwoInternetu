import cv2
from steganocryptopy.steganography import Steganography
from stegano import lsb
import wave


## Decode GCD encoded image
# decode message GCB algorithm
def decrypt_image_GCD(img_loc):
    img = get_image(img_loc)
    pattern = gcd(len(img), len(img[0]))
    message = ''
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (i-1 * j-1) % pattern == 0:
                if img[i-1][j-1][0] != 0:
                    message = message + chr(img[i-1][j-1][0])
                else:
                    return message


def get_image(image_path):
    img = cv2.imread(image_path)
    return img

# find GCD for the length and width of the image
def gcd(x, y):
    print(x, y)
    while(y):
        x, y = y, x % y
    print(x)
    return x

# decode message algorytm 2
def decrypt_message_key(key, image_path):
    return Steganography.decrypt(key, image_path)


# decode message algorytm 1
def decrypt_message_without_key(image_path):
    return lsb.reveal(image_path)

# decode message wav algorithm
def decrypt_message_in_audio(path):
    audio = wave.open(path, mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    # Convert byte array back to string
    message = "".join(chr(int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
    # Cut off at the filler characters
    decoded_msg = message.split("###")[0]

    # Print the extracted text
    print(decoded_msg)
    audio.close()

    return decoded_msg