import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY


def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(
            anon=False,
            key=AWS_ACCESS_KEY_ID,
            secret=AWS_ACCESS_KEY
        )
        return s3
    except Exception as e:
        print(f'Error connecting to S3: {e}')

def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket_name:str):
    try:
        if not s3.exists(bucket_name):
            s3.mkdir(bucket_name)
            print(f'Bucket {bucket_name} created')
        else:
            print(f'Bucket {bucket_name} already exists')

    except Exception as e:
        print(f'Error creating bucket: {e}')

def upload_to_s3(s3: s3fs.S3FileSystem, file_path:str, bucket_name:str, s3fs_filename:str):
    try:
        s3.put(file_path, f'{bucket_name}/raw/{s3fs_filename}')
        print(f'{file_path} uploaded to S3 bucket: {bucket_name}')
    except Exception as e:
        print (f'Error uploading to S3: {e}')