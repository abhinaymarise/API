from Question_21.src.Config.config import ssms_db_config
import pyodbc

def ssms_connection():
    db=ssms_db_config
    conn=(
        f"Driver={db['Driver']};"
        f"Server={db['Server']};"
        f"UID={db['Username']};"
        f"PWD={db['Password']};"
        f"Database={db['database']}"
    )

    return pyodbc.connect(conn,autocommit=True)


from Question_21.src.Config.config import sql_url
from sqlalchemy import create_engine

def connect():

    engine=create_engine(sql_url)
    return engine
