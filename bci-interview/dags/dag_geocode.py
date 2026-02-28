from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from src.utils.reader import read_json
from src.utils.writer import write_json
from src.transformers.address_transformer import transform

def run_pipeline():
    json_file_input = "data/int_test_input/input_sample.json"
    json_file_output = "data/int_test_output/output_sample.json"

    data = read_json(json_file_input)
    data_transformed = transform(data)

    write_json(data_transformed, json_file_output)

with DAG(
    dag_id="geocode_pipeline",
    description="ETL pipeline for geocode hubexo",
    start_date=datetime(2026, 2, 28),
    schedule="@daily",
    catchup=False,
    tags=["etl", "geocode"],
    default_args={"retries": 1},
) as dag:
    
    run_etl = PythonOperator(
        task_id="run_geocode_pipeline",
        python_callable=run_pipeline,
    )

    run_etl