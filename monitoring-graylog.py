#!/usr/bin/python3

# Autor: Bezaleel Ramos( bramos@onxsolutions.net)
# NickName: Beza
# Date: 01/10/2018
# Version: v2

## Imports##
import requests
import json
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


## Credentials user##
apiUserGray="<Username Graylog>"
apiPassGray="<Password Username>"

## Args ##
key = sys.argv[1]

## Functions to login in Api Rest ##
def apiGrayLog(valueApi):
    r = requests.get('http://<Ip GrayLog Server>:9000/api/%s' % valueApi, auth=(apiUserGray,apiPassGray), verify=False)
    return r.text

## Function to get /system/metrics ##
def monmetric(itemMon01, itemMon02):
    getvaluemon = json.loads(apiGrayLog('system/metrics/%s' % itemMon01))
    print(getvaluemon[ itemMon02 ])

## Function to get metrics shared bufffer Processors##
def monprocessbuffer(itemMon01, itemMon02):
    getvaluemon = json.loads(apiGrayLog('system/metrics/org.graylog2.shared.buffers.processors.%s' % itemMon01))
    print(getvaluemon[itemMon02 ])

## Funcition to get metrics /api/cluster ##
def moncluster(nodeID,metric01):
    getvaluemon= json.loads(apiGrayLog('cluster'))
    print(getvaluemon[ nodeID ][ metric01 ])

## Function to get metrics node in JVM ##
def monnode(nodeId,metric01):
    getvaluemon= json.loads(apiGrayLog('cluster/%s/jvm' % nodeId))
    print(getvaluemon[metric01]['bytes'])

## Function to Low Level Discovery(LLD) Nodes ##
def lldgraylognode():
    lldGraylog = json.loads(apiGrayLog('cluster'))
    arrayGetNode = []
    for getNodeID in lldGraylog:
        nodeId = {}
        nodeId['{#NODEID}'] = getNodeID
        arrayGetNode.append(nodeId)
    print(json.dumps({'data': arrayGetNode }, indent=4, separators=(',',':')))

## Test if parameter is lldgraylognode ##
if key == 'lldgraylognode':
    eval(key+"()")
else :
    itemMon01 = sys.argv[2]
    itemMon02 = sys.argv[3]
    eval(key+"('{0}','{1}')".format( itemMon01, itemMon02))
