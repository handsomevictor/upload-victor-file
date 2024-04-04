import os
import hashlib
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        data = f.read()

    # 生成随机的盐值
    salt = os.urandom(16)

    # 使用 PBKDF2HMAC 密码派生函数生成密钥
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,  # 迭代次数，可根据需要调整
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # 生成随机的初始化向量
    iv = os.urandom(16)

    # 使用 AES 加密算法进行加密
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    # 将盐值、初始化向量和加密数据写入输出文件
    with open(output_file, 'wb') as f:
        f.write(salt)
        f.write(iv)
        f.write(encrypted_data)


def decrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        # 从输入文件中读取盐值、初始化向量和加密数据
        salt = f.read(16)
        iv = f.read(16)
        encrypted_data = f.read()

    # 使用 PBKDF2HMAC 密码派生函数生成密钥
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,  # 迭代次数，与加密时保持一致
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # 使用 AES 解密算法进行解密
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # 将解密后的数据写入输出文件
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)


# 示例用法
if __name__ == "__main__":
    input_file = os.path.join(os.getcwd(), 'folder_test', 'for_test.txt')
    encrypted_file = os.path.join(os.getcwd(), 'folder_test', 'encrypted_file_for_test.bin')
    decrypted_file = os.path.join(os.getcwd(), 'folder_test', 'decrypted_file_for_test.txt')
    password = "700512"

    # 加密文件
    encrypt_file(input_file, encrypted_file, password)
    print("File encrypted successfully.")

    # 解密文件
    decrypt_file(encrypted_file, decrypted_file, password)
    print("File decrypted successfully.")
