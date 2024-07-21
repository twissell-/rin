#!/bin/bash -e

SCRIPT_NAME=/rin gunicorn rin:rin \
    --chdir "${RIN_DIR}/src" \
    -b 127.0.0.1:20464
