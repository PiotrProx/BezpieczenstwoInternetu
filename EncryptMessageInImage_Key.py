from steganocryptopy.steganography import Steganography

def generate_key():
    Steganography.generate_key("key")


def encrypt_message():
    encrypted = Steganography.encrypt("key", "1.png", "classified.us")
    encrypted.save("encrypted_image_with_key2.png")


def decrypt_message():
    return Steganography.decrypt('key', "encrypted_image_with_key2.png")


def main():
    print(main)
    encrypt_message()
    message = decrypt_message()
    print(message)

if __name__ == '__main__':
    main()
