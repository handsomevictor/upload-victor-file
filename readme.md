# 加密解密脚本

## 声明

该加密解密脚本是一个用于加密和解密文件的简单工具。使用者需要注意以下事项：

- **密码安全性：** 使用者应该谨慎选择密码，并且保证密码的安全性。如果忘记了密码，将无法解密文件。
- **版权声明：** 该脚本为开源项目，任何人都可以使用，但请遵守相关的版权声明和许可证。

## 功能介绍

该加密解密脚本具有以下功能：

- **加密文件：** 使用者可以通过指定输入文件、输出文件和密码，对文件进行加密。
- **解密文件：** 使用者可以通过指定加密后的文件、输出解密后的文件和密码，对加密文件进行解密。

## 使用方法

### 加密文件
```angular2html
python3 encrypt_cli.py input_file.txt encrypted_file.bin my_password
```

- `input_file.txt`：要加密的输入文件路径。
- `encrypted_file.bin`：加密后的输出文件路径。
- `my_password`：加密密码。

### 解密文件

```angular2html
python3 decrypt_cli.py encrypted_file.bin decrypted_file.txt my_password
```

- `encrypted_file.bin`：要解密的加密文件路径。
- `decrypted_file.txt`：解密后的输出文件路径。
- `my_password`：解密密码。

## 注意事项

- **密码保密性：** 强烈建议使用者选择强密码，并妥善保管密码，以确保文件的安全性。
- **文件完整性：** 解密后的文件应该与加密前的文件完全一致。如果文件大小、内容或格式发生变化，可能意味着解密出现了问题或者密码错误。
- **python版本：** 推荐使用3.11版本的Python运行脚本。

## 联系方式

作者不愿意透露任何联系方式，若想表示支持，请发送你想支持的SOL金额到以下地址：
8WLqc1QXsogBLkcxT3sFBGSburviY1q8gf467vuk5Fqo
