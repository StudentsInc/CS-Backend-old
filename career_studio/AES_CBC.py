# from base64 import b64decode, b64encode
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from Crypto.Util.Padding import pad, unpad
#
#
# class AESCipher:
#
#     @staticmethod
#     def encrypt(data):
#         iv = get_random_bytes(AES.block_size)
#         key = get_random_bytes(AES.block_size)
#         cipher = AES.new(key, AES.MODE_CBC, iv)
#         return b64encode(key + iv + cipher.encrypt(pad(data.encode('utf-8'), AES.block_size)))
#
#     @staticmethod
#     def decrypt(data):
#         raw = b64decode(data)
#         key = raw[:AES.block_size]
#         cipher = AES.new(key, AES.MODE_CBC, raw[AES.block_size:(2 * AES.block_size)])
#         return unpad(cipher.decrypt(raw[(2 * AES.block_size):]), AES.block_size).decode('utf-8')
