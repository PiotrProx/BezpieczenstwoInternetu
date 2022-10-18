# The script encodes and decodes the hidden message in the image based on the GCD of the length and width of the image.

import cv2


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

# encode message
def encode_image(image_path, msg):
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
                    return img

# decode message
def decode_image(img_loc):
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


def main():
    image_path = r"E:\Szyfrator-Deszyfrator\1.png"
    msg = 'testowa wiadomosc'
    encoded_image = encode_image(image_path, msg)
    cv2.imwrite("EncodedImage.png", encoded_image)
    decoded_message = decode_image('EncodedImage.png')
    print(decoded_message)



if __name__ == '__main__':
    main()
