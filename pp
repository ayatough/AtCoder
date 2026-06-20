#!/bin/bash

dir=$(cd $(dirname $0); pwd)
uv run -p $dir/.venv_pypy/bin/python python $@
