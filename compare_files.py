import os
import hashlib


def calculate_md5(file_path):
    # 计算文件的 MD5 校验和
    with open(file_path, 'rb') as f:
        data = f.read()
        md5_hash = hashlib.md5()
        md5_hash.update(data)
        return md5_hash.hexdigest()


def compare_files(file1, file2):
    # 比较两个文件的 MD5 校验和
    md5_file1 = calculate_md5(file1)
    md5_file2 = calculate_md5(file2)
    return md5_file1 == md5_file2


if __name__ == "__main__":
    file1_path = os.path.join(os.getcwd(), 'folder_test', 'for_test.txt')
    file2_path = os.path.join(os.getcwd(), 'folder_test', 'decrypted_file_for_test.txt')

    if compare_files(file1_path, file2_path):
        print("Files are identical.")
    else:
        print("Files are not identical.")
