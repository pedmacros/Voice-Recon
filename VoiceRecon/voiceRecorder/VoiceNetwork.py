from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import csv

X = []
Y = []


def trainNetwork():
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        mylist = list(reader)
    print(mylist[0][0])
