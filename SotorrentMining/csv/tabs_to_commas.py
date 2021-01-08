import csv
import pprint
from properties  import edit_diferrences_path ,edit_path
import pandas 
def main():
    # print(properties.edit_diferrences)
    # # with open('data/src/sample.csv') as f:
    # #     print(f.read())
    edit_diferrences = open(edit_diferrences_path)
    print(edit_diferrences[0])

if __name__ == '__main__':
    main()