from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
import pandas as pd
import io

def sharepoint_conn(sp_url,folder_name,username,password):
    auth=ClientContext(sp_url).with_credentials(UserCredential(username,password))
    folder=auth.web.get_folder_by_server_relative_url(folder_name)

    files=folder.files
    auth.load(files)
    auth.execute_query()

    json_dfs={}

    #print(f"Loaded file names are :\n")

    for file in files:
        if file.properties["Name"].endswith(".json"):
            file_name=file.properties["Name"]
            file_url=file.properties["ServerRelativeUrl"]
            file_content=file.open_binary(auth,file_url).content
            json_data=pd.read_json(io.BytesIO(file_content))
            json_dfs[file_name]=json_data
            #print(f"- {file_name}\n")

    return json_dfs

