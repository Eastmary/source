import pymysql

# 전역변수 선언부
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row=None

# 메인 코드
conn = pymysql.connect( )
cur = conn.cursor()

cur.execute("SELECT * FROM userTable")

print("사용자ID    사용자이름     e메일    출생연도")
print("----------------------------------------------------")

while (True) :
    row = cur.fetchone()
    
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%10s   %10s   %15s   %5d" % ( ))

conn.close()