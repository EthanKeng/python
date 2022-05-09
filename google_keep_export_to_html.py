import os, json
import pandas as pd

path_to_json = 'Keep/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
# print(json_files)  # for me this prints ['foo.json']


# here I define my pandas Dataframe with the columns I want to get from the json
jsons_data = pd.DataFrame(columns=['title', 'textContent', 'labels'])

# we need both the json and an index number so use enumerate()
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js),encoding="utf8") as json_file:
        json_text = json.load(json_file)

        # here you need to know the layout of your json and each json has to have
        # the same structure (obviously not the structure I have here)
        title = json_text['title']
        textContent = json_text['textContent']
        try:
            labels = json_text['labels'][0]['name']
        except:
            labels=""
        # here I push a list of data into a pandas DataFrame at row given by 'index'
        jsons_data.loc[index] = [title, textContent, labels]

# now that we have the pertinent json data in our DataFrame let's look at it
# print(jsons_data)

c=0
# output the file
file = open("output.html","w",encoding="utf8")
for ind in jsons_data.index:
    if (jsons_data['labels'][ind]=="#Database"):
        print(jsons_data['title'][ind], jsons_data['labels'][ind],jsons_data['textContent'][ind])
        t1="<h2>{}</h2>".format(jsons_data['title'][ind])
        t2="<p>{}</p>".format(jsons_data['textContent'][ind])
        t2=t2.replace('\n', '<br />')


        file.writelines(t1)
        file.writelines("\n")
        file.writelines(t2)
        file.writelines("\n")
        c+=1

file.close()
print(c)
