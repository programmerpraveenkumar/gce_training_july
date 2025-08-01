#!/bin/bash
source /home/hackforge/htdocs/hackforge.in/venv/bin/activate
exec gunicorn app.main:app --workers 3 --bind 127.0.0.1:8000  -k uvicorn.workers.UvicornWorker