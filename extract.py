import json

#read json file
with open('sample.json') as json_file:
    #pritn fields
    data = json.load(json_file)
    ans=[]
    for x in data:
        if(x['fields']['type']=='number'):
            str=x['fields']['state']+'=models.IntegerField(null=True)'
        if(x['fields']['type']=='text'):
            str=x['fields']['state']+'=models.CharField(max_length=50, null=True)'
        if(x['fields']['type']=='bool'):
            str=x['fields']['state']+'=models.BooleanField(null=True)'
        if(x['fields']['type']=='select'):
            str=x['fields']['state']+'=models.CharField(max_length=50, null=True)'
        ans.append(str)

#write to text file ans
with open('ans.txt', 'w') as f:
    for item in ans:
        f.write("%s\n" % item)