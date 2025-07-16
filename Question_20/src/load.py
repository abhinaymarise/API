from Question_20.src.util import connection

def load_into_sql(transformed_tables:dict):
    engine=connection()
    for table_name,df in transformed_tables.items():
        try:
            df.to_sql(table_name,con=engine,if_exists='replace',index=False)
            print(f"{table_name} Sent Successfully!")
        except Exception as e:
            print("Data not sent!")
