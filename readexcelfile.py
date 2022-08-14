import pandas

import json

excel_data_df = pandas.read_excel('itemtype.xlsx', sheet_name='Sheet1')
dic_arr=[]
print(excel_data_df["name"])
for i in range(68):
    if(i<11):
        dic= {
        "model": "related.relatedFacility",
        "pk": i+1,
        "fields": {
        "name": excel_data_df["name"][i],
        "type": "text",
        "topic": "top",
        "disabled":True
        }
    },
    else:
      dic= {
        "model": "related.relatedFacility",
        "pk": i+1,
        "fields": {
        "name": excel_data_df["name"][i],
        "type": "text",
        "topic": "top"
       
        }
    },  
    dic_arr.append(dic)

json_object = json.dumps(dic_arr,indent=3)
# print(json_object)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)