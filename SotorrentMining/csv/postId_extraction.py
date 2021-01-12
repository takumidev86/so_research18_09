import csv
from properties import edits_test_path,user_p,passwd_p,db_p,host_p,SOUrl_GHUrl_path
import MySQLdb
import pprint
import fileinput


def csv_write(cursor):
    
    with open(SOUrl_GHUrl_path, 'a') as f:
        writer = csv.writer(f)
        for (SOUrl, GHUrl) in cursor:
            writer.writerow([f"{SOUrl}",f"{GHUrl}"])

# クエリ実行
def search_postId_query_execution(conn,cursor,postId_count,postId_list):
    query_valiable = {
        "edits":edits_test_path,
        }
    search_postId_query = "SELECT SOUrl,GHUrl FROM PostReferenceGH WHERE ID = %s"
    for postId_list_item in postId_list:
        cursor.execute(search_postId_query,[postId_list_item])
        for (SOUrl, GHUrl) in cursor:
            print(f"{SOUrl} | {GHUrl}")
        csv_write(cursor)

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
                    postId_list.append(i)
    database_connect(postId_count,postId_list)

def main():
    number_split()

if __name__ == '__main__':
    main()