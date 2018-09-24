#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

for FILE in $(find ${DIR} -mindepth 1 -type f -name '*.dot'); do
    dot -Tpng "${FILE}" > "${FILE}.png"
done