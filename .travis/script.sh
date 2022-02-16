#!/bin/bash
set -e

if [ "${TRAVIS_EVENT_TYPE}" = "cron" ];
then
  cspell \"**/*.*\" && md-report . && remark . -e .md -r .remarkrc.json --quiet --frail && eslint -c .eslintrc.json . && find . -type f -name *.py | xargs -I {} pycodestyle --show-source {}
else
  bash ./.travis/test-files-changed.sh
fi
