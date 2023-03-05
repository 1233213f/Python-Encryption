import string


def kaisa_jiami(s, k):
    lower = string.ascii_lowercase  # 小写英文字母
    upper = string.ascii_uppercase  # 大写英文字母
    before = string.ascii_letters  # 全部英文字母字母
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]  # 建立循环字母
    table = ''.maketrans(before, after)  # 创建映射表
    return s.translate(table)


def kaisa_jiemi(s, k):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    before = string.ascii_letters
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = ''.maketrans(after, before)
    return s.translate(table)


def main():
    s = input("请输入要加密的字符串：")
    k = int(input("请输入一个整数密钥："))  # 将k转换为整数，默认输入为字符
    print('需要加密的字符串为：', s)
    a = kaisa_jiami(s, k)
    print("加密后为：", a)
    b = kaisa_jiemi(a, k)
    print("解密后为：", b)


if __name__ == '__main__':
    main()
    '''在密码学中，恺撒密码（英语：Caesar cipher），或称恺撒加密、恺撒变换、变换加密，是一种最简单且最广为人知的加密技术。它是一种替换加密的技术，明文中的所有字母都在字母表上向后（或向前）按照一个固定数目进行偏移后被替换成密文。例如，当偏移量是3的时候，所有的字母A将被替换成D，B变成E，以此类推。这个加密方法是以罗马共和时期恺撒的名字命名的，当年恺撒曾用此方法与其将军们进行联系。'''