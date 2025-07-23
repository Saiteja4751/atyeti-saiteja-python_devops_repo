from google.cloud import storage
from config.gcp_config import BUCKET_NAME
import os

def list_files_in_bucket():
    
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    return [blob.name for blob in bucket.list_blobs() if blob.name.endswith(".csv")]

def download_file(blob_name, destination_folder="downloads"):
    
    client = storage.Client()

    bucket = client.get_bucket(BUCKET_NAME)

    blob = bucket.blob(blob_name)
    os.makedirs(destination_folder, exist_ok=True)

    local_path = os.path.join(destination_folder, os.path.basename(blob_name))

    blob.download_to_filename(local_path)

    print(f"Downloaded: {blob_name} to {local_path}")

    return local_path
