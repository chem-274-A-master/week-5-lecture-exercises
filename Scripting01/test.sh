#!/bin/bash

set -eu

# NOTE - this test is for running locally only. The real tests will may run in a different environment on github

MAIN_FILE=$(dirname $0)/main.sh

export SECRET_FILE="secret_output.txt"
rm -f ${SECRET_FILE}
bash ${MAIN_FILE} abc qrs discovery fuss impact 

REAL_SHA=$(cat secret_output.txt | shasum)

if [[ "8de0e4a4235a304da05bbeaf884a4f7ef7f3b5c0  -" == "${REAL_SHA}" ]]
then
  echo "Success"
  exit 0
else
  echo "Failed"
  echo ${REAL_SHA}
  exit 1
fi
