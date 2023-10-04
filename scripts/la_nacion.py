#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

import json
import requests
from bs4 import BeautifulSoup
import datetime


base_url = "https://www.lanacion.com.ar/dolar-hoy/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


def get_current_month_and_year():
    """Returns the current month and year in the format year-month."""
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    return f"{year}-{month:02d}"


def get_current_date():
    """Returns the current date in the format dd/mm/yy."""
    today = datetime.date.today()
    return f"{today.day}/{today.month}/{today.year % 100}"


def get_current_time():
    """Returns the current time in the format HH:MM:SS."""
    now = datetime.datetime.now()
    return f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"


def pprint_data(d):
    """Prints nicely a dict."""
    data = json.dumps(d, indent=4, ensure_ascii=False)
    print(data)


def process_box(b):
    box_data = {}
    box_base = b
    dolar_name = box_base.find("h2", {"class": "dolar-title"}).text
    dolar_values_name = box_base.findAll("span")
    dolar_values_val = box_base.findAll("strong")
    box_data["name"] = dolar_name
    box_data["coti"] = {}
    coti_base = box_base.findAll("p", {"class": "com-text"})
    for i in coti_base:
        cv_name = i.findAll("span")
        cv_val = i.findAll("strong")
        for k, v in enumerate(cv_name):
            box_data["coti"][v.text] = cv_val[k].text

    return box_data


def process_data(d):
    data = {}
    #  DEBUG INFO
    data["debug_info"] = {}
    data["debug_info"]["running_date"] = get_current_date()
    data["debug_info"]["running_time"] = get_current_time()
    data["data"] = {}
    data["data"]["coti"] = []

    base_data = d.find("div", {"class": "dolar"})
    data_box = base_data.findAll("li")

    for i in data_box:
        data["data"]["coti"].append(process_box(i))

    #  Append data to file.
    append_data_to_json_file(data, get_current_month_and_year())


def get_data():
    """Gets page content."""
    response = requests.get(base_url, headers=headers)
    return response.content


def append_data_to_json_file(new_data, filename):
    """Appends data to a JSON file, creating the file if it does not exist.

    Args:
    new_data: The data to append to the file.
    filename: The path to the JSON file.
    """

    try:
        # Open the file in reading and writing mode.
        with open(f"data/la_nacion/{filename}.json", "r+") as f:
            # Load the existing data from the file.
            existing_data = json.load(f)

            # Append the new data to the existing data.
            existing_data.append(new_data)

            # Seek to the beginning of the file.
            f.seek(0)

            # Write the updated data to the file.
            json.dump(existing_data, f)
    except FileNotFoundError:
        # Create the file if it does not exist.
        with open(f"data/la_nacion/{filename}.json", "w") as f:
            json.dump([new_data], f)


def la_nacion_main():
    soup = BeautifulSoup(get_data(), "html.parser")
    process_data(soup)
