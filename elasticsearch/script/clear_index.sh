#! /bin/bash
#
DATA1=`date -d "- 0 day" +%Y.%m.%d` 
DATA2=`date -d "- 1 day" +%Y.%m.%d`
#
time=`date`

#
curl -XGET "http://127.0.0.1:9200/_cat/indices/?v" | grep $DATA1
if [ $? == 0 ];then
   curl -XDELETE "http://127.0.0.1:9200/*-${DATA1}"
   echo "已在$time清理$DATA1索引"
fi
curl -XGET "http://127.0.0.1:9200/_cat/indices/?v" | grep $DATA2
if [ $? == 0 ];then
   curl -XDELETE "http://127.0.0.1:9200/*-${DATA2}"
   echo "已在$time清理$DATA2索引"
fi
