#!-*- coding:utf-8 -*- 
''' 
Created on 2013-6-15 

@author: shangwei 
'''
''' 
全局变量 
'''
from Crypto.PublicKey import RSA

''' 
publickey为对方的公钥 
privatekey为商户自己的私钥 
'''
publickey = RSA.importKey(open('rsa_public_key.pem', 'r').read())
privatekey = RSA.importKey(open('pkcs8_rsa_private_key.pem', 'r').read())
merchantaccount = 'YB010000000xx'
URL = 'xxx.xxx.com'
