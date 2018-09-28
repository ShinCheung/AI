#!/bin/sh
cat input.txt | python mapper.py | python reducer.py | sort -nr -k 2 | head -$1 > output.txt