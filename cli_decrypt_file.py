import os
import argparse
from encrypt_file import decrypt_file  # 导入您的解密函数
from encrypt_large_file import decrypt_file as decrypt_large_file  # 导入您的大文件解密函数


def main():
    parser = argparse.ArgumentParser(description="Decrypt a file.")
    parser.add_argument("encrypted_file", help="Encrypted file to decrypt")
    parser.add_argument("decrypted_file", help="Output decrypted file")
    parser.add_argument("password", help="Decryption password")

    args = parser.parse_args()

    # 如果文件大小小于 1GB，调用解密函数
    file_size = os.path.getsize(args.encrypted_file)
    if file_size < 1024 * 1024 * 1024:
        print(f'File size is {file_size / (1024 * 1024 * 1024)} GB, using normal decrypt_file.')
        decrypt_file(args.encrypted_file, args.decrypted_file, args.password)
    else:
        # 否则调用大文件解密函数
        print(f'File size is {file_size / (1024 * 1024 * 1024)} GB, using decrypt_large_file.')
        decrypt_large_file(args.encrypted_file, args.decrypted_file, args.password)
    print("File decrypted successfully.")


if __name__ == "__main__":
    main()
