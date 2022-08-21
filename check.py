import json
dic_arr=[]
for i in range(27):
  
    dic= {
        "model": "related.Itemvalidation",
        "pk": i+1,
        "fields": {
      "fieldid": 222,
      "digits": 222,
      "min": 2,
      "max": 22,
      "float": True,
      "floating": 2
    }
    },
   
    dic_arr.append(dic)

json_object = json.dumps(dic_arr,indent=1)
# print(json_object)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)