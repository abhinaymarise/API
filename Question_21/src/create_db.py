from Question_21.src.util import ssms_connection

def create_db(db_name:str):
    con=ssms_connection()
    cursor=con.cursor()

    try:
        cursor.execute("Select name from sys.databases where name=?",db_name)
        result=cursor.fetchone()

        if result:
            print(f"Database {db_name} already exists")
        else:
            cursor.execute(f"Create database {db_name}")
    
            print(f"Database {db_name} created successfully!!")
    
    except Exception as e:
        print("Not created!",e)


create_db("Parquet")