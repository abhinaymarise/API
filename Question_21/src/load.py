from Question_21.src.extract import parquet
from Question_21.src.util import connect

data=parquet()
engine=connect()

def load_into_sql():
    for table_name,df in data.items():
        print(f"Sending {table_name} to database...")
        df.toPandas().to_sql(name=table_name,con=engine,if_exists='replace',index=False)
        print(f"{table_name} sent!")
