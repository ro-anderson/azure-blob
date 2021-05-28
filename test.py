import glob
import os

from dotenv import load_dotenv
import os, uuid
load_dotenv()

#directory = os.path.join(os.getenv("PATH_BLOB_DATA_SERVER"),os.getenv("PATH_BLOB_DATA"))
#print(directory)
#print(os.getenv("PATH_BLOB_DATA_SERVER"))
pattern = eval(os.getenv('OTC_PATH_BLOB_DATA'))
glob_list = glob.glob(pattern)
#glob_list = [lambda x: eval(x) for x in  glob_list]
a = glob_list[0]
print(a)
#os.listdir(eval(os.getenv('PATH_BLOB_DATA')))
#print(os.listdir(eval(os.getenv('OTC_PATH_BLOB_DATA_PARCIAL'))))

#list_ = glob.glob('./data-blob-test/*.csv')
#list_ = glob.glob(pattern)
#print(f"esse é o pattern: \n{pattern}")
#print(f"essa é a lista: \n{list_}")
#for file_name in list_:
#    print(file_name)
#
#upload_file_path = os.path.join(os.getenv("PATH_BLOB_DATA"), os.getenv("LOCAL_FILE_NAME"))
#print(upload_file_path)
#print(os.listdir(os.getenv('PATH_BLOB_DATA')))
#print(list_)
#
#print('criando container')