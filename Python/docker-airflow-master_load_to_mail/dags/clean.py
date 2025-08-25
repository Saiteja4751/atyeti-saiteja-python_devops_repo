import pandas as pd
import datetime,logging
def pre_process():
    logging.info("--> Starting pre-processing of data.")
    print("Before adding date column")
    df = pd.read_csv("~/ip_files/summer.csv")
    df['process_date']=datetime.date.today()

    df=df.fillna("")
    df.to_csv("~/op_files/summer2.csv")
    print('files is cleaned and date is added in file')
    logging.info(" --> Pre-processing complete.")


# pre_process()