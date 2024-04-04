import os
import argparse
from encrypt_file import encrypt_file  # 导入您的加密函数
from encrypt_large_file import encrypt_file as encrypt_large_file  # 导入您的大文件加密函数


def main():
    parser = argparse.ArgumentParser(description="Encrypt a file.")
    parser.add_argument("input_file", help="Input file to encrypt")
    parser.add_argument("encrypted_file", help="Output encrypted file")
    parser.add_argument("password", help="Encryption password")

    args = parser.parse_args()

    # 如果文件大小小于 1GB，调用解密函数
    file_size = os.path.getsize(args.encrypted_file)
    if file_size < 1024 * 1024 * 1024:
        print(f'File size is {file_size / (1024 * 1024 * 1024)} GB, using normal encrypt_file.')
        encrypt_file(args.input_file, args.encrypted_file, args.password)
    else:
        # 否则调用大文件解密函数
        print(f'File size is {file_size / (1024 * 1024 * 1024)} GB, using encrypt_large_file.')
        encrypt_large_file(args.input_file, args.encrypted_file, args.password)

    print("File encrypted successfully.")


if __name__ == "__main__":
    main()
