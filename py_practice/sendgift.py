"""
发礼物：
1拥有礼物的标识
2定义一个发礼物的方法
3定义一个展示礼物的方法
4启动方法
"""
# 拥有礼物的标识
have_gift = False


# 发礼物的方法
def send():
    print("发礼物啦")
    global have_gift
    have_gift = True


# 展示礼物的方法
def show():
    if have_gift == True:
        print("收到礼物")
    else:
        print("没有礼物")


print(f"name变量的值{__name__}")  # 变量
print(locals())  # 查看本地全局变量
if __name__ == '__main__':
    send()
    show()
