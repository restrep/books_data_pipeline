#dag - directed acyclic graph
#tasks : 1) fetch amazon data (extract) 2) clean data (transform) 3) create and store data in table on postgres (load)
#operators : Python Operator and PostgresOperator
#hooks - allows connection to postgres
#dependencies

from airflow import DAG
from datetime import datetime, timedelta


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024,6,20),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


dag = DAG(
    dag_id= "fetch_and_store_books",
    default_args=default_args,
    description= "A simple DAG to fecht book data and store it in postgres",
    schedule="@daily",
)



