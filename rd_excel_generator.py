#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import pymysql

def make_generator():
    data = xlrd.open_workbook("xxxxx.xlsx") #打开excel(绝对路径)
    table = data.sheets()[0]
    nrows = table.nrows #获得行数
    for i in range(1, nrows):#
        rows  = table.row_values(i) #行的数据放在数组里
        a = rows[0].encode('utf-8')
        b = rows[1].encode('utf-8')
        yield a, b

def main():
    pmq= pymysql.connect(host='xxx', db='xxx', user='xxxx', passwd='xx', charset='utf8')
    cursor = pmq.cursor(cursor=pymysql.cursors.DictCursor)
    for a, b in make_generator():
        sql = """
              update db
              set column_1 = '{column_1}'
              where column_2 = '{column_2}'
              """.format(column_1=column_1, column_2=column_2)
        cursor.execute(sql)
    pmq.commit()
    pmq.close()

if __name__ == '__main__':
    main()
