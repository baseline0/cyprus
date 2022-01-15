#!/bin/bash

# fix for: no named module

CYPRUS_DIR=$(pwd)
#export PYTHONPATH="$PYTHONPATH:$CYPRUS_DIR"
export PYTHONPATH="$CYPRUS_DIR:$CYPRUS_DIR/cyprus"

echo "PYTHONPATH now includes cyprus"
echo $PYTHONPATH
