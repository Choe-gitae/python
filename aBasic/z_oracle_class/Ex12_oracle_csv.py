# Ex12_oracle_csv.py

import cx_Oracle as oci
import csv


def create_db_table():
    conn = oci.connect('scott/tiger@localhost:1521/xe')
    sql = '''
    CREATE TABLE supply
    (
        ID              NUMBER          PRIMARY KEY,
        SUPPLIER_NAME   VARCHAR2(50),
        INVOICE_NUMBER  VARCHAR2(50),
        PART_NUMBER     VARCHAR2(30),
        COST            NUMBER,
        PURCHASE_DATE   DATE
    )
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    sql2 = 'CREATE SEQUENCE SEQ_SUPPLY_ID'
    cursor.execute(sql2)

    cursor.close()
    conn.close()


def save_db_table(data):
    conn = oci.connect('scott/tiger@localhost:1521/xe')
    sql = '''
    INSERT INTO SUPPLY VALUES(SEQ_SUPPLY_ID.NEXTVAL, :0, :1, :2, :3, :4)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, data)
    cursor.close()
    conn.commit()   # 잊지말자
    conn.close()


def view_db_table(table_name):
    # 넘겨받은 테이블명의 데이터를 화면에 출력
    conn = oci.connect('scott/tiger@localhost:1521/xe')
    sql = 'SELECT * FROM {}'.format(table_name)
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    for row in datas:
        print(row)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # (1) 테이블 생성
    # create_db_table() # 생성 완료

    # (2-0) 입력 확인
    # imsi = ['kosmo', '9999', '8888', 1000, '2022-12-24']
    # save_db_table(imsi)   # 입력 완료

    # (2) CSV 파일을 읽어서 -> DB 에 입력
    # with open('supply.csv', 'r') as file:
    #     datas = csv.reader(file)
    #     header = next(datas, None)
    #     print(header)
    #     for row in datas:
    #         save_db_table(row)

    # (3) 테이블 내용 출력
    view_db_table('SUPPLY')
