import numpy as np
from struct import unpack, pack
import time
from json import dumps, loads

rmStruct = []
rmTree = {}
rmTree["LVDS"] = []


def decode_item(buf, name, width, typ, flag, section, starbit, endbit, func):

    rmStruct.append({'name': name, 'width': width, 'type': typ})
    # if parent not in rmTree:
    #     rmTree[parent] = [name]
    # else:
    #     rmTree[parent].append(name)
    rmTree["LVDS"].append(name)

    lensec = len(section)

    def padlen(length, section):
        if length == len(section):
            return section
        else:
            return chr(0) * (length - len(section)) + section
    unpack_data = 0
    if lensec == 8:
        unpack_data = unpack('>Q', padlen(8, section))[0]
    elif lensec == 4:
        unpack_data = unpack('>i', padlen(4, section))[0]
    elif lensec == 4:
        unpack_data = unpack('>I', padlen(4, section))[0]
    # elif lensec == 2:
        # unpack_data = unpack('>h', padlen(2, section))[0]
    elif lensec == 2:
        unpack_data = unpack('>H', padlen(2, section))[0]
    elif lensec == 1:
        unpack_data = unpack('>B', padlen(1, section))[0]
    elif lensec == 1:
        unpack_data = unpack('>B', padlen(1, section))[0]
    # elif fmt == 'u24':

    if flag == 'byte':
        if name in buf:
            buf[name] = buf[name] + [func(unpack_data)]
        else:
            buf[name] = func(unpack_data)

    elif flag == 'bit':
        standby_byte = (2 ** (endbit + 1)) - 1
        bit_data = (unpack_data & standby_byte) >> starbit
        if name in buf:
            buf[name] = buf[name] + [func(bit_data)]
        else:
            buf[name] = func(bit_data)


def to_version(x):
    startbit = [0, 4, 8]
    endbit = [3, 7, 11]
    bit = []
    for i in range(3):
        standby_byte = (2 ** (endbit[i] + 1)) - 1
        bit.append((x & standby_byte) >> startbit[i])
    return str(bit[0]) + '.' + str(bit[1]) + '.' + str(bit[2])


def judge(x):
    if x == 255:
        return 1
    if x == 170:
        return 0


