# Ex11_oracle_test

import cx_Oracle as oci

# 1. 연결객체 얻어오기 ( Connection )
conn = oci.connect('scott/tiger@localhost:1521/xe')
print(conn.version)

# 2. sql 문장
sql = 'SELECT * FROM EMP'

# 3. cursor 객체 얻어오기
cursor = conn.cursor()

# 4. 실행
cursor.execute(sql)
datas = cursor.fetchall()
# print(datas)
for row in datas:
    print(row)

# 5. cursor 객체 닫기
cursor.close()

# 6. 연결객체 닫기
conn.close()
