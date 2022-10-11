from cmath import nan
from xmlrpc.client import Boolean
import pandas
import math
import json

excel_data_df = pandas.read_excel('trans.xlsx', sheet_name='Trans')
dic_arr_ot=[]
dic_arr_fr=[]
dic_arr_ru=[]
dic_arr_sp=[]
dic_arr_en=[]
dic_arr_ar=[]
dic_arr_ch=[]





for i in range(len(excel_data_df)):
    cl=excel_data_df['Clause'][i]
    en=excel_data_df['EN'][i]
    fr=excel_data_df['FR'][i]
    ar=excel_data_df['AR'][i]
    ru=excel_data_df['RU'][i]
    sp=excel_data_df['SP'][i]
    ot=excel_data_df['Other'][i]
    ch=excel_data_df['CH'][i]
    if str(en)=='nan':
        en=cl
    if str(fr)=='nan':
        fr='FR: '+cl
    if str(ar)=='nan':
        ar='AR: '+cl
    if str(ru)=='nan':
        ru='RU: '+cl
    if str(sp)=='nan':
        sp='SP: '+cl
    if str(ot)=='nan':
        ot='OT: '+cl
    if str(ch)=='nan':
        ch='CH: '+cl
    
    if ("'" in cl ):
        cl=cl.replace("'", "#")
    if ("'" in en):
        en=en.replace("'", "#")
    if ("'" in fr):
        fr=fr.replace("'", "#")
    if ("'" in ar):
        ar=ar.replace("'", "#")
    if ("'" in ru):
        ru=ru.replace("'", "#")
    if ("'" in sp):
        sp=sp.replace("'", "#")
    if ("'" in ot):
        ot=ot.replace("'", "#")
    if ("'" in ch):
        ch=ch.replace("'", "#")

   
    data_en=  {
      "model": "languages.languages_words",
      "pk": i*7+1,
      "fields": {
        "id":i*7+1,
        "language":1,
        "word":cl,
        "translate":en

      }
    }
    dic_arr_en.append(data_en)
    data_ar=  {
      "model": "languages.languages_words",
      "pk": i*7+2,
      "fields": {
        "id":i*7+2,
        "language":2,
        "word":cl,
        "translate":ar

      }
    }
    dic_arr_ar.append(data_ar)
    data_fr=  {
      "model": "languages.languages_words",
      "pk": i*7+3,
      "fields": {
        "id":i*7+3,
        "language":3,
        "word":cl,
        "translate":fr

      }
    }
    dic_arr_fr.append(data_fr)
    data_es=  {
      "model": "languages.languages_words",
      "pk": i*7+4,
      "fields": {
        "id":i*7+4,
        "language":4,
        "word":cl,
        "translate":sp

      }
    }
    dic_arr_sp.append(data_es)
    data_fa=  {
      "model": "languages.languages_words",
      "pk": i*7+5,
      "fields": {
        "id":i*7+5,
        "language":5,
        "word":cl,
        "translate":ot

      }
    }
    dic_arr_ot.append(data_fa)
    data_ru=  {
      "model": "languages.languages_words",
      "pk": i*7+6,
      "fields": {
        "id":i*7+6,
        "language":6,
        "word":cl,
        "translate":ru

      }
    }
    dic_arr_ru.append(data_ru)
    data_ch=  {
      "model": "languages.languages_words",
      "pk": i*7+7,
      "fields": {
        "id":i*7+7,
        "language":8,
        "word":cl,
        "translate":ch

      }
    }
    dic_arr_ch.append(data_ch)
final=[]
for a,b,c,d,e,f,g in zip(dic_arr_en,dic_arr_ar,dic_arr_fr,dic_arr_sp,dic_arr_ot,dic_arr_ru,dic_arr_ch):
    
    final.append(a)
    final.append(b)
    final.append(c)
    final.append(d)
    final.append(e)
    final.append(f)
    final.append(g)
with open("fix.json", "w") as outfile:
    outfile.write(str(final))       
