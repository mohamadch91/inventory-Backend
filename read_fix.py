from cmath import nan
from xmlrpc.client import Boolean
import pandas
import math
import json

excel_data_df = pandas.read_excel('IGA_New_Translaton_file_draft_4_12_09_2022_with_some_FrArRuSp.xlsx', sheet_name='Final')
dic_arr_fa=[]
dic_arr_fr=[]
dic_arr_ru=[]
dic_arr_sp=[]
dic_arr_en=[]
dic_arr_ar=[]



for i in range(len(excel_data_df)):
    
    data_en=  {
      "model": "languages.languages_words",
      "pk": i*6+1,
      "fields": {
        "id":i*6+1,
        "language":1,
        "word":excel_data_df['EN'][i],
        "translate":excel_data_df['EN'][i]

      }
    }
    dic_arr_en.append(data_en)
    data_ar=  {
      "model": "languages.languages_words",
      "pk": i*6+2,
      "fields": {
        "id":i*6+2,
        "language":2,
        "word":excel_data_df['EN'][i],
        "translate":excel_data_df['AR'][i]

      }
    }
    dic_arr_ar.append(data_ar)
    data_fr=  {
      "model": "languages.languages_words",
      "pk": i*6+3,
      "fields": {
        "id":i*6+3,
        "language":3,
        "word":excel_data_df['EN'][i],
        "translate":excel_data_df['FR'][i]

      }
    }
    dic_arr_fr.append(data_fr)
    data_es=  {
      "model": "languages.languages_words",
      "pk": i*6+4,
      "fields": {
        "id":i*6+4,
        "language":4,
        "word":excel_data_df['EN'][i],
        "translate":excel_data_df['SP'][i]

      }
    }
    dic_arr_sp.append(data_es)
    data_fa=  {
      "model": "languages.languages_words",
      "pk": i*6+5,
      "fields": {
        "id":i*6+5,
        "language":5,
        "word":excel_data_df['EN'][i],
        "translate":excel_data_df['PR'][i]

      }
    }
    dic_arr_fa.append(data_fa)
    data_ru=  {
      "model": "languages.languages_words",
      "pk": i*6+6,
      "fields": {
        "id":i*6+6,
        "language":6,
        "word":excel_data_df['EN'][i],
        "translate":excel_data_df['RU'][i]

      }
    }
    dic_arr_ru.append(data_ru)

final=dic_arr_en+dic_arr_fa+dic_arr_ar+dic_arr_fr+dic_arr_ru+dic_arr_sp
with open("fix.json", "w") as outfile:
    outfile.write(str(final))       
