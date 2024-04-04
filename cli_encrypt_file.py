import argparse
from encrypt_file import encrypt_file  # 导入您的加密函数


def main():
    parser = argparse.ArgumentParser(description="Encrypt a file.")
    parser.add_argument("input_file", help="Input file to encrypt")
    parser.add_argument("encrypted_file", help="Output encrypted file")
    parser.add_argument("password", help="Encryption password")

    args = parser.parse_args()

    # 调用加密函数
    encrypt_file(args.input_file, args.encrypted_file, args.password)
    print("File encrypted successfully.")


if __name__ == "__main__":
    main()
