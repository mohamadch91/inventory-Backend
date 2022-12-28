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
dic_arr_uk=[]
dic_arr_vi=[]





for i in range(len(excel_data_df)):
    cl=excel_data_df['Clause'][i]
    en=excel_data_df['EN'][i]
    fr=excel_data_df['FR'][i]
    ar=excel_data_df['AR'][i]
    ru=excel_data_df['RU'][i]
    sp=excel_data_df['ES'][i]
    uk=excel_data_df['UK'][i]
    ot=excel_data_df['Other'][i]
    vi=excel_data_df['VI'][i]
    if str(en)=='nan':
        en=cl
    if str(fr)=='nan':
        fr='FR: '+cl
    if str(ar)=='nan':
        ar='AR: '+cl
    if str(ru)=='nan':
        ru='RU: '+cl
    if str(sp)=='nan':
        sp='ES: '+cl
    if str(ot)=='nan':
        ot='OT: '+cl
    if str(uk)=='nan':
        uk='UK: '+cl
    if str(vi)=='nan':
        vi='VI: '+cl
    
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
    if ("'" in uk):
        uk=uk.replace("'", "#")
    if ("'" in vi):
        vi=vi.replace("'", "#")
    

   
    data_en=  {
      "model": "languages.languages_words",
      "pk": i*8+1,
      "fields": {
        "id":i*8+1,
        "language":1,
        "word":cl,
        "translate":en

      }
    }
    dic_arr_en.append(data_en)
    data_ar=  {
      "model": "languages.languages_words",
      "pk": i*8+2,
      "fields": {
        "id":i*8+2,
        "language":2,
        "word":cl,
        "translate":ar

      }
    }
    dic_arr_ar.append(data_ar)
    data_fr=  {
      "model": "languages.languages_words",
      "pk": i*8+3,
      "fields": {
        "id":i*8+3,
        "language":3,
        "word":cl,
        "translate":fr

      }
    }
    dic_arr_fr.append(data_fr)
    data_es=  {
      "model": "languages.languages_words",
      "pk": i*8+4,
      "fields": {
        "id":i*8+4,
        "language":4,
        "word":cl,
        "translate":sp

      }
    }
    dic_arr_sp.append(data_es)
    data_fa=  {
      "model": "languages.languages_words",
      "pk": i*8+5,
      "fields": {
        "id":i*8+5,
        "language":5,
        "word":cl,
        "translate":ot

      }
    }
    dic_arr_ot.append(data_fa)
    data_ru=  {
      "model": "languages.languages_words",
      "pk": i*8+6,
      "fields": {
        "id":i*8+6,
        "language":6,
        "word":cl,
        "translate":ru

      }
    }
    dic_arr_ru.append(data_ru)
    data_uk=  {
      "model": "languages.languages_words",
      "pk": i*8+7,
      "fields": {
        "id":i*8+7,
        "language":7,
        "word":cl,
        "translate":uk

      }
    }
    dic_arr_uk.append(data_uk)
   
    data_vi=  {
      "model": "languages.languages_words",
      "pk": i*8+8,
      "fields": {
        "id":i*8+8,
        "language":8,
        "word":cl,
        "translate":vi
        
      }
    }
    dic_arr_vi.append(data_vi)

final=[]
for a,b,c,d,e,f,g,h in zip(dic_arr_en,dic_arr_ar,dic_arr_fr,dic_arr_sp,dic_arr_ot,dic_arr_ru,dic_arr_vi,dic_arr_uk):
    
    final.append(a)
    final.append(b)
    final.append(c)
    final.append(d)
    final.append(e)
    final.append(f)
    final.append(g)
    final.append(h)
with open("fix.json", "w") as outfile:
    outfile.write(str(final))       
