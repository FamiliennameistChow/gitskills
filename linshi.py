# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0, 0]
#
# re_list = []
# a = len(nums)
# break_flag = False
# for i in range(a):
#     # tmp.extend([nums[i]])
#     for j in range(i + 1, a):
#         num = nums[i] + nums[j]
#         # tmp.extend([nums[j]])
#         for k in range(j + 1, a):
#             if num + nums[k] == 0:
#                 tmp = []
#                 tmp.extend([nums[i], nums[j], nums[k]])
#                 tmp.sort()
#                 re_list.append(tmp)
#                 break
#
# for c in range(len(re_list)):
#     for b in range(c+1, len(re_list)):
#         if re_list[c] == re_list[b]:
#             re_list.remove(re_list[c])


# rel_list = []
# for b in re_list:
#     if not b in rel_list:
#         rel_list.append(b)
#
# print(rel_list)


# buf = {}
# buf['value'] = []
# for i in range(12):
#     print(type(buf["value"]))
#     buf['value'] = buf['value'].extend(i)
#     if 'value' in buf:
#         buf['value'] = buf['value'] + [i+13]
# print(buf)

# list = []
# # list = list.append(1)
# print(list)

i = 0
while True:
    i += 1
    if i == 5:
        continue
    print(i)
