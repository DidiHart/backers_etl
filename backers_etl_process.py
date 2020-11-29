import pandas as pd
import psycopg2

# selecting columns in excel sheet
cols = [0,1,2,6]
df = pd.read_excel('backer tiers and add-ons.xlsx', usecols=cols)

# make sure Is kickstarter is the same column header as database table column header for Is kickstarter
# and data type aligns with datbase user table values Not sure if it is boolean
df['Is kickstarter'] = True

# database connection
try:
    engine = psycopg2.connect(
    database='database_name',
    user='username',
    password='password',
    host='us-east-1.rds.amazonaws.com',
    port='5432')

    df.to_sql('name_of_user_table', con=engine, if_exists='append', index=False)
except Exception as e:
    print('Database connection failed due to {}'.format(e))


# print(df.head())

# df.to_csv(r'D:\export_dataframe.csv', header=True)
