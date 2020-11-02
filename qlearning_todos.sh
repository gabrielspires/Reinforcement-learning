#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
for file in Entries/*
do
    # echo ""
    # echo "$file"
    # echo ""
    python3 __main__.py $file 0.3 0.9 0.1 300
done