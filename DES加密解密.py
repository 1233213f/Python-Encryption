import base64,datetime,time
from urllib import request
from Crypto.Cipher import DES
from tqdm import tqdm
#依赖安装：pip3 install pycryptodome
ENCRYPT_KEY = "29909"

#补足8位并返回bytes =================>如果是3DES，要import DES3,然后 add_to_16即可
def add_to_8(value):
    while len(value) % 8 != 0:
        value = value + "\0"
    return value.encode(encoding='utf-8')

#DES加密
def encrypt_des(text):
    text = request.quote(text)
    aes = DES.new(add_to_8(ENCRYPT_KEY),DES.MODE_ECB)

    encrypt_aec = aes.encrypt(add_to_8(text))
    encrypt_text = str(base64.encodebytes(encrypt_aec),encoding="utf-8").strip()
    return encrypt_text

#DES解密
def decrypt_des(text):
    aes = DES.new(add_to_8(ENCRYPT_KEY),DES.MODE_ECB)
    decrypt_aec = base64.decodebytes(text.encode(encoding='utf-8'))
    decrypt_text = str(aes.decrypt(decrypt_aec),encoding='utf-8').replace("\0",'')
    decrypt_text = request.unquote(decrypt_text)
    return decrypt_text
m=input("加密:数字or文件")
n=encrypt_des(m)
print(n)
q=input("解密:数字or文件")
l=decrypt_des(q)
print(l)