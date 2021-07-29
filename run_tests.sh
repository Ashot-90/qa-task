#!/bin/bash
############################
# Exit immediately if any command exits with non-zero code
set -e
############################
# Parsing provided arguments
if [ $(($# % 2)) -ne 0 ]; then
  echo "Error: Missed at least one required argument"
  exit 1
fi

while [ -n "$1" ]; do
  case "$1" in
  -portal | -po)
    PORTAL=$2
    shift 2
    ;;
  -parallel | -pa)
    PARALLEL=$2
    shift 2
    ;;
  -browser | -b)
    BROWSER=$2
    shift 2
    ;;
  *)
    echo >&1 "Error: Illegal option '$1'"
    exit 1
    ;;
  esac
done

if [[ -z "$BROWSER" ]]; then
  BROWSER='Chrome'
else
  if [[ "$BROWSER" =~ ^(Chrome|Firefox)$ ]]; then
    echo "Using browser '$BROWSER'"
  else
    echo "Warning: Incorrect portal provided. Using portal 'DE'"
    BROWSER='Chrome'
  fi
fi
export BROWSER

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

if [[ -z "$PARALLEL" ]]; then
  echo "Using default value of parallel 'true'"
  PARALLEL='true'
else
  if [[ "$PARALLEL" =~ ^(true|false)$ ]]; then
    echo "Using parallel '$PARALLEL'"
  else
    echo "Warning: Incorrect parallel argument is provided. Using parallel 'true'"
    PARALLEL='true'
  fi
fi
############################
# Getting CPU cores count in case of parallel
if [ "$PARALLEL" == "true" ]; then
  echo "Running tests in parallel mode"
  if [ "$DOCKER_RUN" == "" ]; then
    PROC_COUNT=$(sysctl hw.ncpu | awk -F ":" '{print $2}' | tr -d ' ')
  else
    PROC_COUNT=$(nproc)
  fi
else
  echo "Running tests by default sequential mode"
  PROC_COUNT=1
fi
############################
# Allure directories
PREFIX="$(date +%d_%m_%y_%H_%M_%s)"
RESULT_DIR="AllureResult_${PREFIX}"
REPORT_DIR="AllureReport_${PREFIX}"
mkdir -p "${RESULT_DIR}"
export RESULT_DIR
############################
# Run command
RUN_CMD="pytest -v -n ${PROC_COUNT} --alluredir=${RESULT_DIR}"
echo "Running : '$RUN_CMD'"
eval "${RUN_CMD}" || :
############################
echo "Generating Allure Report..."
sleep 5
if [ "$DOCKER_RUN" == "" ]; then
  ALLURE_CMD="allure"
else
  ALLURE_CMD="allure-2.7.0/bin/allure"
fi
ALLURE_CMD+=" generate \"${RESULT_DIR}\" -o \"${REPORT_DIR}\""
eval "${ALLURE_CMD}"
#allure open -h 127.0.0.1 -p 8083 "${REPORT_DIR}"
############################
