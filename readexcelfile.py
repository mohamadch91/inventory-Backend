import pandas

import json

excel_data_df = pandas.read_excel('tfac.xlsx', sheet_name='Facilities')
dic_arr=[]
counter=0
for i in range(len(excel_data_df)):
    z=int(excel_data_df['Isdel'][i])
    if(z==0):
        counter+=1
        dic={
          "country": 1,
          "parent":excel_data_df['parent'][i],
          "name": excel_data_df['name'][i],
          "code": excel_data_df['code'][i],
            "level": int(excel_data_df['level'][i]),
            "populationnumber": int(excel_data_df['populationNumber'][i]),
            "childrennumber": int(excel_data_df['childrenNumber'][i]),
            "gpsCordinate": "LatLng("+str(excel_data_df['gps'][i])+")",
            "city": excel_data_df['city'][i],
            "address": excel_data_df['address'][i],
            "havegen": excel_data_df['HaveGenerator'][i],
            "loverlevelfac": excel_data_df['lowerLevel'][i],


        }
        dic_arr.append(dic)

# json_object = json.dumps(dic_arr,indent=1)
# print(json_object)
print(counter)
with open("tfac.json", "w") as outfile:
    outfile.write(str(dic_arr))