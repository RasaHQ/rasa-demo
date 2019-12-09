#!/bin/bash
set -e

if [ "$1" = 'rasa' ]; then
  mkdir -p /app/terms
  echo `whoami` $(date) > /app/terms/agree.txt
  echo pwd: `pwd`
  #find .
  ls -l

  # test if a rasa init has been done
  if [ ! -d /app/data ]; then
    echo "Existing bot not found, running rasa init"
    rasa init --no-prompt
  fi

  echo running: "$@"
  exec "$@"
  #exec rasa "$@"
  #exec gosu rasa "$@"
fi

echo no rasa command, running: "$@"
exec "$@"