#!/usr/bin/env bash

sed -ri 's/([a-z.-]+)\t([0-9]+)/\2 \1/g' ./tweets_full_data_output/part-00000
sed -ri 's/([a-z.-]+)\t([0-9]+)/\2 \1/g' ./tweets_small_data_output/part-00000
sed -ri 's/([a-z.-]+)\t([0-9]+)/\2 \1/g' ./nytimes_full_data_output/part-00000
sed -ri 's/([a-z.-]+)\t([0-9]+)/\2 \1/g' ./nytimes_small_data_output/part-00000

sort -n -r ./tweets_full_data_output/part-00000 -o ./tweets_full_data_output/part-00000
sort -n -r ./tweets_small_data_output/part-00000 -o ./tweets_small_data_output/part-00000
sort -n -r ./nytimes_full_data_output/part-00000 -o ./nytimes_full_data_output/part-00000
sort -n -r ./nytimes_small_data_output/part-00000 -o ./nytimes_small_data_output/part-00000