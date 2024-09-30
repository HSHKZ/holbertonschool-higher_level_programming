#!/usr/bin/env python3
'''2. Converting CSV Data to JSON Format'''


import csv
import json


def convert_csv_to_json(csv_file):
    ''' function that takes the CSV filename as\\
         its parameter and writes the JSON data to data.json'''
    try:
        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open("data.json", "w") as file:
            json.dump(data, file)
        return True
    except FileNotFoundError:
        return False