def decode_data(buf, pkg_name, datastr):
    if pkg_name == "CAK_TST_SCP":
        # decode_item(buf, name, flag, section, starbit, endbit, func):
        # decode_item(buf, name, width, typ, flag, section, starbit, endbit, func):
        index = 0
        # decode_item(buf, 'FRAME_HEAD', 90, "I", "bit", datastr[index:index + 4], 16, 31, lambda x: hex(x))
        decode_item(buf, "STAR_IMG_ID", 90, "I", "bit", datastr[index:index + 4], 0, 15, lambda x: x)
        index += 4
        decode_item(buf, "STATE_BYTE", 90, "I", "bit", datastr[index:index + 4], 16, 31, lambda x: to_version(x))
        decode_item(buf, "THR_OFST", 90, "I", "bit", datastr[index:index + 4], 8, 15, lambda x: x)
        decode_item(buf, "OH_REBOOT_CNT", 90, "I", "bit", datastr[index:index + 4], 0, 7, lambda x: x)
        index += 4
        decode_item(buf, "ITR_T", 90, "I", "bit", datastr[index:index + 4], 16, 31, lambda x: round((x * 5.12)/1000, 2))
        # decode_item(buf, "RESERVED", 90, "I", "bit", datastr[index:index + 4], 0, 15, lambda x: x)
        index += 4
        # decode_item(buf, "RESERVED", 90, "I", "bit", datastr[index:index + 4], 24, 31, lambda x: x)
        decode_item(buf, "ST", 90, "I", "bit", datastr[index:index + 4], 0, 23, lambda x: x)
        index += 4
        # decode_item(buf, "RESERVED", 90, "I", "bit", datastr[index:index + 4], 0, 31, lambda x: x)
        index += 4
        decode_item(buf, "ETR_CNT_ST", 90, "I", "bit", datastr[index:index + 4], 16, 31, lambda x: x)
        decode_item(buf, "ETR_DT_ST", 90, "I", "bit", datastr[index:index + 4], 0, 15, lambda x: round((x * 20)/1000, 2))
        index += 4
        # decode_item(buf, "RESERVED", 90, "I", "bit", datastr[index:index + 4], 8, 31, lambda x: x)
        decode_item(buf, "TEMP_EU", 90, "I", "bit", datastr[index:index + 4], 0, 7, lambda x: x)
        index += 4
        decode_item(buf, "ETR_T", 90, "I", "bit", datastr[index:index + 4], 16, 31, lambda x: round((x * 20)/1000, 2))
        decode_item(buf, "TEMP_SEN", 90, "I", "bit", datastr[index:index + 4], 8, 15, lambda x: x)
        decode_item(buf, "TEMP_SHL", 90, "I", "bit", datastr[index:index + 4], 0, 7, lambda x: x)
        index += 4
        for i in range(125):
            ii = i + 1
            decode_item(buf, "SS_SCP_XG_"+str(ii), 90, "I", "bit", datastr[index:index + 4], 0, 31, lambda x: x)
            index += 4
            decode_item(buf, "SS_SCP_YG_" + str(ii), 90, "I", "bit", datastr[index:index + 4], 0, 31, lambda x: x)
            index += 4
            decode_item(buf, "SS_SCP_S_" + str(ii), 90, "I", "bit", datastr[index:index + 4], 24, 31, lambda x: x)
            decode_item(buf, "SS_SCP_G_" + str(ii), 90, "I", "bit", datastr[index:index + 4], 0, 23, lambda x: x)
            index += 4
            # decode_item(buf, "RESERVED", 90, "I", "bit", datastr[index:index + 4], 0, 31, lambda x: x)
            index += 4
        # 508
        decode_item(buf, "EXP_TIME", 90, "I", "bit", datastr[index:index + 4], 24, 31, lambda x: round(x * 1.31072, 2))
        # decode_item(buf, "RESERVED", 90, "I", "bit", datastr[index:index + 4], 16, 23, lambda x: x)
        # decode_item(buf, "RESERVED", 90, "I", "bit", datastr[index:index + 4], 14, 15, lambda x: x)
        # decode_item(buf, "ERR_FLAG_CREDIT", 90, "I", "bit", datastr[index:index + 4], 13, 13, lambda x: x)
        # decode_item(buf, "ERR_FLAG_ESCAPE", 90, "I", "bit", datastr[index:index + 4], 12, 12, lambda x: x)
        # decode_item(buf, "ERR_FLAG_PANTY", 90, "I", "bit", datastr[index:index + 4], 11, 11, lambda x: x)
        # decode_item(buf, "ERR_FLAG_DISCONNECT", 90, "I", "bit", datastr[index:index + 4], 10, 10, lambda x: x)
        decode_item(buf, "ERR_FLAG_HEAD_REC_CON_STATE", 90, "I", "bit", datastr[index:index + 4], 9, 9, lambda x: x)
        decode_item(buf, "ERR_FLAG_BOX_REC_CON_STATE", 90, "I", "bit", datastr[index:index + 4], 8, 8, lambda x: x)
        decode_item(buf, "ERR_FLAG_HEAD_REC_CON_SUBWIN_STATE", 90, "I", "bit", datastr[index:index + 4], 7, 7, lambda x: x)
        decode_item(buf, "ERR_FLAG_BOX_REC_CON_SUBWIN_STATE", 90, "I", "bit", datastr[index:index + 4], 6, 6, lambda x: x)
        decode_item(buf, "ERR_FLAG_HEAD_REC_STATE", 90, "I", "bit", datastr[index:index + 4], 5, 5, lambda x: x)
        # decode_item(buf, "ERR_FLAG_HEAD_DATA_TRAN_STATE", 90, "I", "bit", datastr[index:index + 4], 3, 4, lambda x: x)
        decode_item(buf, "ERR_FLAG_SUBWIN_CONTROL_HEAD_CNT", 90, "I", "bit", datastr[index:index + 4], 1, 2, lambda x: x)
        decode_item(buf, "ERR_FLAG_SUBWIN_CONTROL_BOX", 90, "I", "bit", datastr[index:index + 4], 0, 0, lambda x: x)
        index += 4   # 509
        decode_item(buf, "LVDS_ON_OFF", 90, "I", "bit", datastr[index:index + 4], 31, 31, lambda x: x)
        decode_item(buf, "DATA_TRAN", 90, "I", "bit", datastr[index:index + 4], 29, 30, lambda x: x)
        # decode_item(buf, "RESERVED", 90, "I", "bit", datastr[index:index + 4], 27, 28, lambda x: x)
        decode_item(buf, "DATA_TRAN_F", 90, "I", "bit", datastr[index:index + 4], 24, 26, lambda x: x)
        decode_item(buf, "SEN_GAIN_OFFSET", 90, "I", "bit", datastr[index:index + 4], 18, 23, lambda x: x)
        decode_item(buf, "SEN_GAIN", 90, "I", "bit", datastr[index:index + 4], 16, 17, lambda x: 2 ** x)
        decode_item(buf, "SEN_OFFSET", 90, "I", "bit", datastr[index:index + 4], 8, 15, lambda x: x)
        decode_item(buf, "TEMP_LEN", 90, "I", "bit", datastr[index:index + 4], 0, 7, lambda x: x)
        index += 4
        # decode_item(buf, "RESERVED", 90, "I", "bit", datastr[index:index + 4], 0, 31, lambda x: x)
        index += 4
        decode_item(buf, "PEL_STATE", 90, "I", "bit", datastr[index:index + 4], 24, 31, lambda x: judge(x))
        # decode_item(buf, "RESERVED", 90, "I", "bit", datastr[index:index + 4], 16, 23, lambda x: x)
        decode_item(buf, "WD_CNT", 90, "I", "bit", datastr[index:index + 4], 8, 15, lambda x: x)
        decode_item(buf, "STAR_NUM_S", 90, "I", "bit", datastr[index:index + 4], 0, 7, lambda x: x)
        index += 4

    if pkg_name == "CAK_TST_THR":
        # decode_item(buf, name, fmt, section, func):
        index = 0
        buf['GRAY_MEAN'] = []
        for i in range(1024):
            decode_item(buf, 'GRAY_MEAN', 90, "I", "byte", datastr[index:index + 2], 0, 15, lambda x: x)
            index += 2

    if pkg_name == "SUBWIN_DAT":
        # decode_item(buf, name, fmt, section, func):
        index = 0
        # decode_item(buf, 'FRAME_HEAD', 90, "I", "byte", datastr[index:index + 2], 0, 15, lambda x: hex(x))
        # index += 2
        # decode_item(buf, "gray_updata", 90, "I", "bit", datastr[index:index + 2], 15, 15, lambda x: x)
        # decode_item(buf, "windown_num", 90, "I", "bit", datastr[index:index + 2], 8, 11, lambda x: x + 1)
        # decode_item(buf, "window_x", 90, "I", "bit", datastr[index:index + 2], 4, 7, lambda x: x + 1)
        # decode_item(buf, "window_y", 90, "I", "bit", datastr[index:index + 2], 0, 3, lambda x: x + 1)
        # index += 2
        buf['WIN1_PIXEL_VALUE'] = []
        buf['WIN1_PIXEL_OVER_FLAG'] = []
        for i in range(253):
            ii = i + 1
            # decode_item(buf, 'RESERVED', 90, "I", "byte", datastr[index:index+2],13, 15, lambda x: x)
            decode_item(buf, 'WIN1_PIXEL_OVER_FLAG', 90, "I", "bit", datastr[index:index + 2], 12, 12, lambda x: x)
            decode_item(buf, 'WIN1_PIXEL_VALUE', 90, "I", "bit", datastr[index:index + 2], 0, 11, lambda x: x)
            index += 2
        decode_item(buf, "GS_ID", 90, "I", "bit", datastr[index:index + 2], 0, 15, lambda x: x)
        index += 2
        decode_item(buf, "wrs", 90, "I", "bit", datastr[index:index + 2], 0, 9, lambda x: x + 1)
        index += 2
        decode_item(buf, "wcs", 90, "I", "bit", datastr[index:index + 2], 0, 9, lambda x: x + 1)
        index += 2
        buf['WIN1_SEG_Y'] = []
        buf['WIN1_SEG_X'] = []
        buf['WIN1_SEG_BKG'] = []
        buf['WIN1_SEG_VLD_FLAG'] = []
        buf['WIN1_SEG_ENER'] = []
        buf['WIN1_SEG_WEIGHTED_ENER_LOW'] = []
        buf['WIN1_SEG_LENGTH'] = []
        buf['WIN1_SEG_WEIGHTED_ENER_HIGHT'] = []
        for i in range(128):
            ii = i + 1
            decode_item(buf, 'WIN1_SEG_Y', 90, "I", "byte", datastr[index:index + 2], 0, 15, lambda x: x + 1)
            index += 2
            decode_item(buf, 'WIN1_SEG_X', 90, "I", "byte", datastr[index:index + 2], 0, 15, lambda x: x + 1)
            index += 2
            decode_item(buf, 'WIN1_SEG_BKG', 90, "I", "bit", datastr[index:index + 2], 4, 15, lambda x: x)
            decode_item(buf, 'WIN1_SEG_VLD_FLAG', 90, "I", "bit", datastr[index:index + 2], 0, 3, lambda x: x)
            index += 2
            decode_item(buf, 'WIN1_SEG_ENER', 90, "I", "byte", datastr[index:index + 2], 0, 15, lambda x: x)
            index += 2
            decode_item(buf, 'WIN1_SEG_WEIGHTED_ENER_LOW', 90, "I", "byte", datastr[index:index + 2], 0, 15, lambda x: x)
            index += 2
            decode_item(buf, 'WIN1_SEG_LENGTH', 90, "I", "bit", datastr[index:index + 2], 12, 15, lambda x: x+1)
            # decode_item(buf, 'RESERVED', 90, "I", "bit", datastr[index:index+2],10, 11, lambda x: x)
            decode_item(buf, 'WIN1_SEG_WEIGHTED_ENER_HIGHT', 90, "I", "bit", datastr[index:index + 2], 0, 9, lambda x: x)
            index += 2

