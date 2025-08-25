from pyspark.sql import SparkSession

def get_spark_session():
    spark = SparkSession.builder \
        .appName("GCP to S3 ETL") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.2") \
        .getOrCreate()
    return spark

def transform_file_spark(file_path):
    spark = get_spark_session()
    df = spark.read.option("header", "true").csv(file_path)
    
    # Example transformation (add your own)
    df_transformed = df.dropna()
    
    return df_transformed
