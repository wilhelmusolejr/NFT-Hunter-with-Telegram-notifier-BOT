import csv
from generate_credentials import generate_credentials

credentials = generate_credentials()

filename = "data.csv"

def add_credentials(data, balance):
    # Data to be appended
    new_data = [data['username'], data['password'], balance]
    # File to store data

    # Append to CSV
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_data)