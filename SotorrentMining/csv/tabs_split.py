import csv
import pprint
from properties import edits_test_path
import pandas 




def number_split():
    number_count = 0
    ans = []
    with open(edits_test_path) as f:
        for row in csv.reader(f):
            tab_split= f"{row}".split('\\t')
            for i in tab_split:
                if i.isnumeric():
                    output = int(i)
                    print(output)
                    number_count = number_count + 1
                    ans.append(output)
        print(ans)
        print(number_count)

def main():
    number_split()
    

if __name__ == '__main__':
    main()