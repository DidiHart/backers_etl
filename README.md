This is an etl process for pushing the backers data into the
user table in the database

An potential failure might occur due to the 'Is kickstarter' column
I added in the pandas dataframe

It exist in the User table as a column
but I am not sure exactly what the column name is and the value data type

I assume it is boolean

line 10: df['Is kickstarter'] = True
