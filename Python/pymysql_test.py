from pymysql import connect

conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

conn = connect(host='127.0.0.1', user='root', password='dbgudwn1!', db='soloDB', charset='utf8')
cur = conn.cursor()
end_query = True
# cur.execute('create table userTable (id char(4), username varchar(10), email char(20), birthday int)')
while(end_query):
    data1 = input("사용자 ID ==> : ")
    if data1 == "":
        break
    data2 = input("사용자 이름 ==> : ")
    data3 = input("사용자 EMAIL ==> : ")
    data4 = input("사용자 출생연도 ==> : ")
    sql = "insert into userTable values('" + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")"
    cur.execute(sql)
    query_status = input("쿼리 종료 Y/N : ")
    if query_status == 'Y':
        end_query = False


conn.commit()
conn.close()