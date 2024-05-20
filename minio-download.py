from minio import Minio
from minio.sse import SseCustomerKey

client = Minio('localhost:9000',
               access_key='minio_access_key',
               secret_key='minio_secret_key',
               secure=False)

end_file = "d:/Geek_Brains/Project/misc/minio-download-file/dataset/kc_house_dataset.csv"
bucket_name = "python-test-bucket"
destination_file = "kc_house_data.csv"

# download file
client.fget_object(bucket_name, destination_file, end_file)

# download feedback 
print('Файл kc_house_data.csv загружен, как kc_house_dataset.csv')