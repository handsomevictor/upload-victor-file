import argparse
from encrypt_file import decrypt_file  # 导入您的解密函数


def main():
    parser = argparse.ArgumentParser(description="Decrypt a file.")
    parser.add_argument("encrypted_file", help="Encrypted file to decrypt")
    parser.add_argument("decrypted_file", help="Output decrypted file")
    parser.add_argument("password", help="Decryption password")

    args = parser.parse_args()

    # 调用解密函数
    decrypt_file(args.encrypted_file, args.decrypted_file, args.password)
    print("File decrypted successfully.")


if __name__ == "__main__":
    main()
