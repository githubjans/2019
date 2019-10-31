def menu():
    os.system("cls")
    print("账号、密码管理系统")
    print("-------------------------")
    print("1. 输入账号、密码")
    print("2. 显示账号、密码")
    print("3. 修  改  密  码")
    print("4. 删除账号、密码")
    print("0. 结  束  程  序")
    print("-------------------------")

def CreatFile(paths):
    if os.path.exists(paths):
        print("该文件已经存在!")
    else:
        f=open(paths,'a',encoding = 'UTF-8-sig')
        f.close()
        
def ReadData(): 
    with open('password.txt','r', encoding = 'UTF-8-sig') as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata)
            return data
        else: return dict()  
        
def disp_data():
    print("账号\t密码")
    print("================")
    for key in data:
        print("{}\t{}".format(key,data[key]))
    input("按任意键返回主菜单")        
    
def input_data():       
    while True:
        name =input("请输入账号(Enter==>停止输入)")
        if name=="": break
        if name in data:
            print("{}账号已存在!".format(name))
            continue
        password=input("请输入密码：")
        data[name]=password
        with open('password.txt','w',encoding = 'UTF-8-sig') as f:
            f.write(str(data))
        print("{}已保存完毕".format(name)) 
    
def edit_data():
    while True:
        name =input("请输入要修改的账号(Enter==>停止输入)")
        if name=="": break
        if not name in data:
            print("{} 账号不存在!".format(name))
            continue
        print("原密码为：{}".format(data[name]))
        password=input("请输入新密码：")
        data[name]=password
        with open('password.txt','w',encoding = 'UTF-8-sig') as f:
            f.write(str(data))
            input("密码更改完毕，请按任意键返回主菜单") 
            break
    
def delete_data():
    while True:
        name =input("请输入要删除的账号(Enter==>停止输入)")
        if name=="": break
        if not name in data:
            print("{} 账号不存在!".format(name))
            continue
        print("确定删除{}的数据!：".format(name))
        yn=input("(Y/N)?")
        if (yn=="Y" or yn=="y"):
            del data[name]
            with open('password.txt','w',encoding = 'UTF-8-sig') as f:
                f.write(str(data))
                input("已删除完毕，请按任意键返回主菜单") 
                break

### 主程序从这里开始 ###

import os,ast
data=dict()

filepath1=os.path.dirname(__file__) + "//" + "password.txt"

if os.path.exists(filepath1)==False:
    CreatFile(filepath1)

data = ReadData()  # 读取文本文件后转换为 dict
while True:
    menu()
    choice = int(input("请输入您的选择："))
    print()
    if choice==1:
        input_data()
    elif choice==2:
        disp_data()
    elif choice==3:
        edit_data()
    elif choice==4:
        delete_data()
    else:
        break    
 
print("程序执行完毕！")

