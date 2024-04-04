import os
from tqdm import tqdm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt_file(input_file, output_file, password, chunk_size=65536):
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

    # 计算文件总大小
    file_size = os.path.getsize(input_file)

    # 逐块读取和加密数据，并显示进度条
    with open(input_file, 'rb') as input_f, open(output_file, 'wb') as output_f:
        output_f.write(salt)
        output_f.write(iv)

        with tqdm(total=file_size, unit='B', unit_scale=True, desc='Encrypting', leave=False) as pbar:
            while True:
                chunk = input_f.read(chunk_size)
                if not chunk:
                    break
                encrypted_chunk = encryptor.update(chunk)
                output_f.write(encrypted_chunk)
                pbar.update(len(chunk))

            output_f.write(encryptor.finalize())

def decrypt_file(input_file, output_file, password, chunk_size=65536):
    with open(input_file, 'rb') as input_f:
        # 从输入文件中读取盐值和初始化向量
        salt = input_f.read(16)
        iv = input_f.read(16)

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

        # 计算文件总大小
        file_size = os.path.getsize(input_file)

        # 逐块读取和解密数据，并显示进度条
        with open(output_file, 'wb') as output_f:
            with tqdm(total=file_size, unit='B', unit_scale=True, desc='Decrypting', leave=False) as pbar:
                while True:
                    chunk = input_f.read(chunk_size)
                    if not chunk:
                        break
                    decrypted_chunk = decryptor.update(chunk)
                    output_f.write(decrypted_chunk)
                    pbar.update(len(chunk))

                output_f.write(decryptor.finalize())


# 示例用法
if __name__ == "__main__":
    input_file = os.path.join(os.getcwd(), 'folder_test', 'type_zip', 'random_compressed_file2.zip')
    encrypted_file = os.path.join(os.getcwd(), 'folder_test', 'type_zip', 'random_compressed_file2.zip.encrypted')
    decrypted_file = os.path.join(os.getcwd(), 'folder_test', 'type_zip', 'random_compressed_file2_decrypted.zip')
    password = "700512"

    # 加密文件
    encrypt_file(input_file, encrypted_file, password)
    print("File encrypted successfully.")

    # 解密文件
    decrypt_file(encrypted_file, decrypted_file, password)
    print("File decrypted successfully.")
