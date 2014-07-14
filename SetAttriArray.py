# coding=utf-8
__author__ = 'hexiaoyu'
import MySQLdb
import database
db = database.Connection(host='192.168.30.239',database='flyphp',user='dev_query',password='OWl32ud0zW8uGLENcNu_')
_db = {
    'flyphp': database.Connection(host='192.168.30.239',database='flyphp',user='dev_query',password='OWl32ud0zW8uGLENcNu_'),
    'local': database.Connection(host='localhost',database='decision_making_tree',user='root',password='')
}

d = _db['local'].query("SELECT VERSION()")  #测试连接上了。。
print d

def FindAttri(sql,b):
    a = _db['flyphp'].query(sql)
    if a:
        for row in a:
            b.append(list(row)[0])

sql= """SELECT customer_id,sex FROM customer_sex""" #从本地把数据读取出来
temp = _db['local'].query(sql)
result = []
for row in temp:  #最终结果在result里，1.将detail放进result，并且转成列表的格式
    result.append(list(row))

#####               还需要专门的写一个文件来确定attri_table
attri_table = []
attri_table = []

####
attri = []
customer_product_table = []
i=0
for row in result:
    all_product = [] #存储一个客户购买过的所有商品#其实可以删除
    all_category = [] #存储一个客户购买过的所有商品种类
    if i==0:
        order=[]  #客户的订单列表
        sql= """SELECT order_id FROM fly_order WHERE customer_id=% """ % row[0]
        FindAttri(sql,order)
        print "order",order,"/"

        for order_id in order:
            product = [] #当前订单下的商品列表
            sql= """SELECT product_id  FROM fly_order_product WHERE order_id=%d """ % order_id
            FindAttri(sql,product)
            print "order_id,product:",order_id,product
            #把单个订单下的商品列表加入到总商品列表中
            all_product.extend(product)
            # print "all_product",all_product

            for product_id in product:
                category = []
                sql="""SELECT category_id FROM fly_product_to_category WHERE product_id=%d """ % product_id
                FindAttri(sql,category)
                print "product_id,category:",product_id,category
                #把单个订单下的商品列表加入到总商品列表中
                all_category.extend(category)
        print "all_category",all_category
        ###############已经把一个客户购买过的所有商品种类都找出来了，接下来只剩下判断这些category是不是在属性表中
        i=i+1


