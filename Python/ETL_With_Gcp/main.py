import os
from gcs_utils.gcs_connector import list_files_in_bucket, download_file
from transform.transformer import transform_file
from s3_utils.s3_uploader import upload_to_s3

def main():
    print("Starting ETL Process...\n")

    files = list_files_in_bucket()
    print(f"Found {len(files)} file(s) in the bucket.")

    for file in files:
        print(f"\nProcessing file: {file}")
        local_path = download_file(file)
        transform_file(local_path)

    print("\nETL Process Complete!")


    import os
    output_files = os.listdir("output")
    for fname in output_files:
        upload_to_s3(os.path.join("output", fname))

    print("\n✅ ETL Process Complete!")

if __name__ == "__main__":
    main()
