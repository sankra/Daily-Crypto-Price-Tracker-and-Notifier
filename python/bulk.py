import os
import csv
import sys
import requests
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def fetch_prices(**kwargs):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    kwargs['ti'].xcom_push(key='prices', value=data)
    print(f"Fetched prices: {data}")
def save_prices_to_csv(prices, filename='prices.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Currency', 'Price (USD)'])
        for currency, price in prices.items():
            writer.writerow([currency, price['usd']])
        if os.path.exists(filename):
            print(f"Prices saved to {filename}")
        else:
            print(f"Failed to save prices to {filename}")

def save_prices_to_db(prices, db_url='sqlite:///prices.db'):
    engine = sqlalchemy.create_engine(db_url)
    # connecting to the database
    with engine.connect() as connection:
        for currency, price in prices.items():
            connection.execute(
                f"INSERT INTO prices (currency, price) VALUES ('{currency}', {price['usd']})"
                f"INSERT INTO prices (currency, price) VALUES ('{currency}', {price['rupee']})"
            )
            print(f"Inserted {currency} price into database")
        print("Prices saved to database")