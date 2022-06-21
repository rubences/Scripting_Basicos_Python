#!/bin/bash

log()
{
	ts=$(date "+%x %X")
	echo "$ts:$1"
}

while true
do 
	log COUCOU
	echo ' socorro!!!' >&2
	sleep 2
done
