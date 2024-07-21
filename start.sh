#!/bin/bash -e
set -o pipefail

# A minimal script to cron and ensure the flask server is always running.
#
# # rin
# * * * * * /home/twissell/bin/rin/start.sh
# 0 0 * * * [ -f /home/twissell/bin/rin/screen/log ] && mv /home/twissell/bin/rin/screen/log /home/twissell/bin/rin/screen/log.1

export RIN_DIR="${RIN_DIR:-/home/twissell/bin/rin}"
export RIN_CONFIG_FILE="${RIN_DIR}/config.json"

source "${RIN_DIR}/venv/bin/activate"

start_command="screen -L -Logfile ${RIN_DIR}/log -dmS rin ${RIN_DIR}/serve.sh"

if ! pgrep -if "${start_command}" &> /dev/null; then
    $start_command
fi
