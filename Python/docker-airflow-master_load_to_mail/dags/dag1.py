import logging
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from clean import pre_process
from filter import filter_function
from final_report import generate_final_status
from airflow.utils.email import send_email


def on_success_callback(context):
    logging.info(f"✅ Task {context['task_instance'].task_id} succeeded in DAG {context['dag'].dag_id}.")

def on_failure_callback(context):
    logging.error(f"❌ Task {context['task_instance'].task_id} failed in DAG {context['dag'].dag_id}.")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 7, 15),
    "on_failure_callback": on_failure_callback,
}

with DAG(
    dag_id='test_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    check_file = BashOperator(
        task_id='check_file',
        bash_command="shasum ~/ip_files/summer.csv",
        retries=2,
        retry_delay=timedelta(seconds=15),
        on_success_callback=on_success_callback,
    )

    pre_process_task = PythonOperator(
        task_id="pre_process",
        python_callable=pre_process,
        on_success_callback=on_success_callback,
    )

    filter_data = PythonOperator(
        task_id="filter_data",
        python_callable=filter_function,
        on_success_callback=on_success_callback,
    )

    generate_status = PythonOperator(
        task_id="generate_status",
        python_callable=generate_final_status,
        on_success_callback=on_success_callback,
        on_failure_callback=on_failure_callback
    )

    def send_final_email(**kwargs):
        # from airflow.utils.email import send_email

        ti = kwargs['ti']
        report_path = ti.xcom_pull(task_ids='generate_status')
        
        if not report_path:
            logging.error("❌ No report path returned from generate_status")
            return

        with open(report_path, 'r') as f:
            body = f.read()

        subject = "✅ DAG Run Success" if "✅" in body else "❌ DAG Run Failed"

        send_email(
            to='althafmd4321@gmail.com',
            subject=subject,
            html_content="<h3>Status: ✅ Success</h3>", 
            files=[report_path],
            cc=['saitejareddybattu1234@gmail.com', 'saridisowmya2002@gmail.com'],
            mime_charset='utf-8'
        )

        logging.info("📧 Final status email sent.")


    email_notify = PythonOperator(
        task_id="email_notify",
        python_callable=send_final_email,
        provide_context=True,
        on_success_callback=on_success_callback,
        on_failure_callback=on_failure_callback,
    )

    # DAG flow
    check_file >> pre_process_task >> filter_data >> generate_status >> email_notify
