from dotenv import load_dotenv
import os, uuid
import glob
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
load_dotenv()


class BlobController:
    def __init__(self):
        self.con_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.con_key = os.getenv("AZURE_STORAGE_CONNECTION_KEY")
        self.blob_service_client = self.connect_to_blob_service_client()

        
    def connect_to_blob_service_client(self):
        '''
        output: BlockServiceClient connected to azure connecting string.
        '''

        try:
            command = f'setx AZURE_STORAGE_CONNECTION_STRING "{self.con_string}"'
            os.system(f"cmd /c {command}")
        except Exception as e:
            print({'exception':f"{e}"})
        

        # connecting to container
        return BlobServiceClient.from_connection_string(self.con_string)


    def create_blob_container(self, container_name):

        '''
        create a blob container.
        '''
        # Create a local directory to hold blob data
        #local_path = os.getenv("PATH_BLOB_DATA")
        #container_name = #os.getenv("CONTAINER_NAME")

        #os.mkdir(local_path)

        # connecting to container
        #blob_service_client = BlobServiceClient.from_connection_string(self.con_string)

        # Create the blob container
        self.blob_service_client.create_container(container_name)


        #upload_file_path = os.path.join(os.getenv("PATH_BLOB_DATA"), os.getenv("LOCAL_FILE_NAME"))

        # Create a blob client using the local file name as the name for the blob
        #blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.getenv("LOCAL_FILE_NAME"))

    def upload_data_to_blob_container(self, container_name, n_files=None, n_files_type=None): 

        '''
        upload LOCAL_FILE_NAME from PATH_BLOB_DATA into container_name.
        '''

        #CREATE A CONTAINER AND UPLOAD DATA TO BLOB
        upload_file_path = os.path.join(os.getenv("PATH_BLOB_DATA"), os.getenv("LOCAL_FILE_NAME"))

        # Create a blob client using the local file name as the name for the blob
        blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=os.getenv("LOCAL_FILE_NAME"))

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)


if __name__ == "__main__":

    # set connection string variable
    load_dotenv()
    con_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    command = f'setx AZURE_STORAGE_CONNECTION_STRING "{con_string}"'
    os.system(f"cmd /c {command}")



    try:
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

        # Quick start code goes here

        # Create a local directory to hold blob data
        local_path = os.getenv("PATH_BLOB_TEST")
        container_name = os.getenv("CONTAINER_NAME")
        #os.mkdir(local_path)

        # connecting to container
        blob_service_client = BlobServiceClient.from_connection_string(con_string)

        # Create the container
        #container_client = blob_service_client.create_container('asd')

        # interact with the specified container
        container_name = os.getenv("CONTAINER_NAME")
        container_client = blob_service_client.get_container_client(container_name)

       # # List the blobs in the container
       # blob_list = container_client.list_blobs()
       # for blob in blob_list:
       #     print("\t" + blob.name)

        # interact with the specified blob
        blob_name = 'JOANINHA.txt'
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.get_blob_properties()

        #CREATE A CONTAINER AND UPLOAD DATA TO BLOB
        upload_file_path = os.path.join(os.getenv("PATH_BLOB_DATA"), os.getenv("LOCAL_FILE_NAME"))

        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.getenv("LOCAL_FILE_NAME"))

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)


    except Exception as ex:
        print('Exception:')
        print(ex)


