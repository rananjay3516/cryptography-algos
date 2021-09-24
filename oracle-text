# get 16 byte blocks c1, c2, c3, c4 from target cipher text
target_text = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
target = []  # 16 x 4
for i in range(0,128,2):
    element = target_text[i] + target_text[i+1]
    target.append(element)

c1 = target[:16]   #iv
c2 = target[16:32]
c3 = target[32:48]
c4 = target[48:]


inter4 = [239, 240, 98, 54, 71, 156, 52, 84, 164, 54, 40, 248, 131, 172, 126, 201]
inter3 = [239, 195, 154, 148, 114, 123, 45, 106, 21, 230, 35, 180, 124, 224, 78, 206]
inter2 = [166, 99, 190, 134, 178, 72, 137, 190, 211, 102, 134, 176, 237, 211, 115, 32]
plain2 = ['T', 'h', 'e', ' ', 'M', 'a', 'g', 'i', 'c', ' ', 'W', 'o', 'r', 'd', 's', ' ']
plain3 = ['·', 'r', 'e', ' ', 'S', 'q', 'u', 'e', 'a', 'm', 'i', 's', 'h', ' ', 'O', 's']
plain4 = ['¥', '\x91', 'f', 'r', 'a', 'g', 'e', '\t', '\t', '\t', '\t', '\t', '\t', '\t', '\t', '\t']

# set up intermediate block and plaintext block
inter = []
plain = []
for i in range(16):
    inter.append('0')
    plain.append('0')
    
inter[15] = int('21', 16) ^ 1
print(inter) # in ints
inter[14] = int('71',16) ^ 2
print(inter) # in ints
inter[13] = int('d0',16) ^ 3
print(inter) # in ints
inter[12] = int('e9',16) ^ 4
print(inter) # in ints
inter[11] = int('b5',16) ^ 5
print(inter) # in ints
inter[10] = int('80',16) ^ 6
print(inter) # in ints
inter[9] = int('61',16) ^ 7
print(inter) # in ints
inter[8] = int('db',16) ^ 8
print(inter) # in ints
inter[7] = int('b7',16) ^ 9
print(inter) # in ints
inter[6] = int('83',16) ^ 10
print(inter) # in ints
inter[5] = int('43',16) ^ 11
print(inter) # in ints
inter[4] = int('be',16) ^ 12
print(inter) # in ints
inter[3] = int('8b',16) ^ 13
print(inter) # in ints
inter[2] = int('b0',16) ^ 14
print(inter) # in ints
inter[1] = int('6c',16) ^ 15
print(inter) # in ints
inter[0] = int('b6',16) ^ 16
print(inter) # in ints
# calculate plain c2

for i in range(16):
    plain[i] = int(c1[i], 16) ^ int(inter[i])
print(plain)
for c in plain:
    plain2.append(chr(c))
print(plain2)
