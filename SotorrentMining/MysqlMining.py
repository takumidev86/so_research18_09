# coding: UTF-8
import re
import fileinput
import pprint
import MySQLdb
import sys
from properties import user_p,passwd_p,host_p,db_p

# クエリ実行
def query_execution(conn,cursor):
    query_valiable = {
        "save_file":'/home/takumi-k/e/csv/test5.csv',
        "s":',',
        "t":'\"'
        }
    csv_output_query = "SELECT * FROM PostReferenceGH INTO OUTFILE %s FIELDS TERMINATED BY %s OPTIONALLY ENCLOSED BY %s"
    cursor.execute(csv_output_query,(query_valiable["save_file"],query_valiable["s"],query_valiable["t"]))

def detabase_connect():
    conn = MySQLdb.connect(
        user= user_p,
        passwd= passwd_p,
        host= host_p,
        db= db_p
    )
    cursor = conn.cursor()
    query_execution(conn,cursor)
    conn.commit()
    # 接続を閉じる
    conn.close

def main():
    detabase_connect()

if __name__ == '__main__':
    main()