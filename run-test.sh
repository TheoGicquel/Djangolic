#!/bin/bash
# Yes this is awful but i really dont have time
echo "[*] launching server"
python3 packages/djangolic/manage.py runserver &

echo "[*] building css"
nx run djangolic:build-css

echo "[*] running test task"
nx run djangolic-e2e:e2e

# killing server, and yes this is bad. i know
lsof -t -i tcp:8000| xargs kill -9