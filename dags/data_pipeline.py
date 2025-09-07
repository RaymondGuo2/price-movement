# Install packages
import sys
sys.path.append("/Users/raymondguo/Desktop/ComputerDSProjects/price-movement")

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from data_sources.yahoo import fetch_yahoo

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "spy_data_pipeline",
    default_args=default_args,
    description="A simple data pipeline to fetch SPY data from Yahoo Finance",
    schedule_interval="0 17 * * *",
    start_date=datetime(2025, 9, 6),
    catchup=False,
    tags=["finance", "yfinance"],
) as dag:
    
    fetch_spy_data = PythonOperator(
        task_id="fetch_spy_data",
        python_callable=fetch_yahoo,
        op_kwargs={"ticker": "SPY", "period": "1y", "interval": "1d"},
    )

    fetch_spy_data 