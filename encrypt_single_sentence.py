import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt_sentence(sentence, password):
    """
    Encrypts a single sentence using the AES algorithm.

    Args:
        sentence (str): The sentence to be encrypted.
        password (str): The password to use for encryption.

    Returns:
        str: The encrypted sentence.
    """
    # Derive a key from the password using PBKDF2
    salt = b'\x8a\xf8\r\x9d\xe0\xc9\xd0\xf6\xa3\xd7\xd6\x14\x91\x03\x5c\xd6'  # A random salt value
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password.encode('utf-8'))

    # Create a Fernet object with the derived key
    fernet = Fernet(base64.urlsafe_b64encode(key))

    # Convert the sentence to bytes and encrypt it
    sentence_bytes = sentence.encode('utf-8')
    encrypted_sentence = fernet.encrypt(sentence_bytes)

    return encrypted_sentence.decode('utf-8')


def decrypt_sentence(encrypted_sentence, password):
    """
    Decrypts an encrypted sentence using the AES algorithm.

    Args:
        encrypted_sentence (str): The encrypted sentence to be decrypted.
        password (str): The password used for encryption.

    Returns:
        str: The decrypted sentence.
    """
    # Derive the key from the password using PBKDF2
    salt = b'\x8a\xf8\r\x9d\xe0\xc9\xd0\xf6\xa3\xd7\xd6\x14\x91\x03\x5c\xd6'  # The same salt value as used for encryption
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password.encode('utf-8'))

    # Create a Fernet object with the derived key
    fernet = Fernet(base64.urlsafe_b64encode(key))

    # Convert the encrypted sentence to bytes and decrypt it
    encrypted_sentence_bytes = encrypted_sentence.encode('utf-8')
    decrypted_sentence_bytes = fernet.decrypt(encrypted_sentence_bytes)

    return decrypted_sentence_bytes.decode('utf-8')


if __name__ == "__main__":
    original_sentence = input("Enter a sentence to encrypt: ")
    password = input("Enter a password for encryption: ")
    print(f"Original sentence: {original_sentence}")

    # Encryption
    encrypted_sentence = encrypt_sentence(original_sentence, password)
    print(f"Encrypted sentence: {encrypted_sentence}")

    # Decryption
    decrypted_sentence = decrypt_sentence(encrypted_sentence, password)
    print(f"Decrypted sentence: {decrypted_sentence}")
