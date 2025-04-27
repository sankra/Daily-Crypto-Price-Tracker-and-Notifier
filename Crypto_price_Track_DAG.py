import os
import csv
import json
import requests
import sqlalchemy


from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': False,
}

def fetch_prices(**kwargs):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    kwargs['ti'].xcom_push(key='prices', value=data)

def save_to_csv(**kwargs):
    data = kwargs['ti'].xcom_pull(key='prices', task_ids='fetch_prices')
    os.makedirs('/opt/airflow/data/prices', exist_ok=True)
    filepath = f"/opt/airflow/data/prices/crypto_{datetime.now().date()}.csv"
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['coin', 'price_usd'])
        for coin, value in data.items():
            writer.writerow([coin, value['usd']])

def price_alert(**kwargs):
    data = kwargs['ti'].xcom_pull(key='prices', task_ids='fetch_prices')
    threshold = 3000
    if data['ethereum']['usd'] > threshold:
        print(f"Alert: ETH > ${threshold}!")
        return 'notify_high_price'
    return 'skip_notification'

def notify():
    print("Sending Email/Slack: ETH crossed threshold!")

with DAG(
    dag_id='crypto_price_tracker',
    description = "Crypto Price Tracker Dag with multiple tasks",
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['crypto', 'example'],
) as dag:

    start = DummyOperator(task_id='start')

    fetch = PythonOperator(
        task_id='fetch_prices',
        python_callable=fetch_prices,
        provide_context=True
    )


    save = PythonOperator(
        task_id='save_to_csv',
        python_callable=save_to_csv,
        provide_context= False
    )


    check_price = BranchPythonOperator(
        task_id='check_price_alert',
        python_callable=price_alert,
        provide_context=True
    )

    notify_high = PythonOperator(
        task_id='notify_high_price',
        python_callable=notify
    )
    load = PythonOperator(
        task_id='load_to_db',
        python_callable=save_to_csv,
        provide_context=False
    )
    # Dummy operator to skip notification

    skip_notify = DummyOperator(task_id='skip_notification')

    end = DummyOperator(task_id='end')


    #process flow
    start >> fetch >> save >> check_price 
    check_price >> [notify_high, skip_notify] >> end
