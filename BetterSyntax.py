#python_version == '3.6'
import csv
def get_average_grades(filename='grades.csv'):
    rows = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            rows.append(row)
    return [ sum(list(map(int,list(filter(lambda x: (x!=-1), x)))))/len(list(filter(lambda x: (x!=-1), x))) for x in zip(*rows) ]
    
# print(get_average_grades())