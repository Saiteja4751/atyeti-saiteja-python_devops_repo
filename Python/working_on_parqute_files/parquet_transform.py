from pyspark.sql import SparkSession
from pyspark.sql.functions import upper, col

# Step 1: Create SparkSession
spark = SparkSession.builder \
    .appName("Parquet Transformation Example") \
    .getOrCreate()

# Step 2: Read the Parquet File
# parquet_file = "converted-file.parquet"  # replace with your file
parquet_file = "titanic.parquet"

df = spark.read.parquet(parquet_file)

# Show original data
print("Original Data:")
df.show()

# Step 3: Transformation Example
# Filter where age > 30
filtered_df = df.filter(col("age") > 30)

# Add a new column with uppercase name
transformed_df = filtered_df.withColumn("name_upper", upper(col("name")))

# Show transformed data
print("Transformed Data:")
transformed_df.show()

# Step 4: Save the transformed DataFrame back to Parquet
transformed_df.coalesce(1) \
    .write.mode("overwrite") \
    .parquet("output_transformed.parquet")

# Stop the SparkSession
spark.stop()
