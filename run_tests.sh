#!/bin/bash
############################
# Exit immediately if any command exits with non-zero code
set -e
############################
# Parsing provided arguments
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
############################
# Getting CPU cores count in case of parallel
if [ "$PARALLEL" == "true" ]; then
  echo "Running tests in parallel mode"
  PROC_COUNT=$(sysctl hw.ncpu | awk -F ":" '{print $2}' |  tr -d ' ')
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
eval "$RUN_CMD" || :
############################
echo "Generating Allure Report..."
sleep 5
allure generate "${RESULT_DIR}" -o "${REPORT_DIR}"
#allure open -h 127.0.0.1 -p 8083 "${REPORT_DIR}"
############################