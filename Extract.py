# coding=utf-8
__author__ = 'hexiaoyu'
import MySQLdb

import database

db = database.Connection(host='192.168.30.239',database='flyphp',user='dev_query',password='OWl32ud0zW8uGLENcNu_')

_db = {
    'flyphp': database.Connection(host='192.168.30.239',database='flyphp',user='dev_query',password='OWl32ud0zW8uGLENcNu_'),
    'local ': database.Connection(host='localhost',database='flyphp',user='root',password='')
}

_db['flyphp']
_db['local']

def GetCustomerCount():
    sql= """select TABLE_ROWS from information_schema.TABLES
            where information_schema.TABLES.TABLE_SCHEMA = 'flyphp'
            and information_schema.TABLES.TABLE_NAME = 'fly_customer'"""
    result = _db['flyphp'].query(sql)
    return result[0][0]

def GetCusSexFromDetail():
    sql= """SELECT customer_id,sex FROM fly_customer_detail where sex <> 0"""
    result = db.query(sql)
    return result

def GetCusSexFromAddress():  # get female address
    sql= """
    SELECT DISTINCT customer_id
    FROM fly_customer_address
    WHERE realname LIKE '%%小姐%%' OR realname LIKE '%%女士%%'
    """
    result = db.query(sql)
    return result

def GetCusSexFromAddress2():  # get male address
    sql= """
    SELECT DISTINCT customer_id
    FROM fly_customer_address
    WHERE realname LIKE '%%先生%%'"""
    result = db.query(sql)
    return result

def LocationInResult(x,list):
    for i in range(len(list)):
        #print "list[i][0]",list[i][0]
        if x == list[i][0]:
            return i
    return 0
        #else:
            #return 0

def AddAdressToResult(result,Address,Address2):
    count = 0
    for row in Address: #1.将address放进result(female)
        location = LocationInResult(row[0], result)  #print "row[0]",row[0]
        if(location):
            #print row[0],'and', result[location][0]  #check consistency
            result[location][1] = 2
            count =count+1
        else:
            result.append([row[0], 2])
    for row in Address2: #2.将address2放进result(male)
        location = LocationInResult(row[0], result)  #print "row[0]",row[0]
        if(location):
            #print row[0],'and', result[location][0]  #check consistency
            result[location][1] = 1
            count =count+1
        else:
            result.append([row[0], 1])
    print 'Overlap: ',count


CusCount = GetCustomerCount()
print "customer count is %s " % CusCount

Detail = GetCusSexFromDetail()
print 'len-Detail:',len(Detail)
Address = GetCusSexFromAddress()

Address2 = GetCusSexFromAddress2()
print 'len-Address:',len(Address)
print 'len-Address2:',len(Address2)
result = []
for row in Detail:  #最终结果在result里，1.将detail放进result，并且转成列表的格式
    result.append(list(row))
#print "result",result
print "Detail result——len", len(result)
#print result
AddAdressToResult(result,Address,Address2)  # 2.将Adress,Adress2 放进result
print "Final result——len", len(result)



for row in result:     #为什么要把qq的去掉
    sql= """
    SELECT email
    FROM fly_customer
    WHERE customer_id=%s
    """ % row[0]
    check_sf = db.query(sql)
    # print check_sf
    # print check_sf[0] #IndexError: tuple index out of range
    # print check_sf[0][0]
    if check_sf and 'sf-express' in check_sf[0][0]:
        print 'removal',check_sf
        result.remove(row)

print "Total result without sf——len", len(result)

customer count is 384767
len-Detail: 5407
len-Address: 3636
len-Address2: 2224
Detail result——len 5407
Overlap:  511
Final result——len 10756
Total result without sf——len 10317

# for row in result:     #为什么要把qq的去掉
#     sql= """
#     SELECT email,customer_id,realname
#     FROM fly_customer
#     WHERE customer_id=%s
#     """ % row[0]
#     check = db.query(sql)
#     print check




