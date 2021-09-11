#!/bin/bash
#This script will query covid data and display it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
PENDING=$(echo $DATA | jq '.[0].pending')
DEATH=$(echo $DATA | jq '.[0].death')
TODAY=$(date)

echo "As of today $TODAY, there has been $HOSPITALIZED patients hospitalized."
