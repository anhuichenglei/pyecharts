class user:
    def __init__(self, name, password):
        self.name = name
        self.password = password


admin = user("root", "123456")  # 系统初始化用户

'*** 让用户输入功能选项，输入1启动登录功能 ***'
'*** 输入2启动注册功能，输入3退出系统 ***'
order = input('1:登录,2:注册（退出输入exit）:')

'*** 使用字典保存注册过的用户信息 ***'
'*** 注意，字典元素的key是用户名，value是用户对象 ***'
userInfos = {"root": admin}

'*** 在下面调整你的代码 ***'
'*** 修改while循环的条件，使用order变量控制循环的结束 ***'
while False:

    '*** 在下面调整你的代码 ***'
    '*** 修改if的条件，根据用户的选择做决定 ***'
    if False: #用户登录
        name = input('请输入用户名:')
        password = input('请输入密码:')

        '*** 在下面调整你的代码 ***'
        '*** 修改if的条件，判断用户是否存在，如果存在，则继续判断密码是否正确 ***'
        if False:
            if password == userInfos.get(name).password:
                print("登录成功")
            else:
                print("密码错误，登录失败！")
        else:
            print("该用户不存在，请核实登录信息")

    elif order == "2": #用户注册
        name = input('请输入用户名:')
        password = input('请输入密码:')

        '*** 在下面调整你的代码 ***'
        '*** 修改if的条件，判断用户是否存在，避免注册同名用户 ***'
        if False:
            print("该用户已存在，请重新注册")
        else:
            '*** 在这里补充你的代码 ***'
            '*** 根据输入内容，使用自定义的类型创建对象 ***'

            userInfos[name] = userInfo
            print("注册成功！")
    else:
        print("操作类型输入有误，请重新输入！")

    '*** 在这里补充你的代码 ***'
    '*** 实现可以多次登录或者注册的功能 ***'

