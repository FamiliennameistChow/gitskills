#!usr/bin/env python
# encoding:utf-8

'''
__Author__:沂水寒城
功能：找出来一个字符串中最长不重复子串
'''


def find_longest_no_repeat_substr(one_str):
    '''
    找出来一个字符串中最长不重复子串
    '''
    res_list = []
    length = len(one_str)
    for i in range(length):
        tmp = one_str[i]
        for j in range(i + 1, length):
            if one_str[j] not in tmp:
                tmp += one_str[j]
            else:
                break
        res_list.append(tmp)
    res_list.sort(key=lambda x: len(x))
    return len(res_list[-1])


if __name__ == '__main__':
    # one_str_list = ['120135435', 'abdfkjkgdok', '123456780423349']
    # for one_str in one_str_list:
    #     res = find_longest_no_repeat_substr(one_str)
    #     print('{0}最长非重复子串为：{1}'.format(one_str, res))

    one_str = "bcadb"
    res = find_longest_no_repeat_substr(one_str)
    print('{0}最长非重复子串为：{1}'.format(one_str, res))

