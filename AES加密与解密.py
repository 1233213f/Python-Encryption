import base64,datetime,time
from urllib import request
from Crypto.Cipher import AES
from tqdm import tqdm


#依赖安装：pip3 install pycryptodome
ENCRYPT_KEY = "chenjq"

#补足16位并返回bytes
def add_to_16(value):
    while len(value) % 16 != 0:
        value = value + "\0"
    return str.encode(value)

#AES加密
def encrypt_aes(text):
    text = request.quote(text)
    aes = AES.new(add_to_16(ENCRYPT_KEY),AES.MODE_ECB)
    encrypt_aec = aes.encrypt(add_to_16(text))
    encrypt_text = str(base64.encodebytes(encrypt_aec),encoding="utf-8").strip()
    return encrypt_text

#AES解密
def decrypt_aes(text):
    aes = AES.new(add_to_16(ENCRYPT_KEY),AES.MODE_ECB)
    decrypt_aec = base64.decodebytes(text.encode(encoding='utf-8'))
    decrypt_text = str(aes.decrypt(decrypt_aec),encoding='utf-8').replace("\0",'')
    decrypt_text = request.unquote(decrypt_text)
    return decrypt_text
m=input("加密:数字or文件")
n=encrypt_aes(m)
print(n)
q=input("解密:数字or文件")
l=decrypt_aes(q)
print(l)

