#!/bin/bash
#This script will query today's covid data and display it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
PENDING=$(echo $DATA | jq '.[0].pending')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
DEATH=$(echo $DATA | jq '.[0].death')

TODAY=$(date)

echo "As of today, $TODAY, there has been $HOSPITALIZED patients hospitalized with covid."

echo "Of the $HOSPITALIZED, $POSITIVE were positive and $PENDING cases are pending.  There has been $NEGATIVE negative results with $DEATH deaths."
