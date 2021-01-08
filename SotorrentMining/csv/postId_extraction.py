import csv
from properties import edits_test_path,user_p,passwd_p,db_p
import MySQLdb
import pprint
import fileinput


# クエリ実行
def search_postId_query_execution(conn,cursor,postId_count,postId_list):
    query_valiable = {
        "edits":edits_test_path,
        # "s":',',
        # "t":'\"'
        }
    search_postId_query = "SELECT SOUrl,GHUrl FROM PostReferenceGH WHERE ID = %s"
    for postId_list_item in postId_list:
        cursor.execure(search_postId_query,postId_list_item)
    # csv_output_query = "SELECT * FROM PostReferenceGH INTO OUTFILE %s FIELDS TERMINATED BY %s OPTIONALLY ENCLOSED BY %s"
    # cursor.execute(csv_output_query,(query_valiable["save_file"],query_valiable["s"],query_valiable["t"]))

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
                    postId_list.append(postId)
    database_connect(postId_count,postId_list)

def main():
    number_split()

if __name__ == '__main__':
    main()