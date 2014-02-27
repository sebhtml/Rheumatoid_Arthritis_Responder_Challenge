#!/bin/bash

for i in $(cat handles.txt)
do

	synapse -u sebhtml -p $(cat ~/.synapse) get $i

done

