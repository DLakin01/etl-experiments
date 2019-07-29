from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "Daniel Lakin",
    "depends_on_past": False,
    "start_date": datetime(2019, 7, 24),
    "email": ["dlakin01@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG("DataExportDag", default_args=default_args)

# Pull data from DB
generate_json = BashOperator(
    task_id="generate_json",
    bash_command="python /Users/macbook/Desktop/ETL-Experiments/airflow_home/dags/src/transform_to_json.py",
    dag=dag
)

generate_xml = BashOperator(
    task_id="generate_xml",
    bash_command="python /Users/macbook/Desktop/ETL-Experiments/airflow_home/dags/src/transform_to_xml.py",
    dag=dag
)

generate_json >> generate_xml