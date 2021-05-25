from dotenv import load_dotenv
import os, uuid
from azure_blob_utils import BlobController



load_dotenv()

if __name__ == '__main__':
    print('a')
    con_blob = BlobController()
    #con_blob.create_blob_container('teste-didier')


    # upload LOCAL_FILE_NAME from PATH_BLOB_DATA into container_name.
    con_blob.upload_data_to_blob_container('teste-didier')