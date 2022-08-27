import pyodbc
import pandas as pd
print(pyodbc.drivers())
conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.10.so.1.1}; \
                        SERVER=localhost; \
                        DATABASE=inventory_aze; \
                        UID={sa};\
                        PORT= "1433";\
                        Trusted_Connection=no;\
                        PWD={mohamaD@1380};')
sql_query = pd.read_sql_query(''' 
                              select * from test_database.dbo.product
                              '''
                              ,conn) # here, the 'conn' is the variable that contains your database connection information from step 2

df = pd.DataFrame(sql_query)
df.to_excel (r'exported_data.csv', index = False) # place 'r' before the path name