import datetime
import os
import sys
import csv
import requests
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def fetch_prices(**kwargs):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    kwargs['ti'].xcom_push(key='prices', value=data)
    print(f"Fetched prices: {data}")

if __name__ == "__main__":
    print("This is the main module.")
    print("Current working directory:", os.getcwd())
    print("Python version:", sys.version)
    print("Requests version:", requests.__version__)
    for i in range(3):
        print(f"sys.path[{i}]: {sys.path[i]}")
        print(f"sys.modules[{i}]: {sys.modules[i]}")
        print(f"sys.modules[{i}]: {sys.modules[i]}")
    print(f"sys.modules[{i}]: {sys.modules[i]}")