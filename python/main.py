import os
import csv
import sys
import requests
import sqlalchemy

for i in range(3):
    print(f"sys.path[{i}]: {sys.path[i]}")
    print(f"sys.modules[{i}]: {sys.modules[i]}")
    print(f"sys.modules[{i}]: {sys.modules[i]}")

    print(f"sys.modules[{i}]: {sys.modules[i]}")
    print(f"sys.modules[{i}]: {sys.modules[i]}")

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

    for i in range(3):
        print(f"sys.path[{i}]: {sys.path[i]}")
        print(f"sys.modules[{i}]: {sys.modules[i]}")
        print(f"sys.modules[{i}]: {sys.modules[i]}")
        print(f"sys.modules[{i}]: {sys.modules[i]}")
        print(f"sys.modules[{i}]: {sys.modules[i]}")

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
            writer.writerow([currency, price['usd']])
        if os.path.exists(filename):
            print(f"Prices saved to {filename}")
        else:
            print(f"Failed to save prices to {filename}")
def save_prices_to_db(prices, db_url='sqlite:///prices.db'):
    engine = sqlalchemy.create_engine(db_url)
    with engine.connect() as connection:
        for currency, price in prices.items():
            connection.execute(
                f"INSERT INTO prices (currency, price) VALUES ('{currency}', {price['usd']})"
            )
            print(f"Inserted {currency} price into database")
        print("Prices saved to database")
    if os.path.exists(db_url):
        print(f"Prices saved to {db_url}")
    else:
        print(f"Failed to save prices to {db_url}")