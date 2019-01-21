from struct import unpack
byteArr1 = b'\x1F\x77'
byteArr2 = b'\x8A\x5B'

head_info = unpack('>H', byteArr2)[0]
win_info = unpack('>H', byteArr1)[0]
win_num = ((win_info & (2 ** 12 - 1)) >> 8) + 1
win_x = ((win_info & (2 ** 8 - 1)) >> 4) + 1
win_y = (win_info & (2 ** 4 - 1)) + 1


print(hex(win_info))
print(win_num)
print(win_x)
print(win_y)

a = [1, 3, 4]
b = [5, 6]
c = a + b
print(c)
# byteArr += b'\xBB'
# startbin = 0
# endbin = 15
# length = endbin - startbin + 1
# a = (2 ** (endbin + 1)) - 1
# # for i in range(length):
# #     a += 1 << startbin + length - i - 1
#
# print(bin(a))
# data = unpack('>h', byteArr)
# print(hex(data[0]))
# newdata = data[0] & a
# print(bin(newdata))
# newdata1 = newdata >> startbin
# print(bin(newdata1))
# print(newdata1)

# byteAr = b'\x01\x21'
# data = unpack('>h', byteAr)[0]
# startbit = [0, 4, 8]
# endbit = [3, 7, 11]
# bit = []
# for i in range(3):
#     standby_byte = (2 ** (endbit[i] + 1)) - 1
#     bit.append((data & standby_byte) >> startbit[i])
# print(str(bit[0])+'.'+str(bit[1])+'.'+str(bit[2]))

# string = 'AABB'
# print(type(string))
# s = "".join(string)
# data = bytes.fromhex(s)
# # data = string.decode('hex')
# print(data)

# rmTree = {}
# name = ["xy", "xu"]
# rmTree["LVDS"] = []
# for i in name:
#     rmTree["LVDS"].append(i)
#
# print(rmTree)





