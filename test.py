import unittest
import os
import hashlib
from encrypt_file import encrypt_file, decrypt_file  # 导入您之前编写的加密和解密函数


class TestEncryption(unittest.TestCase):
    def setUp(self):
        # 在每个测试方法运行之前执行的设置
        self.input_files = [os.path.join(os.getcwd(), 'folder_test', 'type_jpeg', 'new_sad_frog.jpeg'),
                            os.path.join(os.getcwd(), 'folder_test', 'type_zip', 'random_compressed_file.zip'),
                            os.path.join(os.getcwd(), 'folder_test', 'type_rar', 'random_files.rar')]
        self.encrypted_files = [os.path.join(os.getcwd(), 'folder_test', 'type_jpeg',
                                             'encrypted_new_sad_frog.jpeg.encrypted'),
                                os.path.join(os.getcwd(), 'folder_test', 'type_zip',
                                             'encrypted_random_compressed_file.zip.encrypted'),
                                os.path.join(os.getcwd(), 'folder_test', 'type_rar',
                                             'encrypted_random_files.rar.encrypted')]
        self.decrypted_files = [os.path.join(os.getcwd(), 'folder_test', 'type_jpeg', 'decrypted_new_sad_frog.jpeg'),
                                os.path.join(os.getcwd(), 'folder_test', 'type_zip',
                                             'decrypted_random_compressed_file.zip'),
                                os.path.join(os.getcwd(), 'folder_test', 'type_rar', 'decrypted_random_files.rar')]

        self.password = "test_password"

    # def tearDown(self):
    #     # 在每个测试方法运行之后执行的清理
    #     for file in self.encrypted_files + self.decrypted_files:
    #         if os.path.exists(file):
    #             os.remove(file)

    def test_encryption_decryption(self):
        # 对每个输入文件进行加密和解密，并比较加密前和解密后的文件内容是否一致
        for i in range(len(self.input_files)):
            input_file = self.input_files[i]
            encrypted_file = self.encrypted_files[i]
            decrypted_file = self.decrypted_files[i]

            # 加密文件
            encrypt_file(input_file, encrypted_file, self.password)

            # 解密文件
            decrypt_file(encrypted_file, decrypted_file, self.password)

            # 比较加密前和解密后的文件内容是否一致
            md5_before = self.calculate_md5(input_file)
            md5_after = self.calculate_md5(decrypted_file)
            self.assertEqual(md5_before, md5_after)

    def calculate_md5(self, file_path):
        # 计算文件的 MD5 校验和
        with open(file_path, 'rb') as f:
            data = f.read()
            md5_hash = hashlib.md5()
            md5_hash.update(data)
            return md5_hash.hexdigest()


if __name__ == "__main__":
    unittest.main()
