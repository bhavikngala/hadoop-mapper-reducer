#!/usr/bin/env bash

# start hadoop
$HADOOP_HOME/sbin/start-hadoop.sh

# transfer input files to hadoop
# hdfs dfs -put $1 input

# run mapper and reducer
hadoop jar $HADOOP_HOME/contrib/hadoop-streaming-*.jar \
-file $1 -mapper $1 \
-file $2 -reducer $2 \
-input $3 -ouput $4

# stop hadoop server
$HADOOP_HOME/sbin/stop-hadoop.sh