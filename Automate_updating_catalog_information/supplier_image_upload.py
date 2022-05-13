#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

path_to_image = 'supplier-data/images/'
image_files = [img for img in os.listdir(path_to_image) if img.endswith("jpeg") ]

url = "http://localhost/upload/"

for i in image_files:
  with open(os.path.join(path_to_image, i),'rb') as opened:
    r = requests.post(url, files={'file': opened})