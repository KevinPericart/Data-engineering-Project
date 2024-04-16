# Data engineering 2024 Zoomcamp Project

Welcome to the Data Engineering Zoomcamp 2024 project submission. This project tackles several key aspects of modern data engineering, ensuring clarity, efficiency, and seamless functionality from end to end.

## I. Dataset Generation

Utilizing Mockaroo's versatile platform, we craft a JSON-formatted dataset tailored to our project needs, ensuring diverse and realistic data representation.

## II. Data Streaming with Apache Kafka

Data streaming is facilitated through our custom "NiFi_producer.py" script, ensuring smooth transmission of data to the Apache Kafka broker. Special attention is paid to encoding formats to maintain data integrity.

## III. Apache NiFi Workflow

Our Apache NiFi flow, meticulously outlined in the "Cloud_NiFi_Flow.json" file, orchestrates the seamless movement of data, ensuring reliability and efficiency at every step.

<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/858fe40f-4036-4f05-8902-506b971d2df1">

\
<img width="264" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/e6eec186-2d6c-4fa6-a547-64edeb40d43f">

## IV. GCP Cloud Storage Setup

The establishment of our GCP Cloud Storage bucket, exemplified by the "kpe_cloud" bucket, is pivotal for scalable and reliable data storage. Detailed examples, such as "handle_20240401_122325.json," illustrate the practical implementation of our storage solution.

<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/63ca971c-1109-4c81-bc93-df11d1d68716">

\
<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/3d8ea306-e12e-4392-bc25-2b67caf61928">

\
<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/94fbfd73-00ef-46a2-96ad-edc111ff241b">

\
<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/31d7b673-409c-4708-a99f-7402cc9bb726">

## V. Visualization Dashboard Creation

A robust visualization dashboard is produced to provide intuitive insights into our data streams, enhancing accessibility and decision-making capabilities.

\
<img width="488" alt="image" src="https://github.com/KevinPericart/Data-engineering-Project/assets/66140785/614ccf8b-73e6-4bd6-ae35-5a6e96f79cf2">

## VI. Cost Analysis and Optimization

To ensure economic viability and scalability, we conduct a comprehensive cost analysis:

Apache Kafka Cluster Cost: By leveraging a three-node Apache Kafka cluster, each on separate GCP VM instances priced at $25/month, we optimize performance while managing costs effectively.
Partitioning Strategy: Through careful consideration of throughput requirements, we determine an optimal partitioning strategy, balancing performance and resource utilization.
Disk Space Calculation: Utilizing key parameters such as message size, retention period, and replication factor, we accurately estimate disk space requirements, enabling cost-effective storage solutions.
Cloud Storage Migration Cost: We evaluate migration costs to GCP Cloud Storage, accounting for factors such as data volume and storage tier selection, ensuring cost-efficiency in our data storage strategy.
In conclusion, our project not only addresses the core data engineering challenges but also emphasizes optimization and efficiency at every stage, culminating in a robust and scalable data infrastructure.
