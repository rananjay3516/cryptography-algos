import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util import Counter

key = bytes.fromhex('36f18357be4dbd77f050515c73fcf9f2')
nonce_bytes = bytes.fromhex('770b80259ec33beb')
Enonce = b64encode(nonce_bytes).decode('utf-8')
nonce = b64decode(Enonce)

counter = bytes.fromhex('2561358a9f2dc617')

ct_bytes = bytes.fromhex('e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451')
ctE = b64encode(ct_bytes).decode('utf-8')
ct = b64decode(ctE)

cipher = AES.new(key, AES.MODE_CTR, nonce=nonce, initial_value=counter)
pt = cipher.decrypt(ct)
print(pt)
