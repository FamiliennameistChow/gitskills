import os

# ##############################################
# # 定义时带默认参数
# def add(a=3, b=4):
#     return a + b
#
#
# a = add(4, 4)
# print(a)
# print(add())
# ###############################################


##############################################
def foo(x, items=[]):
    items.append(x)
    return items


def foo1(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items


# 默认参数保留了前面调用时的修改
print(foo(1))
print(foo(2))
print(foo(3))

print("----------------")
print(foo1(1))
print(foo1(2))
print(foo1(3))

