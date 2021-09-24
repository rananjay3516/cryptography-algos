import requests
import urllib.request
from urllib.parse import quote

# pad = '5dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
# g = guess byte
# c_attack = attack cipher
# c  = target cipher
# i = intermediary
# p = plain text

# get 16 byte blocks c1, c2, c3, c4 from target cipher text
target_text = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
target = []  # 16 x 4
for i in range(0,128,2):
    element = target_text[i] + target_text[i+1]
    target.append(element)

c1 = target[:16]   # IV
c2 = target[16:32]
c3 = target[32:48]
c4 = target[48:]

# set up 16 byte block of random hex
random_hex = '8eeffa7b27da3727ee928e1c666411c92120a12f883aed461121e71f373451e51adb84ff02d806daa2f9c69a1dfc52bd3e69da3137a0ea31ac8bec21942c5ec5'
c_attack = []
for i in range(0,128,2):
    element = random_hex[i] + random_hex[i+1]
    c_attack.append(element)


c_dash_fixed = c_attack[48:]  # unmodified for later testing
c_dash = []
for i in c_dash_fixed:
    c_dash.append(i)
    
# get error code from passing concat of c_dash and c for decryption
def get_code(c_dash, c):
    Base_URL = 'http://crypto-class.appspot.com/po?er='
    cipher_URL = quote(''.join(c_dash) + ''.join(c))
    URL = Base_URL + cipher_URL
    r = requests.get(URL)
    return r.status_code
    
print(c_dash)
# do the thing for c2[k] with pad p
k = 0 # inter element
p = 16 # pad

c_dash[15] = str(hex(p ^ 32)).lstrip('0x')
c_dash[14] = str(hex(p ^ 115)).lstrip('0x')
c_dash[13] = str(hex(p ^ 211)).lstrip('0x')
c_dash[12] = str(hex(p ^ 237)).lstrip('0x')
c_dash[11] = str(hex(p ^ 176)).lstrip('0x')
c_dash[10] = str(hex(p ^ 134)).lstrip('0x')
c_dash[9] = str(hex(p ^ 102)).lstrip('0x')
c_dash[8] = str(hex(p ^ 211)).lstrip('0x')
c_dash[7] = str(hex(p ^ 190)).lstrip('0x')
c_dash[6] = str(hex(p ^ 137)).lstrip('0x')
c_dash[5] = str(hex(p ^ 72)).lstrip('0x')
c_dash[4] = str(hex(p ^ 178)).lstrip('0x')
c_dash[3] = str(hex(p ^ 134)).lstrip('0x')
c_dash[2] = str(hex(p ^ 190)).lstrip('0x')
c_dash[1] = str(hex(p ^ 99)).lstrip('0x')

print(c_dash)
for i in range(256):
    c_dash[k] = str(hex(i).lstrip('0x'))
    print(c_dash[k])
    if get_code(c_dash, c2) == 404:
        break
