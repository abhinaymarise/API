from Question_20.src.extract import sharepoint_conn
from Question_20.src.transform import transform
from Question_20.src.load import load_into_sql
from Question_20.src.Config.config import SHAREPOINT_URL,FOLDER_NAME,USERNAME,PASSWORD

df=sharepoint_conn(SHAREPOINT_URL,FOLDER_NAME,USERNAME,PASSWORD)


star_schema=transform(df)

# for fname, i in star_schema.items():
#     print(fname)
#     print(i.head())

load_into_sql(star_schema)