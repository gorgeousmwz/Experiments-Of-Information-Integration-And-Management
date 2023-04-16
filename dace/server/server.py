import pymysql
from flask import Flask, render_template, request,jsonify
from flask_cors import cross_origin
ItemMap={
    0:'name',
    1:'id',
    2:'phonenumber',
    3:'email',
    4:'major',
    5:'interest',
    6:'birthday'
}
app = Flask(__name__)

def connectDB():
    '''mysql数据库连接'''
    db=pymysql.connect(#数据库连接
        host='localhost',
        user='root',
        password='090012',
        database='students',
        charset='utf8'
    )
    cursor=db.cursor()#创建游标
    print('连接mysql数据库students成功')
    return db,cursor

def closeDB(db,cursor):
    '''关闭数据库连接'''
    cursor.close()
    db.close()
    print('数据库连接关闭成功')

def start():
    '''启动服务器'''
    print('启动服务器成功')
    app.run(host='127.0.0.1',port=5500)

def add(db,cursor,data):
    '''增加数据'''
    #如果之前不存在，则插入；如果之前存在，则更新
    sql='replace into student values (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');'\
        .format(data['name'],data['id'],data['phonenumber'],\
        data['email'],data['major'],data['interest'],data['birthday'])
    try:
        cursor.execute(sql)#执行sql语句
        db.commit()#提交事务
        print("成功插入:",data)
    except Exception as e:
        print("插入操作出现错误:{}".format(e))
        db.rollback()# 回滚所有更改

def retrieve(db,cursor,flag='*',data='*',method='descend'):
    '''查询数据'''
    if method=='descend':
        method='desc'
    else:
        method='asc'
    sql=''
    if flag=='*' and data=='*':
        sql='select * from student order by id {};'.format(method)
    else:
        sql='select * from student where {} = \'{}\' order by id {};'.format(flag,data,method)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()#获取查询结果
        print("查询【{}={}】成功".format(flag,data))
        return result
    except Exception as e:
        print("查询操作出现错误:{}".format(e))
        return None

def update(db,cursor,data):
    '''更新数据'''
    sql='update student set '
    for i in data.keys():
        if i=='id':
            continue
        sql+=i+' = '+'\''+data[i]+'\','
    sql=sql[:-1]
    sql+=' where id = \'{}\';'.format(data['id'])
    print(sql)
    try:
        cursor.execute(sql)#执行sql语句
        db.commit()#提交事务
        print("成功更新:",data)
    except Exception as e:
        print("更新操作出现错误:{}".format(e))
        db.rollback()# 回滚所有更改

def delete(db,cursor,flag,data):
    '''删除数据'''
    sql=''
    if flag=='*' and data=='*':#删除表中所有数据
        sql='truncate table student;'
    else:
        sql='delete from student where {} = \'{}\';'.format(flag,data);
    try:
        cursor.execute(sql)#执行sql语句
        db.commit()#提交事务
        print("成功删除"+flag+'为'+data+'的数据')
    except Exception as e:
        print("删除操作出现错误:{}".format(e))
        db.rollback()# 回滚所有更改

def transform(data):
    '''格式转换'''
    #将查询结果从元组转换为json列表，便于传输
    if data==():
        return []
    else:
        res=[]
        for item in data:
            line={}
            for i in range(7):
                line[ItemMap[i]]=item[i]
            res.append(line)
        return res

@app.route('/submitData',methods=['POST'])
@cross_origin()#解决跨域请求
def submitData():
    '''数据提交'''
    print('-----------提交数据开始-----------')
    db,cursor=connectDB()#连接数据库
    data=request.get_json()#获取数据
    print('接收到数据:',data)
    add(db,cursor,data)#插入数据
    result=retrieve(db,cursor,'*','*')#查询获得数据库中所有数据
    result=transform(result)#格式转换
    closeDB(db,cursor)#关闭数据库连接
    print('-----------提交数据结束-----------')
    return result

@app.route('/refreshData',methods=['GET'])
@cross_origin()#解决跨域请求
def refreshData():
    print('-----------刷新数据开始-----------')
    db,cursor=connectDB()#连接数据库
    result=retrieve(db,cursor,'*','*',request.args.get('method'))#查询获得数据库中所有数据
    result=transform(result)#格式转换
    closeDB(db,cursor)#关闭数据库连接
    print('刷新成功')
    print('-----------刷新数据结束-----------')
    return result

@app.route('/retrieveData',methods=['GET'])
@cross_origin()#解决跨域请求
def retrieveData():
    print('-----------查询数据开始-----------')
    db,cursor=connectDB()#连接数据库
    data={'flag':request.args.get('flag'),'value':request.args.get('value')}#获取数据
    print("查询【{}={}】的数据".format(data['flag'],data['value'])) 
    result=retrieve(db,cursor,data['flag'],data['value'])#查询
    result=transform(result)#格式转换
    closeDB(db,cursor)#关闭数据库连接
    print('-----------查询数据结束-----------')
    return result

@app.route('/updateData',methods=['PUT'])
@cross_origin()#解决跨域请求
def updateData():
    print('-----------更新数据开始-----------')
    db,cursor=connectDB()#连接数据库
    data=request.get_json()#获取数据
    result=retrieve(db,cursor,'id',data['id'])#查询是否存在这个学号
    if result==():
        print('学号不存在')
        result=[]
    else:
        print('学号存在')
        update(db,cursor,data)#更新数据
        result=retrieve(db,cursor,'*','*')
        result=transform(result)
    closeDB(db,cursor)#关闭数据库连接
    print('-----------更新数据结束-----------')
    return result

@app.route('/deleteData',methods=["DELETE"])
@cross_origin()#解决跨域请求
def deleteData():
    print('-----------删除数据开始-----------')
    db,cursor=connectDB()#连接数据库
    data=request.get_json()#获取数据
    result=[]
    if retrieve(db,cursor,'id',data['id'])==():#查询看是否存在此学号
        print('学号不存在')
        result=[]
    else:
        delete(db,cursor,'id',data['id'])#删除数据
        result=retrieve(db,cursor,'*','*')#查询
        result=transform(result)#格式转换
    closeDB(db,cursor)#关闭数据库连接
    print('-----------删除数据结束-----------')
    return result

if __name__=='__main__':
    start()#启动服务器



