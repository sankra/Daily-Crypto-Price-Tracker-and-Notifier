import awswrangler as wr
import pandas as pd
import os
import sys

def load_data_to_s3():
    # Define the S3 bucket and file path
    bucket = "your-bucket-name"
    file_path = "path/to/your/file.csv" # Replace with your actual file path
    s3_path = f"s3://{bucket}/{file_path}"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

# def load_data_to_redshift():
#     # Define the Redshift connection parameters
#     redshift_conn = {
#         "db_user": "your-db-user",
#         "db_password": "your-db-password",
#         "db_name": "your-db-name",
#         "db_port": 5439,
#         "db_host": "your-db-host",
#         "db_table": "your-db-table"
#     }

if __name__ == "__main__":
    # Load data to S3
    load_data_to_s3()
    # Load data to Redshift
    load_data_to_redshift()