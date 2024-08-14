'''
code ~/.zshrc
cd $LOCAL_HADOOP_CONFIG_DIR
start-all.sh
jps
hdfs dfs -ls /
code ~/workspace/na/Hadoop

hdfs dfs -mkdir /data
hdfs dfs -put ./SalesJan2009.csv /data/
hdfs dfs -cat /data/SalesJan2009.csv

chmod +x mapper.py
chmod +x reducer.py
mapred streaming -files mapper.py,reducer.py -input /data/SalesJan2009.csv -output /output -mapper mapper.py -reducer reducer.py

hdfs dfs -ls /output

hdfs dfs -cat /output/part-00000

hdfs dfs -rm -r /output
hdfs dfs -get /output/part-00000 ./

mapper.py: The mapper will read the CSV data and output key-value pairs. For instance, we might want to group by Product and count the number of occurrences of each product.
'''
