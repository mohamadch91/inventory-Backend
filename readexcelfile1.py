import pandas

import json

excel_data_df = pandas.read_excel('titem.xlsx', sheet_name='Items')
dic_arr=[]
counter=0
for i in range(len(excel_data_df)):
    z=int(excel_data_df['isDel'][i])
    if(z==0):
        cap=float(str(excel_data_df['capacity'][i]).replace(',', '.'))
        net_cap=float(str(excel_data_df['netVaccCapacity'][i]).replace(',', '.'))
        counter+=1
        dic={
          "facility": excel_data_df['facilitycode'][i],
            "item_class": excel_data_df['itemclass'][i],
            "item_type": excel_data_df['itemtype'][i],
            "StorageCondition": excel_data_df['temprange'][i],
            "FreezerNetCapacity": cap,
            "NetVaccineStorageCapacity": net_cap,
            "code": excel_data_df['code'][i],


        }
        dic_arr.append(dic)

# json_object = json.dumps(dic_arr,indent=1)
# print(json_object)
print(counter)
with open("titem.json", "w") as outfile:
    outfile.write(str(dic_arr))