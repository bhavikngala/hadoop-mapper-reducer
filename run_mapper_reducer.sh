#!/usr/bin/env bash

# start hadoop
# $HADOOP_HOME/sbin/start-hadoop.sh
# echo '\n\n\n ~~~~~~~~~~HADOOP STARTED~~~~~~~~~~ \n\n\n'

# transfer input files to hadoop
hdfs dfs -put $3 input
echo '\n\n\n ~~~~~~~~~~FILES COPIED~~~~~~~~~~ \n\n\n'

# run mapper and reducer
hadoop jar $HADOOP_HOME/contrib/hadoop-streaming-*.jar \
-file $1 -mapper $1 \
-file $2 -reducer $2 \
-input input -output output

echo '\n\n\n ~~~~~~~~~~DATA MAP REDUCED~~~~~~~~~~ \n\n\n'

# store output to local directory
hdfs dfs -get output $4
echo '\n\n\n ~~~~~~~~~~COPYING OUTPUT~~~~~~~~~~ \n\n\n'

# stop hadoop server
# $HADOOP_HOME/sbin/stop-hadoop.sh
# echo '\n\n\n ~~~~~~~~~~HADOOP STOPPED~~~~~~~~~~ \n\n\n'