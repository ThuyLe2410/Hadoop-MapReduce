# Hadoop MapReduce Project

## Purpose of the Project

The purpose of this project is to demonstrate the use of Hadoop's MapReduce framework to process and analyze sales data from a CSV file. The project involves a basic implementation of a **mapper** and **reducer** to perform data aggregation, such as counting the occurrences of products in the dataset.

The dataset used in this project is `SalesJan2009.csv`, which contains sales data for the month of January 2009. The MapReduce job processes this data to provide useful insights, such as the number of occurrences of each product.

## Project Structure

- `mapper.py`: The mapper script that reads the CSV data and outputs key-value pairs. For instance, it groups by `Product` and counts the number of occurrences of each product.
- `reducer.py`: The reducer script that aggregates the results from the mapper. It sums up the counts of each product to produce the final output.
- `data/SalesJan2009.csv`: The dataset containing sales data for January 2009.

## Prerequisites

- Hadoop installed and configured in Docker.
- Using Hadoop commands and Python programming.

## Steps to Run the Project

### 1. Configure Hadoop Environment
- Open your shell configuration file to set up any necessary environment variables:
  ```bash
  code ~/.zshrc
- Start all Hadoop daemon:
    ```bash
    start-all.sh
- Verify Hadoop services are running
    ```bash
    jps
### 2. Prepare HDFS
- Create directory in hdfs to store data
    ```bash
    hdfs dfs -mkdir /data
- Upload the SalesJan2009.csv to hdfs
    ```bash
    hdfs dfs -put ./data/SalesJan2009.csv /data/
- Verify the uploaded data
    ```bash
    hdfs dfs -cat /data/SalesJan2009.csv
### 3. Run the MapReduce Jobs:
- Make the mapper and reducer scripts executable
    ```bash
    chmod +x mapper.py
    chmod +x reducer.py
- Execute the MapReduce job using Hadoop streaming:
    ```bash
    mapred streaming -files mapper.py, reducer.py -input /data/SalesJan2009.csv -output /output -mapper mapper.py -reducer reducer.py
### 4. View the results:
- List output directory hdfs
    ```bash
    hdfs dfs -ls /output
- Display the result of MapReduce job
    ```bash
    hdfs dfs -cat /output/part-00000
- Download the result to the local filesystem
    ```bash
    hdfs dfs -get /output/part-00000 ./

## Conclusion
**The output:**

Product1	847

Product2	136

Product3	15

The final result of your MapReduce job will show the count of each product. This result is crucial in understanding the data distribution or performing further analysis.


