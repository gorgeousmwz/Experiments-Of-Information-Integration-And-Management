import requests
import sys
import json
import re
from prettytable import PrettyTable
from requests.exceptions import HTTPError
class App:
    def __init__(self):
        self.optMap={
            '-h':'help',
            '--help':'help',
            '-a':'add',
            '--add':'add',
            '-u':'update',
            '--update':'update',
            '-d':'delete',
            '--delete':'delete',
            '-l':'list',
            '--list':'list',
            '-r':'retrieve',
            '--retrieve':'retrieve',
            '-e':'exit',
            '--exit':'exit',
            '-v':'version',
            '--version':'version'
        }
        self.fieldMap={
            '-n':'name',
            '--name':'name',
            '-i':'id',
            '--id':'id',
            '-p':'phonenumber',
            '--phonenumber':'phonenumber',
            '-e':'email',
            '--email':'email',
            '-m':'major',
            '--major':'major',
            '-h':'interest',
            '--hobby':'interest',
            '-b':'birthday',
            '--birthday':'birthday'
        }
        print('Welcome to MyDATA')
        self.listen()#开始监听

    def listen(self):
        '''监听用户输入,做出相应操作'''
        while True:#循环监听
            args=input('mydata>')
            args=args.split(' ')
            if args[0]!='App':#命令开头必须是App开头
                print('ERROR 001: You have an error in your mydata syntax, please add \'App\' before your commands')
            else:
                if len(args)==1:#没有选项时默认降序罗列操作
                    self.list('descend')
                if len(args)>=2:
                    if args[1] not in self.optMap:
                        print('ERROR 002: You have an error in your mydata syntax, there is not ['+args[1]+'] operation')
                    elif self.optMap[args[1]]=='help':#提示操作
                        if len(args)==2:
                            self.help()
                        else:
                            print('ERROR 003: You have an error in your mydata syntax, please check your [list] operation is right or not')
                    elif self.optMap[args[1]]=='exit':#提示操作
                        if len(args)==2:
                            self.exit()
                        else:
                            print('ERROR 004: You have an error in your mydata syntax, please check your [exit] operation is right or not')
                    elif self.optMap[args[1]]=='list':#罗列操作
                        if len(args)>3:
                            print('ERROR 005: You have an error in your mydata syntax, please check your [list] operation is right or not') 
                        else:
                            method='descend'#默认排列方式
                            flag=True
                            if len(args)==3:
                                if args[2] in ['descend','ascend']:
                                    method=args[2]
                                else:
                                    flag=False
                            if flag:
                                self.list(method)
                            else:
                                print('ERROR 006: You have an error in your mydata syntax, please check your [list] operation\'s method is right or not') 
                    elif self.optMap[args[1]]=='add':#添加操作
                        if len(args)==16:
                            flag=True
                            if len(args[2::2])!=len(set(args[2::2])):#字段不能重复
                                flag=False
                            for i in args[2::2]:#必须是有效字段
                                if  i not in self.fieldMap:
                                    flag=False
                            for i in args[3::2]:#添加值有效
                                if i in self.optMap or i in self.fieldMap:
                                    flag=False
                            if len(args[2::2])!=len(args[3::2]):#每个字段对应一个更新值
                                flag=False
                            if flag:
                                if self.valid(args[2:]):#数据验证
                                    self.add(args[2:])
                            else:
                                print('ERROR 007: You have an error in your mydata syntax, please check your [add] operation\'s fields is right or not')
                        else:
                            print('ERROR 008: You have an error in your mydata syntax, please check your [add] operation is right or not')
                    elif self.optMap[args[1]]=='delete':#删除操作
                        if len(args)==3 and args[2] not in self.optMap and args[2] not in self.fieldMap:
                            self.delete(args[2])
                        else:
                            print('ERROR 009: You have an error in your mydata syntax, please check your [delete] operation is right or not')
                    elif self.optMap[args[1]]=='update':#更新操作
                        if len(args)>=4 and len(args)<=17:
                            flag=True
                            for i in args[3::2]:#字段名有效
                                if i not in self.fieldMap:
                                    flag=False
                            for i in args[2::2]:#更新值有效
                                if i in self.optMap or i in self.fieldMap:
                                    flag=False
                            if len(args[3::2])!=len(set(args[3::2])):#字段不重复
                                flag=False
                            if len(args[3::2])!=len(args[4::2]):#每个字段对应一个更新值
                                flag=False
                            if flag:
                                if self.valid(args[3:]):
                                    self.update(args[2:])
                            else:
                                print('ERROR 010: You have an error in your mydata syntax, please check your [update] operation\' fields is right or not')
                        else:
                            print('ERROR 011: You have an error in your mydata syntax, please check your [update] operation is right or not')
                    elif self.optMap[args[1]]=='retrieve':#查询操作
                        if len(args)==4:
                            flag=True
                            if args[2] not in self.fieldMap:#字段有效
                                flag=False
                            if args[3] in self.optMap or args[3] in self.fieldMap:#查询值有效
                                flag=False
                            if flag:
                                self.retrieve(args[2:])
                            else:
                                print('ERROR 012: You have an error in your mydata syntax, please check your [retrieve] operation\' fields is right or not')
                        else:
                            print('ERROR 013: You have an error in your mydata syntax, please check your [retrieve] operation\ is right or not')
                    elif self.optMap[args[1]]=='version':#版本操作
                        if len(args)==2:
                            self.version()
                        else:
                            print('ERROR 0014: You have an error in your mydata syntax, please check your [version] operation is right or not')

    def list(self,method='descend'):
        '''罗列操作'''
        try:
            res=requests.get("http://localhost:5500/refreshData?method={}".format(method))#发送get请求
            res.raise_for_status()#获取异常
            result=res.json()#获取返回数据
            print('The [list] operation is successful! The data is follows:')
            self.display(result)
        except HTTPError as e:
            print('ERROR 15: The [list] operation is failed. The status code is '+str(res.status_code))
            print('The detail is followed:\n',e)
        
    def add(self,data):
        '''添加操作'''
        submit={}
        for i in range(0,len(data),2):#提交数据预处理
            submit[self.fieldMap[data[i]]]=data[i+1]
        submit=json.dumps(submit)
        try:
            res=requests.post("http://localhost:5500/submitData", headers={"Content-Type": "application/json"},data=submit)
            res.raise_for_status()#获取异常
            print('The [add] operation is successful!')
        except HTTPError as e:
            print('ERROR 16: The [add] operation is failed. The status code is '+str(res.status_code))
            print('The detail is followed:\n',e)

    def retrieve(self,data):
        '''查询操作'''
        try:
            res=requests.get("http://localhost:5500/retrieveData?flag={}&value={}".format(self.fieldMap[data[0]],data[1]))
            res.raise_for_status()#获取异常
            result=res.json()#获取返回数据
            print('The [retrieve] operation is successful! The result is followed:')
            self.display(result)
        except HTTPError as e:
            print('ERROR 17: The [retrieve] operation is failed. The status code is '+str(res.status_code))
            print('The detail is followed:\n',e)

    def update(self,data):
        '''更新操作'''
        #处理数据
        submit={'id':data[0]}
        for i in range(1,len(data),2):
            submit[self.fieldMap[data[i]]]=data[i+1]
        submit=json.dumps(submit)
        try:
            res=requests.put("http://localhost:5500/updateData",headers={"Content-Type": "application/json"},data=submit)
            res.raise_for_status()#获取异常
            result=res.json()#获取返回数据
            if result==[]:
                print('ERROR 18: The id you want to update doesn\'t exist.')
            else:
                print('The [update] operation is successful!')
        except HTTPError as e:
            print('ERROR 19: The [update] operation is failed. The status code is '+str(res.status_code))
            print('The detail is followed:\n',e)

    def delete(self,data):
        '''删除操作'''
        submit={'id':data}
        try:
            res=requests.delete("http://localhost:5500/deleteData",json=submit)
            res.raise_for_status()#获取异常
            result=res.json()#获取返回数据
            if result==[]:
                print('ERROR 20: The id you want to delete doesn\'t exist.')
            else:
                print('The [delete] operation is successful!')
        except HTTPError as e:
            print('ERROR 21: The [delete] operation is failed. The status code is '+str(res.status_code))
            print('The detail is followed:\n',e)

    def help(self):
        '''提示操作'''
        print('For the problems that you faces in your operation in person, MyData prepares very detailed instructions as follows.')
        print('List of all MyData commands:')
        print('Note that all text commands must start with \'App\'!')
        print('--add         (-a)  To add a piece of data in database.           Format: App -a -n [v1] -i [v2] -p [v3] -e [v4] -m [v5] -h [v6] -b [v7]')
        print('--delete      (-d)  To delete the specified data in database.     Format: App -d [id]')
        print('--update      (-u)  To update the specified data in database.     Format: App -u [id] [f1] [v1] [f2] [v2] ...')
        print('--retrieve    (-r)  To select the data you want in database.      Format: App -r [field] [value]')
        print('--list        (-l)  To show all data by asc or desc in database.  Format: App -l [ascend|descend]')
        print('--help        (-h)  To show the tips of MyData.                   Format: App -h')
        print('--version     (-v)  To show the version of MyData.                Format: App -v')
        print('List of all MyData fields:')
        print('Note that all text field must confirm to the valid rule!')
        print('--name        (-n)  Your name.                                    Rule: Be less than 8 characters and don\'t include numbers')
        print('--id          (-i)  The student id which can identify you.        Rule: Length is 13 and the first four numbers are 1900-2022')
        print('--phonenumber (-p)  Your tele-phone number.                       Rule: Length is 11 and it must begin with 1')
        print('--email       (-e)  The email you always use.                     Rule: Must include @ and . which aren\'t the beginning or ending')
        print('--major       (-m)  The subject you major in.                     Rule: There are no limits')
        print('--hobby       (-h)  The things you like to do.                    Rule: Be less than 32 characters')
        print('--birthday    (-b)  The day when you were born.                   Rule: The format is \'year-month-day\' and isn\'t future')

    def version(self):
        '''展示版本信息'''
        print('The MyData is a student data collection tool.')
        print('It has a website version and a command line version,and their usages are the same.')
        print('MyData is made by Wenzhuo Ma who study in WHU.')
        print('The version information is 1.0')
        print('If you have any question, please write an email to 2574485753@qq.com')

    def exit(self):
        '''退出操作'''
        print('Byebye~')
        sys.exit(0)

    def display(self,data):
        '''展示结果'''
        tabledata = []
        for i in data:
            tabledata.append([i['name'],i['id'],i['phonenumber'],i['email'],i['major'],i['interest'],i['birthday']])
        #打印输出
        table=PrettyTable(['name', 'id', 'phonenumber', 'email','major','interest','birthday'])
        for i in tabledata:
            table.add_row(i)
        print(table)
        print('{} rows in set.'.format(len(tabledata)))

    def valid(self,data):
        '''验证'''
        for i in range(0,len(data),2):#逐项验证
            if self.fieldMap[data[i]]=='name':#验证姓名
                if bool(re.search(r'\d',data[i+1]))==True or len(data[i+1])>8:#名字不能含有数字且不能超过8个字符
                    print('ERROR 22: The [name] field is not valid.')
                    return False
            if self.fieldMap[data[i]]=='id':#验证学号
                if bool(re.search(r'^(19\d{11}|20([0-1]\d{10}|2[0-2]\d{9}))$',data[i+1]))==False:#学号13字符，开头四位代表年份(1900-2022)
                    print('ERROR 23: The [id] field is not valid.')
                    return False
            if self.fieldMap[data[i]]=='phonenumber':#验证电话
                if bool(re.search(r'^[1]\d{10}$',data[i+1]))==False:#电话11位数字，开头为1
                    print('ERROR 24: The [phonenumber] field is not valid.')
                    return False
            if self.fieldMap[data[i]]=='email':#验证邮箱
                if bool(re.search(r'^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$',data[i+1]))==False:#邮箱中包含@和.，且不能出现在开头和结尾
                    print('ERROR 25: The [email] field is not valid.')
                    return False
            if self.fieldMap[data[i]]=='interest':#验证兴趣
                if len(data[i+1])>32:#兴趣不能超过32个字符
                    print('ERROR 26: The [interest] field is not valid.')
                    return False
            if self.fieldMap[data[i]]=='birthday':#验证生日
                if bool(re.search(r'^((19[2-9]\d{1})|(20(([0-1][0-9])|(2[0-2]))))\-((0?[1-9])|(1[0-2]))\-((0?[1-9])|([1-2][0-9])|30|31)',data[i+1]))==False:#生日不能是2023年，符合正常逻辑，格式为:年-月-日
                    print('ERROR 27: The [birthday] field is not valid.')
                    return False
        return True
        



if __name__=='__main__':
    App()