#!/bin/bash

#import mapping
/var/nodejs/bin/elasticdump --input=mapping.json  --output=http://127.0.0.1:9200/.kibana --type=mapping

#import data
/var/nodejs/bin/elasticdump --input=data.json  --output=http://127.0.0.1:9200/.kibana --type=data

#done
echo "import done!"
