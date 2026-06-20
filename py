#!/bin/bash

dir=$(cd $(dirname $0); pwd)
uv run -p $dir/.venv_py3/bin/python python $@
