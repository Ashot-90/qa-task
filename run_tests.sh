#!/bin/bash

while [ -n "$1" ]; do
  case "$1" in
  -portal | -po)
    PORTAL=$2
    shift 2
    ;;
  -parallel | -pa)
    PARALLEL=true
    shift 1
    ;;
  *)
    echo >&1 "Error: Illegal option '$1'"
    exit 1
    ;;
  esac
done

if [[ -z "$PORTAL" ]]; then
  echo "Using default portal 'DE'"
  PORTAL='DE'
else
  if [[ "$PORTAL" =~ ^(DE|UK)$ ]]; then
    echo "Using portal '$PORTAL'"
  else
    echo "Warning: Incorrect portal provided. Using portal 'DE'"
    PORTAL='DE'
  fi
fi
export PORTAL

if [ "$PARALLEL" == "true" ]; then
  echo "Running tests in parallel mode"
  RUN_CMD='unittest-parallel -t . -s tests'
else
  echo "Running tests by default sequential mode"
  RUN_CMD='python3 -m unittest discover tests/'
fi

echo "Running : '$RUN_CMD'"
eval "$RUN_CMD"
