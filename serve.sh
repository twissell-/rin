#!/bin/bash -e

gunicorn --chdir src -b :20464 rin:rin
