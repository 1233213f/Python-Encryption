# 栅栏密码加密解密
# @ChenYe
def crypto():
    plain = input('输入明文：')
    n = int(input('输入每组字数'))
    ans = ''
    for i in range(n):
        for j in range(int(plain.__len__() / n + 0.5)):
            try:
                ans += plain[j * n + i]
            except:
                pass
    return ans


def decrypto():
    plain = input('输入密文：')
    for n in range(2, plain.__len__() - 1):
        ans = ''
        for i in range(n):
            for j in range(int(plain.__len__() / n + 0.5)):
                try:
                    ans += plain[j * n + i]
                except:
                    pass
        print(ans)


if __name__ == '__main__':
    print('栅栏密码加密/解密.py')
    while (True):
        choice = input('功能选择：\n1：加密\n2：解密\n')
        # 加密
        if choice == '1':
            print(crypto())
        # 解密
        elif choice == '2':
            decrypto()
        else:
            print('choice error!')