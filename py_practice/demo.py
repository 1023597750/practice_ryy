

a = 1

def fun():
    #定义全局变量
    global a
    a = 2
    # 打印a的内存地址
    print(id(a))
    print(f"变量a的值：{a}")
    # return True


#
# print(a)
# fun()
# print(id(a))

# 没有return则，print(fun())打印None，有的话，这打印return的值
# print(fun())


# 使用python解释器,运行模块的入口
if __name__ == '__main__':
    print("start")
    fun()
    print("end")


