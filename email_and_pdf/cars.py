#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails
import os

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  count_sales = {}
  year_sales={}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    model=item["car"]["car_model"]
    if model not in count_sales:
      count_sales[model] = item["total_sales"]
    else:
      count_sales[model] += item["total_sales"]

    # TODO: also handle most popular car_year
    year=item["car"]["car_year"]
    if year not in year_sales:
      year_sales[year] = item["total_sales"]
    else:
      year_sales[year] += item["total_sales"]



  print(year_sales)

  # Outside of the for-loop
  max_sale_model = max(count_sales, key=count_sales.get)
  max_sale_year = max(year_sales,key=year_sales.get)
  summary = [
    "The {} generated the most revenue: ${}, and The {} had the most sales: {}. The most popular year was {} with {} sales.".format(
      format_car(max_revenue["car"]), max_revenue["revenue"],max_sale_model,count_sales[max_sale_model],max_sale_year,year_sales[max_sale_year]),
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  table_data = cars_dict_to_table(data)
  print(summary)
  # TODO: turn this into a PDF report
  reports.generate("/tmp/cars.pdf", "Sales summary for last month",summary[0], table_data)
  
  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = summary[0]

  message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
  emails.send(message)  

if __name__ == "__main__":
  main(sys.argv)
