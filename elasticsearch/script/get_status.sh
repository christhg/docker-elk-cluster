#! /bin/bash

# get index
echo "--index status--"
curl -XGET "http://127.0.0.1:9200/_cat/indices/?v"
# get health
echo ""
echo "--health status--"
curl -XGET http://127.0.0.1:9200/_cat/health?v

#get node
echo ""
echo "--node status--"
curl -XGET http://127.0.0.1:9200/_cat/nodes?v

echo "done!"
