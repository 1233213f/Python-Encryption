 #构造映射 asc ---> crypt
def dic(x):
    list_x =[]
    list_z = []
    for i in x:
        list_x.append(ord(i))
    for i in range(97,123):
        if i not in list_x:
            list_x.append(i)
    list_ = list_x[26-len(x)-1:]
    cr = list_+list_x[:26-len(list_)]
    for i in range(97,123):
        list_z.append(i)
    return dict(map(lambda x,y:[x,y],list_z,cr))


# 构造映射 crypt ---> asc
def dic_2(x):
    list_x =[]
    list_z = []
    for i in x:
        list_x.append(ord(i))
    for i in range(97,123):
        if i not in list_x:
            list_x.append(i)
    list_ = list_x[26-len(x)-1:]
    cr = list_+list_x[:26-len(list_)]
    for i in range(97,123):
        list_z.append(i)
    return dict(map(lambda x,y:[x,y],cr,list_z))
# 密钥去重
def remove(x):
    unique_x = []
    for i in x:
        if i not in unique_x:
            unique_x.append(i)
    return unique_x
# 加密
def encode():
    x = input('请输入密钥字符：')
    if not x.isalpha():
        print('请输入正确的密钥格式！')
        exit(0)
    s = input('请输入明文：')
    print('加密后字符：',end='')
    unique_x = remove(x)
    dic_ = dic(unique_x)
    for i in s:
        if i.isspace():
            print(' ', end='')
        else:
            print(chr(dic_[ord(i)]),end='')


# 解密
def decode():
    x = input('请输入密钥字符：')
    if not x.isalpha():
        print('请输入正确的密钥格式！')
        exit(0)
    s = input('请输入密文：')
    print('解密后字符：',end='')
    unique_x = remove(x)
    dic_ = dic_2(unique_x)
    for i in s:
        if i.isspace():
            print(' ',end='')
        else:
            print(chr(dic_[ord(i)]),end='')
# 输入指令
answer = input(f'请输入所需的操作：编码/E or 解码/D:  ')
try:
    if answer.upper() == 'E':
        encode()
    elif answer.upper() == 'D':
        decode()
    else:
        print('输入错误！')
except KeyError:
    print('请正确输入小写字母！')
'''密钥加密是发送和接收数据的双方，使用相同的或对称的密钥对明文进行加密解密运算的加密方法。
若加密算法是公开的，那么真正的秘密就在于密钥了，密钥必须是保密的，它通常是一个字符串，并且可以按需频繁更换。因此，密钥的长度很重要，因为一旦找到解密密钥也就破译了密码，而密钥的长度越长，密钥空间就越大，遍历密钥空间所花费的时间就越长，破译的可能性也就越小。'''