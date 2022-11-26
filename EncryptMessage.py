import cv2
from os.path import join
from steganocryptopy.steganography import Steganography
import io
import os
from stegano import lsb
import wave


## Hide message using GCD way
# translate text to unidecode numbers
def unidecode_message(message):
    for c in message:
        yield ord(c)


# find GCD for the length and width of the image
def gcd(x, y):
    print(x, y)
    while(y):
        x, y = y, x % y
    print(x)
    return x


# load image and return numpy.ndarray
def get_image(image_path):
    img = cv2.imread(image_path)
    return img


# encode message GCD
def encrypt_message_GCD(image_path, msg):
    img = get_image(image_path)
    msg_gen = unidecode_message(msg)
    pattern = gcd(len(img), len(img[0]))
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (i+1 * j+1) % pattern == 0:
                try:
                    img[i-1][j-1][0] = next(msg_gen)
                except StopIteration:
                    img[i-1][j-1][0] = 0
    path = image_path.split('.')
    save_path = path[0] + '_hidden' + '.png'
    cv2.imwrite(save_path, img)

# encrypt message with key - Algorytm 2
def encrypt_message_key(key, image_path, message):
    key_path = 'key'
    message_path = 'message.us'
    with open('message.us', 'w', encoding='utf-8') as hiden_message:
        hiden_message.write(message)
    encrypted = Steganography.encrypt(key_path, image_path, message_path)
    path = image_path.split('.')
    save_path = path[0] + '_hidden' + '.png'
    encrypted.save(save_path)
    os.remove('message.us')
    return


# encrypt message with key - LSB
def encrypt_message_without_key(image_path, message):
    secret = lsb.hide(image_path, message)
    path = image_path.split('.')
    save_path = path[0] + '_hidden' + '.png'
    secret.save(save_path)


# encrypt message in wav file
def encrypt_message_in_audio(path, message):
    path = path.split('.')
    save_path = path[0] + '_hidden' + '.wav'
    audio = wave.open(path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    message = message + int((len(frame_bytes) - (len(message) * 8 * 8)) / 8) * '#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in message])))

    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)

    with wave.open(save_path, 'wb') as fd:
        fd.setparams(audio.getparams())
        fd.writeframes(frame_modified)
    audio.close()


# generate 32-bits key
def generate_key():
    Steganography.generate_key('key')
    return os.path.abspath("key")
