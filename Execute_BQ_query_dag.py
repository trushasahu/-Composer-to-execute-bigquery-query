"""
Example DAG using BigQueryExecuteQueryOperator.
"""

import os

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

#PROJECT_ID = os.environ.get("GCP_PROJECT_ID", 'third-campus-303308')
#DATASET_NAME = os.environ.get("GCP_DATASET_NAME", 'airflow_ds')
#SOURCE_TABLE_NAME = os.environ.get("GCP_SRC_TABLE_NAME", 'source_bq_table')
#TARGET_TABLE_NAME = os.environ.get("GCP_TRG_TABLE_NAME", 'target_bq_table')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2), #datetime(2019, 6, 30),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='exeute_bigquery_query',
	catchup=False,
	default_args=default_args,
    schedule_interval='*/5 * * * *'
)

execute_insert_query = BigQueryExecuteQueryOperator(
        task_id="execute_insert_query", 
		sql=""" insert into `third-campus-303308.airflow_ds.target_bq_table` select * from `third-campus-303308.airflow_ds.source_bq_table` limit 10; """, 
		use_legacy_sql=False, 
		dag=dag,
        )

execute_insert_query
