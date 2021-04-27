import csv

with open('criteo_feed.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        for c in row:
            if c.find(u'\u200b')>-1 :
                print("The invisible char is at",line_count+1,"th line")
                print(c)
                print("At the ",c.find(u'\u200b')+1,"th position of the word above")
                print("------")
        line_count += 1
    print(f'Processed {line_count} lines.')
    

# ---Japanese version--
# import csv

# with open('criteo_feed.csv', encoding="utf8") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         for c in row:
#             if c.find(u'\u200b')>-1 :
#                 print("見えないゴミは第",line_count+1,"行目")
#                 print(c)
#                 print("場所は第",c.find(u'\u200b')+1,"の文字に")
#                 print("------")
#         line_count += 1
#     print(f'Processed {line_count} lines.')
