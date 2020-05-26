from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'retries': 0,
}

dag = DAG(
    'hello-world',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
)

t1 = BashOperator(
    task_id='say_hey',
    bash_command='echo "Hello World"',
    dag=dag,
)


