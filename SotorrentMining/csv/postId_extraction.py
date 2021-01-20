import csv
from properties import edits_test_path,user_p,passwd_p,db_p,host_p,SOUrl_GHUrl_path
import MySQLdb
import pprint
import fileinput
import re


def csv_write(cursor):
    
    with open(SOUrl_GHUrl_path, 'a') as f:
        writer = csv.writer(f)
        for (PostId,SOUrl, GHUrl) in cursor:
            writer.writerow([f"{PostId}",f"{SOUrl}",f"{GHUrl}"])

# クエリ実行
def search_postId_query_execution(conn,cursor,postId_count,postId_list):
    query_valiable = {
        "edits":edits_test_path,
        }
    # search_postId_query = "SELECT PostId, SOUrl,GHUrl FROM PostReferenceGH WHERE PostId = %s"
    # for postId_list_item in postId_list:
    #     cursor.execute(search_postId_query,[postId_list_item])
    #     for (PostId,SOUrl, GHUrl) in cursor:
    #         print(f" {PostId} | {SOUrl} | {GHUrl} ")
    #     # csv_write(cursor)
    # print(postId_list)
    c = 0
    search_select_PostId_from_PostVersion = "SELECT PostId From PostVersion WHERE PredPostHistoryId = %s"
    search_postId_query  = "SELECT PostId,SOUrl,GHUrl FROM PostReferenceGH WHERE PostId = %s"
    for postId_list_item in postId_list:
        cursor.execute(search_select_PostId_from_PostVersion,[postId_list_item])
        for (PostId) in cursor:
            # print(f"{PostId}")
            a = f"{PostId}"
            b = re.sub("\\D", "", a)
            # print(b)
        cursor.execute(search_postId_query,[b])
        for (PostId,SOUrl, GHUrl) in cursor:
            print(f" {PostId} | {SOUrl} | {GHUrl} ")
            c = c + 1
        csv_write(cursor)
    # print(postId_list)
    
    print(c)

def database_connect(postId_count,postId_list):
    conn = MySQLdb.connect(
        user= user_p,
        passwd= passwd_p,
        host= host_p,
        db= db_p
    )
    cursor = conn.cursor()
    search_postId_query_execution(conn,cursor,postId_count,postId_list)
    conn.commit()
    conn.close

def number_split():
    postId_count = 0
    postId_list = []
    with open(edits_test_path) as f:
        for row in csv.reader(f):
            tab_split= f"{row}".split('\\t')
            for i in tab_split:
                if i.isnumeric():
                    postId_count = postId_count + 1
                    postId_list.append(int(i))
    print(postId_list)
    database_connect(postId_count,postId_list)

def main():
    number_split()

if __name__ == '__main__':
    main()