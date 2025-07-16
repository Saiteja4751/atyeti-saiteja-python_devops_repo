import pandas as pd
import datetime

def pre_process():
    print("Before adding date column")
    df = pd.read_csv("~/ip_files/summer.csv")
    df['process_date']=datetime.date.today()

    df=df.fillna("")
    df.to_csv("~/op_files/summer2.csv")
    print('files is cleaned and date is added in file')


# pre_process()