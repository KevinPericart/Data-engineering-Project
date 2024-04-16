import json
from kafka import KafkaProducer
from pyspark.sql import SparkSession

# Define the end-to-end pipeline steps
def extract_data(file_path, spark):
    # Read JSON file into Spark DataFrame
    df = spark.read.json(file_path)
    return df

def clean_and_transform_data(df):
    # Clean and transform data using Spark DataFrame operations
    cleaned_df = df.dropna()  # Example: Dropping rows with null values
    transformed_df = cleaned_df  # Placeholder for actual transformation
    return transformed_df

def load_data_to_stream(df, producer, topic):
    # Convert DataFrame to JSON strings and send to Kafka stream
    for row in df.toJSON().collect():
        producer.send(topic, json.dumps(json.loads(row)).encode('utf-8'))

def main():
    # Path to data file
    data_file_path = "file:///path/to/data.json"

    # Kafka producer settings
    bootstrap_servers = '20.126.103.217:9092'
    topic = "KPE_streaming"

    # Initialize Kafka producer
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("DataCleaningAndTransformation") \
        .getOrCreate()

    try:
        # Step 1: Extract data
        data_df = extract_data(data_file_path, spark)

        # Step 2: Clean and transform data
        transformed_data_df = clean_and_transform_data(data_df)

        # Step 3: Load data to Kafka stream
        load_data_to_stream(transformed_data_df, producer, topic)

        # Flush producer buffers
        producer.flush()

    finally:
        # Stop SparkSession
        spark.stop()

if __name__ == "__main__":
    main()
