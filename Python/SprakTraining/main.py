from gcs_utils.gcs_connector import list_files_in_bucket, download_file
from transform.transformer import transform_file_spark
from s3_utils.s3_uploader import upload_to_s3

import os

def main():
    print("🚀 Starting PySpark ETL Process...\n")

    files = list_files_in_bucket()
    print(f"📁 Found {len(files)} file(s) in GCS.")

    for file in files:
        print(f"\n📥 Downloading: {file}")
        local_path = download_file(file)

        # 🔄 Transform using PySpark
        transformed_dir = transform_file_spark(local_path)

        # 📤 Upload each part file from transformed_dir to S3
        if transformed_dir:
            for root, _, files in os.walk(transformed_dir):
                for fname in files:
                    fpath = os.path.join(root, fname)
                    upload_to_s3(fpath)

    print("\n✅ ETL Completed with PySpark!")

if __name__ == "__main__":
    main()
