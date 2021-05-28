from dotenv import load_dotenv
import os, uuid
from azure_blob_utils import BlobController



load_dotenv()

if __name__ == '__main__':
    print('a')
    con_blob = BlobController()
    con_blob.create_blob_container('otc-collections-v2')


    # upload LOCAL_FILE_NAME from PATH_BLOB_DATA into container_name.
    con_blob.upload_data_to_blob_container('otc-collections-v2', n_files=True, n_files_type='CSV')