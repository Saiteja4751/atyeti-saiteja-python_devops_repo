from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator

from clean import pre_process
from filter import filter_function

default_args={
    "owner":"airflow",
    "start_date": datetime(2025,7,15)
}

with DAG(dag_id='test_dag',default_args=default_args,schedule_interval='@daily') as dag:
    #task are available in the dags
    #task1
    check_file = BashOperator(
        task_id='check_file',
        bash_command="shasum ~/ip_files/summer.csv",
        retries = 2,
        retry_delay=timedelta(seconds=15)

    )

    pre_process=PythonOperator(
    task_id="pre_process",
    python_callable =pre_process

    )


    filter_data=PythonOperator(
    task_id="filter_data",
    python_callable =filter_function

    )


    #sending mail
    email=EmailOperator(
        task_id="send_email",
        #to='saitejareddybattu1234@gmail.com',
        to='althafmd4321@gmail.com',
        subject='Daily report Generated 7 report attached',
        html_content='<h1>Hello,your reports are generated sucessfully, Thanks',
        files=['/usr/local/airflow/op_files/updated_filter_data.csv'],
        cc=['saitejareddybattu1234@gmail.com','saridisowmya2002@gmail.com']
    )


     


    
check_file >> pre_process >> filter_data >> email