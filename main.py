class Users():
    users = {}
    def __init__(self, name, password):
        self.name = name
        self.password = password
        Users.users[self.name] = self.password
    @classmethod
    def user(cls):
        return cls.users
    def __str__(self):
        return self.name
admin = Users("root", "123456")

def userscreate():
    print('注册'.center(50, '*'))
    print('*开头为必填项')
    name = input('*Enter a name:')

    if not name in Users.user():
        password = input('*Enter a password:')
        a = Users(name, password)

        print(a, "注册成功")
    else:
        print("用户已经存在")




def userslogin():
    print("登录".center(100,'*'))
    timeout = 0
    while timeout < 3:
        name = input("输入用户名：")
        if not name in Users.users:
            print ("用户不存在")
            timeout+=1

        else:
            password = input('输入密码：')
            if password == Users.users[name]:
               print ('登录成功')
               break
            else:
               print ('密码错误，请重新输入：')
               timeout+=1
    else:
           print ('输入超时')

info = '''
         *********************用户登录管理系统**********************
         1.注册新用户
         2.用户登录
         3.退出系统
         ***********************************************************
        '''
while 1:
     print (info)
     try:
         choice = int(input())
         if choice == 1:
             userscreate()
         elif choice == 2:
             userslogin()
         elif choice == 3:
             print("退出系统")
             break
         else:
             print("重新输入")
     except:
            print("请输入正确字符")
