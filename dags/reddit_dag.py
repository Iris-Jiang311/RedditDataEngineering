import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline





default_args = {
    'owner': 'Iris',
    'start_date': datetime(2025, 2, 11),
}

file_postfix = datetime.now().strftime('%Y%m%d%H%M%S')

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    start_date=datetime(2025, 2, 11),
    tags=['reddit','etl','pipeline'],
)






# extraction from reddit
extract = PythonOperator(
    task_id='extract',
    python_callable= reddit_pipeline,
    op_kwargs ={
        'file_name': f'reddit_data_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
  
)

# upload to S3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable= upload_s3_pipeline,
    dag=dag)

extract >> upload_s3