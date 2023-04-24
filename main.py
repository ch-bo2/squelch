import pandas as pd
import sqlalchemy as sql
import os

dir = os.getcwd()
dir = dir[dir.rindex('/')+1:]

def read_file(file):
    match os.path.splitext(file)[1]:
        case ['.xlsx']:
            pd.read_excel(file)
        case ['.csv']:
            pd.read_csv(file)
        case ['.parquet']:
            pd.read_parquet(file)

def file_ext():
    file_list = [f for f in os.listdir() if os.path.isfile(f)]
    for file in file_list:
        read_file(file)



if __name__ == '__main__':
    #file_ext()
    print(dir)

