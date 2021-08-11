import pymysql
from tkinter import *
from tkinter import messagebox

#함수 선언부
def insertData() :
    con, cur = None, None
    data1, data2, data3, data4 = "", "", ""
    sql=""

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')
    cur=conn.cursor()

    data1 = edt1.get();     data2 = edt2.get();     data1 = edt1.get();     data1 = edt1.get();