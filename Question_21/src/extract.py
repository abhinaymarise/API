from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
from Question_21.src.Config.config import SHAREPOINT_URL,LIBRARY,USERNAME,PASSWORD
from pyspark.sql import SparkSession
import pyarrow.parquet as pq
import io


def parquet():
    spark=SparkSession.builder.appName("Parquet").getOrCreate()
    auth=ClientContext(SHAREPOINT_URL).with_credentials(UserCredential(USERNAME,PASSWORD))

    folder=auth.web.get_folder_by_server_relative_url(LIBRARY)
    files=folder.files
    auth.load(files)
    auth.execute_query()
    
    dataframes={}

    for file in files:
        if file.properties["Name"].endswith(".parquet"):
                print("Processing:",file.properties["Name"])

                file_url=file.properties["ServerRelativeUrl"]
                file_content=File.open_binary(auth,file_url)

                buffer=io.BytesIO(file_content.content)

                table=pq.read_table(buffer)
                pdf=table.to_pandas()
                df=spark.createDataFrame(pdf)

                table_name=file.properties["Name"].replace(".parquet","").lower()
                dataframes[table_name]=df

    return dataframes
    
