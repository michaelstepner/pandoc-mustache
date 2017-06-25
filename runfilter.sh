#!/bin/bash

#pandoc -t json -s | ./filters/mustache.py | pandoc -f json
pandoc test/test.md --filter ./filters/mustache.py