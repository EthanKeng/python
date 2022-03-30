## Learn CSV module

Check [Here](https://github.com/EthanKeng/python/blob/main/Ex_Files_Scripting_for_Testers/Exercise%20Files/02_01/end/readInData.py)

---
## Google Chart API

Check [Here](https://github.com/EthanKeng/python/blob/main/Ex_Files_Scripting_for_Testers/Exercise%20Files/02_02/end/readInData_solution.py)

Use `Template` package:
`from string import Template` 

Then, use google chart api to draw a chart in HTML.

---

## Create Google API service
 - Go to console.developers.google.com to create a project
 - Enable google drive and google sheet API
 - Go back to dashboard then create Credentials>Service account key>New service account
 - Download the JSON key file and open it
 - Then copy email value share with it in google sheet

---
## Interact with Google sheet -- read and write
first, insall `gspread` and `google-api-python-client`: 
```
python -m pip install gspread
python -m pip install google-api-python-client
```

Check [Here](https://github.com/EthanKeng/python/blob/main/Ex_Files_Scripting_for_Testers/Exercise%20Files/02_08/end/Challenge3_Test%20Report%20Page.py)
