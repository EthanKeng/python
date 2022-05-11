#! /usr/bin/env python3
import os
import requests
import json
path_to_txt = '/data/feedback/'
txt_files = [txt for txt in os.listdir(path_to_txt)]

# print(txt_files)
titles= ["title", "name", "date", "feedback" ]
for t in txt_files:
  d={}
  with open(os.path.join(path_to_txt, t),encoding="utf-8") as file:
    for i, f in enumerate(file):
      # use rstrip() to remove \n in the end of text
      d[titles[i]]=f.rstrip()
    # post the dictionary-json to /feedback endpoint
    res = requests.post('http://35.188.72.212/feedback/', data=d)
    print(d)
    res.raise_for_status()
