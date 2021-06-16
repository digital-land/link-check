#!/bin/bash

set -x 

OUTPUT_BASE=./dl-checklink
DEPTH=5
TIMEOUT=5
CHECKLINK=/usr/local/Cellar/perl/5.32.1_1/bin/checklink
EXCLUDE=`paste -sd '|' ignore.cfg`

$CHECKLINK -sber -t$TIMEOUT -D$DEPTH -qi -X $EXCLUDE digital-land.github.io | tee $OUTPUT_BASE.`date -u +"%Y-%m-%dT%H%M"`.out