'''
with open('LVDSDataOrigin181217_112906.txt', 'r') as f:
# with open('8a5b.txt', 'r') as f:
    arr =[]
    for line in f:
        arr += line.split()
        # print(arr)
    res = [x for x in arr]
    # print(data[0])
    # print("%02X" % data[2])
    # for i in range(len(data[4:8])):
    #     print("%02X" % data[4+i])
    # print(data[4:8])
    # Lvds_count = data[0:4]
    # print(hex(data[0])[2::])
    s = "".join(res)
    data = bytes.fromhex(s)

    byteArr = b'\x8A\x5B\x0F\x77'

    head_info = data[0:16]
    # print(hex(headinfo))

    LVDS_HEAD = unpack("<i", head_info[0:4])[0]
    print(hex(LVDS_HEAD))
    if hex(LVDS_HEAD) == "0x5555aaaa":
        print("package head RIGHT")
    else:
        print("package head ERROR")
    LVDS_length = unpack("<I", head_info[4:8])[0]
    print("received total length %s BYTE" % LVDS_length)
    current_package_length = unpack("<I", head_info[8:12])[0]
    # print(hex(current_package_length))
    print("current package length: %s BYTE" % current_package_length)
    package_total = unpack('<H', head_info[12:14])[0]
    # print(hex(package_total))
    print("total package number: %s" % package_total)
    package_count = unpack('<H', head_info[14:16])[0]
    # print(hex(package_count))
    print("current package count: %s" % package_count)

    # data processing
    rm_buffer = {}

    # startime = time.time()
    data = data[16:]
    frame_head_scp = unpack('>H', data[0:2])[0]
    if hex(frame_head_scp) == '0x8a5c':
        decode_data(rm_buffer, "CAK_TST_SCP", data[0:2048])
        data_CAK_TST_THR = data[2048: 4096]
        decode_data(rm_buffer, "CAK_TST_THR", data_CAK_TST_THR[0:2048])
    data = data[4096:]
    start = 0
    end = 0
    cnt = 0
    while start != '0x8a' or end != '0x5b':
        start = hex(data[cnt])
        end = hex(data[cnt+1])
        cnt += 2
    decode_data(rm_buffer, "SUBWIN_DAT", data[cnt-2:])
    print(rm_buffer)
    print(dumps(rm_buffer))
    print(rmStruct)
    print(rmTree)

    # endtime = time.time()
    # print(endtime-startime)
'''






