import csv
from properties import edits_test_path

def search_postId(postId_count,postId_list):
    print(postId_count)
    print(postId_list)

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
    search_postId(postId_count,postId_list)

def main():
    number_split()

if __name__ == '__main__':
    main()