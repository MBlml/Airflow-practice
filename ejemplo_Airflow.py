from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'hello_airflow',
    default_args=default_args,
    description='Un DAG simple que imprime "Hola, Airflow!"',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='print_hello',
    bash_command='echo "Hola, Airflow!"',
    dag=dag,
)
