#!/bin/bash

#export data
/var/nodejs/bin/elasticdump --ignore-errors=true  --scrollTime=120m  --bulk=true --input=http://127.0.0.1:9200/.kibana   --output=data.json  --type=data

#export mapping
/var/nodejs/bin/elasticdump --ignore-errors=true  --scrollTime=120m  --bulk=true --input=http://127.0.0.1:9200/.kibana   --output=mapping.json  --type=mapping

#
echo "export done!"
