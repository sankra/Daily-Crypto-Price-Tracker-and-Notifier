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
