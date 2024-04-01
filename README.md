# Data-engineering-Project
Project submission for Data engineering Zoomcamp 2024 cohort.

## I.	Dataset creation

- Creation of a JSON-format dataset from mockaroo: https://www.mockaroo.com/

## II.	Sending data to the Apache Kafka broker

- Sending data via the "NiFi_producer.py" script. 
- Changes made to UTF-8 string encoding format.

## III.	Flow Apache Nifi

- Implementation of the Apache Nifi flow reproduced in the "Cloud_NiFi_Flow.json" file.

<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/858fe40f-4036-4f05-8902-506b971d2df1">

\
<img width="264" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/e6eec186-2d6c-4fa6-a547-64edeb40d43f">

### IV.	Installing the bucket in GCP Cloud Storage

- Introduction to the "kpe_cloud" bucket. 
- Example of file imported as "handle_20240401_122325.json".

<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/63ca971c-1109-4c81-bc93-df11d1d68716">

\
<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/3d8ea306-e12e-4392-bc25-2b67caf61928">

\
<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/94fbfd73-00ef-46a2-96ad-edc111ff241b">

\
<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/31d7b673-409c-4708-a99f-7402cc9bb726">

## V.	Visualization production

- Production of the visualization dashboard.

\
<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/614ccf8b-73e6-4bd6-ae35-5a6e96f79cf2">

## VI.	Cost calculation 

- To set up the project, we need to use an Apache Kafka cluster consisting of 3 nodes with 3 separate machines.
- Calculating the cost of 3 machines for an Apache Kafka instance: Given that a GCP VM costs $25/month, 3 machines cost $75/month.
- Calculating the number of partitions for a topic: If we want to read 1GB/s, a consumer can process 50MB/s and a producer can write 100MB/s, the number of partitions corresponds to 1000/50, i.e. 20 partitions.
- Calculation of disk space required : 

  * Average message size = 10 KB
  * Number of messages per day = 2000000
  * Retention period in days = 5
  * Replication factor = 3

Considering the following function: (avg-msg-size) x (msgs-per-day) x (retention-period-days) x (replication-factor)
We obtain: 10 * 2000000 * 5 * 3 = 300000000 = 300 GB

- Cost of migration to cloud storage: If we choose standard multi-region storage at a cost of $0.2/Gb/month, the cost of migration for 300 GB represents $60/month.
