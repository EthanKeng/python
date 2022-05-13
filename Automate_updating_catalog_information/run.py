#! /usr/bin/env python3
import os
import requests
import json
path_to_txt = 'supplier-data/descriptions/'
txt_files = [txt for txt in os.listdir(path_to_txt)]

# print(txt_files)
titles= ["name", "weight", "description","image_name"]


for t in txt_files:
  d={}
  with open(os.path.join(path_to_txt, t),encoding="utf-8") as file:
    for i, f in enumerate(file):
      # use rstrip() to remove \n in the end of text
      if f.rstrip().endswith("lbs"):
        f=int(f.split()[0])
        d[titles[i]]=f
      else:
        d[titles[i]]=f.rstrip()
    d[titles[3]]=t.split(".")[0]+".jpeg"
    # post the dictionary-json to /feedback endpoint
    res = requests.post('http://34.71.93.7/fruits/', data=d)
    print(d)
    res.raise_for_status()
