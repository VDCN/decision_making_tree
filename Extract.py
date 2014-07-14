# coding=utf-8
__author__ = 'hexiaoyu'
import MySQLdb

import database

db = database.Connection(host='192.168.30.239',database='flyphp',user='dev_query',password='OWl32ud0zW8uGLENcNu_')

def GetCustomerCount():
    sql= """select TABLE_ROWS from information_schema.TABLES
            where information_schema.TABLES.TABLE_SCHEMA = 'flyphp'
            and information_schema.TABLES.TABLE_NAME = 'fly_customer'"""
    result = db.query(sql)
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

def AddAdressToResult(result,Address):
    count = 0
    for row in Address: #2.将address放进result
        location = LocationInResult(row[0], result)  #print "row[0]",row[0]
        if(location):
            #print row[0],'and', result[location][0]  #check consistency
            result[location][1] = 2
            count =count+1
        else:
            result.append([row[0], 2])
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
AddAdressToResult(result,Address)  #2.将Adress放进result（女)
print "Total result——len", len(result)


for row in result:     #为什么要把qq的去掉
    sql= """
    SELECT email
    FROM fly_customer
    WHERE customer_id=%s
    """ % row[0]
    check_sf = db.query(sql)
    #print type(check_sf[0])
    #print type(check_sf)
    print check_sf
    if 'qq' in check_sf[0][0]:
        print 'removal'
        result.remove(row)

print "Total result without sf——len", len(result)




